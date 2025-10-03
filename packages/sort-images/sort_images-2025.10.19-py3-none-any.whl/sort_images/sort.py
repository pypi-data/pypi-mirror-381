import datetime
import logging
import re
import shutil
from pathlib import Path

import PIL
import PIL.ExifTags
from PIL import Image
from PIL.TiffImagePlugin import DATE_TIME

from sort_images import parse_color

number_re = re.compile("\\d+")
log = logging.getLogger("sort-images")


class SortException(Exception):
    def __init__(self, wrapped):
        super().__init__(f"\"{wrapped}\" was raised while sorting")
        self.wrapped = wrapped


def super_parse_date(string):
    """Takes some date format and interprets it as a sequence of integers. Takes as many as it can and build the date.
    It assumes the integers are in the order:
    - year
    - month
    - day
    - hour
    - minute"""

    numbers = [int(n) for n in number_re.findall(string)]

    if len(numbers) > 5:
        log.debug(f"Too many numbers in date field: {string}")
        raise SortException(None)

    if len(numbers) < 1:
        log.debug(f"Too few numbers in date field: {string}")
        raise SortException(None)

    return datetime.datetime(*numbers)


def resolve_my_format(path: Path, frmt):
    img = Image.open(path)
    exif_data = img.getexif()

    try:
        datetime_field = exif_data[DATE_TIME]
    except KeyError as e:
        log.debug(f"Image {path.name} does not have a DateTime field")
        raise SortException(e)

    try:
        date = super_parse_date(datetime_field)
    except ValueError as e:
        log.debug(f"The date {datetime_field} is not formatted correctly")
        raise SortException(e)

    return (datetime.datetime
            .strftime(date, frmt)
            .replace("%NAME", path.name))


def sort_file(path: Path, dst: Path, frmt, dry_run=False, move=False):
    try:
        new_path = dst / resolve_my_format(path, frmt)
    except PIL.UnidentifiedImageError:
        new_path = dst / "error" / path.name
        log.debug(f"File {path.name} is not an image")
    except SortException:
        new_path = dst / "error" / path.name

    if dry_run:
        log.info(f"Would copy {path.name} to {new_path}")
    else:
        if new_path.exists():
            log.info(parse_color(f"Destination ℂ1.{new_path}ℂ. already exists"))
            return

        log.info(f"{"Moving" if move else "Copying"} {path.name} to {new_path}")
        new_path.parent.mkdir(parents=True, exist_ok=True)
        if move:
            shutil.move(path, new_path)
        else:
            shutil.copy(path, new_path)


def sort(src: Path, dst: Path, frmt, dry_run=False, move=False):
    log.debug(f"Sorting {src} to {dst}")
    for file in src.iterdir():
        log.debug(f"Looking at file {file}")
        if file.is_file():
            sort_file(file, dst, frmt, dry_run=dry_run, move=move)
