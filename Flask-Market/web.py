from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    # items = [
    #     {'id': 1, 'name': 'The Great Gatsby', 'barcode': '9780743273565', 'price': 15},
    #     {'id': 2, 'name': 'To Kill a Mockingbird', 'barcode': '9780061120084', 'price': 18},
    #     {'id': 3, 'name': '1984', 'barcode': '9780451524935', 'price': 12},
    #     {'id': 4, 'name': 'The Hobbit', 'barcode': '9780547928227', 'price': 20},
    #     {'id': 5, 'name': 'Pride and Prejudice', 'barcode': '9781503290563', 'price': 10},
    #     {'id': 6, 'name': '---', 'barcode': '1412415151', 'price': 25}
    # ]
    items = Item.query.all()
    return render_template('market.html', items=items)


'''
bash: python
from web import db, app, Item

# Create tables
with app.app_context():
    db.drop_all()
    db.create_all()

# Adding items
item1 = Item(name='Ite1', price=100, barcode='14124515151', description='desc1')
item2 = Item(name='Item2', price=3531, barcode='4325141515', description='desc2')
item3 = Item(name='Item3', price=2324, barcode='4151241412', description='desc3')

# Add and commit the new items
with app.app_context():
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.commit()
'''



# flask --app application run --debug
