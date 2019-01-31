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

def _get_storage_controllers():
    return (
        "Smart Array P410i in Slot 0 (Embedded)\n"
        "   Controller Status: OK\n"
        "   Cache Status: OK\n"
        "   Battery/Capacitor Status: OK"
    )

def _get_storage_drives(slot):
    return (
        "   physicaldrive 1I:1:1 (port 1I:box 1:bay 1, 2 TB): OK\n"
        "   physicaldrive 1I:1:2 (port 1I:box 1:bay 2, 2 TB): OK\n"
        "   physicaldrive 1I:1:3 (port 1I:box 1:bay 3, 2 TB): OK\n"
        "   physicaldrive 1I:1:4 (port 1I:box 1:bay 4, 2 TB): OK\n"
        "   physicaldrive 2I:1:5 (port 2I:box 1:bay 5, 2 TB): OK\n"
        "   physicaldrive 2I:1:6 (port 2I:box 1:bay 6, 2 TB): OK\n"
        "   physicaldrive 2I:1:7 (port 2I:box 1:bay 7, 2 TB): Failed\n"
        "   physicaldrive 2I:1:8 (port 2I:box 1:bay 8, 2 TB): OK"
    )

def _get_storage_drives_detail(slot):
    return """
Smart Array P410i in Slot 0 (Embedded)

   Array A

      physicaldrive 1I:1:1
         Port: 1I
         Box: 1
         Bay: 1
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10001
         Serial Number: S33ZJ9EF301976
         WWID: 3000000000000000
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 41
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 1I:1:2
         Port: 1I
         Box: 1
         Bay: 2
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10001
         Serial Number: S33ZJ9CF404160
         WWID: 3000000000000001
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 44
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 1I:1:3
         Port: 1I
         Box: 1
         Bay: 3
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10005
         Serial Number: S34RJ9AF813381
         WWID: 3000000000000002
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 24
         Maximum Temperature (C): 56
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 1I:1:4
         Port: 1I
         Box: 1
         Bay: 4
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10007
         Serial Number: S34RJ9AG131043
         WWID: 3000000000000003
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 24
         Maximum Temperature (C): 52
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 2I:1:5
         Port: 2I
         Box: 1
         Bay: 5
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10001
         Serial Number: S321J9AFC01521
         WWID: 3000000000000004
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 44
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 2I:1:6
         Port: 2I
         Box: 1
         Bay: 6
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10001
         Serial Number: S33ZJ9FF602149
         WWID: 3000000000000005
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 23
         Maximum Temperature (C): 48
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 2I:1:7
         Port: 2I
         Box: 1
         Bay: 7
         Status: Failed
         Last Failure Reason: Mark bad failed
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10001
         Serial Number: S321J9AFC01509
         WWID: 3000000000000006
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 27
         Maximum Temperature (C): 45
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None

      physicaldrive 2I:1:8
         Port: 2I
         Box: 1
         Bay: 8
         Status: OK
         Drive Type: Data Drive
         Interface Type: SATA
         Size: 2 TB
         Drive exposed to OS: False
         Logical/Physical Block Size: 512/4096
         Rotational Speed: 5400
         Firmware Revision: 2BC10007
         Serial Number: S34RJ9EG131414
         WWID: 3000000000000007
         Model: ATA     ST2000LM003 HN-M
         SATA NCQ Capable: True
         SATA NCQ Enabled: True
         Current Temperature (C): 24
         Maximum Temperature (C): 48
         PHY Count: 1
         PHY Transfer Rate: 3.0Gbps
         Sanitize Erase Supported: False
         Shingled Magnetic Recording Support: None
"""
