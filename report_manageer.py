from config import SERVICE_FILE, PART_FILE
from storage import load_data
from utils import money


def service_statistics():
    services = load_data(SERVICE_FILE)

    if not services:
        print("No service data available.")
        return

    total_services = len(services)

    total_revenue = sum(
        service["grand_total"]
        for service in services
    )

    received = sum(
        1 for service in services
        if service["status"] == "Received"
    )

    in_progress = sum(
        1 for service in services
        if service["status"] == "In Progress"
    )

    ready = sum(
        1 for service in services
        if service["status"] == "Ready"
    )

    delivered = sum(
        1 for service in services
        if service["status"] == "Delivered"
    )

    print("\n" + "=" * 55)
    print("SERVICE STATISTICS")
    print("=" * 55)

    print(f"Total Services : {total_services}")
    print(f"Received       : {received}")
    print(f"In Progress    : {in_progress}")
    print(f"Ready          : {ready}")
    print(f"Delivered      : {delivered}")
    print(f"Total Revenue  : {money(total_revenue)}")


def low_stock_report():
    parts = load_data(PART_FILE)

    if not parts:
        print("No parts available.")
        return

    print("\n" + "=" * 55)
    print("LOW STOCK REPORT")
    print("=" * 55)

    found = False

    for part in parts:
        if part["stock"] <= 5:
            found = True

            print(
                f"{part['id']} | "
                f"{part['name']} | "
                f"Stock: {part['stock']}"
            )

    if not found:
        print("No low-stock parts.")
