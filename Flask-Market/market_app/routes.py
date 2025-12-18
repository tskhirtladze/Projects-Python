from flask import render_template, url_for, redirect, flash, request
from market_app.forms import RegisterForm, LoginForm
from market_app.models import User
from market_app import db
from market_app import app
from flask_login import login_user, logout_user, login_required, current_user

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
        {'id': 5, 'name': 'Pride and Prejudice', 'barcode': '9781503290563', 'price': 10},
        {'id': 6, 'name': '---', 'barcode': '1412415151', 'price': 25}
    ]
    return render_template('market.html', items=items)



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              name=form.name.data,
                              surname=form.surname.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There is an error while creating the user account: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page'))


@app.route('/user/<username>')
@login_required
def view_user_profile(username):
    profile_user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile_page.html', profile_user=profile_user)

