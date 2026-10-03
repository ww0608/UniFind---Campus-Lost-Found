import json
from datetime import datetime

FILE_NAME = "lost_found.json"

# Load the Item File at the Beginning
def load_items():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save the Updated Items to the Item File
def save_items(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


# Report a Lost / Found Item Features
def add_item(items, item_type):
    print(f"\n===== REPORT A {item_type.upper()} ITEM =====")

    name = input_fields_checking("Item Name: ").strip()
    category = select_category()
    color = input_fields_checking("Color: ").strip()
    location = select_location()
    date = date_checking()
    description = input_fields_checking("Description: ").strip()

    item = {
        "id": get_next_id(items),
        "type": item_type,
        "name": name,
        "category": category,
        "color": color,
        "location": location,
        "date": date,
        "description": description,
        "status": "open"
    }

    items.append(item)
    save_items(items)

    print("\nItem Reported SUCCESSFULLY!")
    print(f"Item ID: {item['id']}")

# Auto-generate ID
def get_next_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1

# Check the Input Field (Input Fields Cannot be Empty)
def input_fields_checking(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")

# Select Categories
def select_category():
    categories = {
        "1": "Electronics",
        "2": "Keys & ID Cards",
        "3": "Wallets & Purses",
        "4": "Bags & Backpacks",
        "5": "Clothing & Accessories",
        "6": "Eyewear",
        "7": "Books & Stationery",
        "8": "Sports & Recreation",
        "9": "Valuables & Jewelry",
        "10": "Other"
    }

    print("Select Category:")
    print("1: Electronics")
    print("2: Keys & ID Cards")
    print("3: Wallets & Purses")
    print("4: Bags & Backpacks")
    print("5: Clothing & Accessories")
    print("6: Eyewear")
    print("7: Books & Stationery")
    print("8: Sports & Recreation")
    print("9: Valuables & Jewelry")
    print("10: Other")

    while True:
        choice = input("Category: ").strip()

        if choice in categories:
            return categories[choice]

        print("Invalid choice. Please select a category from 1 to 10.")

# Select Location
def select_location():
    locations = {
        "1": "Library",
        "2": "Cafeteria",
        "3": "Classroom",
        "4": "Laboratory",
        "5": "Student Accommodation",
        "6": "Sports Centre",
        "7": "Parking Area",
        "8": "Student Services",
        "9": "Other",
    }

    print("Select Locations:")
    print("1: Library")
    print("2: Cafeteria")
    print("3: Classroom")
    print("4: Laboratory")
    print("5: Student Accommodation")
    print("6: Sports Centre")
    print("7: Parking Area")
    print("8: Student Services")
    print("9: Other")

    while True:
        choice = input("Location: ").strip()

        if choice in locations:
            return locations[choice]

        print("Invalid choice. Please select a location from 1 to 9.")

# Check the Date Input (Date Cannot be in Future & Check the Date Format)
def date_checking():
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()

        try:
            selected_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")
            continue

        today = datetime.today().date()

        if selected_date > today:
            print("Date cannot be in the future. Please enter a valid date.")
            continue

        return date

# Search Reported Item Feature
def search_items(items):
    if not items:
        print("\nNo items have been reported yet.")
        return

    print("\n===== SEARCH ITEMS =====")
    print("1. Search by Item Name")
    print("2. Search by Category")
    print("3. Search by Location")
    print("4. Search by Type")
    print("5. Back")

    choice = input("Choose a Search Option: ").strip()

    if choice == "5":
        return

    if choice == "1":
        search_term = input_fields_checking("Enter Item Name: ").casefold()

        results = [
            item for item in items
            if search_term in item["name"].casefold()
        ]
    elif choice == "2":
        category = select_category()

        results = [
            item for item in items
            if item["category"] == category
        ]
    elif choice == "3":
        location = select_location()

        results = [
            item for item in items
            if item["location"] == location
        ]
    elif choice == "4":
        item_type = select_item_type()

        results = [
            item for item in items
            if item["type"] == item_type
        ]
    else:
        print("Invalid search option.")
        return

    if not results:
        print("\nNo matching items were found.")
        return

    print(f"\n===== SEARCH RESULTS ({len(results)}) =====")
    display_items(results)

# Select Item Type
def select_item_type():
    while True:
        print("\n===== SELECT ITEM TYPE =====")
        print("1: Lost")
        print("2: Found")

        choice = input("Item Type: ").strip()

        if choice == "1":
            return "lost"

        if choice == "2":
            return "found"

        print("Invalid choice. Please select 1 or 2.")


# View All Reported Items Feature
def display_items(items):
    if not items:
        print("\nNo items have been reported yet.")
        return

    print("\n===== ALL REPORTED ITEMS =====")
    for item in items:
        print(f"\nID: {item['id']}")
        print(f"Type: {item['type'].upper()}")
        print(f"Name: {item['name']}")
        print(f"Category: {item['category']}")
        print(f"Color: {item['color']}")
        print(f"Location: {item['location']}")
        print(f"Date: {item['date']}")
        print(f"Description: {item['description']}")
        print(f"Status: {item['status'].upper()}")
        print("-" * 31)


# Find Matches Feature
def find_matches(items):
    print("\n===== FIND MATCHES =====")
    print("Enter the details of your lost item.")
    name = input_fields_checking("Item Name: ").strip()
    category = select_category()
    color = input_fields_checking("Color: ").strip()
    location = select_location()

    lost_item = {
        "name": name,
        "category": category,
        "color": color,
        "location": location
    }

    found_items = [
        item for item in items
        if item["type"] == "found" and item["status"] == "open"
    ]

    matches = []

    for found_item in found_items:
        score = calculate_match_score(lost_item, found_item)

        if score >= 2:
            matches.append((found_item, score))

    if not matches:
        print("\nNo possible matches found.")
        return

    print("\n===== POSSIBLE MATCHES =====")
    print("\n Your Lost Item:")
    print(f"Name: {lost_item['name']}")
    print(f"Category: {lost_item['category']}")
    print(f"Color: {lost_item['color']}")
    print(f"Location: {lost_item['location']}")

    for found_item, score in matches:
        print("-" * 28)
        print(f"Found Item ID: {found_item['id']}")
        print(f"Name: {found_item['name']}")
        print(f"Category: {found_item['category']}")
        print(f"Color: {found_item['color']}")
        print(f"Location: {found_item['location']}")
        print(f"Match Score: {score}/4")

        if score == 4:
            print("⭐ STRONG MATCH")
        else:
            print("✓ POSSIBLE MATCH")

# Calculate Match Score
def calculate_match_score(lost_item, found_item):
    score = 0

    if lost_item["name"].casefold() == found_item["name"].casefold():
        score += 1

    if lost_item["category"] == found_item["category"]:
        score += 1

    if lost_item["color"].casefold() == found_item["color"].casefold():
        score += 1

    if lost_item["location"] == found_item["location"]:
        score += 1

    return score


# Claim an Item Feature
def claim_item(items):
    print("\n===== CLAIM AN ITEM =====")
    try:
        item_id = int(input_fields_checking("Enter Item ID: "))
    except ValueError:
        print("Invalid Item ID.")
        return

    item = None

    for current_item in items:
        if current_item["id"] == item_id:
            item = current_item
            break

    if item is None:
        print("Item ID not found.")
        return

    if item["type"] != "found":
        print("Only found items can be claimed.")
        return

    if item["status"] != "open":
        print("This item is no longer available for claiming.")
        return

    print("\n===== ITEM DETAILS =====")
    print(f"Item ID: {item['id']}")
    print(f"Name: {item['name']}")
    print(f"Category: {item['category']}")
    print(f"Color: {item['color']}")
    print(f"Location: {item['location']}")
    print(f"Date: {item['date']}")
    print(f"Description: {item['description']}")

    confirmation = input("\nAre you sure this is your item? (Y/N): ").strip().casefold()

    if confirmation == "y":
        item["status"] = "claimed"
        save_items(items)

        print("\nItem claimed SUCCESSFULLY!")
        print("Please collect your item at Campus Lost & Found Counter")
    else:
        print("\nClaim CANCELLED!")


# Remove Item Feature
def remove_item(items):
    print("\n===== REMOVE AN ITEM =====")
    try:
        item_id = int(input_fields_checking("Enter Item ID: "))
    except ValueError:
        print("Invalid Item ID.")
        return

    item = None

    for current_item in items:
        if current_item["id"] == item_id:
            item = current_item
            break

    if item is None:
        print("Item ID not found.")
        return

    print("\n===== ITEM DETAILS =====")
    print(f"Item ID: {item['id']}")
    print(f"Type: {item['type'].upper()}")
    print(f"Name: {item['name']}")
    print(f"Category: {item['category']}")
    print(f"Color: {item['color']}")
    print(f"Location: {item['location']}")
    print(f"Date: {item['date']}")
    print(f"Description: {item['description']}")
    print(f"Status: {item['status'].upper()}")

    confirmation = input("\nAre you sure this is your item? (Y/N): ").strip().casefold()

    if confirmation == "y":
        items.remove(item)
        save_items(items)

        print("\nItem removed SUCCESSFULLY!")
    else:
        print("\nItem removal CANCELLED!")


def main():
    items = load_items()

    while True:
        print("\n===== CAMPUS LOST & FOUND =====")
        print("1. Report a Lost Item")
        print("2. Report a Found Item")
        print("3. Search Reported Item")
        print("4. View All Reported Items")
        print("5. Find Matches")
        print("6. Claim an Item")
        print("7. Remove an Item")
        print("8. Exit")
        print("=" * 31)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_item(items, "lost")
        elif choice == "2":
            add_item(items, "found")
        elif choice == "3":
            search_items(items)
        elif choice == "4":
            display_items(items)
        elif choice == "5":
            find_matches(items)
        elif choice == "6":
            claim_item(items)
        elif choice == "7":
            remove_item(items)
        elif choice == "8":
            print("Thank you, and bye bye!")
            break
        else:
            print("Invalid option. Please input again!")


if __name__ == "__main__":
    main()

