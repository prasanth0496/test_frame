import json

from playwright.sync_api import sync_playwright

def products_details():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("//input[@id='user-name']").fill("standard_user")
        page.locator("//input[@id='password']").fill("secret_sauce")
        page.locator("//input[@id='login-button']").press("Enter")
        list_of_products = page.locator("//div[@id='inventory_container']/div/div/div[2]").all()
        products_list = []
        for i in list_of_products:
            product_name = i.locator("//div[@class='inventory_item_name']").text_content()
            description = i.locator("//div[@class='inventory_item_desc']").text_content()
            price = i.locator("//div[@class='inventory_item_price']").text_content()

            product_detail= {
                'name': product_name,
                'price': price,
                'description': description
            }
            products_list.append(product_detail)

            print(product_detail)
    with open('sauce_products.json', 'w') as json_file:
        json.dump(products_list,json_file)

products_details()


