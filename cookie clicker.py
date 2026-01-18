# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import time
#
# edge_option=webdriver.EdgeOptions()
# edge_option.add_experimental_option('detach', True)
# driver=webdriver.Edge(edge_option)
# driver.get('https://ozh.github.io/cookieclicker/')
#
# wait=WebDriverWait(driver,20)
# language = wait.until(EC.element_to_be_clickable((By.ID, 'langSelect-EN')))
# language.click()
#
# # try:
# #     cookie=wait.until(EC.presence_of_element_located((By.ID,'bigCookie')))
# #     cookie_spotted=True
# # except  TimeoutException:
# #     cookie_spotted=False
# # print(cookie_spotted)
# cookie=wait.until(EC.element_to_be_clickable((By.ID,'bigCookie')))
# time.sleep(3)
# # for _ in range(100):
# #     cookie.click()
# from time import time
# wait_time = 5                  # check upgrades every 5 seconds
# timeout = time() + wait_time   # next upgrade check
# five_min = time() + 60 * 5     # stop after 5 minutes
# while True:
#     cookie.click()
#
#     # check upgrades every 5 seconds
#     if time() > timeout:
#         # read cookies
#         cookies_element = driver.find_element(By.ID, "cookies")
#         cookie_count = int(cookies_element.text.split()[0].replace(",", ""))
#
#         # get store products
#         products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")
#
#         # buy most expensive affordable
#         best_item = None
#         for product in reversed(products):
#             if "enabled" in product.get_attribute("class"):
#                 best_item = product
#                 break
#         if best_item:
#             best_item.click()
#             print(f"Bought: {best_item.get_attribute('id')}")
#
#         timeout = time() + wait_time
#
#     if time() > five_min:
#         final_cookies = driver.find_element(By.ID, "cookies").text
#         print(f"Final cookies: {final_cookies}")
#         break
#
#
# # driver.close()
# # driver.quit()

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from time import time as t

# --- Setup Edge ---
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', True)
driver = webdriver.Edge(edge_option)
driver.get('https://ozh.github.io/cookieclicker/')

wait = WebDriverWait(driver, 20)

# --- Step 1: Select English ---
language = wait.until(EC.element_to_be_clickable((By.ID, 'langSelect-EN')))
language.click()
time.sleep(1)  # give a moment for JS to start

# --- Step 2: Dismiss cookie consent banner ---
try:
    consent = driver.find_element(By.CLASS_NAME, "cc_btn")
    consent.click()
    print("Cookie consent dismissed")
except:
    print("No cookie consent found")

# --- Step 3: Wait for big cookie ---
cookie = wait.until(EC.element_to_be_clickable((By.ID, 'bigCookie')))
time.sleep(3)  # let the game initialize fully

# --- Step 4: Setup timers ---
wait_time = 5                 # check upgrades every 5 seconds
timeout = t() + wait_time  # next upgrade check
five_min = t() + 60 * 5    # stop after 5 minutes

# --- Step 5: Main loop ---
while True:
    cookie.click()  # click nonstop
    time.sleep(0.01)  # tiny pause to make clicks register

    # check upgrades every 5 seconds
    if t() > timeout:
        try:
            # get current cookie count
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_count = int(cookies_element.text.split()[0].replace(",", ""))

            # get all store items
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

            # buy the most expensive affordable item
            best_item = None
            for product in reversed(products):  # start from most expensive
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            if best_item:
                best_item.click()
                print(f"Bought: {best_item.get_attribute('id')}")
        except:
            print("Error checking/buying upgrades")

        timeout = t() + wait_time  # reset timer

    # stop after 5 minutes
    if t() > five_min:
        final_cookies = driver.find_element(By.ID, "cookies").text
        print(f"Final cookies: {final_cookies}")
        break

# Optional: close browser
# driver.quit()
