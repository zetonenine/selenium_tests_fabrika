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

    driver.find_element_by_css_selector("button[class='button button--size-sm button--is-centered button--state-filled']").click()

    driver.find_element_by_xpath("(//div[@class='checkbox checkbox--no-appearance'])[1]").click()
    driver.find_element_by_xpath("(//div[@class='multiselect__tags'])[1]").click()
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[1]").send_keys('Уменьшаемый план')
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[1]").send_keys(Keys.RETURN)

    element = driver.find_element_by_xpath("(//p[contains(text(), 'Связанные платежи')])")

    assert 'Связанные платежи' in element.text, 'Text not found'

    driver.quit()


if __name__ == '__main__':
    main()