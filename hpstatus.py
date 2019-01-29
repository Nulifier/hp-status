import argparse

from hpstatus.report import FORMATS, get_report
from hpstatus.status import FEATURES

parser = argparse.ArgumentParser(description="Displays HP server status")

parser.add_argument("feature", choices=FEATURES, help="The feature to display the status of")
parser.add_argument("-f", "--format", default="line", choices=FORMATS, help="The format to display the status in")
parser.add_argument("--header", action="store_true", help="Adds a header to the CSV format, defaults to no header")

args = parser.parse_args()

status = get_report(args.feature, args.format, {"header": args.header})
