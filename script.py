import subprocess
import os
import re


print("beginning script")

protontricks_list = None

try:
    protontricks_list = subprocess.run(['mmmmmmmmmmmm', "-l"], capture_output=True)
except:
    print("ERROR: Please install protontricks onto your linux distribution before continuing")
    exit()

games = []

print("==================")
print("fetching all games")

for i in protontricks_list.stdout.decode('utf-8').split('\n')[1:]:
    # find all app id => find all app names
    app_id_match = re.findall(r"\(\d+\)$", i)
    # if no app id found, skip
    if len(app_id_match) == 0:
        continue
    # else add to games list
    app_id = app_id_match[0][1:-1]
    games.append(app_id)
    print(f"Game fetched: appid={app_id}")

# will contain all library folder locations to search for any games compatdata file

print("=====================================")
print("finding all steam game download paths")

possible_paths = []

with open(f"{os.path.expanduser("~")}/.steam/steam/steamapps/libraryfolders.vdf", "r") as file:
    for line in file.readlines():
        if "path" not in line:
            continue
        path = re.split(r"\s+", line)[2][1:-1]
        # returns ["", "path", "{filePath}"]
        possible_paths.append(path + "/steamapps/compatdata")
        print(f"Found library path {path}")
    file.close()

# assign each path to a game by checking each path for what games are in the path

print("==========================")
print("Assigning each game a path")

game_to_path_dict = {}

for path in possible_paths:
    list_of_apps = os.listdir(path)
    for game in games:
        if game in list_of_apps:
            game_to_path_dict[game] = path
            print(f"appid {game} found in path {path}")

# now look into each game and add the following line to ./pfx/user.reg
# "discord_rpc"="native,builtin" under the section [Software\\Wine\\DllOverrides] {someNumberHere}

print("=========================================")
print("adding discord_rpc dll to each found game")

for game in games:
    try:
        data = ""
        with open(f"{game_to_path_dict[game]}/{game}/pfx/user.reg", "r") as file:
            data = file.readlines()
        currentLine = 0
        for i, item in enumerate(data):
            # need to fix this check as it is not working for some reason
            if r"Software\\Wine\\DllOverrides" in item:
                currentLine = i + 2 # add 2 to jump over time and title lines
                break
        # order alphabetically as does winecfg (could cut step out probably)
        while '"discord_rpc"="native,builtin"' > data[currentLine]:
            currentLine+=1
        if '"discord_rpc"="native,builtin"' in data[currentLine]:
            print(f"game {game} already has discord_rpc, did not change {game_to_path_dict[game]}/{game}/pfx/user.reg file")
            continue
        data.insert(currentLine, '"discord_rpc"="native,builtin"\n')
        with open(f"{game_to_path_dict[game]}/{game}/pfx/user.reg", "w") as file:
            file.write("".join(data))
            file.close()
            print(f"added discord_rpc to game {game} in {game_to_path_dict[game]}/{game}/pfx/user.reg")
    except:
        print(f"Could not read user.reg of appid {game}, game likely does not use proton")

print("===============")
print("script finished")
