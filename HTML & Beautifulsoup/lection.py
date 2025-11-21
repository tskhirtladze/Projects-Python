from bs4 import BeautifulSoup
import pandas as pd

data = {}

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    titles = soup.find_all('h5', class_="card-title")
    descriptions = soup.find_all('p', class_="card-text")
    prices = soup.find_all('a', class_="btn btn-primary")

    data['Course'] = [title.text for title in titles]
    data['Description'] = [description.text for description in descriptions]
    data['Price'] = [price.text.split()[-1] for price in prices]

    courses_df = pd.DataFrame(data)
    print(courses_df[['Course', 'Price']])
    courses_df.to_csv('courses.csv')