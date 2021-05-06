from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import email, password, main_link


def main():
    driver = webdriver.Chrome()
    driver.get(main_link)
    driver.implicitly_wait(5)

    # log in
    driver.find_element_by_css_selector("input[type='email']").send_keys(email)
    driver.find_element_by_css_selector("input[type='password']").send_keys(password)
    driver.find_element_by_css_selector("button[class='button button--size-md button--is-rounded button--"
                                        "is-block button--is-centered button--state-filled']").send_keys(Keys.RETURN)

    # open new tab 'Статьи расходов'
    driver.find_element_by_xpath("//button[@class='button button--size-sm button--is-square "
                                         "button--is-rounded button--is-centered button--state-secondary']").click()
    driver.find_element_by_xpath("(//a[@class='side__link side__link--no-icon'])[4]").send_keys(
        Keys.COMMAND + Keys.RETURN)
    tabs = driver.window_handles
    driver.find_element_by_css_selector("button[class='button button--size-sm button--is-square button--is-rounded"
                                        " button--is-centered button--state-secondary']").click()
    driver.switch_to.window(tabs[1])
    driver.find_element_by_css_selector("button[class='button button--size-sm button--is-centered button--state-filled']").click()

    # create new "Статью расходов"
    driver.find_element_by_xpath("(//div[@class='checkbox__content'])[1]").click()
    driver.find_element_by_css_selector("input[class='input__input']").send_keys('Продовольственные Товары')
    driver.find_element_by_css_selector("button[type='submit']").click()
    driver.switch_to.window(tabs[0])

    # create new 'платёж'
    driver.find_element_by_css_selector("button[class='button button--size-sm button--is-centered button--state-filled']").click()
    driver.find_element_by_xpath("(//div[@class='checkbox checkbox--no-appearance'])[1]").click()
    driver.find_element_by_xpath("(//textarea[@class='input__input'])[1]").send_keys('Оплата за 15т товаров')
    driver.find_element_by_xpath("(//div[@class='checkbox__content'])[4]").click()
    driver.find_element_by_xpath("(//input[@class='input__input'])[1]").send_keys(150250)
    driver.find_element_by_xpath("(//input[@class='input__input'])[2]").send_keys(150250)
    driver.find_element_by_xpath("(//div[@class='checkbox checkbox--no-appearance'])[4]").click()

    driver.find_element_by_xpath("(//div[@class='multiselect__tags'])[1]").click()
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[1]").send_keys('Продовольственные Товары')
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[1]").send_keys(Keys.RETURN)

    driver.find_element_by_xpath("(//div[@class='multiselect__tags'])[6]").click()
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[6]").send_keys('Продовольство')
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[6]").send_keys(Keys.RETURN)

    driver.find_element_by_css_selector("button[class='button button--size-sm button--is-centered"
                                        " button--state-filled']").click()

    # screenshot
    driver.save_screenshot("screenshot.png")
    sleep(3)

    # add filter info
    driver.find_element_by_css_selector("div[class='header__side']").click()
    driver.find_element_by_xpath("(//div[@class='form-field__field'])[3]").click()
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[3]").send_keys('Продовольственные Товары')
    driver.find_element_by_xpath("(//input[@class='multiselect__input'])[3]").send_keys(Keys.RETURN)

    # open "Статьи расходов"
    driver.find_element_by_xpath("//button[@class='button button--size-sm button--is-square "
                                        "button--is-rounded button--is-centered button--state-secondary']").click()
    driver.find_element_by_xpath("(//a[@class='side__link side__link--no-icon'])[4]").click()

    # find and delete "Статью расходов"
    element = driver.find_element_by_xpath("(//table[@type='table']/tbody/tr/td[.='Продовольственные Товары']/..)[1]")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    driver.find_element_by_xpath("(//button[@class='button button--size-sm button--is-centered "
                                 "button--state-danger'])").click()

    driver.close()


if __name__ == '__main__':
    main()