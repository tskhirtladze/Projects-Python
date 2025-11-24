import requests
from bs4 import BeautifulSoup
import pandas as pd


lecturers = []
courses = []
courses_links = []

url = "https://smartacademy.ge/cat/19-IT-Development"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')

    course_div = soup.find_all('div', class_="training__item tr")
    for course in course_div:
        lecturer = course.find("p").text.strip()
        course_title = course.find('a').get("title")
        course_link = course.find('a').get("href")

        lecturers.append(lecturer)
        courses.append(course_title)
        courses_links.append(course_link)

    data = {
        'Lecturer': lecturers,
        'Course': courses,
        'Course Link': courses_links
    }

    df = pd.DataFrame(data)
    print(df[['Lecturer', 'Course']])
    df.to_csv('smart.csv')