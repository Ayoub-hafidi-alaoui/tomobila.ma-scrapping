from requests_html import HTMLSession

url = "https://www.tomobila.ma/achat-voiture-occasion/page/0/"
session = HTMLSession()
req = session.get(url)
req.html.render(sleep=2)

cars_div = req.html.xpath("/html/body/div/div[9]/div[2]/div[2]/div[2]/div", first=True)

for car in cars_div.absolute_links:
    req = session.get(car)
    name = req.html.find("a.create-car-alert", first=True)
    price = req.html.find("span.heading-font", first=True)
    if name != None and name.text != "" and name.text != None:
        name = name.text
    if price != None and price.text != "" and price.text != None:
        price = price.text
    print(name, "price: ", price)
