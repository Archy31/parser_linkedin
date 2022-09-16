from time import sleep

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from config import base_url, headers


def get_driver():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnofications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    options.set_preference('general.useragent.override', f'{headers["user-agent"]}')

    driver = webdriver.Firefox(options=options)

    return driver


def get_account():
    driver = webdriver.Chrome()

    email = input('Enter your email >>> ')
    password = input('Enter your account password >>> ')

    def get_my_pages(driver):
        try:
            more_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/a'
            pages_xpath = '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/section[1]/div/div[6]/a'
            driver.find_element(by.By.XPATH, value=more_xpath).click()
            sleep(3)
            driver.find_element(by.By.XPATH, value=pages_xpath).click()
            sleep(3)
            comps_class = 'follows-recommendation-card'
            companes = driver.find_elements(by.By.CLASS_NAME, value=comps_class)
            for i in companes:
                title = i.text
                print(title, '\n')
            sleep(7)

        except Exception as e:
            return e

    email_xpath = '/html/body/div/main/div[2]/div[1]/form/div[1]/input'
    pass_xpath = '/html/body/div/main/div[2]/div[1]/form/div[2]/input'
    signin_xpath = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'

    try:
        driver.get(base_url)
        driver.find_element(by.By.XPATH, value='/html/body/nav/div/a[2]').click()
        sleep(3)
        driver.find_element(by.By.XPATH, value=email_xpath).send_keys(email)
        driver.find_element(by.By.XPATH, value=pass_xpath).send_keys(password)
        driver.find_element(by.By.XPATH, value=signin_xpath).click()
        sleep(5)

        get_my_pages(driver)

    except Exception as e:
        return e

    finally:
        driver.close()
        driver.quit()


def main():
    get_account()


if __name__ == '__main__':
    main()
