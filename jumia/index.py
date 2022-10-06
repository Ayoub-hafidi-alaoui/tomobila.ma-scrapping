from requests_html import HTMLSession
import csv
import time


session = HTMLSession()

with open("jumia_products.csv", "w" ,newline='') as file:
    writer = csv.writer(file)
    product_id = 0
    writer.writerow(["id", "product_name", "price", "reviews_count", "avg_rate"])

    for x in range(1, 51):
        url = f"https://www.jumia.ma/all-products/?page={x}#catalog-listing"
        page = session.get(url)
        print(f"page number{x}")
        all_products = page.html.xpath("/html/body/div/main/div[2]/div[3]/section/div[1]", first=True)
        for product in all_products.absolute_links:
            product_page = session.get(product)
            product_name = product_page.html.find('h1.-pbxs', first=True)
            if(product_name == None):
                product_name = "no title"
            else:
                product_name = product_page.html.find('h1.-pbxs', first=True).text
            price = product_page.html.find("span.-fs24", first=True).text
            reviews = product_page.html.find("p.-pts", first=True)
            if(reviews == None):
                reviews = 0  
            else:
                reviews = product_page.html.find("p.-pts", first=True).text
            avg_rate = product_page.html.find("span.-b", first= True).text
            print("===========")
            print(product_id,product_name, price, reviews, avg_rate)
            product_id +=1
            writer.writerow([product_id, product_name, price, reviews, avg_rate])


    

