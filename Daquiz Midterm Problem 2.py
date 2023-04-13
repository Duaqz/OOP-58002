import tkinter as tk

class FullNameGUI:
    def __init__(self, master):
        self.master = master
        master.title("My Full Name")
        master.configure(background="white")
        master.geometry("350x300")
        master.resizable(False, False)

        self.title_label = tk.Label(master, text="My Full Name", font=("Verdana", 16), fg="red", bg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.given_name_label = tk.Label(master, text="Enter Given Name:", fg="red", bg="white")
        self.given_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.middle_name_label = tk.Label(master, text="Enter Middle Name:", fg="red", bg="white")
        self.middle_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.last_name_label = tk.Label(master, text="Enter Last Name:", fg="red", bg="white")
        self.last_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.full_name_label = tk.Label(master, text="Enter My Full Name is:", fg="red", bg="white")
        self.full_name_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.given_name_entry = tk.Entry(master)
        self.given_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.middle_name_entry = tk.Entry(master)
        self.middle_name_entry.grid(row=2, column=1, padx=10, pady=5)

        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=5)

        self.full_name_entry = tk.Entry(master, state="readonly")
        self.full_name_entry.grid(row=4, column=1, padx=10, pady=5)

        self.show_button = tk.Button(master, text="Show Full Name", command=self.show_full_name, bg="white", width=15)
        self.show_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all, bg="white", width=15)
        self.clear_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    def show_full_name(self):
        given_name = self.given_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()

        full_name = f"{last_name}, {given_name} {middle_name}"
        self.full_name_entry.configure(state="normal")
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.insert(0, full_name)
        self.full_name_entry.configure(state="readonly", fg="red")

    def clear_all(self):
        self.given_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.full_name_entry.configure(state="normal")
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.configure(state="readonly")

root = tk.Tk()
app = FullNameGUI(root)
root.mainloop()
