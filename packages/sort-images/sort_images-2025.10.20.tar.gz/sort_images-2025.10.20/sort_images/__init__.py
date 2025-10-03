import argparse
import logging
from pathlib import Path

from sort_images.terminal_formatting import parse_color
from sort_images import sort
from sort_images.version import program_version

log = logging.getLogger("sort-images")
console = logging.StreamHandler()
log.addHandler(console)
log.setLevel(logging.DEBUG)
console.setFormatter(
    logging.Formatter(parse_color("{asctime} [ℂ3.{levelname:>5}ℂ.] ℂ4.{name}ℂ.: {message}"),
                      style="{", datefmt="%W %a %I:%M"))

PROGRAM_NAME = "sort-images"
DEFAULT_DATE_FORMAT = "%y/%b/%NAME"


def command_entry_point():
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Program was interrupted by user")


def main():
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME,
                                     description="A cli tool to sort images into folders by date",
                                     allow_abbrev=True, add_help=True, exit_on_error=True)

    parser.add_argument("-f", "--format",
                        help=f"Set the output date format, the default is {DEFAULT_DATE_FORMAT.replace("%", "%%")} "
                             f"(The format is the standard python datetime format, except for the special variable %%NAME that allows "
                             f"for the insertion of the file name)", default=DEFAULT_DATE_FORMAT)
    parser.add_argument("-d", "--dry-run", action="store_true", help="Don't copy any files")
    parser.add_argument("-m", "--move", action="store_true", help="Move files instead of copying them")
    parser.add_argument('-v', '--verbose', action='store_true', help="Show more output")
    parser.add_argument("--version", action="store_true", help="Show the current version of the program")
    parser.add_argument("SRC", help=f"The folder in which {PROGRAM_NAME} will look for images")
    parser.add_argument("DST",
                        help="The folder into which the sorted images will be placed (possibly with a path prepended)")

    args = parser.parse_args()

    log.debug("Starting program...")
    log.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    if args.version:
        log.info(f"{PROGRAM_NAME} version {program_version}")
        return

    src = Path(args.SRC)
    dst = Path(args.DST)
    frmt = args.format

    if not src.exists():
        log.error(f"Folder {src} does not exist")
        return

    log.debug("Now starting to sort")
    sort.sort(src, dst, frmt, dry_run=args.dry_run, move=args.move)
