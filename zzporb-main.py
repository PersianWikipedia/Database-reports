#!/usr/bin/python
# -*- coding: utf-8  -*-
#
# Reza(User:reza1615), 2011
#
# MIT license
import catlib ,pagegenerators
import wikipedia,urllib,gzip
import codecs,query,os
from collections import defaultdict
from datetime import timedelta,datetime
from StringIO import StringIO
internetoff=False #-----------------------------------bedoone internet------------------------
wikipedia.config.put_throttle = 0
wikipedia.put_throttle.setDelay()
text=u' '
dict={}
file_content=u' '
now = datetime.now()
yesterday=str(now-timedelta(1)).replace('-','').split(' ')[0].strip()
todayup=u"'''به‌روز شده توسط ربات در تاریخ''''': ~~~~~''\n\n"
titlechart=u'!رتبه!! صفحه!! میزان بازدید در یک روز!!برچسب‌ها!!میان‌ویکی!!تعداد پیوند به!! تعداد رده!!تعداد نگاره!!حجم صغحه (بایت){{سخ}}حجم کمتر از ۱۵ کیلوبایت رنگی نمایش داده میشود !!توضیحات دیگر'+u'\n|-\n'
uppage=todayup+u'\n{| class="wikitable sortable"\n'+titlechart
downpage=u'\n|}\n[[رده:ویکی‌پدیا]]\n[[رده:آمارهای دیتابیس]]\n'
count=0
lines=u' '
file=(u'000000',u'000001',u'000002', u'010000',u'010001',u'010002',u'020000',u'020001',u'020002',u'030000',u'030001',u'030002',u'040000',u'040001',u'040002',u'050000',u'050001',u'050002',u'060000',u'060001',u'060002',u'070000',u'070001',u'070002',u'080000',u'080001',u'080002',
      u'090000',u'090001',u'090002',u'100000',u'100001',u'100002',u'110000',u'110001',u'110002',u'120000',u'120001',u'120002',u'130000',u'130001',u'130002',u'140000',u'140001',u'140002',u'150000',u'150001',u'150002',u'160000',u'160001',u'160002',u'170000',u'170001',u'170002',u'180000',u'180001',u'180002',u'190000',u'190001',u'190002',u'200000',u'200001',u'200002',
      u'210000',u'210001',u'210002',u'220000',u'220001',u'220002',u'230000',u'230001',u'230002')

def condition(text):
      wikipedia.config.put_throttle = 0
      wikipedia.put_throttle.setDelay()
      if internetoff==True:
          return u'||\n|-\n'
      alarm=' '
      try:
         page = wikipedia.Page( wikipedia.getSite( u'fa' ),text )
         wikipedia.output( u'opening %s ...' % page.title() )
         #if page.botMayEdit!=False:
             #alarm=u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'||'+u'ربات اجازه ورود ندارد!\n|-\n'
             #return alarm
         text = page.get()
         alarm+=u' '
         objective=u'||'
        #----------------------------------------------refrences-------------------
         if text.find(u'{{منبع')!=-1:
             alarm+=u'نیازمند منبع ،'
         if text.find(u'{{بهبود')!=-1:
              alarm+=u'بهبود منبع ،'
         if text.find(u'{{بدون منبع')!=-1:
              alarm+=u'بدون منبع ،'
         if text.find(u'{{متخصص')!=-1:
             alarm+=u'متخصص ،'
         if text.find(u'{{نوشتار خوب}}')!=-1:
             alarm+=u'{{قلم رنگ|سورمه‌ای|فیلی|مقاله خوب}}'
         if text.find(u'{{پیشنهاد برگزیدگی}}')!=-1:
             alarm+=u'{{قلم رنگ|بنفش|زرد|پیشنهاد برگزیدگی}}'
         if text.find(u'{{پیشنهاد خوبیدگی}}')!=-1:
             alarm+=u'{{قلم رنگ|سبز|زرد|پیشنهاد خوبیدگی}}'
         if text.find(u'{{مقاله برگزیده}}')!=-1:
             alarm+=u'{{قلم رنگ|سفید|خاکستری|مقاله برگزیده}}'
        #----------------------------------------------khord----------------------
         if text.find(u'خرد}}')!=-1:
           if text.find(u'{{بخش-خرد')!=-1:
               alarm+=u'{{قلم رنگ|بنفش||بخش خرد}} ،'
           else:
		       alarm+=u'خرد ،'
         if text.find(u'نیاز}}')!=-1:
           alarm+=u'نیازمند به ،'
         if text.find(u'{{طرفداری')!=-1:
             alarm+=u'عدم‌بی‌طرفی ،'
         if text.find(u'{{درستی')!=-1:
             alarm+=u'عدم توافق در درستی ،'
         if text.find(u'{{ادغام')!=-1:
             alarm+=u'ادغام ،'
         if text.find(u'{{در دست ویرایش')!=-1:
             alarm+=u'ویرایش ،'
         if text.find(u'{{ویکی‌سازی')!=-1:
             alarm+=u'ویکی‌سازی ،'
         if text.find(u'{{تمیزکاری')!=-1:
             alarm+=u'تمیزکاری ،'
         if text.find(u'{{لحن')!=-1:
             alarm+=u'لحن ،'
         if text.find(u'{{اصلاح')!=-1:
             alarm+=u'نیازمند ترجمه ،'
         if text.find(u'{{ابهام‌زدایی')!=-1:
             alarm+=u'ابهام‌زدایی ،'
         if text.find(u'{{بازنویسی')!=-1:
             alarm+=u'بازنویسی ،'
         if text.find(u'{{به روز رسانی')!=-1:
             alarm+=u'به‌روز رسانی ،'
         if text.find(u'{{به‌روز رسانی')!=-1:
             alarm+=u'به‌روز رسانی ،'


        #--------------------------------------------------------------------------


         if alarm[-1]==u'،':
             alarm=alarm[0:-1].strip()
         interwikis=u'{{subst:formatnum:'+str(len(page.interwiki()) ).strip()+u'}}'
         cats=u'{{subst:formatnum:'+str(len(page.categories(api=True))).strip()+u'}}'
         linked=u'{{subst:formatnum:'+str(len(page.linkedPages())).strip()+u'}}'
         image=u'{{subst:formatnum:'+str(len(page.imagelinks())).strip()+u'}}'
         alarm+=u'||'+interwikis+u'||'+linked+u'||'+cats+u'||'+image+u'||{{حجم مقاله|'+page.title().strip()+u'|15000}}||\n|-\n'
         return alarm
      except wikipedia.IsRedirectPage:
          #page = page.getRedirectTarget()
          #title=str(page.title()).split('#')[0]
          #alarm=u'||'+u'||'+u'||'+u'||'+u'||'+u'||تغییر مسیر به [['+title+u']]\n|-\n '
          #return alarm
          return False
      except:
          #alarm=u'||'+u'||'+u'||'+u'||'+u'||'+u'||این صفحه موجود نیست!\n|-\n'
          return False



for adress in file:
    del file_content
    file_content=' '
    #'''#----------------------------------------------------computer file---------------------
    try:
        #urllinkmain='C:\Users\Reza\Downloads\data\pagecounts-'
        #yesterday=u'20110915'
        #ulinks=urllinkmain+yesterday+'-'+adress+'.gz'
        #print ulinks+'======================================='
        #yesterday=u'20110915'
        openfile = open('/data/project/rezabot/pagecounts-%s-%s.txt' %(yesterday,adress), 'r')
        file_content=openfile.read()
        #f = gzip.open(ulinks, 'rb')
        #file_content = f.read()
        openfile.close()
        del openfile

    except:
        continue
    lines=' '
    line=' '
    del lines
    del line
    lines=file_content.split('\n')
    count=0
    del count
    count=0
    try:
        for line in lines:
                if 'fa ' in line[0:3]:
                    if '.css' in  line:
                        continue
                    line=line.replace('.','%')
                    line=line.replace('25','')
                    count+=1
                    urltext=line[3:]
                    #for a in range(0,10):
                    try:
                        urltext=urllib.unquote_plus(urltext).decode('utf8').strip()
                        urltext=urltext.replace('%','.')
                        if urltext.find(u':')!=-1 or urltext.find(u'=')!=-1 or urltext.find(u'.jpg')!=-1 or urltext.find(u'.gif')!=-1 or urltext.find(u'.js')!=-1 or urltext.find(u'.ogg')!=-1:
                            continue
                        if urltext.find(u'۱')!=-1 or urltext.find(u'۲')!=-1 or urltext.find(u'۳')!=-1  or urltext.find(u'۴')!=-1 or  urltext.find(u'۵')!=-1  or urltext.find(u'۶')!=-1  or urltext.find(u'۷')!=-1  or urltext.find(u'۸')!=-1  or urltext.find(u'۹')!=-1  or urltext.find(u'۰')!=-1 :
                            continue
                        if urltext.split(' ')[0] in dict:
                            dict[urltext.split(' ')[0]]=int(dict[urltext.split(' ')[0]])+int(urltext.split(' ')[1])
                        else:
                            dict[urltext.split(' ')[0]]=int(urltext.split(' ')[1])
                            del urltext

                    except:
                        print count
                        continue

    except Exception as inst:
        print inst
        a=1

del count
count=0
inverse= defaultdict( list )
for k, v in dict.items():
    inverse[int(v)].append( k )
del dict
del lines
del adress
del file_content
for k in sorted(inverse, reverse=True):
    if count>5000:
                break
    for i in range(0,len(inverse[k])):
            count+=1
            if count>1500:
                break
            if condition(inverse[k][i].replace('_',' '))==False:
                count-=1
                continue
            text+=u'|{{subst:formatnum:'+str(count)+u'}}||[['+inverse[k][i].replace('_',' ').strip()+u']]||{{subst:formatnum:'+str(k)+u'}}||'+condition(inverse[k][i].replace('_',' '))
            if count==500 or count==1000 or count==1500:
               text=uppage+text.strip()+downpage
               #---------------------------------------------------------wiki upload----------------------
               countf=str(count).replace(u'0',u'۰').replace(u'1',u'۱').replace(u'2',u'۲').replace(u'3',u'۳').replace(u'4',u'۴').replace(u'5',u'۵').replace(u'6',u'۶').replace(u'7',u'۷').replace(u'8',u'۸').replace(u'9',u'۹')
               countl=str(count-499).replace(u'0',u'۰').replace(u'1',u'۱').replace(u'2',u'۲').replace(u'3',u'۳').replace(u'4',u'۴').replace(u'5',u'۵').replace(u'6',u'۶').replace(u'7',u'۷').replace(u'8',u'۸').replace(u'9',u'۹')
               uptitle=u'ویکی‌پدیا:گزارش دیتابیس/فهرست مقاله‌های پربیننده از %s تا %s/فهرست' %(countl,countf)
               page = wikipedia.Page( wikipedia.getSite( u'fa' ),uptitle)
               page.put(text, u'ربات:به‌روز رسانی', minorEdit = True)
               '''#---------------------------------------------------------computer save--------------------
               with codecs.open( 'page'+str(count)+'.txt',mode = 'w',encoding = 'utf8' ) as f:
                                f.write( text )
               #'''#----------------------------------------------------------------------------------------------
               del text
               text=u' '
sign_page=u'ویکی‌پدیا:گزارش دیتابیس/فهرست مقاله‌های پربیننده/امضا'
madak=u'~~~~~'
site=wikipedia.getSite('fa')
sign_page=wikipedia.Page(site,sign_page)
sign_page.put(madak,u'ربات:تاریخ بروز رسانی')

os.system("rm pagecounts*")
