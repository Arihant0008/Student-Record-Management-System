# main_app.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import the database manager class from the other file
from database_manager import DatabaseManager

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")

        # Initialize the database manager
        self.db_manager = DatabaseManager()

        # Set up the window to be fullscreen
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        # Handle window closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # --- UI Elements ---
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        """Creates and places all the widgets in the main window."""
        # Main Title
        title = tk.Label(self.root, text="Student Record Management System", bd=4, relief="raised", bg="#2c3e50", fg="white", font=("Elephant", 40, "bold"))
        title.pack(side="top", fill="x")

        # --- Left Frame for Options ---
        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="#ecf0f1")
        optFrame.place(width=self.width/3.5, height=self.height-100, x=20, y=80)

        button_font = ("Arial", 16, "bold")
        btn_width = 22
        
        tk.Button(optFrame, text="Add Student", command=self.show_add_frame, bd=3, relief="raised", bg="#27ae60", fg="white", width=btn_width, font=button_font).pack(pady=20)
        tk.Button(optFrame, text="Search Student", command=self.show_search_frame, bd=3, relief="raised", bg="#2980b9", fg="white", width=btn_width, font=button_font).pack(pady=20)
        tk.Button(optFrame, text="Update Record", command=self.show_update_frame, bd=3, relief="raised", bg="#f39c12", fg="white", width=btn_width, font=button_font).pack(pady=20)
        tk.Button(optFrame, text="Remove Student", command=self.show_delete_frame, bd=3, relief="raised", bg="#c0392b", fg="white", width=btn_width, font=button_font).pack(pady=20)
        tk.Button(optFrame, text="Show All", command=self.populate_table, bd=3, relief="raised", bg="#8e44ad", fg="white", width=btn_width, font=button_font).pack(pady=20)

        # --- Feature Buttons ---
        tk.Label(optFrame, text="Advanced Features", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=(40, 10))
        tk.Button(optFrame, text="Export to Excel", command=self.export_to_excel, bd=3, relief="raised", bg="#16a085", fg="white", width=btn_width, font=button_font).pack(pady=20)
        tk.Button(optFrame, text="Show Analytics", command=self.show_analytics_window, bd=3, relief="raised", bg="#34495e", fg="white", width=btn_width, font=button_font).pack(pady=20)

        # --- Right Frame for Details/Table ---
        detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="#bdc3c7")
        detFrame.place(width=self.width - (self.width/3.5) - 60, height=self.height - 180, x=self.width/3.5 + 40, y=80)

        tk.Label(detFrame, text="Student Records", font=("Arial", 25, "bold"), bg="#bdc3c7").pack(side="top", fill="x", pady=10)

        # Table Frame
        tabFrame = tk.Frame(detFrame, bd=4, relief="sunken")
        tabFrame.place(relwidth=0.95, relheight=0.85, relx=0.025, rely=0.12)

        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")

        self.table = ttk.Treeview(tabFrame, columns=("roll", "name", "fname", "sub", "grade"),
                                  xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        
        x_scroll.pack(side="bottom", fill="x")
        y_scroll.pack(side="right", fill="y")
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        self.table.heading("roll", text="Roll No")
        self.table.heading("name", text="Name")
        self.table.heading("fname", text="Father's Name")
        self.table.heading("sub", text="Subject")
        self.table.heading("grade", text="Grade")
        self.table["show"] = "headings"
        
        self.table.column("roll", width=100)
        self.table.column("name", width=200)
        self.table.column("fname", width=200)
        self.table.column("sub", width=150)
        self.table.column("grade", width=100)

        self.table.pack(fill="both", expand=1)
        
        # --- Status Bar ---
        self.status_bar = tk.Label(self.root, text="Welcome to Student Management System v2.0", bd=1, relief="sunken", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

    def populate_table(self):
        """Clears the table and fills it with all student data."""
        self.table.delete(*self.table.get_children())
        all_students = self.db_manager.fetch_all_students()
        if all_students:
            for student in all_students:
                self.table.insert('', tk.END, values=student)
            self.status_bar.config(text=f"Showing {len(all_students)} records.")
        else:
            self.status_bar.config(text="No records found.")

    # --- Action Frame Functions ---
    def _create_action_window(self, title, geometry):
        """Helper function to create a new Toplevel window for actions."""
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(geometry)
        win.grab_set() # Modal window
        win.resizable(False, False)
        return win

    def show_add_frame(self):
        win = self._create_action_window("Add New Student", "450x400")

        tk.Label(win, text="Roll No:", font=("Arial", 12)).grid(row=0, column=0, padx=20, pady=10, sticky="w")
        roll_entry = tk.Entry(win, font=("Arial", 12))
        roll_entry.grid(row=0, column=1, padx=20, pady=10)

        tk.Label(win, text="Name:", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        name_entry = tk.Entry(win, font=("Arial", 12))
        name_entry.grid(row=1, column=1, padx=20, pady=10)
        
        tk.Label(win, text="Father's Name:", font=("Arial", 12)).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        fname_entry = tk.Entry(win, font=("Arial", 12))
        fname_entry.grid(row=2, column=1, padx=20, pady=10)
        
        tk.Label(win, text="Subject:", font=("Arial", 12)).grid(row=3, column=0, padx=20, pady=10, sticky="w")
        sub_entry = tk.Entry(win, font=("Arial", 12))
        sub_entry.grid(row=3, column=1, padx=20, pady=10)
        
        tk.Label(win, text="Grade:", font=("Arial", 12)).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        grade_entry = tk.Entry(win, font=("Arial", 12))
        grade_entry.grid(row=4, column=1, padx=20, pady=10)
        
        add_btn = tk.Button(win, text="Add Student", bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                           command=lambda: self.add_student_action(
                               win, roll_entry.get(), name_entry.get(), fname_entry.get(), sub_entry.get(), grade_entry.get()
                           ))
        add_btn.grid(row=5, column=0, columnspan=2, pady=20)

    def add_student_action(self, win, roll, name, fname, sub, grade):
        if not all([roll, name, fname, sub, grade]):
            messagebox.showerror("Error", "All fields are required.", parent=win)
            return
        try:
            roll_no = int(roll)
        except ValueError:
            messagebox.showerror("Error", "Roll Number must be an integer.", parent=win)
            return

        if self.db_manager.add_student(roll_no, name, fname, sub, grade):
            self.status_bar.config(text=f"Student {name} added successfully.")
            self.populate_table()
            win.destroy()
        else:
            self.status_bar.config(text="Failed to add student.")

    # ... Implement show_search_frame, show_update_frame, show_delete_frame similarly ...
    def show_search_frame(self):
        win = self._create_action_window("Search Student", "450x250")
        
        tk.Label(win, text="Search By:", font=("Arial", 12)).grid(row=0, column=0, padx=20, pady=15, sticky="w")
        search_by_combo = ttk.Combobox(win, values=["rollNo", "name", "sub"], state="readonly", font=("Arial", 12))
        search_by_combo.grid(row=0, column=1, padx=20, pady=15)
        search_by_combo.set("rollNo")
        
        tk.Label(win, text="Search Value:", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=15, sticky="w")
        search_value_entry = tk.Entry(win, font=("Arial", 12))
        search_value_entry.grid(row=1, column=1, padx=20, pady=15)
        
        search_btn = tk.Button(win, text="Search", bg="#2980b9", fg="white", font=("Arial", 12, "bold"),
                              command=lambda: self.search_student_action(
                                  search_by_combo.get(), search_value_entry.get()
                              ))
        search_btn.grid(row=2, column=0, columnspan=2, pady=20)
    
    def search_student_action(self, search_by, search_value):
        if not search_value:
            messagebox.showerror("Error", "Search value cannot be empty.")
            return
        
        results = self.db_manager.search_student(search_by, search_value)
        self.table.delete(*self.table.get_children())
        if results:
            for row in results:
                self.table.insert('', tk.END, values=row)
            self.status_bar.config(text=f"Found {len(results)} record(s).")
        else:
            self.status_bar.config(text="No matching records found.")

    def show_update_frame(self):
        selected_item = self.table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student from the table to update.")
            return
            
        student_data = self.table.item(selected_item)['values']
        roll_to_update = student_data[0]

        win = self._create_action_window("Update Student Record", "450x250")
        
        tk.Label(win, text=f"Updating Roll No: {roll_to_update}", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        tk.Label(win, text="Field to Update:", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=15, sticky="w")
        field_combo = ttk.Combobox(win, values=["name", "fname", "sub", "grade"], state="readonly", font=("Arial", 12))
        field_combo.grid(row=1, column=1, padx=20, pady=15)
        field_combo.set("name")

        tk.Label(win, text="New Value:", font=("Arial", 12)).grid(row=2, column=0, padx=20, pady=15, sticky="w")
        new_value_entry = tk.Entry(win, font=("Arial", 12))
        new_value_entry.grid(row=2, column=1, padx=20, pady=15)
        
        update_btn = tk.Button(win, text="Update", bg="#f39c12", fg="white", font=("Arial", 12, "bold"),
                              command=lambda: self.update_student_action(
                                  win, roll_to_update, field_combo.get(), new_value_entry.get()
                              ))
        update_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def update_student_action(self, win, roll_no, field, new_value):
        if not new_value:
            messagebox.showerror("Error", "New value cannot be empty.", parent=win)
            return

        if self.db_manager.update_student(roll_no, field, new_value):
            self.status_bar.config(text=f"Record for Roll No {roll_no} updated.")
            self.populate_table()
            win.destroy()
        else:
            self.status_bar.config(text="Failed to update record.")
            
    def show_delete_frame(self):
        selected_item = self.table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student from the table to remove.")
            return
            
        student_data = self.table.item(selected_item)['values']
        roll_to_delete = student_data[0]
        student_name = student_data[1]

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to remove {student_name} (Roll No: {roll_to_delete})?"):
            if self.db_manager.delete_student(roll_to_delete):
                self.status_bar.config(text=f"Student {student_name} removed.")
                self.populate_table()
            else:
                self.status_bar.config(text="Failed to remove student.")
    
    # --- Feature Implementations ---
    def export_to_excel(self):
        """Exports the current student data to an Excel file."""
        records = self.db_manager.fetch_all_students()
        if not records:
            messagebox.showinfo("No Data", "There is no data to export.")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if not filepath:
            return

        try:
            df = pd.DataFrame(records, columns=["RollNo", "Name", "FathersName", "Subject", "Grade"])
            df.to_excel(filepath, index=False)
            messagebox.showinfo("Success", f"Data exported successfully to {filepath}")
            self.status_bar.config(text="Data exported to Excel.")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred: {e}")

    def show_analytics_window(self):
        """Shows a new window with a pie chart of grade distribution."""
        data = self.db_manager.get_grade_distribution()
        if not data:
            messagebox.showinfo("No Data", "Not enough data to generate analytics.")
            return

        win = self._create_action_window("Student Analytics", "600x500")
        
        grades = [item[0] for item in data]
        counts = [item[1] for item in data]
        
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.pie(counts, labels=grades, autopct='%1.1f%%', startangle=90,
               wedgeprops=dict(width=0.4), textprops={'fontsize': 10})
        ax.set_title("Student Grade Distribution")
        
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)
        
    def on_closing(self):
        """Handles the window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.db_manager.close_connection()
            self.root.destroy()

if __name__ == "__main__":
    # Use ThemedTk for a modern look. Themes: "arc", "breeze", "elegance", etc.
    root = ThemedTk(theme="arc")
    app = StudentApp(root)
    root.mainloop()