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

    return datetime.datetime(*numbers)


def resolve_my_format(path: Path, frmt):
    img = Image.open(path)
    exif_data = img.getexif()

    try:
        datetime_field = exif_data[DATE_TIME]
    except KeyError as e:
        raise SortException(e)

    try:
        date = super_parse_date(datetime_field)
    except ValueError as e:
        raise SortException(e)

    return (datetime.datetime
            .strftime(date, frmt)
            .replace("%NAME", path.name))


def sort_file(path: Path, dst: Path, frmt, dry_run=False):
    try:
        new_path = dst / resolve_my_format(path, frmt)
    except PIL.UnidentifiedImageError:
        log.debug(f"File {path.name} is not an image")
        return
    except SortException as e:
        if isinstance(e.wrapped, KeyError):
            log.debug(f"Image {path.name} does not have a DateTime field")
            return
        if isinstance(e.wrapped, ValueError):  # from the super_parse_date method
            log.debug(f"The date {string} is not formatted correctly")
            return

        raise e

    log.info(f"Copying {path.name} to {new_path}")

    if not dry_run:
        if new_path.exists():
            log.info(parse_color(f"Destination ℂ1.{new_path}ℂ. already exists"))
            return
        new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, new_path)


def sort(src: Path, dst: Path, frmt, dry_run=False):
    for file in src.iterdir():
        if file.is_file():
            sort_file(file, dst, frmt, dry_run=dry_run)
