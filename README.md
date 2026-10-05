# Vehicle Service Management System

A modular Python-based application for managing vehicle service
operations.

## Features

### Customer Management

- Add customers
- View customers
- Search customers
- Delete customers

### Vehicle Management

- Register vehicles
- View vehicles
- Search vehicles
- View customer vehicles

### Spare Parts

- Add spare parts
- View parts
- Search parts
- Update stock
- Low-stock report

### Service Management

- Create service records
- Add customer complaints
- Add multiple spare parts
- Calculate labor cost
- Calculate parts cost
- Calculate subtotal
- Calculate GST
- Calculate grand total
- Update service status
- Search services
- View service details

### Reports

- Total services
- Service status statistics
- Total revenue
- Low-stock parts

## Technologies

- Python
- JSON
- File Handling
- Datetime
- Functions
- Modules

## Project Structure

vehicle-service-management/
│
├── main.py
├── config.py
├── storage.py
├── utils.py
├── customer_manager.py
├── vehicle_manager.py
├── parts_manager.py
├── service_manager.py
├── report_manager.py
│
├── data/
│   ├── customers.json
│   ├── vehicles.json
│   ├── parts.json
│   └── services.json
│
└── README.md

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/vehicle-service-management.git
