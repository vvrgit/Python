
def add_product(products, product_id, name, category, price, quantity):
    products[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    print("Product added successfully.")

def display_products(products):
    print("\n----- INVENTORY -----")

    for product_id, product in products.items():
        print("Product ID :", product_id)
        print("Name       :", product["name"])
        print("Category   :", product["category"])
        print("Price      :", product["price"])
        print("Quantity   :", product["quantity"])
        print("---------------------")


def search_product(products, product_id):
    if product_id in products:
        product = products[product_id]

        print("\nProduct Found")
        print("Name     :", product["name"])
        print("Category :", product["category"])
        print("Price    :", product["price"])
        print("Quantity :", product["quantity"])
    else:
        print("Product not found.")

def update_quantity(products, product_id, quantity):
    if product_id in products:
        products[product_id]["quantity"] = quantity
        print("Quantity updated successfully.")
    else:
        print("Product not found.")


def low_stock_products(products, limit=5):
    print("\n----- LOW STOCK PRODUCTS -----")

    found = False

    for product_id, product in products.items():
        if product["quantity"] <= limit:
            print(
                product_id,
                product["name"],
                "Quantity:",
                product["quantity"]
            )
            found = True

    if not found:
        print("No products require restocking.")
