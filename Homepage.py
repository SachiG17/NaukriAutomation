import time
import os
import glob
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NaukriLocators
from selenium.webdriver.common.by import By


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

# Configure Chrome options for CI (headless mode)
chrome_options = Options()
chrome_options.add_argument("--disable-cookies")
chrome_options.add_argument("--headless")  # Required for GitHub Actions
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")  # 🛠️ KEY FIX
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)
driver.get("https://www.naukri.com/")
logging.info("Opened Naukri")
 # optional: print HTML to logs
driver.save_screenshot("debug.png")
driver.maximize_window()

load_dotenv()  # loads variables from .env into environment

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
RESUME_PATH = os.path.abspath("SachinG_Automationtester.pdf")


WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(NaukriLocators.LOGIN_BTN)
).click()
logging.info("Clicked LogIn Button")
driver.find_element(*NaukriLocators.EMAIL).send_keys(EMAIL)
logging.info("Added Username")
driver.find_element(*NaukriLocators.PASSWORD).send_keys(PASSWORD)
logging.info("Added Password")
driver.find_element(*NaukriLocators.LOGIN_SUBMIT).click()
logging.info("Clicked Submit")
driver.find_element(*NaukriLocators.PROFILE_BTN).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(*NaukriLocators.PROFILE_BTN)
)

logging.info("Clicked Profile")
driver.find_element(*NaukriLocators.VIEW_UPDATE).click()
logging.info("Clicked View Update Profile")

upload_button = driver.find_element(*NaukriLocators.UPLOAD)
driver.execute_script("arguments[0].style.display='block';", upload_button)
upload_button.send_keys(RESUME_PATH)
logging.info("clicked upload")

try:
    success_msg = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(NaukriLocators.SUCCESS_MESSAGE)
    )
    print("Resume uploaded successfully.")
except TimeoutException:
    print("Upload failed or success message did not appear in time.")
driver.close()
