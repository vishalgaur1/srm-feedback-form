#Make Sure to install all the packages before use
import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def submit_form(event=None):  # Add event=None as a parameter
    email = email_entry.get()
    password = password_entry.get()
    theory = int(theory_entry.get())
    labs = int(lab_entry.get())
    comment = comment_entry.get()

    # Initialize Chrome WebDriver
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get("https://academia.srmist.edu.in/#Course_Feedback")
    time.sleep(3)

    # Enter Email and press Enter
    for key in email:
        pyautogui.press(key)
    pyautogui.press("enter")
    time.sleep(3)

    # Enter Password and press Enter
    for key in password:
        pyautogui.press(key)
    pyautogui.press("enter")

    time.sleep(30)

    # Enter Theory Feedback
    for i in range(theory):
        for j in range(14):
            if j == 0:
                pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.press("down")
            pyautogui.press("enter")

        pyautogui.press("tab")
        for key in comment:
            pyautogui.press(key)

    # Enter Lab Feedback
    pyautogui.press("tab")
    for i in range(labs):
        for j in range(13):
            if j == 0:
                pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.press("down")
            pyautogui.press("enter")

        pyautogui.press("tab")
        for key in comment:
            pyautogui.press(key)

    # Submit Feedback
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(15)

    driver.quit()
    messagebox.showinfo("Feedback Submission", "Feedback has been submitted successfully.")

# Create the main window
root = tk.Tk()
root.title("Feedback Submission")
root.configure(bg="#f2f2f2")

# Create a label and entry for email id
email_label = tk.Label(root, text="Email:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
email_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for password
password_label = tk.Label(root, text="Password:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label and entry for number theory of subjects
theory_label = tk.Label(root, text="Number of Theory subjects:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
theory_label.grid(row=2, column=0, padx=10, pady=10)
theory_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
theory_entry.grid(row=2, column=1, padx=10, pady=10)
theory_entry.config(validate="key", validatecommand=(root.register(lambda s: s.isdigit()), '%S'))

# Create a label and entry for number of lab subjects
lab_label = tk.Label(root, text="Number of lab subjects:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
lab_label.grid(row=3, column=0, padx=10, pady=10)
lab_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
lab_entry.grid(row=3, column=1, padx=10, pady=10)
lab_entry.config(validate="key", validatecommand=(root.register(lambda s: s.isdigit()), '%S'))

comment_label = tk.Label(root, text="Comment:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
comment_label.grid(row=4, column=0, padx=10, pady=10)
comment_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
comment_entry.grid(row=4, column=1, padx=10, pady=10)


submit_button = tk.Button(root, text="Submit", bg="#4CAF50", fg="white", font=("Helvetica", 12), command=submit_form)
submit_button.grid(row=5, column=1, padx=10, pady=20)

rel_label = tk.Label(root, text="SIT BACK AND RELAX, DO NOT INTERRUPT", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12), justify='center')
rel_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


# Create a label frame for rules
rules_frame = tk.LabelFrame(root, text="Rules", bg="#f2f2f2", font=("Helvetica", 12))
rules_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="we")


# Create a listbox to display the rules with bullets
rules_listbox = tk.Listbox(rules_frame, bg="#f2f2f2", fg="#666666", font=("Helvetica", 12), selectbackground="#f2f2f2", selectmode="none", width=60)
rules_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="w")


# Define the rules
rules = [
    "MAKE SURE YOUR CAPS LOCK IS OFF",
    "MAKE SURE YOU FILL ALL THE FIELDS",
    "MAKE SURE YOU HAVE A GOOD INTERNET CONNECTION",
]

# Insert rules into the listbox with bullets
for index, rule in enumerate(rules, start=1):
    rules_listbox.insert(index, f"• {rule}")

# Disable the vertical scrollbar
rules_listbox.config(yscrollcommand="")


root.bind('<Return>', submit_form)
root.mainloop()
