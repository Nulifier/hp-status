import re

_UNITS = {
	"KB": 1000,
	"MB": 1000 * 1000,
	"GB": 1000 * 1000 * 1000,
	"TB": 1000 * 1000 * 1000 * 1000,
	"PB": 1000 * 1000 * 1000 * 1000 * 1000,
	"EB": 1000 * 1000 * 1000 * 1000 * 1000 * 1000,
	"KIB": 1024,
	"MIB": 1024 * 1024,
	"GIB": 1024 * 1024 * 1024,
	"TIB": 1024 * 1024 * 1024 * 1024,
	"PIB": 1024 * 1024 * 1024 * 1024 * 1024,
	"EIB": 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
}

def from_nice_size(size, iec=False):
	m = re.search(r"(\d+)\s*(\S+)", size)
	amount = m.group(1)
	unit = m.group(2).upper()

	# Check if we are to force IEC units
	if iec and len(unit) == 2:
		unit = unit[0] + "I" + unit[1]
	
	return int(amount) * _UNITS[unit]
