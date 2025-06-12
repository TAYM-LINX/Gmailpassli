import os
import sys
from colorama import Fore, Style
from pyfiglet import figlet_format

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_passwords(password_file):
    # تحقق من وجود ملف كلمات المرور
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        sys.exit()

    with open(password_file, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def guess_password(passwords, target_email):
    print("[*] Starting to guess passwords...\n")

    for password in passwords:
        print(f"Trying password: {password}")
        print(f"{target_email} : {password}")

    print("\nFinished guessing passwords.")
    input("Press Enter to exit...")
    sys.exit()

if __name__ == "__main__":
    clear_screen()
    
    ascii_art = figlet_format("Gmailpassli", font="slant")
    print(Fore.RED + ascii_art)
    print(Style.RESET_ALL + "Version: 1.0")
    print("[-] Tool Created by Your Name")
    
    target_email = input("Enter your email: ")
    password_file = input("Enter password file (e.g., rockyou.txt): ")

    # إذا كان اسم الملف هو rockyou.txt، استخدمه مباشرة
    if password_file.lower() == "rockyou.txt":
        password_file = "rockyou.txt"

    print(f"Using password file: {password_file}")

    passwords = load_passwords(password_file)
    guess_password(passwords, target_email)
