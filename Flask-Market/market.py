from market_app import app


#Checks if the humor.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)