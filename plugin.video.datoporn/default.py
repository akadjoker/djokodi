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
def notify(header=None, msg='', duration=5000):
    if header is None: header = 'DjokerSoft'
    builtin = "XBMC.Notification(%s,%s, %s)" % (header, msg, duration)
    xbmc.executebuiltin(builtin)
    
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

def remove_duplicates(l):
    return list(set(l))   

def removeduplicates(x):
    z = [x[0]]
    for i in range(1,len(x)):
        for y in range(0, i):
            if x[i] == x[y]:
                break
        else:
            z.append(x[i])
    return z 

def ordered_set(in_list):
    out_list = []
    added = set()
    for val in in_list:
        if not val in added:
            out_list.append(val)
            added.add(val)
    return out_lis    

def PAGEVIDEOLINKS(url,name):
    content = getUrl(url)
    match = re.compile('<div class="vid_block">.*?<a href="(.*?)".*?background: (.*?) no-repeat.*?<span>(.*?)</span>.*?class="link"><b>(.*?)</b>.*?<div class="category">', re.DOTALL ).findall(content)     

    if (match):
        for url,img,time,title in match:
          #  print url
            image = img.replace("url('","").replace("')","")
            addDownLink(title+' '+'[COLOR hotpink]'+time+'[/COLOR]',url,2,image)
          #  print time
          #  print title
          
           # VIDEOLINKS(url)
    match2 = re.compile('<div class="rrd row"><div class="paging">(.*?)</small></div></div>',re.DOTALL ).findall(content)
    if match2:
        lst=re.findall("(https?://\S+')", match2[0])
        if lst:
            links=removeduplicates(lst)
            for i in range(0,len(links)-1):
                s = links[i].replace("'","")
                pg = s.split('/')[5].replace("page","")
                addDir('Next Page [COLOR hotpink]'+pg+'[/COLOR]',s,1,"")

                #print pg

        
              

            
    
       

def PLAYVIDEO(name,url):
    xbmc.Player().play(url)
    #notify(None,name)
    

def VIDEOLINKS(url,name):
    content = getUrl(url)
    match = re.compile("<script type='text/javascript'>(.*?)</script>", re.DOTALL ).findall(content)     
    #notify(None,'Parse Videos')
    if (match):
        data= match[0].split("|")
        link=None
        if len(data)==107: 
           link='https://s5.datoporn.co/'+data[96]+'/v.'+data[95]
           PLAYVIDEO(name,link)
        elif len(data)==106: 
           link='https://s5.datoporn.co/'+data[95]+'/v.'+data[94]
           PLAYVIDEO(name,link)
        elif len(data)==105: 
           link='https://s5.datoporn.co/'+data[94]+'/v.'+data[93]
           PLAYVIDEO(name,link)
        else:
            notify(None,'NO LInks')
        
   
def CATEGORIES():
    url="https://datoporn.co/categories_all"
    content = getUrl(url)
    match = re.compile('<div class="boxvid".*?href="(.*?)" .*?:url(.*?);".*?<span>(.*?)</span>.*? .*?.*?" class="link"><b>(.*?)</b>.*?', re.DOTALL ).findall(content)
    if (match):
       for url,img,count,title in match:
            icon= img.replace("(","").replace(")","")
            addDir(title+' '+'[COLOR hotpink]'+count+'[/COLOR]',url,1,icon)

    

def Playvid(url, name):
    listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
    listitem.setProperty("IsPlayable","true")
    pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    pl.clear()
    pl.add(url, listitem)
    xbmc.Player().play(pl)
    #   listitem.setPath(str(url))
    #   xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)


def PLAYVIDEOLINKS(url, name):
    #from F4mProxy import f4mProxyHelper
    #f4mp=f4mProxyHelper()
   # f4mp.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved,swf,callbackpath, callbackparam,iconImage)
    #f4mp.playF4mLink(url,name)#,proxy=None,use_proxy_for_chunks=False, maxbitrate=0, simpleDownloader=False, auth=None, streamtype='HLS',setResolved=False,swf=None , #callbackpath="",callbackparam="", iconImage='')

    #notify(None,url+''+name)
    xbmc.Player().play(url)
   # return None    
   # Playvid(url,name)
    



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
    PAGEVIDEOLINKS(topurl, topname)

elif topmode == 2:
    VIDEOLINKS(topurl, topname)

elif topmode == 3:
    PLAYVIDEOLINKS(topurl, topname)


   
    


xbmcplugin.endOfDirectory(int(sys.argv[1]))
