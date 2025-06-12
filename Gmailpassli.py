import os

def guess_password(password_file):
    # تحقق من وجود ملف كلمات المرور
    if not os.path.isfile(password_file):
        print("Password file not found. Exiting.")
        return

    # اسم البريد الإلكتروني الثابت
    target_email = "email@example.com"  # استبدل بهذا البريد الإلكتروني

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    print("[*] Starting to guess passwords...\n")

    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}")
        
        # هنا يمكنك إضافة منطق لتخمين كلمة المرور
        # على سبيل المثال، إذا كنت تريد طباعة البريد وكلمة المرور
        print(f"{target_email} : {password}")

    print("\nFinished guessing passwords.")

if __name__ == "__main__":
    print("Gmailpassli")
    print("Version: 1.0")
    print("[-] Tool Created by Your Name")
    
    # تحديد اسم ملف كلمات المرور بشكل ثابت
    password_file = "passwords.txt"  # تأكد من أن الملف موجود في نفس الدليل
    guess_password(password_file)
