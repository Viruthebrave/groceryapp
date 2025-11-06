from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# -------------------------
# Grocery items (20 items)
# -------------------------
items = [
    {"id": 1, "name": "Rice", "category": "Grains", "price": 60, "stock": 100, "unit": "kg"},
    {"id": 2, "name": "Wheat Flour", "category": "Grains", "price": 55, "stock": 80, "unit": "kg"},
    {"id": 3, "name": "Sugar", "category": "Essentials", "price": 45, "stock": 70, "unit": "kg"},
    {"id": 4, "name": "Salt", "category": "Essentials", "price": 20, "stock": 90, "unit": "kg"},
    {"id": 5, "name": "Tur Dal", "category": "Pulses", "price": 120, "stock": 60, "unit": "kg"},
    {"id": 6, "name": "Sunflower Oil", "category": "Oils", "price": 180, "stock": 40, "unit": "L"},
    {"id": 7, "name": "Tea Powder", "category": "Beverages", "price": 150, "stock": 30, "unit": "pack"},
    {"id": 8, "name": "Milk Packet", "category": "Dairy", "price": 25, "stock": 200, "unit": "packet"},
    {"id": 9, "name": "Butter", "category": "Dairy", "price": 60, "stock": 80, "unit": "pack"},
    {"id": 10, "name": "Biscuits", "category": "Snacks", "price": 20, "stock": 150, "unit": "pack"},
    {"id": 11, "name": "Chips", "category": "Snacks", "price": 30, "stock": 90, "unit": "pack"},
    {"id": 12, "name": "Bread", "category": "Bakery", "price": 40, "stock": 60, "unit": "loaf"},
    {"id": 13, "name": "Eggs", "category": "Poultry", "price": 7, "stock": 300, "unit": "piece"},
    {"id": 14, "name": "Onions", "category": "Vegetables", "price": 30, "stock": 200, "unit": "kg"},
    {"id": 15, "name": "Tomatoes", "category": "Vegetables", "price": 25, "stock": 180, "unit": "kg"},
    {"id": 16, "name": "Apples", "category": "Fruits", "price": 180, "stock": 40, "unit": "kg"},
    {"id": 17, "name": "Bananas", "category": "Fruits", "price": 50, "stock": 80, "unit": "dozen"},
    {"id": 18, "name": "Detergent Powder", "category": "Household", "price": 80, "stock": 50, "unit": "pack"},
    {"id": 19, "name": "Shampoo", "category": "Personal Care", "price": 150, "stock": 30, "unit": "bottle"},
    {"id": 20, "name": "Soap", "category": "Personal Care", "price": 30, "stock": 100, "unit": "bar"}
]

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html', items=items)

# Run Flask app
if __name__ == '__main__':
    # Host 0.0.0.0 makes it accessible via localhost or IP (for Docker later)
    app.run(host='0.0.0.0', port=5000, debug=True)
