import os
import sys
from colorama import Fore, Style
from pyfiglet import figlet_format

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_password(password_file, target_email):
    # تحقق من وجود ملف كلمات المرور
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        sys.exit()

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    print("[*] Starting to guess passwords...\n")

    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}")
        print(f"{target_email} : {password}")

    print("\nFinished guessing passwords.")
    input("Press Enter to exit...")
    sys.exit()

if __name__ == "__main__":
    clear_screen()
    
    # عرض اسم الأداة بتنسيق ASCII
    ascii_art = figlet_format("Gmailpassli", font="slant")
    print(Fore.RED + ascii_art)
    print(Style.RESET_ALL + "Version: 1.0")
    print("[-] Tool Created by Your Name")
    
    # إدخال البريد الإلكتروني واسم ملف كلمات المرور من المستخدم
    target_email = input("Enter your email: ")
    password_file = input("Enter password file: ")

    print(f"Using password file: {password_file}")
    guess_password(password_file, target_email)
