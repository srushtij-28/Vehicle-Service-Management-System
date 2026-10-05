from config import PART_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id, money


def add_part():
    parts = load_data(PART_FILE)

    name = input("Enter part name: ").strip()
    category = input("Enter category: ").strip()

    try:
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid price or stock.")
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    part = {
        "id": generate_id(parts, "P"),
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    parts.append(part)

    save_data(PART_FILE, parts)

    print("\nPart added successfully.")
    print(f"Part ID: {part['id']}")


def view_parts():
    parts = load_data(PART_FILE)

    if not parts:
        print("No parts found.")
        return

    print("\n" + "=" * 75)
    print("SPARE PARTS")
    print("=" * 75)

    for part in parts:
        print(f"ID       : {part['id']}")
        print(f"Name     : {part['name']}")
        print(f"Category : {part['category']}")
        print(f"Price    : {money(part['price'])}")
        print(f"Stock    : {part['stock']}")
        print("-" * 75)


def search_part():
    parts = load_data(PART_FILE)

    keyword = input(
        "Enter part ID, name, or category: "
    ).strip().lower()

    results = [
        part
        for part in parts
        if keyword in part["id"].lower()
        or keyword in part["name"].lower()
        or keyword in part["category"].lower()
    ]

    if not results:
        print("No parts found.")
        return

    for part in results:
        print(
            f"{part['id']} | "
            f"{part['name']} | "
            f"{money(part['price'])} | "
            f"Stock: {part['stock']}"
        )


def update_stock():
    parts = load_data(PART_FILE)

    part_id = input("Enter Part ID: ").strip()

    part = find_by_id(parts, part_id)

    if not part:
        print("Part not found.")
        return

    try:
        stock = int(input("Enter new stock quantity: "))
    except ValueError:
        print("Invalid stock quantity.")
        return

    if stock < 0:
        print("Stock cannot be negative.")
        return

    part["stock"] = stock

    save_data(PART_FILE, parts)

    print("Stock updated successfully.")
