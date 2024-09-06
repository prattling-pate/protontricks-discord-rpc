# protontricks discord rich presence adding script
This script allows you to quickly add discord rich presence to all of your steam proton run games without manually adding discord_prc to every game using protontricks winecfg (https://github.com/ValveSoftware/Proton/wiki/Enabling-Discord-Rich-Presence).
## Requirements
Needed to have finished this guide to have ability to add discord_prc to registry files for wine registries: \
https://github.com/ValveSoftware/Proton/wiki/Enabling-Discord-Rich-Presence \
Software:
- Python 3
- protontricks
- Steam
- Proton
## Information
Very simple python script which finds your games appids through protontricks and then uses the library folders to identify where to find the wine prefix for each game to add discord rich presence to it through its user registry.
## Usage
Designed for Linux, tested on ArchLinux. \
To execute the script simply run the following command in a terminal once you're in the same folder.
```
python script.py
```
