import os
import time
import subprocess
import json
import requests
import fade

# Constants
ROBLOX_PROCESS_NAME = "RobloxPlayerBeta.exe"
SETTINGS_FILE = "settings.json"
UPDATE_URL = "https://raw.githubusercontent.com/Sloupsy/Roblox-Launcher/main/latest_version.json"

# Global Variables
roblox_launcher_path = ""
launch_count = 0

def set_console_size():
    os.system("mode con: cols=130 lines=30")

def load_settings():
    global roblox_launcher_path, launch_count
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            roblox_launcher_path = settings.get("roblox_launcher_path", "")
            launch_count = settings.get("launch_count", 0)

def save_settings():
    global roblox_launcher_path, launch_count
    with open(SETTINGS_FILE, "w") as file:
        json.dump({"roblox_launcher_path": roblox_launcher_path, "launch_count": launch_count}, file)

def check_for_updates():
    response = requests.get(UPDATE_URL)
    if response.status_code == 200:
        latest_version_info = response.json()
        latest_version = latest_version_info['version']
        current_version = "1.0.0"  # Change to your current version

        if latest_version > current_version:
            print("A new update is available. Downloading...")
            script_url = latest_version_info['script_url']
            update_script(script_url)

def update_script(script_url):
    response = requests.get(script_url)
    if response.status_code == 200:
        with open("launcher.py", "wb") as f:
            f.write(response.content)
        print("Update downloaded successfully. Please restart the script.")
        exit()  # Exit after updating

def display_ascii_art():
    ascii_art = """
██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗    ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    print(fade.purplepink(ascii_art.strip()))

def launch_application(command):
    try:
        subprocess.Popen(command)
    except Exception as e:
        print(fade.red(f"Error: {e}"))
        input("Press any key to return to the menu...")

def is_roblox_running():
    try:
        tasklist = subprocess.check_output(['tasklist'], universal_newlines=True)
        return ROBLOX_PROCESS_NAME in tasklist
    except Exception as e:
        print(fade.red(f"Error checking processes: {e}"))
        return False

def get_rank():
    if launch_count < 10:
        return "Explorer"
    elif launch_count < 20:
        return "Warrior"
    elif launch_count < 50:
        return "Champion"
    elif launch_count < 80:
        return "Hero"
    elif launch_count < 100:
        return "Mastermind"
    elif launch_count < 120:
        return "Strategist"
    elif launch_count < 140:
        return "Builder"
    elif launch_count < 180:
        return "Adventurer"
    elif launch_count < 500:
        return "Elite Player"
    elif launch_count < 5000:
        return "GOD OF ROBLOX"
    else:
        return "Owner of the Launcher"

def display_current_rank():
    rank = get_rank()
    print(f"Current Rank: {rank} (Launches: {launch_count})\n")

def launch_roblox():
    global launch_count
    if not roblox_launcher_path:
        print(fade.red("Roblox launcher path is not set. Please set it in the menu."))
        return
    launch_count += 1
    save_settings()
    rank = get_rank()
    print(fade.purplepink(f"Launching Roblox... (Rank: {rank})"))
    time.sleep(2)
    launch_application([roblox_launcher_path])

def show_rank_page():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_ascii_art()
    print("\n============================")
    print("Ranks and Requirements:")
    print("============================")
    print("0-9 Launches: Explorer")
    print("10-19 Launches: Warrior")
    print("20-49 Launches: Champion")
    print("50-79 Launches: Hero")
    print("80-99 Launches: Mastermind")
    print("100-119 Launches: Strategist")
    print("120-139 Launches: Builder")
    print("140-179 Launches: Adventurer")
    print("180-499 Launches: Elite Player")
    print("500-4999 Launches: GOD OF ROBLOX")
    print("5000+ Launches: Owner of the Launcher")
    print("============================\n")
    input("Press any key to return to the menu...")

def set_roblox_launcher_path():
    global roblox_launcher_path
    roblox_launcher_path = input("Enter the full path to the Roblox launcher: ")
    save_settings()

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        set_console_size()
        display_ascii_art()
        display_current_rank()
        
        print("\n============================")
        print("[1] Launch Roblox")
        print("[2] Close Roblox")
        print("[3] View Rank Page")
        print("[4] Set Roblox Launcher Path")
        print("[5] Exit")
        print("============================")

        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            launch_roblox()
        elif choice == '2':
            if is_roblox_running():
                print(fade.purplepink("Closing Roblox..."))
                os.system(f"taskkill /f /im {ROBLOX_PROCESS_NAME}")
                time.sleep(2)
            else:
                print(fade.red("Roblox is not running."))
                time.sleep(2)
        elif choice == '3':
            show_rank_page()
        elif choice == '4':
            set_roblox_launcher_path()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    check_for_updates()
    load_settings()
    menu()
