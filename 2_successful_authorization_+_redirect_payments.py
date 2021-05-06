from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import email, password, main_link


def main():
    driver = webdriver.Chrome()
    driver.get(main_link)
    driver.implicitly_wait(5)

    driver.find_element_by_css_selector("input[type='email']").send_keys(email)
    driver.find_element_by_css_selector("input[type='password']").send_keys(password)

    driver.find_element_by_css_selector("button[class='button button--size-md button--is-rounded button--"
                                        "is-block button--is-centered button--state-filled']").send_keys(Keys.RETURN)

    header = driver.find_element_by_xpath("//h1[@class='typography typography--type-heading']")

    assert 'Платежи' in header.text, 'Wrong Header'

    driver.quit()

if __name__ == '__main__':
    main()