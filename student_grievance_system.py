import json
import os

FILE_NAME = "grievances.json"


# ---------- DATA HANDLING ----------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# ---------- GRIEVANCE CLASS ----------
class Grievance:
    def __init__(self, name, roll, dept, category, description):
        self.name = name
        self.roll = roll
        self.dept = dept
        self.category = category
        self.description = description
        self.status = "Pending"

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "dept": self.dept,
            "category": self.category,
            "description": self.description,
            "status": self.status
        }


# ---------- CORE FUNCTIONS ----------
def add_grievance():
    g = Grievance(
        input("Name: "),
        input("Roll No: "),
        input("Department: "),
        input("Category: "),
        input("Description: ")
    )

    data = load_data()
    data.append(g.to_dict())
    save_data(data)

    print("\u2705 Grievance Added Successfully!")


def view_grievances():
    data = load_data()

    if not data:
        print("No grievances found.")
        return

    print("\n----- ALL GRIEVANCES -----")
    for i, g in enumerate(data, 1):
        print(f"\nID: {i}")
        for k, v in g.items():
            print(f"{k}: {v}")


def search_grievance():
    key = input("Enter Roll No or Name: ").lower()
    data = load_data()

    found = False
    for g in data:
        if g["roll"] == key or g["name"].lower() == key:
            print("\n✔ Record Found:")
            print(json.dumps(g, indent=4))
            found = True

    if not found:
        print("❌ No record found")


def delete_grievance():
    roll = input("Enter Roll No: ")
    data = load_data()

    new_data = [g for g in data if g["roll"] != roll]

    if len(new_data) == len(data):
        print("❌ No matching record found")
    else:
        save_data(new_data)
        print("🗑️ Deleted Successfully")


def update_status():
    roll = input("Enter Roll No: ")
    data = load_data()

    for g in data:
        if g["roll"] == roll:
            g["status"] = input("Enter Status (Pending/Resolved): ")
            save_data(data)
            print("✅ Status Updated")
            return

    print("❌ Record not found")


def analytics():
    data = load_data()

    if not data:
        print("No data available")
        return

    count = {}

    for g in data:
        count[g["category"]] = count.get(g["category"], 0) + 1

    print("\n📊 Category-wise Grievance Count:")
    for k, v in count.items():
        print(f"{k}: {v}")


# ---------- MAIN MENU ----------
def menu():
    while True:
        print("\n==============================")
        print(" STUDENT GRIEVANCE SYSTEM ")
        print("==============================")
        print("1. Add Grievance")
        print("2. View All Grievances")
        print("3. Search Grievance")
        print("4. Delete Grievance")
        print("5. Update Status")
        print("6. Analytics")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_grievance()
        elif choice == "2":
            view_grievances()
        elif choice == "3":
            search_grievance()
        elif choice == "4":
            delete_grievance()
        elif choice == "5":
            update_status()
        elif choice == "6":
            analytics()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")


# ---------- RUN ----------
if __name__ == "__main__":
    menu()