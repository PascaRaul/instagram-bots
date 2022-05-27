# in same folder with this script needs to be filename.txt containing all the instagram usernames that you want to DM, 1 per line.
# run the script sql_add_data.py to add the usernames from filename.txt inserted in database (dog.db in example bellow - you can change whatever db you want)
# the usernames from filename.txt can be duplicated but in the db will only be inserted one username.
# after the DM has been sent the db is updated and will never send again DM to the same username.
# TIPS: use some scrapper to get fast usernames and copy to filename.txt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import schedule
import random
import sys
import sqlite3

# comment that you want to send
first = "First line"
second = "Second line"
third = "Third line"

forth = "forth line"

fifth = "fifth line"


file_data = [i.strip('\n').split(',') for i in open('filename.txt')]
new_data = [a for a in file_data]  # convert string id to integer

con = sqlite3.connect("dog.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS usernames
                    (user TEXT PRIMARY KEY, bolean INTEGER DEFAULT 0 ) ''')

cur.executemany("INSERT OR IGNORE INTO usernames (user) VALUES (?)", new_data)


options = Options()
# options.add_argument("user-data-dir=/home/pi/.config/chromium/Default")

# uncoment next line if you needed for running on raspberry pi or if you want to run in the background
# options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


def instaschedule():
    class InstagramBot:

        def __init__(self, username, password):
            self.username = username
            self.password = password

            self.driver = webdriver.Chrome(
                executable_path="C:\\Users\\R\\Desktop\\chromedriver.exe", chrome_options=options)
            self.driver.implicitly_wait(10)
            # location of chromedriver on raspberry pi usually
            # self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options)

        def closeBrowser(self):
            self.driver.close()

        def paste_keys(self):
            def mess_input(): return self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Message...']")
            mess_input().click()
            mess_input().clear()
            time.sleep(random.randint(2, 3))

            for letter in first:
                mess_input().send_keys(letter)
                delay = random.randint(1, 5) / 30
                time.sleep(delay)
            time.sleep(random.randint(1, 2))

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            for letter in second:
                mess_input().send_keys(letter)
                delay = random.randint(1, 5) / 30
                time.sleep(delay)
            time.sleep(random.randint(1, 2))

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            for letter in third:
                mess_input().send_keys(letter)
                delay = random.randint(1, 5) / 30
                time.sleep(delay)
            time.sleep(random.randint(1, 2))

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            for letter in forth:
                mess_input().send_keys(letter)
                delay = random.randint(1, 5) / 30
                time.sleep(delay)
            time.sleep(random.randint(1, 2))

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(self.driver).send_keys(
                Keys.RETURN).perform()
            webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()

            for letter in fifth:
                mess_input().send_keys(letter)
                delay = random.randint(1, 5) / 30
                time.sleep(delay)
            time.sleep(random.randint(1, 2))

        def login(self):

            try:

                driver = self.driver
                driver.get("https://www.instagram.com/")
                time.sleep(random.randint(15, 16))
                user_name_elem = driver.find_element_by_xpath(
                    "//input[@name='username']")

            except Exception:
                print("Instagram reload\n")

                time.sleep(random.randint(2, 3))
                driver = self.driver
                driver.get("https://www.instagram.com/")
                time.sleep(random.randint(14, 16))

            try:

                accept_cookies = driver.find_element_by_class_name(
                    "aOOlW.bIiDR")
                accept_cookies.click()
            except Exception:
                print("There are no cookies")
            try:

                time.sleep(random.randint(10, 11))
                user_name_elem = driver.find_element_by_xpath(
                    "//input[@name='username']")
                user_name_elem.clear()
                user_name_elem.send_keys(self.username)
                passworword_elem = driver.find_element_by_xpath(
                    "//input[@name='password']")
                passworword_elem.clear()
                passworword_elem.send_keys(self.password)
                passworword_elem.send_keys(Keys.RETURN)
                time.sleep(random.randint(10, 12))
                self.driver.refresh()
            except Exception:
                print("You are already logged in")
            try:
                time.sleep(random.randint(5, 7))

                second_time_username = driver.find_element_by_xpath(
                    "//input[@name='username']")
                second_time_username.clear()
                second_time_username.send_keys(self.username)
                second_time_password = driver.find_element_by_xpath(
                    "//input[@name='password']")
                second_time_password.clear()
                second_time_password.send_keys(self.password)
                time.sleep(random.randint(14, 16))
                self.driver.refresh()
            except Exception:
                print("No second time user/pass needed")
            time.sleep(4)
            driver = self.driver
            driver.get("https://www.instagram.com/direct/new/?hl=en")
            try:
                time.sleep(random.randint(3, 4))
                not_now = self.driver.find_element_by_xpath(
                    "/html/body/div[6]/div/div/div/div[3]/button[2]")
                not_now.click()
            except Exception:
                print("No not element")
            time.sleep(random.randint(3, 4))

        def instadm(self):
            driver = self.driver
            driver.get("https://www.instagram.com/direct/new/?hl=en")
            time.sleep(random.randint(5, 6))

            def dm_input(): return driver.find_element_by_xpath(
                "//input[@placeholder='Search...']")
            dm_input().click()
            dm_input().clear()

            cur.execute("SELECT user, bolean FROM usernames where bolean = 0")
            usern = cur.fetchone()[0]
            print(usern)
            cur.execute('SELECT bolean FROM usernames WHERE user= ?', (usern,))

            try:
                username = usern
                for letter in username:
                    dm_input().send_keys(letter)
                    delay = random.randint(1, 7) / 30
                    time.sleep(delay)

                time.sleep(random.randint(5, 7))

                user_found = self.driver.find_element_by_xpath(
                    "((//div[@aria-labelledby]/div/span//img[@data-testid='user-avatar'])[1]//..//..//..//div[2]/div[2]/div)[1]")
                user_found.click()
                time.sleep(random.randint(6, 8))

                nextElement = self.driver.find_element_by_xpath(
                    "//div[contains(@class,'rIacr')]")
                nextElement.click()
                time.sleep(random.randint(5, 6))

                ig.paste_keys()
                time.sleep(random.randint(2, 3))

                def mess_input(): return self.driver.find_element_by_xpath(
                    "//textarea[@placeholder='Message...']")
                mess_input().click()

                mess_input().send_keys(Keys.RETURN)
            except Exception:
                print("%s" % usern + " " + "error receving DM")
                time.sleep(random.randint(2, 3))

            cur.execute(
                'UPDATE usernames SET bolean=? WHERE user=?', (1, usern))
            print("%s" % usern + " " + "updated")
            con.commit()
            time.sleep(random.randint(6, 8))

    if __name__ == "__main__":

        username = ""  # insert Instagram username
        password = ""  # insert Instagram password

        ig = InstagramBot(username, password)

        ig.login()

        # loop for sending 5 messages and than sleep 1hour, repeated 5 times = 25DM send/day
        try:

            for i in range(5):
                try:
                    ig.instadm()
                    time.sleep(random.randint(2, 3))
                except Exception:
                    continue
            print("finished 1st loop, time to sleep")
            time.sleep(random.randint(60*61, 60*65))

            for i in range(5):
                try:
                    ig.instadm()
                    time.sleep(random.randint(2, 3))
                except Exception:
                    continue
            print("finished 2nd loop, time to sleep")
            time.sleep(random.randint(60*61, 60*65))

            for i in range(5):
                try:
                    ig.instadm()
                    time.sleep(random.randint(2, 3))
                except Exception:
                    continue
            print("finished 3rd loop, time to sleep")
            time.sleep(random.randint(60*61, 60*65))

            for i in range(5):
                try:
                    ig.instadm()
                    time.sleep(random.randint(2, 3))
                except Exception:
                    continue
            print("finished 4th loop, time to sleep")
            time.sleep(random.randint(60*61, 60*65))

            for i in range(5):
                try:
                    ig.instadm()
                    time.sleep(random.randint(2, 3))
                except Exception:
                    continue
            print("finished 5th loop, time to sleep and finish")
            time.sleep(random.randint(20, 27))

        except Exception:
            ig.closeBrowser()
            con.commit()
            con.close()

        con.commit()
        con.close()
        ig.closeBrowser()
        sys.exit()


# uncomment bellow line to start the bot immediately
# instaschedule()

#####Schedule to start every day- good for raspberry pi where script run forever####
# random time for starting the bot 1153 means 11:53 time every day - !don't insert values bigger that 60 at last two digits
randomtime = random.randint(1153, 1158)
for i in str(randomtime):
    s = str(randomtime)
    s1 = s[0:2]
    s2 = s[2:4]

timeComputed = s1 + ":" + s2
print(timeComputed)

schedule.every().day.at(timeComputed).do(instaschedule)
while True:
    schedule.run_pending()
    time.sleep(1)
