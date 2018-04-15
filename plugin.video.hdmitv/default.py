import urllib, urllib2, re, sys, xbmcplugin, xbmcgui,xbmc
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

Request = urllib2.Request
urlopen = urllib2.urlopen



import os           # access operating system commands
import urlparse     # splits up the directory path - much easier importing this than coding it up ourselves
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}



USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}



def log(msg, level=LOGDEBUG):
    xbmc.log('[%s] %s' % (addonname, msg), level)


def getHtml2(url):
    req = Request(url, None, mobileagent)
    response = urlopen(req, timeout=5)
    data = response.read()
    response.close()
    return data

def getHtml(url, referer='', hdr=None, NoCookie=None, data=None):
    try:
        if not hdr:
            req = Request(url, data, headers)
        else:
            req = Request(url, data, hdr)
        if len(referer) > 1:
            req.add_header('Referer', referer)
        if data:
            req.add_header('Content-Length', len(data))
        response = urlopen(req, timeout=60)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            f.close()
        else:
            data = response.read()
        response.close()
    except urllib2.HTTPError as e:
        data = e.read()
        raise urllib2.HTTPError()
    return data
    
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

def cleanex(text):
    text = text.replace(u'\xda','U').replace(u'\xc9','E').replace(u'\xd3','O').replace(u'\xd1','N').replace(u'\xcd','I').replace(u'\xc1','A').replace(u'\xf8','o').replace(u'\xf1','n')
    return text

def CATEGORIES():
    addDir('Start Ace Engine','http://hdmi-tv.ru/',2,'')
    addDir('Main','https://www.hdmi-tv.ru/main/',3,'')
    addDir('Sports','http://hdmi-tv.ru/sport/',3,'')
    addDir('Music','http://hdmi-tv.ru/music/',3,'')
    addDir('Humor','http://hdmi-tv.ru/humor/',3,'')
    addDir('Children','http://hdmi-tv.ru/children/',3,'')
    addDir('Films','https://www.hdmi-tv.ru/films/',3,'')
    addDir('Educational','https://www.hdmi-tv.ru/educational/',3,'')
    addDir('Men','https://www.hdmi-tv.ru/men/',3,'')
    #addDir('Adult','https://www.hdmi-tv.ru/xxx/',3,'')
    

    

def SUBCATEGORIES(url,name):
    link = getHtml2(url)
    match = re.compile('<div class="short">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)" .+?',          re.DOTALL).findall(link)
    for url,title,img in match:
        addDownLink(title, url, 1, "http://hdmi-tv.ru/"+img)

    match2 = re.compile('<div class="navigation" align="center" ><span>(.+?)</span> <span>(.+?)</span> <a href="(.+?)">(.+?)</a>',          re.DOTALL).findall(link)
    if match2:
       addDir("Next Page "+str(match2[0][1]), str(match2[0][2]), 3, '')
       #xbmcgui.Dialog().ok(str(match2[0][0]),str(match2[0][1]),str(match2[0][2]))
       

def play_p2ps(url,name):
    url= url.replace('acestream://','').replace('ts://','').replace('st://','')
    url='plugin://plugin.video.p2p-streams/?url=%s&mode=1&name=%s'%(url,name.replace(' ','+'))
    xbmc.Player().play(url)


def play_plexus(url,name):
    url='plugin://program.plexus/?url=%s&mode=1&name=%s'%(url,name.replace(' ','+'))
    xbmc.Player().play(url)

    
def VIDEOLINKS(url, name):
    xbmc.log("DJOKER-- VIDEOLINK")
    listhtml = getHtml2(url)
    match = re.compile('<source  src="(.+?)" type="application/x-mpegURL">',re.DOTALL | re.MULTILINE).findall(str(listhtml))
    link=str(match[0]).replace("http://127.0.0.1:6878/ace/manifest.m3u8?id=","acestream://")
    play_plexus(link,name);


def notify(msg='', duration=5000):
    header = 'DjokerSoft'
    builtin = "XBMC.Notification(%s,%s, %s)" % (header, msg, duration)
    xbmc.executebuiltin(builtin)
    

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
    log("categories")
    
    CATEGORIES()

elif topmode == 1:
    log("play video")
    VIDEOLINKS(topurl, topname)
elif topmode == 2:
    notify('Start AceEngine - Plataform:'+sys.platform+' ')
    if sys.platform.startswith('win32'):
        p = subprocess.Popen('start-engine --client-gtk', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elif sys.platform.startswith('linux'):
        p = subprocess.Popen(os.environ['HOME']+'/acestream/start-engine --client-gtk', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else: 
        p = subprocess.Popen('start-engine --client-gtk', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
elif topmode == 3:
    SUBCATEGORIES(topurl, topname)
    


xbmcplugin.endOfDirectory(int(sys.argv[1]))
