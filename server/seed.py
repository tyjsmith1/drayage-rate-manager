from datetime import datetime, timedelta
from app import db, app  # Adjust this import according to your actual app structure
from werkzeug.security import generate_password_hash
from models import User, Carrier, Rate

def seed_data():
    db.create_all()

    print("Clearing db...")
    User.query.delete()
    Carrier.query.delete()
    Rate.query.delete()
    db.session.commit()

    # Creating carriers
    print("Seeding Carriers...")
    carrier_data = [
        {"company_name": "Interstate Distributors", "phone": "000000001", "address": "123 Main St, Chicago, IL"},
        {"company_name": "Cargo Solutions", "phone": "000000002", "address": "456 Park Ave, New York, NY"},
        {"company_name": "Pride Intermodal", "phone": "000000003", "address": "789 Broadway St, San Francisco, CA"},
        {"company_name": "Madaris Intermodal", "phone": "000000004", "address": "101 Main St, Los Angeles, CA"},
        {"company_name": "Hub Group", "phone": "000000005", "address": "202 Elm St, Dallas, TX"},
        {"company_name": "Marina Logistics", "phone": "000000006", "address": "303 Pine St, Seattle, WA"},
        {"company_name": "Crosstown Logistics", "phone": "000000007", "address": "404 Vine St, Philadelphia, PA"},
        {"company_name": "Shade Ball Carrier", "phone": "000000008", "address": "505 Oak St, Miami, FL"},
        {"company_name": "Double Brokers Ltd", "phone": "000000009", "address": "606 Maple St, Denver, CO"},
        {"company_name": "Hold Your Freight Hostage LLC", "phone": "000000010", "address": "707 Cedar St, Boston, MA"},
    ]
    carriers = [Carrier(**data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in carrier_data]
    db.session.add_all(carriers)
    db.session.commit()

    # Creating users for each carrier
    for i, carrier in enumerate(carriers, start=1):
        user = User(
            username=f"user{i}",
            password_hash=generate_password_hash("testpassword"),
            email_address=f"user{i}@example.com",
            role="admin",
            association_id=carrier.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(user)

    # Creating rates for each carrier to different destinations from "CityA"
    print("Seeding Rates...")
    destinations = ["CityB", "CityC", "CityD", "CityE", "CityF"]
    for carrier in carriers:
        for destination in destinations:
            rate = Rate(
                company_id=carrier.id,
                origin="CityA",
                destination=destination,
                rate=100.00 + 10 * destinations.index(destination),  # Example rate calculation
                effective_date=datetime.utcnow(),
                expiry_date=datetime.utcnow() + timedelta(days=365),  # Assuming a 1-year validity
                accessorial_fees=10.00 + 2 * destinations.index(destination),  # Example fee calculation
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.session.add(rate)

    # Committing changes to the database
    db.session.commit()

if __name__ == "__main__":
        with app.app_context():
            seed_data()
