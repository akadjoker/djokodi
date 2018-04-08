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
                    addDir("Main","https://www.cam4.com/featured",1,'')
                    addDir("Female","https://www.cam4.com/female",1,'')
                    addDir("Female HD","https://www.cam4.com/female/hd",1,'')
                    addDir("Female New","https://www.cam4.com/female/new",1,'')
                    addDir("Female Portugal","http://www.cam4.com/female/portugal",1,'')
                    addDir("Female Brazil","http://www.cam4.com/female/brazil",1,'')

                    addDir("Female Usa","http://www.cam4.com/female/usa",1,'')
                    addDir("Female France","http://www.cam4.com/female/france",1,'')
                    addDir("Female Italy","http://www.cam4.com/female/italy",1,'')
                    addDir("Female Uk","http://www.cam4.com/female/uk",1,'')
                    addDir("Female Australia","http://www.cam4.com/female/australia",1,'')


                    addDir("Female Canada","http://www.cam4.com/female/canada",1,'')
                    addDir("Female Argentina","http://www.cam4.com/female/argentina",1,'')
                    addDir("Female Germany","http://www.cam4.com/female/germany",1,'')
                    addDir("Female Spain","http://www.cam4.com/female/spain",1,'')
                    addDir("Female Colombia","http://www.cam4.com/female/colombia",1,'')
                    addDir("Female Chile","http://www.cam4.com/female/chile",1,'')


                    addDir("Female Japan","http://www.cam4.com/female/japan",1,'')
                    addDir("Female Philippines","http://www.cam4.com/female/philippines",1,'')
                    addDir("Female Thailand","http://www.cam4.com/female/thailand",1,'')

                    addDir("Female Russia","http://www.cam4.com/female/russianfederation",1,'')

                    addDir("Female Romania","http://www.cam4.com/female/romania",1,'')
                    addDir("Female Poland","http://www.cam4.com/female/poland",1,'')
                    addDir("Female Turkey","http://www.cam4.com/female/turkey",1,'')
                    addDir("Female India","http://www.cam4.com/female/india",1,'')



                    addDir("Female Bulgaria","http://www.cam4.com/female/bulgaria",1,'')
                    addDir("Female Switz","http://www.cam4.com/female/switzerland",1,'')
                    addDir("Female Sweden","http://www.cam4.com/female/sweden",1,'')




                    addDir("Female Angola","http://www.cam4.com/female/angola",1,'')
                    addDir("Female Madagascar","http://www.cam4.com/female/madagascar",1,'')

                    addDir("Female English","http://www.cam4.com/female/english",1,'')
                    addDir("Female Portuguese","http://www.cam4.com/female/portuguese",1,'')
                    addDir("Female Spanish","http://www.cam4.com/female/spanish",1,'')


                    addDir("Couple","http://www.cam4.com/couple",1,'')
                    addDir("Male","http://www.cam4.com/male",1,'')
                    addDir("Transsexual","http://www.cam4.com/shemale",1,'')
                    addDir("Gay","http://www.cam4.com/cams/gay",1,'')

                    addDir("Anal","http://www.cam4.com/tags/anal",1,'')
                    addDir("Cum","http://www.cam4.com/tags/cum",1,'')
                    addDir("Pussy","http://www.cam4.com/tags/pussy",1,'')
                    addDir("Dirty","http://www.cam4.com/tags/dirty",1,'')
                    addDir("Naked","http://www.cam4.com/tags/naked",1,'')
                    addDir("Wet","http://www.cam4.com/tags/wet",1,'')
                    addDir("Teen","http://www.cam4.com/tags/teen",1,'')
                    addDir("Fuckmachine","http://www.cam4.com/tags/fuckmachine",1,'')
                    addDir("Dirtyshow","http://www.cam4.com/tags/dirtyshow",1,'')
                    addDir("Tits","http://www.cam4.com/tags/tits",1,'')
                    addDir("Boobs","http://www.cam4.com/tags/boobs",1,'')
                    addDir("Bigass","http://www.cam4.com/tags/bigass",1,'')
                    addDir("Dildo","http://www.cam4.com/tags/dildo",1,'')
                    addDir("Curve","http://www.cam4.com/tags/curve",1,'')
                    addDir("BBW","http://www.cam4.com/tags/bbw",1,'')
                    addDir("Lesbian","http://www.cam4.com/tags/lersbian",1,'')
                    addDir("Squirt","http://www.cam4.com/tags/squirt",1,'')
                    addDir("Ass","http://www.cam4.com/tags/ass",1,'')
                    addDir("LiveTouch","http://www.cam4.com/tags/livetouch",1,'')
                    addDir("Pee","http://www.cam4.com/tags/pee",1,'')
                    addDir("Fuck","http://www.cam4.com/tags/fuck",1,'')

    
def VIDEOLINKS(url, name):
    try:
        listhtml = makeRequest(url)
        with open("cam4.html", "w") as text_file:
             text_file.write(listhtml)
    except:
        log('Oh oh', 'It looks like this website is down.')
        return None
    #match = re.compile('profileDataBox"> <!-- preview --> <a href="([^"]+)".*?src="([^"]+)" title="Chat Now Free with ([^"]+)"',  re.DOTALL | re.IGNORECASE).findall(listhtml)
    match = re.compile('profileDataBox"> <!-- preview --> <a href="([^"]+)".*?data-hls-preview-url="(.*?)">.*?src="([^"]+)" title="Chat Now Free with ([^"]+)"',  re.DOTALL | re.IGNORECASE).findall(listhtml)
    count = 0
    for videourl,link, img, name in match:
        name = cleantext(name)
        videourl = "http://www.cam4.com" + videourl
        addDownLink(name,videourl,2,img)

def PLAYVIDEOLINKS(url, name):
    #xbmc.Player().play(url)
    listhtml = getHtml(url, '', mobileagent)
    match = re.compile('src="(http[^"]+m3u8)', re.DOTALL | re.IGNORECASE).findall(listhtml)
    if match:
       videourl = match[0]
       xbmc.Player().play(videourl)
       #from F4mProxy import f4mProxyHelper
       #f4mp=f4mProxyHelper()
       #f4mp.playF4mLink(videourl,name,proxy=None,use_proxy_for_chunks=False, maxbitrate=0, simpleDownloader=False, auth=None, streamtype='HLS',setResolved=False,swf=None , #callbackpath="",callbackparam="", iconImage='')
     #  listas = getHtml(videourl, '', mobileagent)
     #  mylist = listas.split("\n")
     #  numList=len(mylist)

    



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
