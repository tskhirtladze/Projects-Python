from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'The Great Gatsby', 'barcode': '9780743273565', 'price': 15},
        {'id': 2, 'name': 'To Kill a Mockingbird', 'barcode': '9780061120084', 'price': 18},
        {'id': 3, 'name': '1984', 'barcode': '9780451524935', 'price': 12},
        {'id': 4, 'name': 'The Hobbit', 'barcode': '9780547928227', 'price': 20},
        {'id': 5, 'name': 'Pride and Prejudice', 'barcode': '9781503290563', 'price': 10}
    ]
    return render_template('market.html', items=items)

# flask --app application run --debug