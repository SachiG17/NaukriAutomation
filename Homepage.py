import time
import os
import glob
import logging
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NaukriLocators

# 🔄 Delete old log files
for old_log in glob.glob("naukri_upload_log_*.log"):
    try:
        os.remove(old_log)
    except Exception as e:
        print(f"⚠️ Could not delete {old_log}: {e}")

#Setup Logging
timestamp = time.strftime("%Y%m%d-%H%M%S")
log_filename = f"naukri_upload_log_{timestamp}.log"

# Configure logging
logging.basicConfig(
    filename=log_filename,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

driver = webdriver.Chrome()
driver.implicitly_wait(30)
chrome_options = Options()
chrome_options.add_argument("--disable-cookies")
driver.get("https://www.naukri.com/")
logging.info("Opened Naukri")
driver.maximize_window()

driver.find_element(*NaukriLocators.LOGIN_BTN).click()
logging.info("Clicked LogIn Button")
driver.find_element(*NaukriLocators.EMAIL).send_keys("sachinghanteppagol17@gmail.com")
logging.info("Added Username")
driver.find_element(*NaukriLocators.PASSWORD).send_keys("Allthebest@2025")
logging.info("Added Password")
driver.find_element(*NaukriLocators.LOGIN_SUBMIT).click()
logging.info("Clicked Submit")
driver.find_element(*NaukriLocators.PROFILE_BTN).click()
logging.info("Clicked Profile")
driver.find_element(*NaukriLocators.VIEW_UPDATE).click()
logging.info("Clicked View Update Profile")

upload_button = driver.find_element(*NaukriLocators.UPLOAD)
driver.execute_script("arguments[0].style.display='block';", upload_button)
upload_button.send_keys("C:\\Users\\Sachin\\PycharmProjects\\NaukriUpdate\\SachinG_Automationtester.pdf")
logging.info("clicked upload")

try:
    success_msg = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(NaukriLocators.SUCCESS_MESSAGE)
    )
    print("Resume uploaded successfully.")
except TimeoutException:
    print("Upload failed or success message did not appear in time.")
driver.close()
