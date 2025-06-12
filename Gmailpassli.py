import os
import sys
from colorama import Fore, Style
from pyfiglet import figlet_format

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_password_file(file_name):
    for root, dirs, files in os.walk('/'):  # يبدأ البحث من الجذر
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def load_passwords(password_file):
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        sys.exit()

    with open(password_file, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def guess_password(passwords, target_email):
    print("[*] Starting to guess passwords...\n")

    for password in passwords:
        print(f"Trying password: {password}")
        # هنا يمكنك إضافة شرط للتحقق مما إذا كانت كلمة المرور صحيحة
        if attempt_login(target_email, password):
            print(f"Password found: {password}")
            return
    print("Password not found. Exiting.")
    sys.exit()

def attempt_login(email, password):
    # هنا يمكنك إضافة المنطق للتحقق من كلمة المرور
    # حاليًا، ستعيد False فقط
    return False

if __name__ == "__main__":
    clear_screen()
    
    ascii_art = figlet_format("Gmailpassli", font="slant")
    print(Fore.RED + ascii_art)
    print(Style.RESET_ALL + "Version: 1.0")
    print("[-] Tool Created by Your Name")
    
    target_email = input("Enter your email: ")
    password_file_name = input("Enter password file name: ")

    # البحث عن الملف في جميع أنحاء الجهاز
    password_file_path = find_password_file(password_file_name)

    if not password_file_path:
        print("Password file not found. Exiting.")
        sys.exit()

    print(f"Using password file: {password_file_path}")

    passwords = load_passwords(password_file_path)
    guess_password(passwords, target_email)
