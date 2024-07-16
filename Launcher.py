import os
import fade

def display_ascii_art():
    """Display welcome ASCII art."""
    ascii_art = """
███████╗██╗██╗     ███████╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║██║     ██╔════╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██║██║     █████╗      █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝      ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(fade.purplepink(ascii_art))

def file_exists(filename):
    """Search for the file in the current directory and subdirectories."""
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return None

def main():
    display_ascii_art()
    filename = input("Enter the filename to look for: ")
    result = file_exists(filename)

    if result:
        print(fade.purplepink(f"The file '{filename}' was found at: {result}"))
    else:
        print(fade.red(f"The file '{filename}' does not exist in the current directory or subdirectories."))

if __name__ == "__main__":
    main()
