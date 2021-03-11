from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


def main():
    class Remover():
        def __init__(self):
            self.driver = webdriver.Chrome('./chromedriver.exe')
            self.driver.get('https://discord.com/login')
            self.work()

        def work(self):
            messages = 1
            print("Welcome!\n"
                  "This little program will hopefully help you prune chat you dont want to have(deletes only your "
                  "messages).\n"
                  "To use this program simply choose chat you want to delete, "
                  "click ENTER, click again on chat you want to delete and wait for magic to happen\n"
                  "(You need to login in order to use it - don't know how to do it diffrently >:D)")
            input()
            time.sleep(5)
            name = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[2]/div[1]/div').text
            print(f"Logged as {name}")
            while True:
                chatbox = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[3]/div[2]/div')
                chatbox.click()
                chatbox.send_keys(Keys.ARROW_UP)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('delete', 'space', 'enter', interval=0.25)
                deletebox = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[6]/div[2]/div/div/div[3]/button[1]/div').click()
                messages += 1
                time.sleep(0.5)
    bot = Remover()


if __name__ == '__main__':
    main()
