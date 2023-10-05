import requests
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto("http://www.flipkart.com")
    links = page.locator("//a").all()
    result = requests.get(links)
    for link in links:
        print(link)




