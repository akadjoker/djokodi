import urllib, urllib2, re, sys, xbmcplugin, xbmcgui
import os
import sys
import urllib
import urllib2
import cookielib
from xbmc import LOGDEBUG, LOGERROR, LOGFATAL, LOGINFO, LOGNONE, LOGNOTICE, LOGSEVERE, LOGWARNING  # @UnusedImport
import re
import requests
import cookielib
import os.path
import sys
import time
import subprocess
import urlresolver
Request = urllib2.Request
urlopen = urllib2.urlopen



import os           # access operating system commands
import urlparse     # splits up the directory path - much easier importing this than coding it up ourselves
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)


addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
dialog       = xbmcgui.Dialog()                     # A basic dialog message command
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path
addon_folder = os.path.join(home_folder,'addons')   # Join our folder above with 'addons' so we have a link to our addons folder

IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'


def log(msg, level=LOGDEBUG):
    xbmc.log('[%s] %s' % (addonname, msg), level)

def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', FF_USER_AGENT)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

    
def addDownLink(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + \
        str(mode) + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png",
                           thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=False)
    return ok

def addDir(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + \
        str(mode) + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png",
                           thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=True)
    return ok

def addMenuitem(url, li, folder):
 return xbmcplugin.addDirectoryItem(addon_handle, url=url, listitem=li, isFolder=folder)
def endMenu():
 xbmcplugin.endOfDirectory(addon_handle)



def CATEGORIES():

    addDir("Geral","http://fullxxxmovies.net/",1,"")
    addDir("2018","http://fullxxxmovies.net/tag/2018/",1,"")
    addDir("2017","http://fullxxxmovies.net/tag/2017/",1,"")
    addDir("2016","http://fullxxxmovies.net/tag/2016/",1,"")
    addDir("Anal","http://fullxxxmovies.net/tag/anal/",1,"")
    addDir("Amateur","http://fullxxxmovies.net/tag/amateur/",1,"")
    addDir("Lingerie","http://fullxxxmovies.net/tag/lingerie/",1,"")
    addDir("Hardcore","http://fullxxxmovies.net/tag/hardcore/",1,"")
    addDir("Pornstar","http://fullxxxmovies.net/tag/pornstar/",1,"")
    addDir("Interracial","http://fullxxxmovies.net/tag/interracial/",1,"")
    addDir("Big Asses","http://fullxxxmovies.net/tag/big-asses/",1,"")
    addDir("DvdRip","http://fullxxxmovies.net/tag/dvdrip/",1,"")
    addDir("HD","http://fullxxxmovies.net/tag/hd/",1,"")
    addDir("Clips","http://fullxxxmovies.net/tag/clips/",1,"")
    addDir("English","http://fullxxxmovies.net/tag/english/",1,"")
    addDir("Europen","http://fullxxxmovies.net/tag/european/",1,"")
    addDir("Brazil","http://fullxxxmovies.net/tag/brazil/",1,"")
    addDir("German","http://fullxxxmovies.net/tag/german/",1,"")
    addDir("Public","http://fullxxxmovies.net/tag/public/",1,"")
    addDir("Milf","http://fullxxxmovies.net/tag/milf/",1,"")
    addDir("Moms","http://fullxxxmovies.net/tag/mom/",1,"")
    addDir("Teens","http://fullxxxmovies.net/tag/teens/",1,"")
    addDir("Teenies","http://fullxxxmovies.net/tag/teenies/",1,"")
    
    addDir("Brasileirinhas","http://fullxxxmovies.net/tag/brasileirinhas/",1,"")
    addDir("Blow","http://fullxxxmovies.net/tag/blow/",1,"")
    addDir("Gonzo","http://fullxxxmovies.net/tag/gonzo/",1,"")
    addDir("Blowjob","http://fullxxxmovies.net/tag/blowjob/",1,"")
    addDir("Jav","http://fullxxxmovies.net/tag/jav/",1,"")
    addDir("Pov","http://fullxxxmovies.net/tag/pov/",1,"")
    addDir("Fetish","http://fullxxxmovies.net/tag/fetish/",1,"")
    addDir("Double Penetration","http://fullxxxmovies.net/tag/double-penetration/",1,"")

    
    addDir("Lesbian","http://fullxxxmovies.net/tag/lesbian/",1,"")
    addDir("Older","http://fullxxxmovies.net/tag/older/",1,"")
    addDir("Mature","http://fullxxxmovies.net/tag/mature/",1,"")
    
    
    
    addDir("Claudie","http://fullxxxmovies.net/tag/claudie/",1,"")
    addDir("Big Dick","http://fullxxxmovies.net/tag/big-dick/",1,"")
    addDir("Big Tits","http://fullxxxmovies.net/tag/big-tits/",1,"")
    addDir("Evil Angel","http://fullxxxmovies.net/tag/evil-angel/",1,"")
    addDir("Devils Angel","http://fullxxxmovies.net/tag/devils-angel/",1,"")
    addDir("ATV","http://fullxxxmovies.net/tag/atv-entertainment-producitons/",1,"")
    
    addDir("Openload Porn","http://fullxxxmovies.net/tag/openload-porn-movies/",1,"")
    

def notify(header=None, msg='', duration=5000):
    if header is None: header = 'DjokerSoft'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, uwcicon)
    xbmc.executebuiltin(builtin)
    
def VIDEOLINKS(url, name):
    content = getUrl(url)
    match2 = re.compile('<link rel="next" href="(.*?)" /><meta property="og:locale"', re.DOTALL ).findall(content)     
    
    match = re.compile('class="entry-title"><a href="(.*?)".*?"bookmark">(.*?)</a>.*?datetime="(.*?)</time>.*?.*?src="(.*?)class="attachment-anninapro_masonry-post', re.DOTALL ).findall(content)     
    if (match):
        for url,title,date,img in match:
            date=date.replace('">',' ')
            addDir(title+'[COLOR hotpink]'+date+'[/COLOR]',url,2,img)
   
    if (match2):
        addDir('[COLOR red]Next Page[/COLOR]',match2[0],1,'')
              





    

def PAGEVIDEOLINKS(url, name):
    content = getUrl(url)
    match = re.compile('</p><p>([^"]+)</p><p><em>(.*?)</em><br /> <a href="(.*?)" rel="nofollow"  target="_blank" class="external">', re.DOTALL ).findall(content)     
    if (match):
        for misc,names,video in match:
            misc=misc.replace("</p>","")
            misc=misc.replace("<p>","")
            misc=misc.replace("&#","*")
            addDownLink(names+'[COLOR hotpink]'+misc+'[/COLOR]',video,3,'')

def PLAYVIDEOLINKS(url, name):
    host = urlresolver.HostedMediaFile(url)
    if host:
        xbmc.executebuiltin("XBMC.Notification(Load OpenLoad ;)")
        resolver = urlresolver.resolve(url)
        xbmcgui.Dialog().ok("url",str(resolver.resolve().msg))
        xbmc.Player().play(resolver)
    return None    
    
    



def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param



topparams = get_params()
topurl = None
topname = None
topmode = None

try:
    topurl = urllib.unquote_plus(topparams["url"])
except:
    pass
try:
    topname = urllib.unquote_plus(topparams["name"])
except:
    pass
try:
    topmode = int(topparams["mode"])
except:
    pass

print "Mode: " + str(topmode)
print "URL: " + str(topurl)
print "Name: " + str(topname)

if topmode == None or topurl == None or len(topurl)<1:
    CATEGORIES()

elif topmode == 1:
    VIDEOLINKS(topurl, topname)

elif topmode == 2:
    PAGEVIDEOLINKS(topurl, topname)

elif topmode == 3:
    PLAYVIDEOLINKS(topurl, topname)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
