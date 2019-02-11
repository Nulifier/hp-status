import hpstatus.status as status
import hpstatus.format as fmt

FEATURES = [
    "fans",
	"powermeter",
	"powersupply",
	"temp",
    "storage"
]

# These keys are used as tags for each feature
TAGS = {
    "fans": ["id", "location"],
    "powermeter": ["id"],
    "powersupply": ["id"],
    "temp": ["id", "location"],
    "storage_controller": ["id"],
    "storage_drive": ["location", "port", "box", "bay"],
}

def _format_data(data, feature, format, opts):
    if format == "line":
        return fmt.to_line(data, feature, TAGS[feature], opts["prefix"])
    elif format == "csv":
        return fmt.to_csv(data, opts["header"])
    elif format == "json":
        return fmt.to_json(data, opts["pretty"])
    else:
        raise ValueError("Invalid format passed")

def get_report(feature, format, opts):
    if feature == "all" and format == "csv":
        raise ValueError("Cannot return all data in csv format")

    # We need a list of controller slots in order to pull the drive status
    if feature == "storage":
        controllers = status.get_storage_controllers()
        controller_slots = [ctrl["id"] for ctrl in controllers]
        text = _format_data(controllers, "storage_controller", format, opts)

        # Get the drives for each slot
        for slot in controller_slots:
            drives = status.get_storage_drives_detail(slot)
            text += "\n" + _format_data(drives, "storage_drive", format, opts)
        
        return text
    else:
        if feature == "fans":
            data = status.get_fans()
        elif feature == "powermeter":
            data = status.get_powermeter()
        elif feature == "powersupply":
            data = status.get_powersupply()
        elif feature == "temp":
            data = status.get_temp()
        else:
            raise ValueError("Invalid feature passed: '{}'".format(feature))
        return _format_data(data, feature, format, opts)
