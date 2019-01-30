def _get_system_feature(feature):
    if feature == "fans":
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
