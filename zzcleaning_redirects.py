#!/usr/bin/python
# -*- coding: utf-8  -*-
# Distributed under the terms of the CC-BY-SA 3.0 .
# Reza (User:Reza1615) Code structure + Developing the code
import re,codecs,os,wikipedia,query
bot_address=u'/home/reza/compat/'
faSite = wikipedia.getSite('fa')
#----------------
SimilarPersianCharacters=ur'\u0643\uFB91\uFB90\uFB8F\uFB8E\uFEDC\uFEDB\uFEDA\uFED9\u0649\uFEEF\u064A\u06C1\u06D5\u06BE\uFEF0-\uFEF4'
vowels = ur'\u064B-\u0650\u0652\u0654-\u0670'
persianCharacters = ur'\u0621-\u0655\u067E\u0686\u0698\u06AF\u06A9\u0643\u06AA\uFED9\uFEDA\u06CC\uFEF1\uFEF2'+SimilarPersianCharacters

#----------------
persianGlyphs = {
        # these two are for visually available ZWNJ #visualZwnj
        u'‌ه': u'ﻫ',u'ی‌': u'ﻰﻲ',
        u'ﺃ': u'ﺄﺃ',u'ﺁ': u'ﺁﺂ',u'ﺇ': u'ﺇﺈ',u'ا': u'ﺎا',
        u'ب': u'ﺏﺐﺑﺒ',u'پ': u'ﭖﭗﭘﭙ',u'ت': u'ﺕﺖﺗﺘ',u'ث': u'ﺙﺚﺛﺜ',
        u'ج': u'ﺝﺞﺟﺠ',u'چ': u'ﭺﭻﭼﭽ',u'ح': u'ﺡﺢﺣﺤ',u'خ': u'ﺥﺦﺧﺨ',
        u'د': u'ﺩﺪ',u'ذ': u'ﺫﺬ',u'ر': u'ﺭﺮ',u'ز': u'ﺯﺰ',
        u'ژ': u'ﮊﮋ',u'س': u'ﺱﺲﺳﺴ',u'ش': u'ﺵﺶﺷﺸ',u'ص': u'ﺹﺺﺻﺼ',
        u'ض': u'ﺽﺾﺿﻀ',u'ط': u'ﻁﻂﻃﻄ',u'ظ': u'ﻅﻆﻇﻈ',u'ع': u'ﻉﻊﻋﻌ',
        u'غ': u'ﻍﻎﻏﻐ',u'ف': u'ﻑﻒﻓﻔ',u'ق': u'ﻕﻖﻗﻘ',u'ک': u'ﮎﮏﮐﮑﻙﻚﻛﻜ',
        u'گ': u'ﮒﮓﮔﮕ',u'ل': u'ﻝﻞﻟﻠ',u'م': u'ﻡﻢﻣﻤ',u'ن': u'ﻥﻦﻧﻨ',
        u'ه': u'ﻩﻪﻫﻬ',u'هٔ': u'ﮤﮥ',u'و': u'ﻭﻮ',u'ﺅ': u'ﺅﺆ',
        u'ی': u'ﯼﯽﯾﯿﻯﻰﻱﻲﻳﻴ',u'ئ': u'ﺉﺊﺋﺌ',u'لا': u'ﻼ',u'ﻹ': u'ﻺ',
        u'ﻷ': u'ﻸ',u'ﻵ': u'ﻶ'
        }
#-----------------
def Check_Page_Exists(page_link):
    page_link=page_link.replace(u' ',u'_')

    params = {
        'action': 'query',
        'prop':'info',
        'titles': page_link
    }
    query_page = query.GetData(params,faSite)
    try:
        for i in query_page[u'query'][u'pages']:    
            redirect_link=query_page[u'query'][u'pages'][i]['pageid']  
            return False# page existed
    except:
        return True# page not existed

def getlinks(BadLink,correctLink):
        site = wikipedia.getSite('fa')
        try:
            page = wikipedia.Page(site,BadLink)
            linktos=page.getReferences()
        except:
            return True
        for page in linktos:
                try:
                    text=page.get()
                except:
                    continue
                wikipedia.output(u'checking '+page.title()+u' .....')    
                text2=text
                if text.find(BadLink)!=-1:  
                        text2=text2.replace(u'[['+BadLink+u']]',u'[['+correctLink+u']]').replace(u'[['+BadLink+u'|',u'[['+correctLink+u'|').replace(u'\r',u'')
                        text2=text2.replace(u'[[ '+BadLink+u']]',u'[['+correctLink+u']]').replace(u'[[ '+BadLink+u'|',u'[['+correctLink+u'|')
                        text2=text2.replace(u'[[ '+BadLink+u' ]]',u'[['+correctLink+u']]').replace(u'[[ '+BadLink+u' |',u'[['+correctLink+u'|')
                        text2=text2.replace(u'[['+BadLink+u' ]]',u'[['+correctLink+u']]').replace(u'[['+BadLink+u' |',u'[['+correctLink+u'|')
                        text2=text2.replace(u'[[  '+BadLink+u' ]]',u'[['+correctLink+u']]').replace(u'[[  '+BadLink+u' |',u'[['+correctLink+u'|')
                        #-------------------------------------------for cats-----------------------------------
                        text2=text2.replace(u'[[:'+BadLink+u']]',u'[[:'+correctLink+u']]').replace(u'[[:'+BadLink+u'|',u'[[:'+correctLink+u'|')
                        text2=text2.replace(u'[[: '+BadLink+u']]',u'[[:'+correctLink+u']]').replace(u'[[: '+BadLink+u'|',u'[[:'+correctLink+u'|')
                        text2=text2.replace(u'[[: '+BadLink+u' ]]',u'[[:'+correctLink+u']]').replace(u'[[: '+BadLink+u' |',u'[[:'+correctLink+u'|')
                        text2=text2.replace(u'[[:'+BadLink+u' ]]',u'[[:'+correctLink+u']]').replace(u'[[:'+BadLink+u' |',u'[[:'+correctLink+u'|')
                        text2=text2.replace(u'[[ :'+BadLink+u' ]]',u'[[:'+correctLink+u']]').replace(u'[[ :'+BadLink+u' |',u'[[:'+correctLink+u'|')
                        text2=text2.replace(u'[[ : '+BadLink+u' ]]',u'[[:'+correctLink+u']]').replace(u'[[ : '+BadLink+u' |',u'[[:'+correctLink+u'|')
       
                        if text2.find(correctLink)==-1:
                            wikipedia.output(u'\03{lightblue}could not find any link\03{default}')
                        if text!=text2:
                            try:
                                page.put(text2,u'ربات:اصلاح پیوند به تغییرمسیر نامحتمل (دارای کارکترهای نادرست)')
                                wikipedia.output(u'\03{lightgreen}the page '+page.title()+u' had replcae item [['+BadLink+u']] > [['+correctLink+u']]\03{default}')
                            except:
                                wikipedia.output(u'\03{lightred}the page '+page.title()+u' could not replaced so it passed\03{default}')
                                continue
                else:
                     wikipedia.output(u'\03{lightred}could not find andy link\03{default}')        
        return True

def NoneFarsi_to_Farsi(txt):
    old_txt=txt

    # Function for removing incorrect ZWNJs
    txt =re.sub(ur"([\u200c\u200e])([\s\n])", ur'\2',txt)
    txt =re.sub(ur"([\s\n])([\u200c\u200e])", ur'\1',txt)
    #واکه‌های کوتاه پشت سرهم نمی‌آیند و یک حرف باید بینشان فاصله باشد
    txt = re.sub(ur'([' + vowels + ur']){2,}', ur"\1",txt)

    #تبدیل نویسه‌های منقطع به نویسه‌های استاندارد
    for i in persianGlyphs:
        txt =re.sub(ur'[' + persianGlyphs[i] + ur']', i,txt)

    return txt

def ZWNJ_cleaning(text):
    old_text=text
    #تمیزکاری فاصلهٔ مجازی
    text = re.sub(u'(\u202A|\u202B|\u202C|\u202D|\u202E|\u200F)',u'\u200C', text)#حذف کارکترهای تغییرجهت
    text = re.sub(ur'‌{2,}', ur'‌', text) # پشت‌سرهم
    text = re.sub(ur'‌(?!['+persianCharacters+u']|[\u0900-\u097F]|ֹ)', ur'', text) # در پس DEVANAGARI
    text = re.sub(ur'(?<![['+persianCharacters+u']|[\u0900-\u097F]|f|ֹ)‌', ur'', text) # در پیش DEVANAGARI
    # Clean ZWNJs after characters that don't conncet to the next letter
    text = re.sub(ur'([۰-۹0-9إأةؤورزژاآدذ،؛,\:«»\\\/@#$٪×\*\(\)ـ\-=\|])\u200c', ur"\1", text)
    # Clean ZWNJs before and after English characters
    text = re.sub(ur'\u200c([\w])', u"\1", text)
    text = re.sub(ur'([\w])\u200c', u"\1", text)
    # Clean ZWNJs after and before punctuation
    text = re.sub(ur'\u200c([\n\s\[\]\.،«»\:\(\)\؛\؟\?\;\$\!\@\-\=\+\\\|])', ur"\1", text)
    text = re.sub(ur'([\n\s\[\.،«»\:\(\)\؛\؟\?\;\$\!\@\-\=\+\\\|])\u200c', ur"\1", text)
    # Clean ZWNJs before brakets which have sapce after\before them
    text = re.sub(ur'\u200c(\]\][\s\n])', ur"\1", text)
    text = re.sub(ur'([\n\s]\[\[)\u200c', ur"\1", text)
    return text

def main():
    os.system(u'sql fawiki_p "SELECT page_title FROM page WHERE page_namespace = 0 AND page_is_redirect = 1;" >'+bot_address+u'fa_redirect_list.txt')
    print 'Qury is got!'

    text = codecs.open(bot_address+u"fa_redirect_list.txt",'r' ,'utf8' )
    text = text.read()
    text=text.replace(u'\r',u'').replace(u'_',u' ')
    list1,list2=u'\n',u'\n'
    for line in text.split(u'\n'):
        line=u' '+line+u' '
        old_line=line
        line=NoneFarsi_to_Farsi(line)
        line=ZWNJ_cleaning(line)
        if line!=old_line and len(old_line[1:-1])>1:
            if Check_Page_Exists(line[1:-1]):
                list1+=u'\n* [['+old_line[1:-1]+u']]'
            else:
                list2+=u'\n* [['+old_line[1:-1]+u']]> [['+line[1:-1]+u']]'
            wikipedia.output(u'Orginal='+old_line+u'|'+line+u'|')
            wikipedia.output(u'Second='+old_line[1:-1]+u'|'+line[1:-1]+u'|')
            result= getlinks(old_line[1:-1],line[1:-1])
    fapage=wikipedia.Page(faSite,u'ویکی‌پدیا:گزارش دیتابیس/تغییرمسیرهای دارای نویسنه نادرست')
    fapage.put(u'== برای حذف ==\nموارد زیر در مقالات و صفحات با موارد درست جایگزین شدهاند و فقط باید آنها را حذف کرد.\n'+list1+u'\n== برای انتقال ==\nموارد زیر بعد از انتقال ستون اول را میتوان حذف کرد\n'+list2,u'ربات:به‌روزرسانی گزارش')
main()