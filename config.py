import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMER_FILE = os.path.join(DATA_DIR, "customers.json")
VEHICLE_FILE = os.path.join(DATA_DIR, "vehicles.json")
PART_FILE = os.path.join(DATA_DIR, "parts.json")
SERVICE_FILE = os.path.join(DATA_DIR, "services.json")

GST_RATE = 18

SERVICE_STATUSES = [
    "Received",
    "In Progress",
    "Ready",
    "Delivered"
]
