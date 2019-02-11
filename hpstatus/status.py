import subprocess
import re
from hpstatus import util

def _get_system_feature(feature):
    return subprocess.check_output('/sbin/hpasmcli -s "SHOW {}"'.format(feature.upper()), shell=True).decode("utf-8")

def _get_storage_controllers():
    return subprocess.check_output("/usr/sbin/ssacli ctrl all show status", shell=True).decode("utf-8")

def _get_storage_drives(slot):
    return subprocess.check_output("/usr/sbin/ssacli ctrl slot={} physicaldrive all show status".format(slot), shell=True).decode("utf-8")

def _get_storage_drives_detail(slot):
    return subprocess.check_output("/usr/sbin/ssacli ctrl slot={} physicaldrive all show detail".format(slot), shell=True).decode("utf-8")

def get_fans():
    exp = re.compile(r"^#(?P<id>\d+)\s+(?P<location>\S+)\s+(?P<present>Yes|No)\s+(?P<speed>\S+)\s+(?P<percentage>\d+)%\s+(?P<redundant>Yes|No)\s+(?P<partner>\d+)\s+(?P<hot_pluggable>Yes|No)", re.I | re.M)
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
    exp = re.compile(r"^Power Meter #(?P<id>\d+)\s*Power Reading\s*:\s*(?P<reading>\d+)", re.I | re.M)
    meters = []
    for match in re.finditer(exp, _get_system_feature("powermeter")):
        meters.append({
            "id":       int(match.group("id")),
            "reading":  float(match.group("reading"))
        })
    return meters

def get_powersupply():
    exp = re.compile(r"^Power supply #(?P<id>\d+)[^:]*:\s*(?P<present>Yes|No)[^:]*:\s*(?P<redundant>Yes|No)[^:]*:\s*(?P<condition>\S+)[^:]*:\s*(?P<hotplug>\S+)[^:]*:\s*(?P<reading>\d+) Watts", re.I | re.M)
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
    exp = re.compile(r"^#(?P<id>\d+)\s+(?P<location>\S+)\s+(?P<temp>\d+)C/\d+F\s+(?P<threshold>\d+)C/\d+F", re.I | re.M)
    temps = []
    for match in re.finditer(exp, _get_system_feature("temp")):
        temps.append({
            "id":           int(match.group("id")),
            "location":     match.group("location"),
            "temp":         float(match.group("temp")),
            "threshold":    float(match.group("threshold"))
        })
    return temps

def get_storage_controllers():
    exp = re.compile(r"^\s*(?P<model>.+) in Slot (?P<id>\d+).+Controller Status: (?P<status>\S+).+Cache Status: (?P<cache>\S+).+Battery/Capacitor Status: (?P<battery>\S+)", re.I | re.M | re.S)
    controllers = []
    for match in re.finditer(exp, _get_storage_controllers()):
        controllers.append({
            "id":       int(match.group("id")),
            "model":    match.group("model"),
            "status":   match.group("status"),
            "cache":    match.group("cache"),
            "battery":  match.group("battery")
        })
    return controllers

def get_storage_drives(slot):
    exp = re.compile(r"physicaldrive (?P<location>\S+) \(port (?P<port>[^:]+):box (?P<box>\d+):bay (?P<bay>\d+), (?P<size>[^\)]+)\): (?P<status>\S+)", re.I | re.M)
    drives = []
    for match in re.finditer(exp, _get_storage_drives(slot)):
        drives.append({
            "location": match.group("location"),
            "port":     match.group("port"),
            "box":      int(match.group("box")),
            "bay":      int(match.group("bay")),
            "size":     util.from_nice_size(match.group("size")),
            "status":   match.group("status")
        })
    return drives

def get_storage_drives_detail(slot):
    exp = re.compile(r"physicaldrive (?P<location>\S+)\s+Port: (?P<port>\S+)\s+Box: (?P<box>\d+)\s+Bay: (?P<bay>\d+)\s+Status: (?P<status>\S+).+?Size: (?P<size>\d+ ?\S+).+?Serial Number: (?P<serial>\S+).+?Current Temperature \(C\): (?P<temp>\d+)\s+Maximum Temperature \(C\): (?P<max_temp>\d+)", re.I | re.M | re.S)
    drives = []
    for match in re.finditer(exp, _get_storage_drives_detail(slot)):
        drives.append({
            "location": match.group("location"),
            "port":     match.group("port"),
            "box":      int(match.group("box")),
            "bay":      int(match.group("bay")),
            "size":     util.from_nice_size(match.group("size")),
            "status":   match.group("status"),
            "serial":   match.group("serial"),
            "temp":     float(match.group("temp")),
            "max_temp": float(match.group("max_temp"))
        })
    return drives
