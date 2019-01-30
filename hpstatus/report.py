import hpstatus.status as status
import hpstatus.format as format

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
        value = format.to_line(data, feature, TAGS[feature], opts["prefix"])
    elif format == "csv":
        value = format.to_csv(data, opts["header"])
    elif format == "json":
        value = format.to_json(data, opts["pretty"])
    else:
        raise ValueError("Invalid format passed")

    print(value)
