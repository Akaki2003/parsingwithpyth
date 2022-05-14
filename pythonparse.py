import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'yvelazesashineliparoligamosacnobad',
    database = 'test'
)

curs = mydb.cursor()


while True:
    try:
        #IN CASE YOU ENTER WRONG CITY, DEFAULT GOES TO TBILISI AND TABLE NAME IS THE ONE YOU WILL ENTER
        city = input("დაასახელეთ რომელი ქალაქის პროგნოზი გსურთ: ")
        curs.execute(f"CREATE TABLE {city}(WEATHER VARCHAR(255),WEEKDAY VARCHAR(255),DAY VARCHAR(255))")
        URL = (f"https://amindi.ge/ka/city/{city}/?d=10")
        req = requests.get(URL)
        soup = BeautifulSoup(req.content, 'html5lib')

        weather = soup.findAll('div', class_='degrees')
        weekdays = soup.findAll('div', class_='weekDay')
        day = soup.findAll('p',class_='day')
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


        print("ტემპერატურა შემდეგი ხუთი დღის განმავლობაში")
        # WEEKDAYS AND TEMPERATURES 5 DAYS
        count = 0
        for i,j,k,d in zip(firstvalues, secondvalues,weekvalues,dayvalues):
            print(f"{d} - {k} - {i}-დან {j}-მდე")
            count+=1

            if(count==5):
                break
        print('\n')
        print("ტემპერატურა შემდეგი ათი დღის განმავლობაში")


        # WEEKDAYS AND TEMPERATURES 10 DAYS + INSERTING INTO DATABASE
        for i, j, k, d in zip(dayvalues,weekvalues,firstvalues,secondvalues):
            print(f"{i} - {j} - {k}°-დან {d}°-მდე")
            insert = f"INSERT INTO {city}(WEATHER,WEEKDAY,DAY) values(%s,%s,%s)"
            val = ((f"{k}°-{d}°"),j,i)
            curs.execute(insert,val)

        mydb.commit()


        retry = input("გსურთ თავიდან?(კი/არა): ")
        if (retry != "კი"):
            break



    except Exception as e:
        print(e)
        retry = input("მოხდა შეცდომა. გსურთ თავიდან?(კი/არა): ")
        if (retry != "კი"):
            break




