# -*- coding: utf-8 -*-
import codecs
import re

import xmlreader
dump = xmlreader.XmlDump("fawiki-20150325-pages-articles.xml.bz2")
a = 0
f = codecs.open("markup.txt", "w", "utf-8")
f.write("")
f.close()
rer = re.compile(ur'(<table|<pre>\s*?</pre>|<noinclude>\s*?</noinclude>|'
                 '<includeonly>\s*?</includeonly>|__NOGALLERY__|'
                 '__NOEDITSECTION__|__TOC__|__NOTOC__)')
for entry in dump.new_parse():
        if entry.ns in ['0', '14', '6', '4']:
            if rer.search(entry.text):
                a += 1
                print "found one: %d" % a
                f = codecs.open("markup.txt", "a", "utf-8")
                f.write(u"[[%s]]\n" % entry.title)
                f.close()
