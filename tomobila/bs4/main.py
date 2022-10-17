import requests
from bs4 import BeautifulSoup
import csv

# response = requests.get("https://www.tomobila.ma/achat-voiture-occasion/")
# print(response)
# soup = BeautifulSoup(response.text, 'lxml')

with open('cars.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Car name", "price", "city"])
    for page in range(1000):
        response = requests.get(f"https://www.tomobila.ma/achat-voiture-occasion/page/{page}")
        soup = BeautifulSoup(response.text, 'lxml')
        cars = soup.findAll("div", {"class": "listing-list-loop"})
        for car in cars:
            title = car.find("div", "labels").text
            price = car.find("span", "heading-font").text
            city = car.find("div", "value").text
            print("title: ",title, "price: ", price, "city: ", city)
            writer.writerow([title, price, city])

