# === Constants ===
SIZE_PRICES = {
    "small": 300,
    "large": 450,
    "family": 600
}
TOPPINGS = ["cheese", "shrimp", "pepperoni", "cream cheese"]
FREE_TOPPINGS = 2
EXTRA_TOPPING_COST = 50
DELIVERY_BASE_KM = 4
DELIVERY_BASE_FEE = 50
DELIVERY_ADDITIONAL_PER_KM = 10
DELIVERY_MAX_KM = 8
VAT_RATE = 0.12

def display_menu():
    print("\n=== PIZZA MENU ===")
    print("Sizes:")
    print("  Small (9\")  - Php 300")
    print("  Large (13\") - Php 450")
    print("  Family (16\") - Php 600")
    print("Toppings Available:")
    for topping in TOPPINGS:
        print(f"  - {topping.capitalize()}")
    print("Note: First 2 toppings are free. Each additional topping costs Php 50.")

def get_pizza_size():
    while True:
        size = input("Choose size (small/large/family): ").lower()
        if size in SIZE_PRICES:
            return size
        print("Invalid size. Please try again.")

def get_toppings():
    selected = []
    print("Select toppings (type 'done' to finish):")
    while True:
        topping = input("Add topping: ").lower().strip()
        if topping == 'done':
            break
        elif topping in TOPPINGS and topping not in selected:
            selected.append(topping)
        elif topping in selected:
            print("Topping already added.")
        else:
            print("Invalid topping.")
    return selected

def calculate_topping_cost(toppings):
    extra_count = max(0, len(toppings) - FREE_TOPPINGS)
    return extra_count * EXTRA_TOPPING_COST

def calculate_delivery_fee(km):
    km = min(km, DELIVERY_MAX_KM)
    if km <= DELIVERY_BASE_KM:
        return DELIVERY_BASE_FEE
    extra_km = km - DELIVERY_BASE_KM
    return DELIVERY_BASE_FEE + extra_km * DELIVERY_ADDITIONAL_PER_KM

def calculate_totals(orders, delivery_fee):
    subtotal = sum(order['price'] for order in orders)
    vat = subtotal * VAT_RATE
    total = subtotal + delivery_fee + vat
    return round(subtotal, 2), round(vat, 2), round(total, 2)

def simulate_distance_from_shop(address):
    # Simulate distance between 2km to 8km
    return round(random.uniform(2, 8), 1)

def display_order_summary(orders, delivery_fee, vat, total, distance, address):
    print("\n=== ORDER SUMMARY ===")
    for i, order in enumerate(orders, 1):
        print(f"{i}. {order['size'].capitalize()} Pizza - Php {SIZE_PRICES[order['size']]}")
        print(f"   Toppings: {', '.join(order['toppings']) or 'None'}")
        print(f"   Extra Topping Charge: Php {order['topping_cost']}")
        print(f"   Total Pizza Price: Php {order['price']}")
    print(f"\nDelivery Fee (for {distance:.1f} km): Php {delivery_fee}")
    print(f"VAT (12%): Php {vat}")
    print(f"TOTAL: Php {total}")
    print(f"Delivery Address: {address}")

def main():
    address = None
    distance = None
    delivery_fee = None

    while True:
        orders = []

        # Pizza ordering loop
        while True:
            display_menu()
            size = get_pizza_size()
            toppings = get_toppings()
            topping_cost = calculate_topping_cost(toppings)
            base_price = SIZE_PRICES[size]
            total_price = base_price + topping_cost

            orders.append({
                "size": size,
                "toppings": toppings,
                "topping_cost": topping_cost,
                "price": total_price
            })

            more = input("Would you like to order more? (yes/no): ").lower().strip()
            if more != 'yes':
                break

        # Get address once
        if not address:
            address = input("Enter your delivery address: ").strip()
            distance = simulate_distance_from_shop(address)
            delivery_fee = calculate_delivery_fee(distance)

        # Calculate totals
        subtotal, vat, total = calculate_totals(orders, delivery_fee)

        # Display summary
        display_order_summary(orders, delivery_fee, vat, total, distance, address)

        # Confirm
        confirm = input("\nWould you like to complete the order? (yes/no): ").lower().strip()
        if confirm == 'yes':
            print(f"\nOrder placed! Please prepare Php {total}.")
            break
        else:
            print("\nRestarting order (delivery info saved)...\n")

if __name__ == "__main__":
    main()
