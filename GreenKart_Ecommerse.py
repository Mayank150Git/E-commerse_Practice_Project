import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

Service_Obj = Service()
driver = webdriver.Chrome(service = Service_Obj)

#TC1: Hit the URL and Validate if the user is redirected to the correct page

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
assert driver.title == "GreenKart - veg and fruits kart"
driver.implicitly_wait(10)

#TC2: Search for the iteam and add them to the cart

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)

Product_List_after_search = driver.find_elements(By.XPATH, "//h4[@class = 'product-name']")

for Product in Product_List_after_search:
    print(Product.text)

Add_to_Cart = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")

for Buttons in Add_to_Cart:
    for Buttons in (driver.find_element(By.XPATH, "(//div[@class='product'])[1]//button[text()='ADD TO CART']"),driver.find_element(By.XPATH, "(//div[@class='product'])[2]//button[text()='ADD TO CART']")):
        Buttons.click()
        time.sleep(2)
    break

time.sleep(2)

#TC3: View the cart and Verify if the correct iteams are added

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()

Cart_Items = driver.find_elements(By.XPATH, "//ul[@class='cart-items']")

for Items in Cart_Items:
    print(Items.text)

#TC4: Proceed to the CheckOut Page

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("DummyCode")
Explicit_Wait = WebDriverWait(driver, 5)
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

Explicit_Wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

#TC5: Choose the country and Proceed

Selection = Select(driver.find_element(By.XPATH, "//select"))
driver.find_element(By.XPATH, "//select").click()

Selection.select_by_visible_text("Bermuda")

driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

driver.get_screenshot_as_file("Thankyou_page.png")




