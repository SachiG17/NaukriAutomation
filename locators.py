from selenium.webdriver.common.by import By
class NaukriLocators:
    LOGIN_BTN = (By.ID, "login_Layer")
    EMAIL = (By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Enter your password']")
    LOGIN_SUBMIT = (By.XPATH,"//button[@type='submit']")
    PROFILE_BTN = (By.XPATH,"//div[@class='nI-gNb-drawer__icon']")
    VIEW_UPDATE = (By.LINK_TEXT, "View & Update Profile")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Resume has been successfully uploaded.')]")
    UPLOAD = (By.XPATH,"//input[@type='file']")