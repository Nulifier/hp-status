import io
import csv
import hpstatus.status as status

FORMATS = [
	"line",
	"csv",
	"json"
]

# These keys are used as tags for each feature

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
		value = _to_line(data)
	elif format == "csv":
		value = _to_csv(data, opts["header"])
	elif format == "json":
        value = _to_json(data, opts["pretty"])
	else:
		raise ValueError("Invalid format passed")

	print(value)

def _to_line(data):
	return ""

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
