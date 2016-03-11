import sys
sys.path.append('YouTubeCrawl')
from crawler import Crawler
from main1 import youtube
from GetDate import get_day_of_day as getday
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

baseURL='https://www.youtube.com'
query=input("search:")
#query='soccer'
result=youtube(baseURL,query)
pageFrom=1
pageTo=10
response=result.getPage(pageFrom,pageTo)
print response
c= Crawler()
viewcount=[0]*120
maxlen=0
for vid in response:
    dailyviews=c.single_crawl(vid)
    if len(dailyviews)>maxlen:
        maxlen=len(dailyviews)
    #print len(dailyviews),dailyviews[-1]
    if len(dailyviews)>=120:
        for i in range(120):
            viewcount[-i-1]+=dailyviews[-i-1]
    if len(dailyviews)<120:
        for i in range(len(dailyviews)):
            viewcount[-i-1]+=dailyviews[-i-1]
#viewcount.pop(0)
    
date=['']*120
for i in range(120):
    date[-i-1]=getday(-i)
#for i in range(120):
    #date[i]=str(date[i])
    #viewcount[i]=str(viewcount[i])

#for i in range(120):
    #date[i]=string(date[i]]

if maxlen<120:
    del(viewcount[0:120-maxlen])
    del(date[0:120-maxlen])
for i in range(len(date)):
    print date[i],':',viewcount[i]

plt.plot(date,viewcount,'g')
#plt.xticks([date[0],date[29],date[59],date[89],date[119]])
#plt.set(gca,'xtick',[2005,2006,2007,2008,2009,2010])
plt.show()



