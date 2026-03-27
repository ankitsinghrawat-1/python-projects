from selenium import webdriver
from selenium.webdriver.common.by import By

query = input("Enter product to search on Amazon: ").strip()
if not query:
    query = "laptop"
    print("No input provided. Using default: laptop")

max_results_raw = input("How many results to print? (default 10): ").strip()
max_results = int(max_results_raw) if max_results_raw.isdigit() and int(max_results_raw) > 0 else 10

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")

driver.maximize_window()

driver.find_element(By.XPATH , "//input[@id='twotabsearchtextbox']").send_keys(query)

driver.find_element(By.XPATH , "//input[@id='nav-search-submit-button']").click()

products = driver.find_elements(By.XPATH , "//div[@data-component-type='s-search-result']//h2//span")

if len(products) == 0:
    products = driver.find_elements(By.XPATH , "//h2[contains(@class,'a-size-base-plus')]//span")

print("Total number of products found: " + str(len(products)))

for i, product in enumerate(products[:max_results], start=1):
    if product.text.strip():
        print(str(i) + ". " + product.text)

driver.quit()
