from config import CUSTOMER_FILE, VEHICLE_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_vehicle():
    customers = load_data(CUSTOMER_FILE)
    vehicles = load_data(VEHICLE_FILE)

    if not customers:
        print("Please add a customer first.")
        return

    print("\nCustomers:")

    for customer in customers:
        print(
            f"{customer['id']} - "
            f"{customer['name']} - "
            f"{customer['phone']}"
        )

    customer_id = input("Enter Customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    registration = input(
        "Enter vehicle registration number: "
    ).strip().upper()

    brand = input("Enter vehicle brand: ").strip()
    model = input("Enter vehicle model: ").strip()

    try:
        year = int(input("Enter manufacturing year: "))
    except ValueError:
        print("Invalid year.")
        return

    if not registration or not brand or not model:
        print("Required fields cannot be empty.")
        return

    for vehicle in vehicles:
        if vehicle["registration"] == registration:
            print("Vehicle registration already exists.")
            return

    vehicle = {
        "id": generate_id(vehicles, "V"),
        "customer_id": customer["id"],
        "customer_name": customer["name"],
        "registration": registration,
        "brand": brand,
        "model": model,
        "year": year
    }

    vehicles.append(vehicle)

    save_data(VEHICLE_FILE, vehicles)

    print("\nVehicle added successfully.")
    print(f"Vehicle ID: {vehicle['id']}")


def view_vehicles():
    vehicles = load_data(VEHICLE_FILE)

    if not vehicles:
        print("No vehicles found.")
        return

    print("\n" + "=" * 80)
    print("VEHICLES")
    print("=" * 80)

    for vehicle in vehicles:
        print(f"ID           : {vehicle['id']}")
        print(f"Customer     : {vehicle['customer_name']}")
        print(f"Registration : {vehicle['registration']}")
        print(f"Brand        : {vehicle['brand']}")
        print(f"Model        : {vehicle['model']}")
        print(f"Year         : {vehicle['year']}")
        print("-" * 80)


def search_vehicle():
    vehicles = load_data(VEHICLE_FILE)

    keyword = input(
        "Enter registration, brand, model, or customer: "
    ).strip().lower()

    results = [
        vehicle
        for vehicle in vehicles
        if keyword in vehicle["registration"].lower()
        or keyword in vehicle["brand"].lower()
        or keyword in vehicle["model"].lower()
        or keyword in vehicle["customer_name"].lower()
    ]

    if not results:
        print("No vehicles found.")
        return

    for vehicle in results:
        print(
            f"{vehicle['id']} | "
            f"{vehicle['registration']} | "
            f"{vehicle['brand']} {vehicle['model']} | "
            f"{vehicle['customer_name']}"
        )


def customer_vehicles():
    vehicles = load_data(VEHICLE_FILE)

    customer_id = input("Enter Customer ID: ").strip()

    results = [
        vehicle
        for vehicle in vehicles
        if vehicle["customer_id"].lower()
        == customer_id.lower()
    ]

    if not results:
        print("No vehicles found for this customer.")
        return

    print("\nCustomer Vehicles")

    for vehicle in results:
        print(
            f"{vehicle['id']} | "
            f"{vehicle['registration']} | "
            f"{vehicle['brand']} {vehicle['model']}"
        )
