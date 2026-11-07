# =====================================================================
# DATASET
# =====================================================================
transactions = [
    ("T01", "Ana", "Livros", 2500),
    ("T02", "Bruno", "Tecnologia", 8000),
    ("T03", "Ana", "Tecnologia", 5000),
    ("T02", "Bruno", "Tecnologia", 8000),
    ("T04", "Carla", "Livros", 3000),
    ("T05", "Bruno", "Livros", 2000),
    ("T06", "Ana", "Livros", 1500)
]

# =====================================================================
# EXERCISE 1: Deduplicate Transactions by ID
# =====================================================================
def remove_duplicates(transactions):
    """Removes duplicate transactions based strictly on transaction ID.

    Preserves the initial occurrence and original insertion order.

    Args:
        transactions (list[tuple]): Raw list of transaction tuples.

    Returns:
        list[tuple]: Deduplicated list containing only the first seen instance
        of each transaction ID.
    """
    unique_transactions = []
    seen = set()
    
    for transaction in transactions:
        tx_id = transaction[0]
        if tx_id not in seen:
            seen.add(tx_id)
            unique_transactions.append(transaction)
    
    return unique_transactions

unique_transactions = remove_duplicates(transactions)
print(f"1. Transactions after removing duplicates:")
for transaction in unique_transactions:
    print(transaction)

# =====================================================================
# EXERCISE 2: Total Amount Spent per Customer
# =====================================================================
def total_amount_per_customer(transactions):
    """Calculates the cumulative amount spent by each unique customer.

    Args:
        transactions (list[tuple]): Deduplicated list of transactions.

    Returns:
        dict: Mapping of customer names to total spending in cents.
    """
    customer_totals = {}
    
    for _, customer, _, amount in transactions:
        # Accumulate amount, defaulting to 0 for initial encounter
        customer_totals[customer] = customer_totals.get(customer, 0) + amount
    return customer_totals

customer_totals = total_amount_per_customer(unique_transactions)
print(f"\n2. Total amounts per customer: {customer_totals}")

# =====================================================================
# EXERCISE 3: Nested Spending Breakdown (Customer -> Category)
# =====================================================================
def total_amount_per_category_customer(transactions):
    """Constructs a nested dictionary categorizing spending per customer.

    Format: {customer_name: {category: total_amount_in_cents}}

    Args:
        transactions (list[tuple]): Deduplicated list of transactions.

    Returns:
        dict: Two-level nested dictionary of spending.
    """
    category_totals = {}
    
    for _, customer, category, amount in transactions:
        # Initialize sub-dictionary for new customers
        category_totals.setdefault(customer, {})
        # Accumulate category spend for the customer
        category_totals[customer][category] = (
            category_totals[customer].get(category, 0) + amount
        )
    
    return category_totals

category_totals = total_amount_per_category_customer(unique_transactions)
print(f"\n3. Total amounts per category: {category_totals}")

# =====================================================================
# EXERCISE 4: Sort Customers by Spending (Tiebreaker: Alphabetical)
# =====================================================================
# Convert dictionary items to tuples (customer, total) and sort:
# - Key criterion 1: -x[1] (negative amount) sorts totals descending
# - Key criterion 2: x[0] sorts names alphabetically ascending on ties
sorted_customers = sorted(customer_totals.items(), key=lambda x: (-x[1], x[0]))
print(f"\nCustomers sorted by total amount spent (descending) and name (ascending): {sorted_customers}")

# =====================================================================
# EXERCISE 5: Top Revenue Category (Supports Multiple Winners on Ties)
# =====================================================================
# Step 5.1: Calculate aggregate billing across each distinct product category
invoice_by_category = {}
for _, _, categoria, valor in unique_transactions:
    invoice_by_category[categoria] = (
        invoice_by_category.get(categoria, 0) + valor
    )

# Step 5.2: Identify the maximum revenue value recorded
max_value = max(invoice_by_category.values())

# Step 5.3: Filter all categories that matched the peak revenue (handles ties)
top_categories = list(
    filter(lambda cat: invoice_by_category[cat] == max_value, invoice_by_category)
)

result = {
    "categories": top_categories,
    "max_value": max_value
}
print(f"5. Highest billing category: {result}")