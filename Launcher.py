import os
import time
import subprocess
import fade

# Define paths to executables
BLOXSTRAP_PATH = r"C:\Path\To\Bloxstrap\bloxstrap.exe"
FAST_FLAGS_PATH = r"C:\Path\To\FastFlags\flag1.json"
ROBLOX_PROCESS_NAME = "RobloxPlayerBeta.exe"

def display_ascii_art():
    ascii_art = """
██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗    ██╗      █████╗ ██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██║     ██╔══██╗██║   ██║██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║     ███████║██║   ██║██║     ███████║█████╗  ██████╔╝
██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║     ██╔══██║██║   ██║██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ███████╗██║  ██║╚██████╔╝╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    print(fade.purplepink(ascii_art))

def show_credits():
    credits = """
Credits:
- Creator: Sloupsy
- Inspired by the Roblox community
- Using the 'fade' library for text effects
    """
    print(fade.purple(credits))

def launch_application(command):
    try:
        subprocess.Popen(command)
    except FileNotFoundError:
        print(fade.red(f"Error: The application could not be found at {command}."))

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_ascii_art()

        print("\n============================")
        print("[1] Launch Roblox")
        print("[2] Close Roblox")
        print("[3] Launch Bloxstrap with FastFlags 1")
        print("[4] Show Credits")
        print("[5] Exit")
        print("============================")

        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            print(fade.purplepink("Launching Roblox..."))
            time.sleep(2)
            launch_application(BLOXSTRAP_PATH)
            input("Press any key to return to the menu...")
        elif choice == '2':
            print(fade.purplepink("Closing Roblox..."))
            time.sleep(2)
            os.system(f"taskkill /f /im {ROBLOX_PROCESS_NAME}")
            input("Press any key to return to the menu...")
        elif choice == '3':
            print(fade.purple("Launching Bloxstrap with FastFlags 1..."))
            time.sleep(2)
            launch_application([BLOXSTRAP_PATH, '--fastFlags', FAST_FLAGS_PATH])
            input("Press any key to return to the menu...")
        elif choice == '4':
            show_credits()
            input("Press any key to return to the menu...")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    menu()
