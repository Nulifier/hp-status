import subprocess, re

FEATURES = [
	"fans",
	"powermeter",
	"powersupply",
	"temp"
]

def _get_system_feature(feature):
    return subprocess.check_output('hpasmcli -s "SHOW {}"'.format(feature.upper()))
    if feature == "fans":
        # return subprocess.check_output('hpasmcli -s "SHOW FANS"')
        return (
            "Fan  Location        Present Speed  of max  Redundant  Partner  Hot-pluggable\n"
            "---  --------        ------- -----  ------  ---------  -------  -------------\n"
            "#1   SYSTEM          Yes     NORMAL  13%     Yes        0        Yes\n"
            "#2   SYSTEM          Yes     NORMAL  18%     Yes        0        Yes\n"
            "#3   SYSTEM          Yes     NORMAL  21%     Yes        0        Yes\n"
            "#4   SYSTEM          Yes     NORMAL  18%     Yes        0        Yes\n"
            "#5   SYSTEM          Yes     NORMAL  13%     Yes        0        Yes\n"
            "#6   SYSTEM          Yes     NORMAL  13%     Yes        0        Yes"
        )
    elif feature == "powermeter":
        return (
            "Power Meter #1\n"
            "        Power Reading  : 122\n"
            "Power Meter #2\n"
            "        Power Reading  : 132"
        )
    elif feature == "powersupply":
        return (
            "Power supply #1\n"
            "        Present  : Yes\n"
            "        Redundant: Yes\n"
            "        Condition: Ok\n"
            "        Hotplug  : Supported\n"
            "        Power    : 60 Watts\n"
            "Power supply #2\n"
            "        Present  : Yes\n"
            "        Redundant: Yes\n"
            "        Condition: Ok\n"
            "        Hotplug  : Supported\n"
            "        Power    : 60 Watts"
        )
    elif feature == "temp":
        return (
            "Sensor   Location              Temp       Threshold\n"
            "------   --------              ----       ---------\n"
            "#1        AMBIENT              26C/78F    42C/107F\n"
            "#2        CPU#1                40C/104F   82C/179F\n"
            "#3        CPU#2                 -         82C/179F\n"
            "#4        MEMORY_BD            37C/98F    87C/188F\n"
            "#5        MEMORY_BD            34C/93F    87C/188F\n"
            "#6        MEMORY_BD            33C/91F    87C/188F\n"
            "#7        MEMORY_BD            33C/91F    87C/188F"
        )

def get_fans():
    exp = re.compile("^#(?P<id>\d+)\s+(?P<location>\S+)\s+(?P<present>Yes|No)\s+(?P<speed>\S+)\s+(?P<percentage>\d+)%\s+(?P<redundant>Yes|No)\s+(?P<partner>\d+)\s+(?P<hot_pluggable>Yes|No)$", re.I | re.M)
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
