import os
import time
import subprocess
import fade
import json
import requests

# Constants
ROBLOX_PROCESS_NAME = "RobloxPlayerBeta.exe"
LAUNCH_COUNT_FILE = "launch_count.json"
SETTINGS_FILE = "settings.json"
CURRENT_VERSION = "1.0.1"
UPDATE_URL = "https://raw.githubusercontent.com/<username>/<repository>/main/latest_version.json"  # JSON containing latest version info
SCRIPT_URL = "https://raw.githubusercontent.com/<username>/<repository>/main/launcher.py"  # URL for the latest script

# Global Variables
roblox_launcher_path = ""

# Function to check for updates
def check_for_updates():
    try:
        response = requests.get(UPDATE_URL)
        latest_info = response.json()
        latest_version = latest_info['version']
        
        if latest_version != CURRENT_VERSION:
            print(fade.yellow(f"Update available: {latest_version}. Downloading..."))
            download_latest_script()
        else:
            print(fade.green("You are using the latest version."))
    except Exception as e:
        print(fade.red(f"Error checking for updates: {e}"))

# Function to download the latest script
def download_latest_script():
    try:
        response = requests.get(SCRIPT_URL)
        with open("launcher.py", "wb") as file:
            file.write(response.content)
        print(fade.green("Update downloaded successfully. Please restart the application."))
        time.sleep(2)
        exit()  # Exit the program after updating
    except Exception as e:
        print(fade.red(f"Error downloading the update: {e}"))

# Set the console size
def set_console_size(width=130, height=30):
    os.system(f"mode con: cols={width} lines={height}")

# Load the launch count from a file
def load_launch_count():
    if os.path.exists(LAUNCH_COUNT_FILE):
        with open(LAUNCH_COUNT_FILE, "r") as file:
            return json.load(file).get("launch_count", 0)
    return 0

# Save the launch count to a file
def save_launch_count(count):
    with open(LAUNCH_COUNT_FILE, "w") as file:
        json.dump({"launch_count": count}, file)

# Load settings from a file
def load_settings():
    global roblox_launcher_path
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            roblox_launcher_path = settings.get("roblox_launcher_path", "")
            print(fade.purplepink(f"Loaded Roblox Launcher Path: {roblox_launcher_path}"))

# Save settings to a file
def save_settings():
    global roblox_launcher_path
    with open(SETTINGS_FILE, "w") as file:
        json.dump({"roblox_launcher_path": roblox_launcher_path}, file)

launch_count = load_launch_count()
load_settings()

# Display ASCII art
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

# Launch the application
def launch_application(command):
    try:
        subprocess.Popen(command)
    except Exception as e:
        print(fade.red(f"Error: {e}"))
        input("Press any key to return to the menu...")

# Check if Roblox is running
def is_roblox_running():
    try:
        tasklist = subprocess.check_output(['tasklist'], universal_newlines=True)
        return ROBLOX_PROCESS_NAME in tasklist
    except Exception as e:
        print(fade.red(f"Error checking processes: {e}"))
        return False

# Get the rank based on launch count
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

# Display the current rank
def display_current_rank():
    rank = get_rank()
    print(f"Current Rank: {rank} (Launches: {launch_count})\n")

# Launch Roblox
def launch_roblox():
    global launch_count
    launch_count += 1
    save_launch_count(launch_count)
    rank = get_rank()
    print(fade.purplepink(f"Launching Roblox... (Rank: {rank})"))
    time.sleep(2)
    launch_application(roblox_launcher_path)

# Show rank page
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

# Set Roblox launcher path
def set_roblox_launcher_path():
    global roblox_launcher_path
    roblox_launcher_path = input("Enter the full path to the Roblox launcher: ")
    save_settings()

# Main menu
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
    menu()
