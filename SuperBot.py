import time
print("""********************************************           -InstaBot-         ***********************************************

The Following software is an A.I which is used as an Instagram-Bot______[Creator : ASHWIN] :
And this Bot can increase followers and overall engagement of an INSTA - Account (1500+ Followers-Tested Fine)
Just Enter the Username and Password , than select the feature you wants to use:
Pls Close the window of GUI before entering into the bot:)
PLs STOP the software if anything suspisious gets found
=>This Bot can Attract Around 50 - 100 Followers/day With 100% Activeness and Full Organic Growth
::::::::::::::::New Accounts Find Changes in Few Hours of Use------| Only For Meme Pages |::::::::::::::::::::::::::::::::::::::

********************************************************************************************************************************

                                        version 1.0- InstaBot-Ashwin
                                        
******************************************************************************************************************************** 
                                       Please Wait For a While ......""")
start = time.time()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import pandas as pd
import os

from tkinter import *
master = Tk()
master.title('COMMAND BOT')
master.geometry('300x200')
Label(master,text='COMMAND BOT , SELECT FEATURES :',font=30).grid(row=0,column=1)
Label(master,text='Please close this window to start',font=30).grid(row=4,column=1)
follower_choice=7
like_choice= 2
comment_choice=8

user_username = "9gag_st"
user_password = "05012020"

print(f'****************************************        Account User : {user_username}        ******************************')
def followers():
    global follower_choice
    if var1.get()==1:
        follower_choice=2
        print('Follow on')
    else:
        follower_choice = 7
        print('Follow off')

def likes():
    global like_choice
    if var2.get()==1:
        like_choice=2
        print('likes on')
    else:
        like_choice = 3
        print('likes off')
def comments():
    global comment_choice
    if var3.get()==1:
        comment_choice=8
        print('comment on')
    else:
        comment_choice = 0
        print('comment off')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Checkbutton(master, text="Follow", command= followers,variable=var1).grid(row=3,column=1, sticky=W)
Checkbutton(master, text="Like",command=likes,variable=var2).grid(row=1,column=1, sticky=W)
Checkbutton(master, text="Comment",command=comments,variable=var3).grid(row=2,column=1, sticky=W)
Button(master,text='Start',command=master.quit()).grid(row=4,column=2, sticky=W)
mainloop()



# user_list = []
user_list = pd.read_csv('last_users_followed_list.csv')
user_list = list(user_list['Accounts'])

webdriver = webdriver.Chrome("chromedriver.exe")
sleep(2)
webdriver.get('https://www.instagram.com')
sleep(3)


comment_1 = 'hahah, Amazing POST, dUDE can u CHECK OUT MY PAGE TOO,and drop a follow if u like it:)'
comment_2 = 'This post real? Lol i laughed hard after seeing this thing, can u check my pg and drop a follow?:0'
comment_3 = 'Dang , From where do u get these memes?----Can u check out my page too and drop a follow if u like it--:)'
comment_4 = 'hoosh!!Hilarious, would you mind checking my page too?:) Wanna be fan? LOL'
username = webdriver.find_element_by_name('username')
username.send_keys(user_username)
password = webdriver.find_element_by_name('password')
password.send_keys(user_password)
login_button = webdriver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(5)
try:
    webdriver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
    sleep(3)
except:
    print("success running...")
notnow = webdriver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['memes', 'animememes', 'memepage', 'dankmemes', 'weebmemes', 'memesfordays']
# hashtag_list = ['dogs' , 'cats' , 'elephant' , 'doggo' , 'kitty']


prev_user_list = []
# prev_user_list = pd.read_csv('last_users_followed_list.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
new_followers = []

tag = randint(0, len(hashtag_list) - 1)
followed = 0
likes = 0
comments = 0
total_user = 0
cycle = 0

follower_increment = 0
webdriver.get(f'http://www.instagram.com/9gag_st')
sleep(5)
follower_count = webdriver.find_element_by_xpath(
     '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
follower_count = int(follower_count.replace(',', ''))
initial_follower = follower_count
following_count = webdriver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
following_count = int(following_count.replace(',', ''))
initial_following = following_count
print(f"Initial Followers = {follower_count}-----------------Initial Following = {following_count}")
while (cycle < 100):
        pop_clone = 3
        term = randint(-3, 0)
        # term = 1  # follow - unfollow quicker (time - Approx 4 mins)
        if term > 0:
            webdriver.get("https://www.instagram.com/watchtopzzvideo")
            sleep(3)

            following_button = webdriver.find_element_by_xpath("//a[contains(@href,'following')]")
            following_button.click()
            sleep(randint(5, 8))
            following_number = webdriver.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
            tab_window = webdriver.find_element_by_xpath("//div[@class='isgrP']")
            scroll = 0
            joker = 1
            trial_follow = 1
            trial_following = 1
            sleep(randint(5, 9))

            if webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button').text == 'Following':
                print('Time to unFollow')
                if trial_following > 0:
                    if joker > 0:
                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[4]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[4]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[5]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[5]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[6]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[6]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[7]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[7]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 4))
                    while scroll < 1:
                        webdriver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                            tab_window)

                        # tab_window.send_keys(Keys.PAGE_DOWN)
                        print('okay')

                        scroll += 1
                        sleep(0.2)
                    roker = 1
                    if roker > 0:
                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[8]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[8]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 7))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[9]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[9]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 6))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[10]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[10]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(3, 9))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[11]/div/div[3]/button').text == 'Following':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[11]/div/div[3]/button").click()
                            sleep(0.5)
                            webdriver.find_element_by_xpath(
                                "/html/body/div[5]/div/div/div[3]/button[1]").click()
                            print("unfollowed")
                        sleep(randint(2, 7))
                        webdriver.get('http://www.instagram.com/watchtopzzvideo')
                        sleep(randint(3, 6))

                        end = time.time()
                        elapsed_time = end - start
                        yummy = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                        print(yummy)
                        following_button = webdriver.find_element_by_xpath("//a[contains(@href,'following')]")
                        following_button.click()
                        sleep(5)
            if webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button').text == 'Follow':
                if trial_follow > 0:
                    if joker > 0:
                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button").click()
                            sleep(0.5)

                        sleep(randint(2, 9))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[4]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[4]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 5))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[5]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[5]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[6]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[6]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 5))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[7]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[7]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))
                    while scroll < 1:
                        webdriver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                            tab_window)

                        # tab_window.send_keys(Keys.PAGE_DOWN)
                        print('okay')

                        scroll += 1
                        sleep(0.2)
                    roker = 1
                    if roker > 0:
                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[8]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[8]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[9]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[9]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[10]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[10]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(6, 12))

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div/div[2]/ul/div/li[11]/div/div[3]/button').text == 'Follow':
                            webdriver.find_element_by_xpath(
                                "/html/body/div[4]/div/div[2]/ul/div/li[11]/div/div[3]/button").click()
                            sleep(0.5)

                            print("followed")
                        sleep(randint(2, 4))
                        webdriver.get('http://www.instagram.com/watchtopzzvideo')
                        sleep(4)
                        following_button = webdriver.find_element_by_xpath("//a[contains(@href,'following')]")
                        following_button.click()
                        sleep(randint(15, 25))
                        webdriver.refresh()
                        sleep(randint(4, 10))
                        end = time.time()
                        elapsed_time = end - start
                        yummy = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                        sleep(randint(15, 40))
                        webdriver.get(f'https://www.instagram.com/{user_username}')
                        sleep(5)
                        follower_count_1 = int(
                            webdriver.find_element_by_xpath(
                                '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',',
                                                                                                                  ''))
                        print(
                            f'''{yummy} : IF {int(initial_follower)}------------------ >CF {int(follower_count_1)}--------------
                ---------------------------  + {int(follower_count_1)-int(initial_follower)}  -------------------''')
                        follower_increment = int(follower_count_1) - int(initial_follower)

                        # os.remove(f'{user_username}_runtimegrowth.csv')
                        # new_followers = new_followers.append(follower_increment)
                        # new_followers = pd.DataFrame(new_followers)
                        # new_followers.to_csv(f'{user_username}_runtimegrowth.csv')
                        sleep(randint(20, 35))
        # like - comment - follow (time - Approx 30 mins)
        if term < 0:
            print('Time To Explore....Approx Time 30 mins')
            for hashtag in hashtag_list:
                webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
                sleep(5)
                counter = 0
                while counter < 2:
                    tab_window = webdriver.find_element_by_xpath('/html')
                    tab_window.send_keys(Keys.PAGE_DOWN)
                    sleep(0.2)
                    counter += 1
                sleep(randint(2, 5))
                first_thumbnail = webdriver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
                first_thumbnail.click()
                sleep(randint(2, 4))

                random_number = randint(1, 15)
                pop = 0

                print(
                    '**************************************************************************************Program proceeding')
                while (pop < random_number):
                    try :
                        sleep(5)
                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                            username = webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
                            print("Current Profile : " + username)

                            sleep(2)


                            if username not in user_list:
                                random_like = randint(1, 2)
                                print(f"new user : processing...{int(random_like)}")
                                if random_like == like_choice:
                                    print("Like passed! Successfully!!")

                                    # Liking the picture
                                    button_like = webdriver.find_element_by_css_selector(
                                        'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > svg')
                                    button_like.click()
                                    likes += 1
                                    sleep(randint(8, 15))
                                random_comment = randint(1, 45)

                                if random_comment < comment_choice:

                                    print("comment passed! Successfully!!")

                                    # Comments and tracker
                                    comm_prob = randint(7, 11)
                                    # comm_prob = 0  # if action blocked from commenting
                                    # print('{}_{}: {}'.format(hashtag, x, comm_prob))
                                    if comm_prob > 6:
                                        comments += 1
                                        webdriver.find_element_by_css_selector(
                                            'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > div > svg').click()
                                        comment_box = webdriver.find_element_by_css_selector(
                                            "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")

                                        randuser_1 = user_list[randint(4, len(user_list) - 1)]
                                        randuser_2 = user_list[randint(4, len(user_list) - 1)]
                                        # randuser_2=user_list[randint((len(user_list)/2,len(user_list)-1))]

                                        if (comm_prob == 8):
                                            ##username = webdriver.find_element_by_css_selector(
                                               # 'body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.Jv7Aj.pZp3x > div > a').text
                                            comment_box.send_keys(
                                                f"""Hey {username} , {comment_1}""")
                                            sleep(3)
                                        elif (comm_prob == 7):
                                            comment_box.send_keys(f'''Hey {username}, {comment_2}''')
                                            sleep(3)
                                        elif comm_prob == 9:
                                            comment_box.send_keys(f'''Bruhhh!!{username}, {comment_3}''')
                                            sleep(3)
                                        elif comm_prob == 10:
                                            comment_box.send_keys(f'''So cool! :), Drop a Follow on my page Else i"ll delete u''')
                                            sleep(3)
                                        elif comm_prob == 11:
                                            comment_box.send_keys(
                                                f'''Sup? {username}, {comment_4}''')
                                            sleep(3)
                                        # Enter to post comment
                                        sleep(1)
                                        webdriver.find_element_by_css_selector(
                                            'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button').click()
                                        sleep(5)
                                        random_follow = 2
                                        if random_follow == follower_choice:
                                            print('Follow passed')
                                            print(username + "  : Followed")
                                            if webdriver.find_element_by_css_selector(
                                                    '#react-root > section > main > div > div.ltEKP > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button').text == 'Follow':
                                                webdriver.find_element_by_css_selector(
                                                    '/#react-root > section > main > div > div.ltEKP > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button').click()

                                                followed += 1

                                        sleep(randint(11, 17))




                                total_user += 1
                                user_list.append(username)

                            os.remove('last_users_followed_list.csv')
                            end = time.time()
                            elapsed_time = end - start
                            yummy = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

                            updated_user_df = pd.DataFrame(user_list)
                            updated_user_df['Accounts'] = user_list
                            updated_user_df.to_csv('last_users_followed_list.csv')
                            print(
                                f'Time : {yummy} | Total : {total_user} | {pop}/{random_number} | Likes : {likes} | Comments : {comments} | Followed : {followed}')
                            # Next picture

                            webdriver.find_element_by_link_text('Next').click()
                            sleep(randint(8, 13))
                            pop_clone = 0

                    except:
                        print(
                            '=-=-=-=-=-=-=-=-=-=-=-=-=--  | page not loaded so next post.. | =-=-=-=-=-=-=-=-=-=-=-=-=-')
                        # webdriver.find_element_by_link_text('Next').click()
                        pop_clone = 1
                        sleep(1)
                    if pop_clone == 0:
                        pop = pop + 1
                    if pop_clone == 1:
                        pop = pop + 5
                    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next

            end = time.time()
            elapsed_time = end - start
            yummy = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            sleep(randint(15, 25))
            webdriver.get(f'https://www.instagram.com/9gag_st')
            sleep(5)
            follower_count_1 = int(
                webdriver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',', ''))
            print(
                f'''{yummy} : IF {int(initial_follower)}------------------ >CF {int(follower_count_1)}--------------
               ---------------------------  + {int(follower_count_1)-int(initial_follower)}  -------------------''')
            follower_increment = int(follower_count_1) - int(initial_follower)
            # os.remove(f'{user_username}_runtimegrowth.csv')

            # new_followers = pd.DataFrame(new_followers)
            # new_followers = new_followers.append(follower_increment)
            # new_followers.to_csv('last_users_followed_list.csv')

            sleep(randint(6, 9))

        if term == 0:
            end = time.time()
            elapsed_time = end - start
            yummy = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            webdriver.get(f'https://www.instagram.com/9gag_st')
            sleep(5)
            follower_count_1 = int(
                webdriver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',', ''))
            print(
                f'''{yummy} : IF {int(initial_follower)}------------------ >CF {int(follower_count_1)}--------------
    ---------------------------  + {int(follower_count_1)-int(initial_follower)}  -------------------''')
            follower_increment = int(follower_count_1) - int(initial_follower)
            # os.remove(f'{user_username}_runtimegrowth.csv')

            # new_followers = pd.DataFrame(new_followers)
            # new_followers = new_followers.append(follower_increment)
            # new_followers.to_csv(f'{user_username}_runtimegrowth.csv')
            # print(f'Current Progress saved in File : {user_username}----->PROFILE REFRESH<-------|')

        cycle += 1

