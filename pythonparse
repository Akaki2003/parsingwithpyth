import requests
from bs4 import BeautifulSoup

while True:
    try:
        #IN CASE YOU ENTER WRONG CITY, DEFAULT GOES TO TBILISI
        city = input("დაასახელეთ რომელი ქალაქის პროგნოზი გსურთ: ")
        URL = (f"https://amindi.ge/ka/city/{city}/?d=10")
        req = requests.get(URL)
        soup = BeautifulSoup(req.content, 'html5lib')

        weather = soup.findAll('div', class_='degrees')
        weekdays = soup.findAll('div', class_='weekDay')
        city = soup.findAll('div',class_='weather-current pt-0')
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


        # WEEKDAYS AND TEMPERATURES 10 DAYS
        for i, j, k, d in zip(dayvalues,weekvalues,firstvalues,secondvalues):
            print(f"{i} - {j} - {k}°-დან {d}°-მდე")
            count += 1


        retry = input("გსურთ თავიდან?(კი/არა): ")
        if (retry != "კი"):
            break



    except Exception as e:
        # print(e)
        retry = input("მოხდა შეცდომა. გსურთ თავიდან?(კი/არა): ")
        if (retry != "კი"):
            break




