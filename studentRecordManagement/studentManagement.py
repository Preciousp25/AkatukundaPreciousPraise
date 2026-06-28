import csv
import json
import logging
import os

#  LOGGING SETUP 
logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# CUSTOM EXCEPTION 
class StudentNotFoundError(Exception):
    """Raised when a student is not found in the system."""
    pass

# FILES 
CSV_FILE = "students.csv"
JSON_FILE = "students.json"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reg_no", "name", "age", "program"])

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as file:
        json.dump({}, file)

#  FUNCTIONS 

def load_students():
    students = {}
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row["reg_no"]] = row
    except Exception as e:
        logging.error(f"Error loading students: {e}")
    return students


def save_students(students):
    try:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["reg_no", "name", "age", "program"])
            writer.writeheader()
            writer.writerows(students.values())
    except Exception as e:
        logging.error(f"Error saving students: {e}")


def load_extra_details():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading JSON: {e}")
        return {}


def save_extra_details(data):
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")


def add_student():
    try:
        reg_no = input("Enter Registration Number: ").strip()
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: ").strip())
        program = input("Enter Program: ").strip()

        students = load_students()

        if reg_no in students:
            print("Student already exists!")
            return

        students[reg_no] = {
            "reg_no": reg_no,
            "name": name,
            "age": age,
            "program": program
        }

        save_students(students)

        # JSON extra details
        extra = load_extra_details()
        extra[reg_no] = {
            "address": input("Enter Address: "),
            "contact": input("Enter Contact: "),
            "program_level": input("Enter Program Level: ")
        }
        save_extra_details(extra)

        logging.info(f"Added student {reg_no}")
        print("Student added successfully!")

    except ValueError:
        print("Age must be a number!")
        logging.error("Invalid age input")
    except Exception as e:
        logging.error(f"Error adding student: {e}")
    finally:
        print("Add operation completed.\n")


def view_students():
    try:
        students = load_students()
        extra = load_extra_details()

        if not students:
            print("No student records found.")
            return

        for reg, data in students.items():
            print("\n------------------------")
            print(f"Reg No: {reg}")
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Program: {data['program']}")

            if reg in extra:
                print("Address:", extra[reg].get("address"))
                print("Contact:", extra[reg].get("contact"))
                print("Level:", extra[reg].get("program_level"))

        logging.info("Viewed all students")

    except Exception as e:
        logging.error(f"Error viewing students: {e}")
    finally:
        print("View operation completed.\n")


def search_student():
    try:
        reg_no = input("Enter Registration Number: ").strip()
        students = load_students()
        extra = load_extra_details()

        if reg_no not in students:
            raise StudentNotFoundError("Student not found!")

        student = students[reg_no]
        print("\nStudent Found:")
        print(student)

        if reg_no in extra:
            print("Extra Details:", extra[reg_no])

        logging.info(f"Searched student {reg_no}")

    except StudentNotFoundError as e:
        print(e)
        logging.warning(str(e))
    except Exception as e:
        logging.error(f"Search error: {e}")
    finally:
        print("Search operation completed.\n")


def update_student():
    try:
        reg_no = input("Enter Registration Number to update: ").strip()
        students = load_students()

        if reg_no not in students:
            raise StudentNotFoundError("Student not found!")

        print("Leave blank to keep current value.")

        name = input("New Name: ")
        age = input("New Age: ")
        program = input("New Program: ")

        if name:
            students[reg_no]["name"] = name
        if age:
            students[reg_no]["age"] = int(age)
        if program:
            students[reg_no]["program"] = program

        save_students(students)
        logging.info(f"Updated student {reg_no}")
        print("Student updated successfully!")

    except StudentNotFoundError as e:
        print(e)
        logging.warning(str(e))
    except ValueError:
        print("Invalid age input!")
        logging.error("Invalid age during update")
    except Exception as e:
        logging.error(f"Update error: {e}")
    finally:
        print("Update operation completed.\n")


def delete_student():
    try:
        reg_no = input("Enter Registration Number to delete: ").strip()
        students = load_students()
        extra = load_extra_details()

        if reg_no not in students:
            raise StudentNotFoundError("Student not found!")

        del students[reg_no]
        if reg_no in extra:
            del extra[reg_no]

        save_students(students)
        save_extra_details(extra)

        logging.info(f"Deleted student {reg_no}")
        print("Student deleted successfully!")

    except StudentNotFoundError as e:
        print(e)
        logging.warning(str(e))
    except Exception as e:
        logging.error(f"Delete error: {e}")
    finally:
        print("Delete operation completed.\n")


# MENU 
def menu():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Choose option: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                update_student()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                print("Exiting system...")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")
        finally:
            logging.info("Menu accessed")


if __name__ == "__main__":
    menu()