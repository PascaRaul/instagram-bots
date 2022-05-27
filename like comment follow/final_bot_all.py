from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import schedule
import random
import sys


options = Options()
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
            # location of chromedriver.exe from your computer
            self.driver = webdriver.Chrome(
                executable_path="C:\\Users\\R\\Desktop\\chromedriver.exe", chrome_options=options)
            # location of chromedriver on raspberry pi usually
            # (executable_path="/usr/bin/chromedriver", chrome_options=options)

        def closeBrowser(self):
            self.driver.close()

        def login(self):

            driver = self.driver
            driver.get("https://www.instagram.com/")
            time.sleep(random.randint(5, 7))

            try:

                accept_cookies = driver.find_element_by_class_name(
                    "aOOlW.bIiDR")
                accept_cookies.click()
            except Exception:
                print("there are no cookies")
            try:

                time.sleep(random.randint(10, 15))
                user_name_elem = driver.find_element_by_xpath(
                    "//input[@name='username']")
                user_name_elem.clear()
                user_name_elem.send_keys(self.username)
                passworword_elem = driver.find_element_by_xpath(
                    "//input[@name='password']")
                passworword_elem.clear()
                passworword_elem.send_keys(self.password)
                passworword_elem.send_keys(Keys.RETURN)
                time.sleep(random.randint(2, 3))
            except Exception:
                print("you are already logged in")
            try:
                time.sleep(random.randint(2, 3))

                second_username = driver.find_element_by_xpath(
                    "//input[@name='username']")
                second_username.clear()
                second_username.send_keys(self.username)
                second_password = driver.find_element_by_xpath(
                    "//input[@name='password']")
                second_password.clear()
                second_password.send_keys(self.password)
                time.sleep(random.randint(2, 3))
            except Exception:
                print("all good")
            time.sleep(4)

        def like_photo(self, hashtag):
            driver = self.driver
            driver.get(
                "https://www.instagram.com/explore/tags/" + hashtag + "/")
            time.sleep(random.randint(2, 3))

            # gathering photos
            pic_hrefs = []
            for i in range(1, 3):
                try:
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randint(2, 3))
                    # get tags
                    hrefs_in_view = driver.find_elements_by_tag_name('a')
                    # finding relevant hrefs
                    hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                     if '.com/p/' in elem.get_attribute('href')]
                    # building list of unique photos
                    [pic_hrefs.append(href)
                     for href in hrefs_in_view if href not in pic_hrefs]

                except Exception:
                    continue

            # Liking photos
            # pic2 =pic_hrefs[8:15] #nine posts after top nine
            pic2 = pic_hrefs[1:9]  # top nine posts
            unique_photos = len(pic2)
            for pic_href in pic2:
                driver.get(pic_href)
                time.sleep(random.randint(2, 3))
                try:
                    #####Comment function#####
                    # n= [1,2,3,4] # 50% comment
                    # r = random.choice(n)
                    # if r == 1:
                    #     comment_input =lambda: self.driver.find_element_by_class_name('Ypffh')
                    #     time.sleep(random.randint(2, 3))
                    #     comment_input().click()
                    #     comment_input().clear()
                    #     #comments:
                    #     lines = open('dogquote.txt').readlines()
                    #     random.shuffle(lines)
                    #     open('random_quotes.txt', 'w').writelines(lines)

                    #     lines = open('greetings.txt').readlines()
                    #     random.shuffle(lines)
                    #     open('random_greeting.txt', 'w').writelines(lines)

                    #     # emojis = []
                    #     # random_emojis = random.choice(emojis)

                    #     quote = open('random_quotes.txt').read().splitlines()
                    #     greet = open('random_greeting.txt').read().splitlines()
                    #     myline =random.choice(greet)
                    #     myline2 =random.choice(quote)

                    #     com1 = myline +" " + myline2
                    #     com2 = myline2
                    #     com_all =[com1, com2]
                    #     comments =random.choice(com_all)
                    #     #end_comments
                    #     comment = comments
                    #     for letter in comment:
                    #         comment_input().send_keys(letter)
                    #         delay = random.randint(1, 7) / 30
                    #         time.sleep(delay)
                    #     time.sleep(random.randint(2, 3))

                    #     # comment_input().send_keys(Keys.RETURN)

                    time.sleep(random.randint(2, 4))
                    def like_button(): return self.driver.find_element_by_xpath(
                        '//span[@class="fr66n"]')
                    like_button().click()
                    time.sleep(random.randint(2, 4))

                    def follow_button(): return self.driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
                    follow_button().click()
                    time.sleep(random.randint(2, 4))

                    for second in reversed(range(0, random.randint(30, 35))):
                        print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                        + " | Sleeping " + str(second))
                        time.sleep(1)

                except Exception as e:
                    time.sleep(random.randint(2, 3))
                unique_photos -= 1

    if __name__ == "__main__":

        username = ""  # insert instagram username
        password = ""  # insert instagram password

        ig = InstagramBot(username, password)
        ig.login()

        hashtags = []  # insert hashtags

    while True:
        try:
            tag = hashtags[len(hashtags)-1]
            ig.like_photo(tag)
            hashtags.pop()
            time.sleep(random.randint(60*40, 60*50))
        except Exception:

            ig.closeBrowser()


# uncomment line bellow if you want to start the bot instantly
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
