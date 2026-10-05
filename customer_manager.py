from config import CUSTOMER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_customer():
    customers = load_data(CUSTOMER_FILE)

    name = input("Enter customer name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    customer = {
        "id": generate_id(customers, "C"),
        "name": name,
        "phone": phone,
        "email": email
    }

    customers.append(customer)

    save_data(CUSTOMER_FILE, customers)

    print("\nCustomer added successfully.")
    print(f"Customer ID: {customer['id']}")


def view_customers():
    customers = load_data(CUSTOMER_FILE)

    if not customers:
        print("No customers found.")
        return

    print("\n" + "=" * 70)
    print("CUSTOMERS")
    print("=" * 70)

    for customer in customers:
        print(f"ID    : {customer['id']}")
        print(f"Name  : {customer['name']}")
        print(f"Phone : {customer['phone']}")
        print(f"Email : {customer['email']}")
        print("-" * 70)


def search_customer():
    customers = load_data(CUSTOMER_FILE)

    keyword = input(
        "Enter customer ID, name, or phone: "
    ).strip().lower()

    results = [
        customer
        for customer in customers
        if keyword in customer["id"].lower()
        or keyword in customer["name"].lower()
        or keyword in customer["phone"].lower()
    ]

    if not results:
        print("No customer found.")
        return

    for customer in results:
        print(
            f"{customer['id']} | "
            f"{customer['name']} | "
            f"{customer['phone']}"
        )


def delete_customer():
    customers = load_data(CUSTOMER_FILE)

    customer_id = input("Enter Customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    customers.remove(customer)

    save_data(CUSTOMER_FILE, customers)

    print("Customer deleted successfully.")
