# protontricks discord rich presence adding script
This script allows you to quickly add discord rich presence to all of your steam proton run games.
## Requirements
Software:
- Python 3
- protontricks
- Steam
- proton
Needed to have finished this guide to have ability to add discord_prc to registry files for wine registries:
[Enabling Discord Rich Presence - ValveSoftware]https://github.com/ValveSoftware/Proton/wiki/Enabling-Discord-Rich-Presence
## Information
Very simple python script which finds your games appids through protontricks and then uses and library folders to identify where to find the wine prefix for each game to add discord rich presence to it through its registry.