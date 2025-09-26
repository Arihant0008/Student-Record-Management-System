
import pymysql
from tkinter import messagebox

class DatabaseManager:
    """A class to manage all interactions with the MySQL database."""

    def __init__(self, host="localhost", user="root", password="Arihant123", db="student"):
        """Initializes the database connection."""
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.db
            )
            print("Database connection successful.")
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to the database: {e}")
            # Exit or handle appropriately if the connection fails
            exit()

    def close_connection(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def fetch_all_students(self):
        """Fetches all student records from the database."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM student")
                return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Fetch Error", f"Error fetching students: {e}")
            return []

    def add_student(self, rollNo, name, fname, sub, grade):
        """Adds a new student record to the database."""
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO student (rollNo, name, fname, sub, grade) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (rollNo, name, fname, sub, grade))
            self.connection.commit()
            return True
        except pymysql.err.IntegrityError:
             messagebox.showerror("Error", f"A student with Roll No {rollNo} already exists.")
             return False
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Add Error", f"Error adding student: {e}")
            return False

    def update_student(self, rollNo, field_to_update, new_value):
        """Updates a specific field for a student identified by rollNo."""
        # Whitelist of allowed columns to prevent SQL injection
        allowed_columns = ["name", "fname", "sub", "grade"]
        if field_to_update not in allowed_columns:
            messagebox.showerror("Error", "Invalid field selected for update.")
            return False
        
        try:
            with self.connection.cursor() as cursor:
                # Safely format the query
                query = f"UPDATE student SET {field_to_update} = %s WHERE rollNo = %s"
                cursor.execute(query, (new_value, rollNo))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Update Error", f"Error updating student: {e}")
            return False

    def delete_student(self, rollNo):
        """Deletes a student record from the database by rollNo."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM student WHERE rollNo = %s", (rollNo,))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Delete Error", f"Error deleting student: {e}")
            return False

    def search_student(self, search_by, search_value):
        """Searches for students based on a specific criterion."""
        allowed_columns = ["rollNo", "name", "sub"]
        if search_by not in allowed_columns:
            messagebox.showerror("Error", "Invalid search field.")
            return []

        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT * FROM student WHERE {search_by} = %s"
                cursor.execute(query, (search_value,))
                return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Search Error", f"Error searching for students: {e}")
            return []
            
    def get_grade_distribution(self):
        """Fetches the count of students for each grade for analytics."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT grade, COUNT(*) FROM student GROUP BY grade")
                return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Analytics Error", f"Error fetching grade data: {e}")
            return []