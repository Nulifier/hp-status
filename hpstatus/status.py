import subprocess
import re

FEATURES = [
    "all",
	"fans",
	"powermeter",
	"powersupply",
	"temp"
]

def _get_system_feature(feature):
    return subprocess.check_output('hpasmcli -s "SHOW {}"'.format(feature.upper()), shell=True).decode("utf-8")

def get_fans():
    exp = re.compile("^#(?P<id>\d+)\s+(?P<location>\S+)\s+(?P<present>Yes|No)\s+(?P<speed>\S+)\s+(?P<percentage>\d+)%\s+(?P<redundant>Yes|No)\s+(?P<partner>\d+)\s+(?P<hot_pluggable>Yes|No)", re.I | re.M)
    fans = []
    for match in re.finditer(exp, _get_system_feature("fans")):
        fans.append({
            "id":		        int(match.group("id")),
            "location":	        match.group("location"),
            "present":          match.group("present") == "Yes",
            "speed":            match.group("speed"),
            "percentage":       float(match.group("percentage")) / 100.0,
            "redundant":        match.group("redundant") == "Yes",
            "partner":          int(match.group("partner")),
            "hot_pluggable":    match.group("hot_pluggable") == "Yes"
        })
    return fans

def get_powermeter():
    exp = re.compile("^Power Meter #(?P<id>\d+)\s*Power Reading\s*:\s*(?P<reading>\d+)", re.I | re.M)
    meters = []
    for match in re.finditer(exp, _get_system_feature("powermeter")):
        meters.append({
            "id":       int(match.group("id")),
            "reading":  float(match.group("reading"))
        })
    return meters

def get_powersupply():
    exp = re.compile("^Power supply #(?P<id>\d+)[^:]*:\s*(?P<present>Yes|No)[^:]*:\s*(?P<redundant>Yes|No)[^:]*:\s*(?P<condition>\S+)[^:]*:\s*(?P<hotplug>\S+)[^:]*:\s*(?P<reading>\d+) Watts", re.I | re.M)
    supplies = []
    for match in re.finditer(exp, _get_system_feature("powersupply")):
        supplies.append({
            "id":           int(match.group("id")),
            "present":      match.group("present") == "Yes",
            "redundant":    match.group("redundant") == "Yes",
            "condition":    match.group("condition"),
            "hotplug":      match.group("hotplug"),
            "reading":      float(match.group("reading"))
        })
    return supplies

def get_temp():
    exp = re.compile("^#(?P<id>\d+)\s+(?P<location>\S+)\s+(?P<temp>\d+)C/\d+F\s+(?P<threshold>\d+)C/\d+F", re.I | re.M)
    temps = []
    for match in re.finditer(exp, _get_system_feature("temp")):
        temps.append({
            "id":           int(match.group("id")),
            "location":     match.group("location"),
            "temp":         float(match.group("temp")),
            "threshold":    float(match.group("threshold"))
        })
    return temps
