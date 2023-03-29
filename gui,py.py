import tkinter as tk
import password_manager

def create_password_dialog():
    # create a dialog box to get user input
    dialog = tk.Toplevel()
    dialog.title("Create Password")
    label1 = tk.Label(dialog, text="Number of characters:")
    label1.pack(padx=20, pady=10)
    entry1 = tk.Entry(dialog)
    entry1.pack(padx=20, pady=10)
    label2 = tk.Label(dialog, text="Special characters (separate with commas):")
    label2.pack(padx=20, pady=10)
    entry2 = tk.Entry(dialog)
    entry2.pack(padx=20, pady=10)
    button = tk.Button(dialog, text="Create", command=lambda: save_password(entry1, entry2, dialog))
    button.pack(padx=20, pady=10)

def save_password(num_chars_entry, allowed_chars_entry, dialog):
    num_chars = int(num_chars_entry.get())
    allowed_chars = allowed_chars_entry.get()
    password = password_manager.create_password(num_chars, allowed_chars)

    # create a dialog box to get website name
    dialog.withdraw()
    save_dialog = tk.Toplevel()
    save_dialog.title("Save Password")
    label = tk.Label(save_dialog, text="Website:")
    label.pack(padx=20, pady=10)
    entry = tk.Entry(save_dialog)
    entry.pack(padx=20, pady=10)
    button = tk.Button(save_dialog, text="Save", command=lambda: store_password(entry, password, save_dialog))
    button.pack(padx=20, pady=10)

def store_password(website_entry, password, dialog):
    website = website_entry.get()
    password_manager.store_password(website, password)
    dialog.destroy()
    root.deiconify()

def view_passwords_dialog():
    # create a dialog box to display stored passwords
    dialog = tk.Toplevel()
    dialog.title("View Passwords")
    pairs = password_manager.view_passwords()
    for website, password in pairs:
        label = tk.Label(dialog, text=f"{website}: {password}")
        label.pack(padx=20, pady=10)

def main():
    global root
    root = tk.Tk()

    # create the main window
    root.title("Password Manager")
    root.geometry("300x150")
    create_button = tk.Button(root, text="Create Password", command=create_password_dialog)
    create_button.pack(padx=20, pady=10)
    view_button = tk.Button(root, text="View Passwords", command=view_passwords_dialog)
    view_button.pack(padx=20, pady=10)

    # start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
