import os

from config import (
    DATA_DIR,
    CUSTOMER_FILE,
    VEHICLE_FILE,
    PART_FILE,
    SERVICE_FILE
)

from storage import save_data

from customer_manager import (
    add_customer,
    view_customers,
    search_customer,
    delete_customer
)

from vehicle_manager import (
    add_vehicle,
    view_vehicles,
    search_vehicle,
    customer_vehicles
)

from parts_manager import (
    add_part,
    view_parts,
    search_part,
    update_stock
)

from service_manager import (
    create_service,
    view_services,
    view_service_details,
    update_service_status,
    search_services
)

from report_manager import (
    service_statistics,
    low_stock_report
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [
        CUSTOMER_FILE,
        VEHICLE_FILE,
        PART_FILE,
        SERVICE_FILE
    ]

    for filename in files:
        if not os.path.exists(filename):
            save_data(filename, [])


def show_menu():
    print("\n")
    print("=" * 65)
    print("          VEHICLE SERVICE MANAGEMENT SYSTEM")
    print("=" * 65)

    print("\nCUSTOMERS")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Delete Customer")

    print("\nVEHICLES")
    print("5. Add Vehicle")
    print("6. View Vehicles")
    print("7. Search Vehicle")
    print("8. Customer Vehicles")

    print("\nSPARE PARTS")
    print("9. Add Part")
    print("10. View Parts")
    print("11. Search Part")
    print("12. Update Part Stock")

    print("\nSERVICE")
    print("13. Create Service")
    print("14. View Services")
    print("15. Service Details")
    print("16. Update Service Status")
    print("17. Search Services")

    print("\nREPORTS")
    print("18. Service Statistics")
    print("19. Low Stock Report")

    print("\n20. Exit")

    print("=" * 65)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "5":
            add_vehicle()

        elif choice == "6":
            view_vehicles()

        elif choice == "7":
            search_vehicle()

        elif choice == "8":
            customer_vehicles()

        elif choice == "9":
            add_part()

        elif choice == "10":
            view_parts()

        elif choice == "11":
            search_part()

        elif choice == "12":
            update_stock()

        elif choice == "13":
            create_service()

        elif choice == "14":
            view_services()

        elif choice == "15":
            view_service_details()

        elif choice == "16":
            update_service_status()

        elif choice == "17":
            search_services()

        elif choice == "18":
            service_statistics()

        elif choice == "19":
            low_stock_report()

        elif choice == "20":
            print(
                "Thank you for using "
                "Vehicle Service Management System."
            )
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
