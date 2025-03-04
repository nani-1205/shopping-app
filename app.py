from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data (replace with a database in a real application)
products = [
    {"id": 1, "name": "T-shirt", "price": 20.00, "image": "tshirt.jpg", "description": "A comfortable cotton t-shirt."},
    {"id": 2, "name": "Jeans", "price": 50.00, "image": "jeans.jpg", "description": "Classic denim jeans."},
    {"id": 3, "name": "Sneakers", "price": 75.00, "image": "sneakers.jpg", "description": "Stylish and comfortable sneakers."},
    {"id": 4, "name": "Hat", "price": 15.00, "image": "hat.jpg", "description": "A fashionable hat to complete your look."}
]

# Shopping cart (stored in a session - would typically use a database in a real app)
cart = {}  #  product_id: quantity


@app.route("/")
def index():
    """Displays the product listing page."""
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    """Displays the details for a specific product."""
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template("product_detail.html", product=product)
    else:
        return "Product not found", 404


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    """Adds a product to the shopping cart."""
    product_id = int(request.form["product_id"])
    quantity = int(request.form["quantity"])

    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    return redirect(url_for("cart_view"))  # Redirect to cart page after adding


@app.route("/cart")
def cart_view():
    """Displays the shopping cart."""
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            item_total = product["price"] * quantity
            cart_items.append({"product": product, "quantity": quantity, "item_total": item_total})
            total_price += item_total

    return render_template("cart.html", cart_items=cart_items, total_price=total_price)


@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):
    """Removes a product from the shopping cart."""
    if product_id in cart:
        del cart[product_id]
    return redirect(url_for("cart_view"))

@app.route("/checkout")
def checkout():
    """Placeholder for the checkout process."""
    # In a real application, you would handle payment processing,
    # order confirmation, and database updates here.
    total_price = 0
    for product_id, quantity in cart.items():
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            item_total = product["price"] * quantity
            total_price += item_total

    return render_template("checkout.html", total_price=total_price)  # Render a simple checkout page.  More complex logic needed for real checkout

@app.route("/clear_cart")
def clear_cart():
    """Clears the entire shopping cart."""
    cart.clear()
    return redirect(url_for("index"))  # Redirect to the product listing page.


if __name__ == "__main__":
    app.run(debug=True)