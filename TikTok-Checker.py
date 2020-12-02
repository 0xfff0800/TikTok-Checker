import requests
import json
import time
from colorama import Fore,init
green_color = "\033[1;93m"
C = "\033[0m"
W = "\033[96m"

print( green_color +'''


  _______ _ _ _______    _            _____ _               _             
 |__   __(_) |__   __|  | |          / ____| |             | |            
    | |   _| | _| | ___ | | ________| |    | |__   ___  ___| | _____ _ __ 
    | |  | | |/ / |/ _ \| |/ /______| |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |  | |   <| | (_) |   <       | |____| | | |  __/ (__|   <  __/ |   
    |_|  |_|_|\_\_|\___/|_|\_\       \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                          
                                                                          
           

==============================================
[developer] => FaLaH - 0xfff0800 [developer_email] => f***7@g****.com) 
[developer_snapchat] => flaah999
==============================================

''')

falah = input('''
1 - TikTok-Checker - username list
2 - TikTok-Checker - Suggestions
-> ''')
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
if falah =="1":
    dd = input ('username list : ')
print (W + """│
└──=> { Extracting session id through Burp Suite Or from the Chrome browser } """)
sessionId = input("   "
                  "                       └──=> sessionid : ")

password = open(dd).read().splitlines()
for password in password:
      url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+password+"&app_language=ar"
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
      response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
      post = str (response.json ()["status_msg"])
      print ("")
      print (" -" * 15)
      print ("")
      print ('https://www.tiktok.com/@' + password + '  ' + post )
