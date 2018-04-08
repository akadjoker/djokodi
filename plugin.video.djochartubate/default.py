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

mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}



def log(msg, level=LOGDEBUG):
    xbmc.log('[%s] %s' % (addonname, msg), level)


def cleantext(text):
    text = text.replace('&amp;', '&')
    text = text.replace('&#8211;', '-')
    text = text.replace('&ndash;', '-')
    text = text.replace('&#038;', '&')
    text = text.replace('&#8217;', '\'')
    text = text.replace('&#8216;', '\'')
    text = text.replace('&#8230;', '...')
    text = text.replace('&quot;', '"')
    text = text.replace('&#039;', '`')
    text = text.replace('&rsquo;', '\'')
    return text


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def getHtml2(url):
    req = Request(url, None, mobileagent)
    response = urlopen(req, timeout=5)
    data = response.read()
    response.close()
    return data
def makeRequest(url, headers=None):
    try:
        if not headers:
            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data
    except:
        sys.exit(0)

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


def CATEGORIES():
                addDir("Main","https://chaturbate.com/female-cams/?page=1",1,'')
                addDir("Couple","https://chaturbate.com/couple-cams/?page=1",1,'')
                addDir("Male","https://chaturbate.com/male-cams/?page=1",1,'')
                addDir("Transsexual","https://chaturbate.com/transsexual-cams/?page=1",1,'')
       
                addDir("New Cams","https://chaturbate.com/new-cams/?page=1",1,'')
                addDir("New Female","https://chaturbate.com/new-cams/female/?page=1",1,'')
                addDir("New Couple","https://chaturbate.com/new-cams/couple/?page=1",1,'')
                addDir("New Male","https://chaturbate.com/new-cams/male/?page=1",1,'')

       
                addDir("Teen Cams (18+)","https://chaturbate.com/teen-cams/?page=1",1,'')
                addDir("Teen Cams (18+) - Female","https://chaturbate.com/teen-cams/female/?page=1",1,'')
                addDir("Teen Cams (18+) - Couple","https://chaturbate.com/teen-cams/couple/?page=1",1,'')
                addDir("Teen Cams (18+) - Male","https://chaturbate.com/teen-cams/male/?page=1",1,'')

                addDir("18 to 21 ","https://chaturbate.com/18to21-cams/?page=1",1,'')
                addDir("18 to 21 Female","https://chaturbate.com/18to21-cams/female/?page=1",1,'')
                addDir("18 to 21 Couple","https://chaturbate.com/18to21-cams/couple/?page=1",1,'')
                addDir("18 to 21 Male","https://chaturbate.com/18to21-cams/male/?page=1",1,'')

                addDir("20 to 30 ","https://chaturbate.com/20to30-cams/?page=1",1,'')
                addDir("20 to 30 Female","https://chaturbate.com/20to30-cams/female/?page=1",1,'')
                addDir("20 to 30 Couple","https://chaturbate.com/20to30-cams/couple/?page=1",1,'')
                addDir("20 to 30 Male","https://chaturbate.com/20to30-cams/male/?page=1",1,'')

                addDir("30 to 50 Cams","https://chaturbate.com/30to50-cams/?page=1",1,'')
                addDir("30 to 50 Female","https://chaturbate.com/30to50-cams/female/?page=1",1,'')
                addDir("30 to 50 Couple","https://chaturbate.com/30to50-cams/couple/?page=1",1,'')
                addDir("30 to 50 Male","https://chaturbate.com/30to50-cams/male/?page=1",1,'')

                addDir("Mature  (50+)","https://chaturbate.com/mature-cams/?page=1",1,'')
                addDir("Mature  (50+) - Female","https://chaturbate.com/mature-cams/female/?page=1",1,'')
                addDir("Mature  (50+) - Couple","https://chaturbate.com/mature-cams/couple/?page=1",1,'')
                addDir("Mature  (50+) - Male","https://chaturbate.com/mature-cams/male/?page=1",1,'')

      
                addDir("HD Cams","https://chaturbate.com/hd-cams/?page=1",1,'')
                addDir("HD Female","https://chaturbate.com/hd-cams/female/?page=1",1,'')
                addDir("HD Couple","https://chaturbate.com/hd-cams/couple/?page=1",1,'')
                addDir("HD Male","https://chaturbate.com/hd-cams/male/?page=1",1,'')

                addDir("North American ","https://chaturbate.com/north-american-cams/?page=1",1,'')
                addDir("North American Female","https://chaturbate.com/north-american-cams/female/?page=1",1,'')
                addDir("North American Couple","https://chaturbate.com/north-american-cams/couple/?page=1",1,'')
                addDir("North American Male","https://chaturbate.com/north-american-cams/male/?page=1",1,'')

                addDir("Other Region ","https://chaturbate.com/other-region-cams/?page=1",1,'')
                addDir("Other Region Female","https://chaturbate.com/other-region-cams/female/?page=1",1,'')
                addDir("Other Region Couple","https://chaturbate.com/other-region-cams/couple/?page=1",1,'')
                addDir("Other Region Male","https://chaturbate.com/other-region-cams/male/?page=1",1,'')

                addDir("Euro Russian ","https://chaturbate.com/euro-russian-cams/?page=1",1,'')
                addDir("Euro Russian Female","https://chaturbate.com/euro-russian-cams/female/?page=1",1,'')
                addDir("Euro Russian Couple","https://chaturbate.com/euro-russian-cams/couple/?page=1",1,'')
                addDir("Euro Russian Male","https://chaturbate.com/euro-russian-cams/male/?page=1",1,'')

                addDir("Philippines ","https://chaturbate.com/philippines-cams/?page=1",1,'')
                addDir("Philippines Female","https://chaturbate.com/philippines-cams/female/?page=1",1,'')
                addDir("Philippines Couple","https://chaturbate.com/philippines-cams/couple/?page=1",1,'')
                addDir("Philippines Male","https://chaturbate.com/philippines-cams/male/?page=1",1,'')

                addDir("Asian ","https://chaturbate.com/asian-cams/?page=1",1,'')
                addDir("Asian Female","https://chaturbate.com/asian-cams/female/?page=1",1,'')
                addDir("Asian Couple","https://chaturbate.com/asian-cams/couple/?page=1",1,'')
                addDir("Asian Male","https://chaturbate.com/asian-cams/male/?page=1",1,'')

                addDir("South American ","https://chaturbate.com/south-american-cams/?page=1",1,'')
                addDir("South American Female","https://chaturbate.com/south-american-cams/female/?page=1",1,'')
                addDir("South American Couple","https://chaturbate.com/south-american-cams/couple/?page=1",1,'')
                addDir("South American Male","https://chaturbate.com/south-american-cams/male/?page=1",1,'')
          

    
def VIDEOLINKS(url, name):
    try:
        listhtml = getHtml(url, url)

    except:
        print('Oh oh', 'It looks like this website is down.')
        return None
    match = re.compile(
        r'<li>\s+<a href="([^"]+)".*?src="([^"]+)".*?<div[^>]+>([^<]+)</div>.*?href[^>]+>([^<]+)<.*?age[^>]+>([^<]+)<',
        re.DOTALL | re.IGNORECASE).findall(listhtml)

    for videopage, img, status, name, age in match:
        name = cleantext(name.strip())
        status = status.replace("\n", "").strip()
        name = 'Name:' + name + ', Age: ' + age
        videopage = "https://chaturbate.com" + videopage
        addDownLink(name,videopage,2,img)
        
        

def PLAYVIDEOLINKS(url, name):
    listhtml = getHtml(url, USER_AGENT)
    m3u8url = re.compile(r"jsplayer, '([^']+)", re.DOTALL | re.IGNORECASE).findall(listhtml)
    print(m3u8url[0])
    if m3u8url:
        m3u8stream = m3u8url[0]
        m3u8stream = m3u8stream.replace('_fast', '')
        xbmc.Player().play(m3u8stream)




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
    PLAYVIDEOLINKS(topurl, topname)
    


xbmcplugin.endOfDirectory(int(sys.argv[1]))
