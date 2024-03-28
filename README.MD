# LnkAnalyser
A Python module for the forensic analysis of Windows shortcuts (they're surprisingly useful.) This package is parses
shortcuts against the [Windows MS-SHLLINK standard](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943).

## Usage
    TODO: Rewrite and add proper documentation

```
from LnkAnalyser import lnkanalyser

analyser = lnkanalyser.go("Microsoft Office.lnk")

print("Header Size: {}".format(analyser["header_size"])
print("Creation of Target: {}".format(analyser["creation_time_of_link_target"]))
...
```

You can convert the timestamp formats out of the byte pattern using the helper function, convert_to_readable_date()

```
print("Creation of Target: {}".format(analyser["creation_time_of_link_target"]))

print("Readable date: {}".format(
  lnkanalyser.convert_to_readable_date(analyser["creation_time_of_link_target"])
)
```

## Properties
The dictionary returned by ```lnkanalyser.go()``` has a full parse of the header structure of Windows shortcut files. You
can inspect the keys in the structure yourself, but this list is a breakdown of what's in there.

### Header
* header_size: The header size should always be 0x0000004C as the header is always 76 bytes. This value is taken from
  the shortcut file, so if it's not 0x0000004C, then the shortcut file would be invalid. This package obeys the header
  size. A smaller header size will invalid other properties in the header structure only.
* link_class_id: The GUID representing the link class.
* link_flags: The byte pattern for the link flags as specified by the Microsoft standard.
* file_attributes: The file attributes of the shortcut
* creation_time_of_link_target: This is the timestamp of the creation date for the target of the shortcut. It is in 
MSTYP date format, and can be converted using ```lnkanalyser.convert_to_readable_date()```

* access_time_of_link_target: This timestamp covers the last access time of the shortcut target. It can be converted to
  a readable format using ```lnkanalyser.convert_to_readable_date()```
* write_time_of_link_target: This timestamp is for the last time the shortcut target was modified. It can be converted
  to a readonable format using ```lnkanalyser.convert_to_readable_date()```
* target_file_size: This value is the file size of the target binary at the time the shortcut was created.
* icon_index: Icon index refers to the position within the icon file, usually 0.
* expected_window_state: This value refers to the Window state of the target (minimised, normal, maximised). No helper
  function exists yet.
* hot_key: 
* reserved_one: This should be null per the Windows standard.
* reserved_two: This should be null per the Windows standard.
* reserved_three: This should be null per the Windows standard.
