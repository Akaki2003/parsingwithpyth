import requests
from bs4 import BeautifulSoup


URL = f"https://amindi.ge/ka/"
req = requests.get(URL)
soup = BeautifulSoup(req.content,'html5lib')


import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yvelazesashineliparoligamosacnobad',
    database='test'
)

curs = mydb.cursor()

while True:
    try:
        city = input("დაასახელეთ რომელი ქალაქის პროგნოზი გსურთ: ")
        dayamount = input("დაასახელეთ რამდენი დღის პროგნოზი გსურთ(5/10/15/25): ")
        curs.execute(f"DROP TABLE IF EXISTS {city}")
        curs.execute(f"CREATE TABLE {city}(WEATHER VARCHAR(255),WEEKDAY VARCHAR(255),DAY VARCHAR(255))")
        URL = f"https://amindi.ge/ka/city/{city}/?d={dayamount}"
        req = requests.get(URL)
        soup = BeautifulSoup(req.content, 'html5lib')


        city_list = soup.find('div',class_='dropdown-menu').findAll('ul')[0].findAll('li') +\
                    soup.find('div',class_='dropdown-menu').findAll('ul')[1].findAll('li')
        weather = soup.findAll('div', class_='degrees')
        weekdays = soup.findAll('div', class_='weekDay')
        day = soup.findAll('p', class_='day')
        # ARRAY OF ALL THE CITIES
        city_array = []
        for i in city_list:
            current_city = i.find("a").text.rstrip((i.find('a').find('span').text))
            city_array.append(current_city)

        if city not in city_array:
            raise Exception("ქალაქის სახელი არასწორადაა შეყვანილი")

        if dayamount not in ["5","10","15","25"]:
            raise Exception("დღეების რაოდენობა არასწორადაა შეყვანილი")
        # CODE FOR THE DAY VALUES
        dayvalues = []

        for i in day:
            dayvalues.append(i.text)

        # CODE FOR THE FIRST VALUE OF TEMPERATURE
        firstvalues = []

        for i in weather:
            firstvalues.append(i.span.text)

        # REMOVE THE FIRST INDEX (WE DON'T NEED IT)
        firstvalues.pop(0)

        #  THE CODE FOR THE SECOND VALUE OF TEMPERATURE
        secondvalues = []
        for div in weather:
            span = div.find_next('span').find_next('span')
            secondvalues.append(span.text)
        #  REMOVE FIRST INDEX
        secondvalues.pop(0)
        #  WEEKDAY LIST
        weekvalues = []
        for div in weekdays:
            weekvalues.append(div.text)

        if dayamount == 5 or dayamount == 10 or dayamount == 15 or dayamount == 25:
            print(f"ტემპერატურა შემდეგი {dayamount} დღის განმავლობაში")
        # WEEKDAYS AND TEMPERATURES FOR ENTERED DAYS
        else:
            print(f"ტემპერატურა შემდეგი 5 დღის განმავლობაში")

        for i, j, k, d in zip(firstvalues, secondvalues, weekvalues, dayvalues):
            print(f"{d} - {k} - {i}-დან {j}-მდე")
            insert = f"INSERT INTO {city}(WEATHER,WEEKDAY,DAY) values(%s,%s,%s)"
            val = ((f"{i}°-{j}°"), k, d)
            curs.execute(insert, val)

        mydb.commit()

        retry = input("გსურთ თავიდან?(კი/არა): ")
        if retry != "კი":
            break

    except Exception as e:
        print(e)
        retry = input("გსურთ თავიდან?(კი/არა): ")
        if retry != "კი":
            break






