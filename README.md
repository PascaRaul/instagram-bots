# Python Instagram bots

Both bots work on raspberry pi and on desktop. <br />
To run on descktop you need to download chromedriver for your current Chrome version.<br />
To run on raspberry pi uncomment line : <br />
options.add_argument('--headless')<br />
and bellow <br />
self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options) (and insert the location of chromedriver on raspberry pi)<br />
<br />
1.Direct message bot:<br />
a.first update the db following the steps bellow<br />
# in same folder with this script needs to be filename.txt containing all the instagram usernames that you want to DM, 1 per line.<br />
# run the script sql_add_data.py to add the usernames from filename.txt inserted in database (dog.db in example bellow - you can change whatever db you want)<br />
# the usernames from filename.txt can be duplicated but in the db will only be inserted one username.<br />
# after the DM has been sent the db is updated and will never send again DM to the same username.<br />
# TIPS: use some scrapper to get fast usernames and copy to filename.txt<br />
b.fill the username and password for instagram<br />
c.write the DM that bot should send to usernames<br />
d.compute the time you want to automaticly run the script every day<br />
e.run the autorestart_botDM.py script to start automatically next day after it finished.<br />
<br />
2.Like, Comment and follow bot:<br />
a.fill the username and password for instagram<br />
b.write the comment that bot should send to posts (curently disabled)<br />
c.insert hashtags<br />
d.compute the time you want to automaticly run the script every day<br />
e.run the autorestart_bot.py script to start automatically next day after it finished.<br />
