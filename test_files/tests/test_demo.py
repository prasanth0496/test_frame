

def test_flipkart(page):
    page.goto("https://www.flipkart.com")
    page.locator("(//input[@type='text'])[2]").fill("8667402754")
    page.locator("//*[@id='container']/div/div[3]/div/div[2]/div/form/div[3]/button").click()
