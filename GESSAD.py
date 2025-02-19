import random, threading, time, os, sys
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

try:
    import requests, uuid, colorama, cursor, json
    import bs4
    from colorama import Fore, Back, Style
except ImportError as e:
    input(f"Package {e} is not installed")
    sys.exit(f"Install {e}")

proxyDebug = False

class Checker:
    def __init__(self):
        colorama.init(convert=True, autoreset=True)
        cursor.hide()
        self.mag = colorama.Fore.MAGENTA
        self.grn = colorama.Fore.GREEN
        self.white = colorama.Fore.WHITE
        self.blue = colorama.Fore.CYAN
        self.sample = "abcdefghijklmnopqrstuvwxyz0123456789_"
        self.num = 4
        self.threads = 10 
        self.hits = 0
        self.fails = 0
        self.rates = 0
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=5, status_forcelist=[500, 502, 503, 504, 429])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""{self.mag}
     ██████╗ ███████╗███████╗███████╗ █████╗ ██████╗ 
    ██╔════╝ ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
    ██║  ███╗█████╗  ███████╗███████╗███████║██║  ██║
    ██║   ██║██╔══╝  ╚════██║╚════██║██╔══██║██║  ██║
    ╚██████╔╝███████╗███████║███████║██║  ██║██████╔╝
     ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ 
    {self.white}
    By © 2025 ~ 0xfff0800\n""",
            "\n\n",
        )

        self.check2()

    def check2(self):
        USER_AGENTS = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
        ]
        while True:
            try:
                username = "".join(random.choices(self.sample, k=self.num))
                proxy = random.choice(open("proxy.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
                if proxyDebug:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
                
                named_tuple = time.localtime() 
                self.time = time.strftime("%H:%M:%S", named_tuple)
                headers = {
                    "Host": "www.tiktok.com",
                    "user-agent": random.choice(USER_AGENTS),
                    "accept-encoding": "gzip, deflate, br"
                }
                response = self.session.get(
                    f"https://www.tiktok.com/@{username}", headers=headers, proxies=proxyDict, timeout=30, stream=True
                )

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser") 
                    if "statusCode\":10221" in response.text:
                        print(
                        f"    [ {self.grn}$ {self.white}]{self.grn} Username Available {self.blue}{username}{self.white} Hits ~ {self.hits} : Fails ~ {self.fails} : Rates ~ {self.rates} : Time ~ {self.time}"
                    )
                        print(username, file=open("available.txt", "a"))
                        self.hits += 1
                    else:
                        self.fails += 1
                        print(
                        f"    [ {self.grn}$ {self.white}]{Fore.RED} Not Available {self.blue}{username}{self.white} Hits ~ {self.hits} : Fails ~ {self.fails} : Rates ~ {self.rates} : Time ~ {self.time}"
                    )
                elif response.status_code == 404:
                    print(
                        f"    [ {self.grn}$ {self.white}]{self.grn} Available/Banned {self.blue}{username}{self.white} Hits ~ {self.hits} : Fails ~ {self.fails} : Rates ~ {self.rates} : Time ~ {self.time}"
                    )
                    print(username, file=open("available.txt", "a"))
                    self.hits += 1

                elif response.status_code == 429:
                    self.fails += 1
                    self.rates += 1
                    print(
                        f"    [ {self.grn}$ {self.white}]{Fore.RED} Connection blocked {self.white}429{self.white} Hits ~ {self.hits} : Fails ~ {self.fails} : Rates ~ {self.rates} : Time ~ {self.time}"
                    )
                    time.sleep(20)
                else:
                    self.fails += 1
            except requests.exceptions.ChunkedEncodingError:
                print(f"    {Fore.RED}ChunkedEncodingError: Try again 👍...{Fore.RESET}")
                self.fails += 1
                time.sleep(5) 
                continue
            except requests.exceptions.RequestException as e:
                print(f"    {Fore.RED}Request Error: {e}{Fore.RESET}")
                self.fails += 1
                time.sleep(5)
                continue
            except KeyboardInterrupt: 
                print(f"    [ {Fore.RED}$ {self.white}]{Fore.RED} Exit ...")
                exit()

if __name__ == "__main__":
    Checker()
