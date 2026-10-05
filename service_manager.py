from config import (
    CUSTOMER_FILE,
    VEHICLE_FILE,
    PART_FILE,
    SERVICE_FILE,
    GST_RATE,
    SERVICE_STATUSES
)

from storage import load_data, save_data

from utils import (
    generate_id,
    find_by_id,
    current_datetime,
    money
)


def create_service():
    customers = load_data(CUSTOMER_FILE)
    vehicles = load_data(VEHICLE_FILE)
    parts = load_data(PART_FILE)
    services = load_data(SERVICE_FILE)

    if not customers:
        print("Please add a customer first.")
        return

    if not vehicles:
        print("Please add a vehicle first.")
        return

    customer_id = input("Enter Customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    customer_vehicles = [
        vehicle
        for vehicle in vehicles
        if vehicle["customer_id"] == customer["id"]
    ]

    if not customer_vehicles:
        print("This customer has no registered vehicles.")
        return

    print("\nCustomer Vehicles:")

    for vehicle in customer_vehicles:
        print(
            f"{vehicle['id']} - "
            f"{vehicle['registration']} - "
            f"{vehicle['brand']} {vehicle['model']}"
        )

    vehicle_id = input("Enter Vehicle ID: ").strip()

    vehicle = find_by_id(
        customer_vehicles,
        vehicle_id
    )

    if not vehicle:
        print("Vehicle not found.")
        return

    complaint = input(
        "Enter customer complaint: "
    ).strip()

    try:
        labor_cost = float(
            input("Enter labor cost: ")
        )
    except ValueError:
        print("Invalid labor cost.")
        return

    if labor_cost < 0:
        print("Labor cost cannot be negative.")
        return

    service_items = []

    while True:
        print("\nAvailable Parts:")

        for part in parts:
            print(
                f"{part['id']} - "
                f"{part['name']} - "
                f"{money(part['price'])} - "
                f"Stock: {part['stock']}"
            )

        part_id = input(
            "\nEnter Part ID or type DONE: "
        ).strip()

        if part_id.lower() == "done":
            break

        part = find_by_id(parts, part_id)

        if not part:
            print("Part not found.")
            continue

        try:
            quantity = int(
                input("Enter quantity: ")
            )
        except ValueError:
            print("Invalid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > part["stock"]:
            print("Not enough stock.")
            continue

        service_items.append({
            "part_id": part["id"],
            "part_name": part["name"],
            "price": part["price"],
            "quantity": quantity,
            "amount": part["price"] * quantity
        })

    parts_total = sum(
        item["amount"]
        for item in service_items
    )

    subtotal = labor_cost + parts_total

    gst = subtotal * GST_RATE / 100

    grand_total = subtotal + gst

    service = {
        "id": generate_id(services, "SRV"),
        "customer_id": customer["id"],
        "customer_name": customer["name"],
        "vehicle_id": vehicle["id"],
        "registration": vehicle["registration"],
        "vehicle": f"{vehicle['brand']} {vehicle['model']}",
        "complaint": complaint,
        "labor_cost": labor_cost,
        "parts": service_items,
        "parts_total": parts_total,
        "subtotal": subtotal,
        "gst_rate": GST_RATE,
        "gst": gst,
        "grand_total": grand_total,
        "status": "Received",
        "created_at": current_datetime()
    }

    for item in service_items:
        part = find_by_id(parts, item["part_id"])

        if part:
            part["stock"] -= item["quantity"]

    services.append(service)

    save_data(SERVICE_FILE, services)
    save_data(PART_FILE, parts)

    print("\nService created successfully.")

    display_service(service)


def display_service(service):
    print("\n" + "=" * 70)
    print("SERVICE BILL")
    print("=" * 70)

    print(f"Service ID : {service['id']}")
    print(f"Customer   : {service['customer_name']}")
    print(f"Vehicle    : {service['vehicle']}")
    print(f"Number     : {service['registration']}")
    print(f"Complaint  : {service['complaint']}")
    print(f"Status     : {service['status']}")

    print("\nParts:")

    if not service["parts"]:
        print("No parts used.")
    else:
        for item in service["parts"]:
            print(
                f"{item['part_name']} | "
                f"Qty: {item['quantity']} | "
                f"{money(item['amount'])}"
            )

    print("-" * 70)

    print(
        f"Labor Cost : "
        f"{money(service['labor_cost'])}"
    )

    print(
        f"Parts Cost : "
        f"{money(service['parts_total'])}"
    )

    print(
        f"Subtotal   : "
        f"{money(service['subtotal'])}"
    )

    print(
        f"GST ({service['gst_rate']}%) : "
        f"{money(service['gst'])}"
    )

    print(
        f"Grand Total: "
        f"{money(service['grand_total'])}"
    )


def view_services():
    services = load_data(SERVICE_FILE)

    if not services:
        print("No service records found.")
        return

    for service in services:
        print("\n" + "=" * 75)

        print(
            f"{service['id']} | "
            f"{service['customer_name']} | "
            f"{service['registration']} | "
            f"{service['status']} | "
            f"{money(service['grand_total'])}"
        )


def view_service_details():
    services = load_data(SERVICE_FILE)

    service_id = input(
        "Enter Service ID: "
    ).strip()

    service = find_by_id(
        services,
        service_id
    )

    if not service:
        print("Service record not found.")
        return

    display_service(service)


def update_service_status():
    services = load_data(SERVICE_FILE)

    service_id = input(
        "Enter Service ID: "
    ).strip()

    service = find_by_id(
        services,
        service_id
    )

    if not service:
        print("Service record not found.")
        return

    print("\nStatus Options:")

    for index, status in enumerate(
        SERVICE_STATUSES,
        start=1
    ):
        print(f"{index}. {status}")

    try:
        choice = int(
            input("Select status: ")
        )

        new_status = SERVICE_STATUSES[
            choice - 1
        ]

    except (ValueError, IndexError):
        print("Invalid status.")
        return

    service["status"] = new_status

    save_data(SERVICE_FILE, services)

    print("Service status updated successfully.")


def search_services():
    services = load_data(SERVICE_FILE)

    keyword = input(
        "Enter service ID, customer, registration, or vehicle: "
    ).strip().lower()

    results = [
        service
        for service in services
        if keyword in service["id"].lower()
        or keyword in service["customer_name"].lower()
        or keyword in service["registration"].lower()
        or keyword in service["vehicle"].lower()
    ]

    if not results:
        print("No service records found.")
        return

    for service in results:
        print(
            f"{service['id']} | "
            f"{service['customer_name']} | "
            f"{service['registration']} | "
            f"{service['status']}"
        )
