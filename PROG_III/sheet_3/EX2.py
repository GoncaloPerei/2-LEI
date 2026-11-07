# =====================================================================
# DATASET
# =====================================================================
# Main inventory database mapping each product ID to its details
inventory = {
    "P01": {"nome": "Teclado", "preco": 30.0, "stock": 10},
    "P02": {"nome": "Rato", "preco": 15.0, "stock": 8},
    "P03": {"nome": "Monitor", "preco": 180.0, "stock": 4}
}

# Transaction log represented as tuples: (product_id, movement_type, quantity)
movements = [
    ("P01", "saida", 3),
    ("P02", "entrada", 5),
    ("P03", "saida", 6),
    ("P04", "entrada", 2),
    ("P01", "entrada", 4)
]

# =====================================================================
# CORE FUNCTIONS
# =====================================================================
def process_movements(inventory, movements):
    """Processes inventory transactions in chronological order.

    Updates stock levels in-place and rejects transactions that violate
    business rules (missing products, non-positive quantities, insufficient
    stock, or unrecognized movement types).

    Args:
        inventory (dict): Mapping of product IDs to their respective details.
        movements (list): Collection of tuples formatted as (product_id,
          movement_type, quantity).

    Returns:
        list[dict]: Detailed records of all rejected movements and failure
        reasons.
    """

    rejected_movements = []

    for product_id, movement_type, quantity in movements:
        # Rule 1: Product must exist in the inventory catalog
        if product_id not in inventory:
            rejected_movements.append(dict(product_id=product_id, movement_type=movement_type, quantity=quantity, reason="Product not found"))
            continue

        # Rule 2: Quantity must be strictly positive (greater than zero)
        if quantity < 0:
            rejected_movements.append(dict(product_id=product_id, movement_type=movement_type, quantity=quantity, reason="Negative quantity"))
            continue

        # Rule 3: Process transaction based on operation type
        if movement_type == "entrada":
            # Incoming stock: increment current balance
            inventory[product_id]["stock"] += quantity

        elif movement_type == "saida":
            # Outgoing stock: verify sufficient availability prior to deduction
            if inventory[product_id]["stock"] >= quantity:
                inventory[product_id]["stock"] -= quantity
            else:
                rejected_movements.append(dict(product_id=product_id, movement_type=movement_type, quantity=quantity, reason="Not enough stock"))
        else:
            # Rule 4: Reject unknown operation identifiers
            rejected_movements.append(dict(product_id=product_id, movement_type=movement_type, quantity=quantity, reason="Unknown movement type"))
    return rejected_movements

def get_product_less_than_5(inventory):
    """Filters and returns product IDs whose stock is strictly below 5 units.

    Args:
        inventory (dict): Mapping of product IDs to their respective details.

    Returns:
        list[str]: Product IDs with critical stock levels (< 5).
    """
    return [product_id for product_id, details in inventory.items() if details["stock"] < 5]

def inventory_total_value(inventory):
    """Computes the total monetary valuation of all items in stock.

    Args:
        inventory (dict): Mapping of product IDs to their respective details.

    Returns:
        float: Total inventory value (price * quantity across all items).
    """
    return round(sum(item["preco"] * item["stock"] for item in inventory.values()), 2)

# =====================================================================
# EXECUTION & REPORTING
# =====================================================================
# Create a copy of the inventory to preserve the original data
copy_inventory = inventory.copy()
# Process stock movements and capture rejected logs
rejected = process_movements(copy_inventory, movements)

print(f"Original inventory: {inventory}")
print(f"\nUpdated inventory after processing movements: {copy_inventory}")
print(f"\nTotal inventory value: {inventory_total_value(copy_inventory)}€")
print(f"\nProducts with stock less than 5: {get_product_less_than_5(copy_inventory)}")
print(f"\nRejected movements: {rejected}")