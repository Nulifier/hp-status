import io
import csv
import json
import hpstatus.status as status

# The formats that are supported
FORMATS = [
    "line",
    "csv",
    "json"
]

# These keys are used as tags for each feature
TAGS = {
    "fans": ["id", "location"],
    "powermeter": ["id"],
	"powersupply": ["id"],
	"temp": ["id", "location"]
}

def get_report(feature, format, opts):
    data = []
    if feature == "fans":
        data = status.get_fans()
    elif feature == "powermeter":
        data = status.get_powermeter()
    elif feature == "powersupply":
        data = status.get_powersupply()
    elif feature == "temp":
        data = status.get_temp()
    else:
        raise ValueError("Invalid feature passed")
    
    value = ""
    if format == "line":
        value = _to_line(data, feature, opts["prefix"])
    elif format == "csv":
        value = _to_csv(data, opts["header"])
    elif format == "json":
        value = _to_json(data, opts["pretty"])
    else:
        raise ValueError("Invalid format passed")

    print(value)

def _to_line(data, feature, prefix=""):
    tags = TAGS[feature]
    lines = []
    for row in data:
        # The measurement name is the first tag
        row_tags = [prefix + feature]
        for tag in tags:
            row_tags.append("{}={}".format(tag, row[tag]))

        row_values = ["{}={}".format(key, value) for key, value in row.items() if key not in tags]

        lines.append("{} {}".format(",".join(row_tags), ",".join(row_values)))
    return "\n".join(lines)

def _to_csv(data, header=True, delimiter=","):
    keys = list(data[0])

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=keys, delimiter=delimiter)

    if header:
        writer.writeheader()
    
    for row in data:
        writer.writerow(row)
    
    return output.getvalue()

def _to_json(data, pretty=False, indent=4):
    if pretty:
        return json.dumps(data, indent=indent)
    else:
        return json.dumps(data, separators=(",", ":"))
