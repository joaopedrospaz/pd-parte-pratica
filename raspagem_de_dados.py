from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


def get_bitcoin_price():
    driver.get("https://coinmarketcap.com/pt-br/")
    time.sleep(2)
    find_bitcoin_price = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[1]/td[4]/div',
    )

    price = float(find_bitcoin_price.text.split("$")[1].split(".")[0].replace(",", "."))
    return price


def send_email(personal_email):
    price = get_bitcoin_price()
    if price > 300:
        driver.get(
            "https://www.google.com/webhp?hl=pt-BR&ictx=2&sa=X&ved=0ahUKEwiO8IvbueCHAxXXGbkGHZhUPX4QPQgK"
        )
        time.sleep(2)

        search_input = driver.find_element(By.CLASS_NAME, "gLFyf")
        search_input.send_keys("gmail")
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)

        gmail_link = driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md")
        gmail_link.click()
        time.sleep(2)

        login_button = driver.find_element(By.CLASS_NAME, "button--medium")
        login_button.click()
        time.sleep(2)

        input_email = driver.find_element(By.TAG_NAME, "input")
        input_email.send_keys("alunos.pd.pratica@gmail.com")
        input_email.send_keys(Keys.ENTER)
        time.sleep(2)

        input_password = driver.find_element(By.CLASS_NAME, "whsOnd")
        input_password.send_keys("abcd1234@")
        input_password.send_keys(Keys.ENTER)
        time.sleep(8)

        new_email_button = driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3")
        new_email_button.click()
        time.sleep(4)

        input_personal_email = driver.find_element(By.CSS_SELECTOR, ".agP.aFw")
        input_personal_email.send_keys(personal_email)
        input_personal_email.send_keys(Keys.ENTER)

        email_title = driver.find_element(By.CLASS_NAME, "aoT")
        email_title.send_keys("Valor do Bitcoin")
        email_message = driver.find_element(
            By.CSS_SELECTOR, ".Am.aiL.Al.editable.LW-avf.tS-tW"
        )
        email_message.send_keys(f"Valor do Bitcoin está em {price}")
        time.sleep(4)

        driver.find_element(By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()


send_email("email_desejado")
driver.quit()
