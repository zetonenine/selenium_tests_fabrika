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
    driver.find_element_by_xpath("(//div[@class='checkbox checkbox--no-appearance'])[2]").click()

    list_of_headers = []
    for i in range(1, 5):
        elem = driver.find_element_by_xpath(f"(//div[@class='typography typography--type-title'])[{i}]")
        list_of_headers.append(elem.text)

    print(list_of_headers)
    assert 'За что' not in list_of_headers, 'Text is present in the list'

    driver.quit()


if __name__ == '__main__':
    main()