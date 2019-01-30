import io
import csv
import json

# The formats that are supported
FORMATS = [
    "line",
    "csv",
    "json"
]

def _format_line(value, tag=False):
    if not tag and isinstance(value, str):
        # Suround field values with double quotes
        return '"{}"'.format(value)
    elif isinstance(value, int) and not isinstance(value, bool):
        return "{}i".format(value)
    else:
        return value

def to_line(data, feature, tags=[], prefix=""):
    lines = []
    for row in data:
        # The measurement name is the first tag
        row_tags = [prefix + feature]
        for tag in tags:
            row_tags.append("{}={}".format(tag, _format_line(row[tag], True)))

        row_values = []
        for key, value in row.items():
            if key not in tags:
                row_values.append("{}={}".format(key, _format_line(value)))

        lines.append("{} {}".format(",".join(row_tags), ",".join(row_values)))
    return "\n".join(lines)

def to_csv(data, header=True, delimiter=","):
    keys = list(data[0])

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=keys, delimiter=delimiter)

    if header:
        writer.writeheader()
    
    for row in data:
        writer.writerow(row)
    
    return output.getvalue()

def to_json(data, pretty=False, indent=4):
    if pretty:
        return json.dumps(data, indent=indent)
    else:
        return json.dumps(data, separators=(",", ":"))
