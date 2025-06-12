import os

def guess_password(target_email, password_file):
    
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        return

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    print(f"[*] Starting to guess passwords for {target_email}...\n")

    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}")
        
        
    print("\nFinished guessing passwords.")

if __name__ == "__main__":
    print("Gmailpassli")
    print("Version: 1.0")
    print("[-] Tool Created by Your Name")
    print("[-] Enter the victim's Gmail:")
    email = input("Enter the victim's Gmail: ")
    password_file = input("Enter password file: ")
    guess_password(email, password_file)
