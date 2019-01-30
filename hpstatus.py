import argparse

from hpstatus.report import get_report
from hpstatus.status import FEATURES
from hpstatus.format import FORMATS

parser = argparse.ArgumentParser(description="Displays HP server status")

parser.add_argument("feature", choices=FEATURES, help="The feature to display the status of")
parser.add_argument("-f", "--format", default="line", choices=FORMATS, help="The format to display the status in")
parser.add_argument("--header", action="store_true", help="Adds a header to the CSV format, defaults to no header")
parser.add_argument("--pretty", action="store_true", help="Pretty prints the JSON format, defaults to off")
parser.add_argument("--prefix", default="hp_", help="Prefix to prepend to the measurement name in the line format")

args = parser.parse_args()

if args.feature == "all":
    for feature in FEATURES:
        status = get_report(feature, args.format, {"header": args.header, "pretty": args.pretty, "prefix": args.prefix})
        print(status)
else:
    status = get_report(args.feature, args.format, {"header": args.header, "pretty": args.pretty, "prefix": args.prefix})
    print(status)
