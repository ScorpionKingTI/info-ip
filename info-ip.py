import requests, os, time
def gt():
   print('\n\033[34;01mdeseja fazer uma nova consulta?\n1. sim\n2. sair\n\033[0;0m\n')
   df=input('>')
   if df == '1':
    ipss()
   elif df == '2':
    print('\n\033[32;1mobrigado por usar os serviços do scorpion king\033[0;0m\n')
    exit()
   elif df != 1 and 2:
    print('\n\033[33;1mseleção invalida digite 1 ou 2\n')
    gt()
def ipss():
 print('\033[32;1m')
 print('\033[32;1m     ██╗███╗  ██╗███████╗ █████╗ ')
 time.sleep(0.1)      
 print('\033[32;1m     ██║████╗ ██║██╔════╝██╔══██╗')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██╔██╗██║█████╗  ██║  ██║')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██║╚████║██╔══╝  ██║  ██║')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██║ ╚███║██║     ╚█████╔╝')
 time.sleep(0.1)      
 print('\033[32;1m     ╚═╝╚═╝  ╚══╝╚═╝      ╚════╝')
 time.sleep(0.1) 
 print('')
 time.sleep(0.1)      
 print('\033[32;1m             ██╗██████╗')
 time.sleep(0.1)      
 print('\033[32;1m             ██║██╔══██╗')
 time.sleep(0.1)      
 print('\033[32;1m             ██║██████╔╝')
 time.sleep(0.1)      
 print('\033[32;1m             ██║██╔═══╝')
 time.sleep(0.1)      
 print('\033[32;1m             ██║██║')
 time.sleep(0.1)      
 print('\033[32;1m             ╚═╝╚═╝')
 time.sleep(0.1)      
 print('')
 print('''\033[34;1m
 ____________________________________________
 |
 |---------- 1. consultar um ip
 |---------- 2. ajuda
 |---------- 3. sair 
 |___________________________________________
 ''')
 s=input('\nDigite a opção que deseja\n          >')
 if s == '1':
  print("\n\033[34;1mDigite o endereço ip, ex :170.245.225.107...se caso o campo da digitação estiver vazio e for dado enter você verá informação sobre seu ip atual: \033[0;0m\n")
  ipg=input('>')
  api = requests.get("https://ipapi.co/{}/json".format(ipg))
  resultado = api.json()
  zs=requests.get('http://ip-api.com/json/{}'.format(ipg))
  k=zs.json()
  lks=k['query']
  if 'message' not in k:
   print('\n\033[32;1m==>IP ENCONTRADO<==\033[0;0m')
   print('\n\033[34;1m◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n◆-')
   print('\033[34;1m◆-Ip: \033[0;0m\033[37;1m{}'.format(lks))
   print('\033[34;1m◆-Pais: \033[0;0m\033[37;1m{}'.format(k['country']))
   print('\033[34;1m◆-Codigo do pais: \033[37;1m{}'.format(k['countryCode']))
   print('\033[34;1m◆-Regiao: \033[37;1m{}'.format(k['region']))
   print('\033[34;1m◆-Estado: \033[37;1m{}'.format(k['regionName']))
   print('\033[34;1m◆-Cidade: \033[37;1m{}'.format(k['city']))
   print('\033[34;1m◆-Cep: \033[37;1m{}'.format(k['zip']))
   print('\033[34;1m◆-Latitude: \033[37;1m{}'.format(k['lat']))
   print('\033[34;1m◆-Longitude: \033[37;1m{}'.format(k['lon']))
   print('\033[34;1m◆-Fuso horario: \033[37;1m{}'.format(k['timezone']))
   print('\033[34;1m◆-Isp: \033[37;1m{}'.format(k['isp']))
   print('\033[34;1m◆-Servidora: \033[37;1m{}'.format(k['org']))
   print('\033[34;1m◆-As: \033[37;1m{}'.format(k['as']))
   print('\033[34;1m◆-Abreviação do país: \033[37;1m{}'.format(resultado['country_code']))
   print('\033[34;1m◆-Capital do país: \033[37;1m{}'.format(resultado['country_capital']))
   print('\033[34;1m◆-População do país: \033[37;1m{}'.format(resultado['country_population']))
   print('\033[34;1m◆-Moeda: \033[37;1m{}'.format(resultado['currency']))
   print('\033[34;1m◆-Nome da moeda: \033[37;1m{}'.format(resultado['currency_name']))
   print('\033[34;1m◆-Código da região: \033[37;1m{}'.format(resultado['region_code']))
   print('\033[34;1m◆-Código do país: \033[37;1m{}'.format(resultado['country_code']))
   print('\033[34;1m◆-Código do país ISO3: \033[37;1m{}'.format(resultado['country_code_iso3']))
   print('\033[34;1m◆-Área do país: \033[37;1m{}'.format(resultado['country_area']))
   print('\033[34;1m◆-País TLD: \033[37;1m{}'.format(resultado['country_tld']))
   print('\033[34;1m◆-Código área: \033[37;1m{}'.format(resultado['country_area']))
   print('\033[34;1m◆-Código do continente: \033[37;1m{}'.format(resultado['continent_code']))
   print('\033[34;1m◆-União Européia: \033[37;1m{}'.format(resultado['in_eu']))
   print('\033[34;1m◆-Código de Chamada: \033[37;1m{}'.format(resultado['country_calling_code']))
   print('\033[34;1m◆-línguas: \033[37;1m{}'.format(resultado['languages']))
   print('\033[34;1m◆-ASN: \033[37;1m{}'.format(resultado['asn']))
   print('\033[34;1m◆-Deslocamento UTF: \033[37;1m{}'.format(resultado['utc_offset']))
   print('\033[34;1m◆-Versão: \033[37;1m{}'.format(resultado['version']))
   print('\033[34;1m◆-\n◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆')
   gt()
  else:
   print('\n\033[33;1mIP não existe\033[0;0m\n')
   gt()
 if s =='2':
  print('\n\033[32;1mEssa script retorna informação a partir de um determinado ip...caso queira ver status de seu proprio ip basta dar enter sem digitar nada\n')
  gt()
 if s =='3':
  print('\n\033[32;1mObrigado por ultilizar os serviços do scorpion king\n')
  exit()
 if s != 1 and 2 and 3 and '':
  print('\033[33;1mSeleção invalida\033[0;0m')
  time.sleep(3)
  ipss()
os.system('clear')
print("\033[34;1m                    coded by:")
time.sleep(0.1)      
print("")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)       
print("       ┃      ✪   SCORPION KING   ✪    ┃")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡")  
print('')
time.sleep(5) 
os.system('clear')
ipss()
