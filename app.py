from flask import Flask, render_template, request, redirect, session, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "mac-secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")
USERS_FILE = os.path.join(BASE_DIR, "users.json")


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("user_login"))
    return render_template("index.html", products=load_data())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            session["admin"] = True
            session.permanent = True
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                session["user"] = username
                session.permanent = True
                flash("Logged in successfully!")
                return redirect(url_for("index"))
        flash("Invalid username or password")
    return render_template("user_login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if username and password and email:
            users = load_users()
            # Check if username exists
            for user in users:
                if user["username"] == username:
                    flash("Username already exists")
                    return render_template("register.html")
            users.append({"username": username, "password": password, "email": email})
            save_users(users)
            flash("Registration successful! Please login.")
            return redirect(url_for("user_login"))
        else:
            flash("Please fill all fields")
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("login"))  # Redirect to admin login
    return render_template("dashboard.html", products=load_data())


@app.route("/update", methods=["POST"])
def update():
    # if not session.get("admin"):
    #     return redirect(url_for("login"))

    products = load_data()
    idx = int(request.form["index"])
    products[idx]["price"] = request.form["price"]
    products[idx]["desc"] = request.form["desc"]
    products[idx]["ram"] = request.form["ram"]
    products[idx]["storage"] = request.form["storage"]
    products[idx]["display"] = request.form["display"]
    products[idx]["battery"] = request.form["battery"]
    products[idx]["processor"] = request.form["processor"]
    save_data(products)

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for("index"))


@app.route("/add_to_cart/<int:index>")
def add_to_cart(index):
    if 'cart' not in session:
        session['cart'] = []
    if index not in session['cart']:
        session['cart'].append(index)
    flash("Added to cart!")
    return redirect(url_for('index'))


@app.route("/cart")
def cart():
    products = load_data()
    cart_items = [products[i] for i in session.get('cart', []) if i < len(products)]
    return render_template("cart.html", cart_items=cart_items)


@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):
    if 'cart' in session and index in session['cart']:
        session['cart'].remove(index)
    flash("Removed from cart!")
    return redirect(url_for('cart'))


@app.route("/checkout")
def checkout():
    products = load_data()
    cart_items = [products[i] for i in session.get('cart', []) if i < len(products)]
    total = sum(float(p['price'].replace('₹', '').replace(',', '')) for p in cart_items)
    return render_template("checkout.html", cart_items=cart_items, total=f"₹{total:,.0f}")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "POST":
        # Simulate payment processing
        session.pop('cart', None)
        flash("Payment successful! Thank you for your purchase.")
        return redirect(url_for('index'))
    return render_template("payment.html")


if __name__ == "__main__":
    print("✅ Flask app starting...")
    app.run(host="127.0.0.1", port=5000, debug=True)

