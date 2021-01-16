import requests
import json
import time
from colorama import Fore,init
from time import sleep


count=0

green_color = "\033[1;93m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"
print( green_color +'''


  _______ _ _ _______    _            _____ _               _             
 |__   __(_) |__   __|  | |          / ____| |             | |            
    | |   _| | _| | ___ | | ________| |    | |__   ___  ___| | _____ _ __ 
    | |  | | |/ / |/ _ \| |/ /______| |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |  | |   <| | (_) |   <       | |____| | | |  __/ (__|   <  __/ |   
    |_|  |_|_|\_\_|\___/|_|\_\       \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                          
                                                                          
           

==============================================
[developer] => FaLaH - 0xfff0800 
[developer_snapchat] => flaah999
[Edting] => Wx
[insta] => oh.bx
[snap] => oh-bx
==============================================

''')

falah = input('''
1 - TikTok-Checker - username list
2 - TikTok-Checker - Suggestions
3 - TikTok-Checker - username list no sessionid
-> ''')


if falah =="3":

    user = input ("username list: ")
    print("")
    print("Without the session ID, you will see the closed accounts available")
    print("")

    signature = "oKxAeAAgEBgX6bvJMQKua6CsQWAAP4r"
    verifyFp = ""

    referer = "https://www.tiktok.com/@0xfff0800"
    password = open(user).read().splitlines()

        # Back up one character, print a space to erase the spinner, then a newline
        # so that the prompt after the program exits isn't on the same line as our
        # message


    for password in password:
          url = "https://m.tiktok.com/node/share/user/@"+password+"/?count=30&id=1&type=5&secUid=&maxCursor=1&minCursor=0&sourceType=12&appId=1233" + \
    "&verifyFp=" + verifyFp + \
    "&_signature=" + signature
          response = requests.request("GET",url, headers={"method": "GET",
                                "accept-encoding": "gzip, deflate, br",
                                "Referer": referer,
                                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
                                })
          post = str (response.json ()["userInfo"])
          if 'user' in post:
                  count += 1
                  print(green_color+"{}: {}".format(count, W+password.strip())+BRed+" | غير متوفر  ")
                  with open('accountfound.txt', 'a') as x:
                      x.write(password + '\n')
          else:
                  count += 1
                  print(green_color+"{}: {}".format(count, W+password.strip())+Green+" |  متوفر  ")
          print("________________")
          
          print("")
          
          
    exit()

if falah =="2":
    dd = input ('username : ')
    print (W + """│
└──=> { Extracting session id through Burp Suite Or from the Chrome browser } """)
    sessionId = input ("   "
                       "                       └──=> sessionid : ")

    url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + dd + "&app_language=ar"
    payload = ""
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"

        }
    cookies = {'sessionid': sessionId}
    response = requests.request ("GET", url, data=payload, headers=headers, cookies=cookies)
    post = str (response.json ()["recommended_unique_ids"])
    print ("")
    print (" -" * 15)
    print ("")
    print ('',post)

    exit()
if falah =="1"or " ":
    dd = input ('username list : ')
    print (W + """│
└──=> { Extracting session id through Burp Suite Or from the Chrome browser } """)
    sessionId = input("   "
                      "                       └──=> sessionid : ")
    if dd =="1"or " ":
        dd=""+dd+""
        password = open(dd).read().splitlines()

        # Back up one character, print a space to erase the spinner, then a newline
        # so that the prompt after the program exits isn't on the same line as our
        # message


        for password in password:
              url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+password+"&app_language=ar"
              payload = ""
              headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


        }
              cookies = {'sessionid': sessionId}
              response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
              post = str (response.json ()["status_msg"])
              if post==""or"":
                  count += 1
                  print(green_color+"{}: {}".format(count, W+password.strip())+Green+" |  متوفر  ")
                  with open('accountfound.txt', 'a') as x:
                      x.write(password + '\n')
              else:
                  count += 1
                  print(green_color+"{}: {}".format(count, W+password.strip())+BRed+" | غير متوفر  ")
exit()
