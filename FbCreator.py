import sys

import certifi

print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
❖ › Github :- @jatintiwari0 
❖ › By      :- JATIN TIWARI
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛                """)
print('\x1b[38;5;208m⇼' * 60)
print('\x1b[38;5;22m•' * 60)
print('\x1b[38;5;22m•' * 60)
print('\x1b[38;5;208m⇼' * 60)
import requests
import random
import string
import json
import hashlib
from faker import Faker

ua = []

try:
    url = "https://github.com/Shadid21/Fuck-Clone/blob/main/database"
    response = requests.get(url, verify=certifi.where())
    datax = response.text.splitlines()[0]
    for u in datax.split("|"):
        ua.append(u)
except Exception as e:
    print("[!!] Internet Error:", e)
    sys.exit()


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


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


def get_mail_domains():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error : {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error : {e}')
        return None


def create_mail_tm_account():
    fake = Faker()
    mail_domains = get_mail_domains()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password": password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'')
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email Error : {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error : {e}')
            return None, None, None, None, None


def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key, 'attempt_login': True, 'birthday': birthday.strftime('%Y-%m-%d'),
           'client_country_code': 'EN',
           'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
           'fb_api_req_friendly_name': 'registerAccount', 'firstname': first_name, 'format': 'json', 'gender': gender,
           'lastname': last_name, 'email': email, 'locale': 'en_US', 'method': 'user.register', 'password': password,
           'reg_instance': generate_random_string(32), 'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req)
    print(reg)
    id = reg['new_user_id']
    token = reg['session_info']['access_token']
    print(f'''
\x1b[38;5;22m⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ EMAIL : {email}
﴾𝐕𝐈𝐏﴿ ID : {id}
﴾𝐕𝐈𝐏﴿ PASSWORD : {password}
﴾𝐕𝐈𝐏﴿ NAME : {first_name} {last_name}
﴾𝐕𝐈𝐏﴿ BIRTHDAY : {birthday} 
﴾𝐕𝐈𝐏﴿GENDER : {gender}
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ Token : {token}
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙''')


open('username.txt', 'a')

ua = []
try:
    url = "https://raw.githubusercontent.com/Shadid21/Fuck-Clone/main/database"
    response = requests.get(url, verify=certifi.where())
    datax = response.text.splitlines()[0]
    for u in datax.split("|"):
        ua.append(u)
except Exception as e:
    print("[!!] Internet Error:", e)
    sys.exit()

def _call(url, params, post=True):



    meth = input("Which Method -> 1, 2, 3, 4, 5, 6, 7 ?")
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
    headers = {'User-Agent': useragent}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()


for i in range(int(input('[+] How Many Accounts You Want:  '))):
    email, password, first_name, last_name, birthday = create_mail_tm_account()
    if email and password and first_name and last_name and birthday:
        register_facebook_account(email, password, first_name, last_name, birthday)
print('\x1b[38;5;208m⇼' * 60)
