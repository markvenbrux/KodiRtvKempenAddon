import sys
import xbmcgui
import xbmcplugin
from datetime import date
from datetime import timedelta

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://www.rtv.be/cdn1/video/20150508_nieuwskempen.mp4'

d = date.today()
url = 'http://www.rtv.be/cdn1/video/{0}_nieuwskempen.mp4'.format(d.strftime("%Y%m%d"))
li = xbmcgui.ListItem('Vandaag!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


d = date.today() - timedelta(days=1)
url = 'http://www.rtv.be/cdn1/video/{0}_nieuwskempen.mp4'.format(d.strftime("%Y%m%d"))
li = xbmcgui.ListItem('Gisteren!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
