import random
import string
import tkinter as tk
from tkinter import messagebox

# دالة لتخمين كلمة المرور
def guess_password():
    target_email = email_entry.get()
    target_password = password_entry.get()
    attempts = 0
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        guess = ''.join(random.choices(characters, k=len(target_password)))
        attempts += 1
        
        if guess == target_password:
            messagebox.showinfo("Success", f"Password guessed successfully:\npassword = {guess}\nemail = {target_email}\nin {attempts} attempts.")
            break

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("PASSGLUINX")

# عنوان
title_label = tk.Label(root, text="PASSGLUINX", font=("Arial", 24))
title_label.pack(pady=20)

# حقل البريد الإلكتروني
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# حقل كلمة المرور
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# زر بدء التخمين
guess_button = tk.Button(root, text="Guess Password", command=guess_password)
guess_button.pack(pady=20)

# تشغيل التطبيق
root.mainloop()
