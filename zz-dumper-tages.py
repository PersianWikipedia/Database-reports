# -*- coding: utf-8 -*-
#
# MIT license
#http://dumps.wikimedia.your.org/fawiki/
#
#fawiki-20140802-pages-meta-current.xml.bz2
#http://dumps.wikimedia.your.org/fawiki/20150325/fawiki-20150325-pages-meta-current.xml.bz2
import wikipedia, xmlreader, codecs, re
import os
bot_adress="/data/project/rezabot/"
TheDay='20150325'

urllinkmain='http://dumps.wikimedia.your.org/fawiki/%s/fawiki-%s-pages-meta-current.xml.bz2' %(TheDay,TheDay)
print urllinkmain
#os.system('wget '+urllinkmain +" "+bot_adress+"fawiki-"+TheDay+"-pages-meta-current.xml.bz2")
dump = xmlreader.XmlDump(bot_adress+"fawiki-"+TheDay+"-pages-meta-current.xml.bz2")

pre,noinclude,includeonly,tags1,tags2=u'\n',u'\n',u'\n',u'\n',u'\n'
for entry in dump.new_parse():
    if entry.ns =='0':
        text=entry.text.replace(u' /',u'/').replace(u'/ ',u'/').replace(u'< ',u'<').replace(u' >',u'>')

        if u'<noinclude>' in text or u'</noinclude>' in text:
            noinclude+=u"#[[%s]]\n" % entry.title
        elif u'<includeonly>' in text or u'</includeonly>' in text:
            includeonly+=u"#[[%s]]\n" % entry.title
        elif u'<pre>' in text or u'</pre>' in text:
            pre+=u"#[[%s]]\n" % entry.title
        elif u'__NOGALLERY__' in text:
            tags1+=u"#[[%s]]\n" % entry.title
        elif u'__NOEDITSECTION__' in text:
            tags2+=u"#[[%s]]\n" % entry.title
        else:
            continue
        wikipedia.output(entry.title)
my_text=u'\n== pre ==\n'+pre+u'\n== noinclude ==\n'+noinclude+u'\n== includeonly ==\n'+includeonly+u'\n== NOGALLERY ==\n'+tags1+u'\n== NOEDITSECTION ==\n'+tags2
f=codecs.open(bot_adress+"zztages.txt","w","utf-8")
f.write(my_text)
f.close()
#os.system("rm "+bot_adress+"fawiki-%s-pages-meta-current.xml.bz2" %(TheDay))
site = wikipedia.getSite('fa')
page = wikipedia.Page(site,u"ویکی‌پدیا:گزارش دیتابیس/مقالاتی که تگ الگو دارند")
my_text=u'مقالات زیر ممکن است الگو درون آنها به اشتباه استفاده شده‌باشد \n'+my_text
page.put(my_text,u"ربات: به‌روز رسانی آمار دیگر ویکی‌ها")
