import os
import sys
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_password(password_file):
    # تحقق من وجود ملف كلمات المرور
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        sys.exit()

    target_email = "email@example.com"  # استبدل بهذا البريد الإلكتروني

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    print("[*] Starting to guess passwords...\n")

    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}")
        print(f"{target_email} : {password}")

    print("\nFinished guessing passwords.")
    # انتظر حتى يضغط المستخدم على أي مفتاح قبل الخروج
    input("Press Enter to exit...")
    sys.exit()

if __name__ == "__main__":
    clear_screen()
    print(Fore.RED + "Gmailpassli")
    print(Style.RESET_ALL + "Version: 1.0")
    print("[-] Tool Created by Your Name")
    
    password_file = "passwords.txt"  # تأكد من أن الملف موجود في نفس الدليل
    print("Enter your email: ")
    print("Email: email@example.com")
    print("Enter password file: ")
    print(f"Using password file: {password_file}")
    
    guess_password(password_file)
