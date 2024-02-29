#!/data/data/com.termux/files/usr/bin/python

import json, requests ,uuid,random,base64
#ff
uid="61556637603800"
ps="Dighi21@@.."
user_agent="Dalvik/2.1.0 (Linux; U; Android 8.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/483.0.0.16.537;FBPN/com.facebook.orca;FBLC/en_US;FBBV/346852117;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/8.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920)"
            
adid = str(uuid.uuid4())
deviceid= str(uuid.uuid4())
fm_deviceid = str(uuid.uuid4())
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
"api_key": "882a8490361da98704bf97a021ddc14d"}
head = {
'User-Agent': user_agent,
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
'X-fb-connection-token': 'd29d67d38eca387482a8a5b740f84f62',}
url1= 'https://b-graph.facebook.com/auth/login'
po = requests.post(url=url1,data=data,headers=head,allow_redirects=False).json()
#coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])


print(po)
