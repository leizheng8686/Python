import urllib
import urllib2
import re

class youtube:
    def __init__(self,baseURL,query):
        self.baseURL=baseURL
        self.query='/results?search_query='+str(query)
        self.view=[]
        self.date=[]
        self.vid=[]
        

    def getPage(self,pageFrom,pageTo):
        try:
            while pageFrom<=pageTo:
                url=self.baseURL+self.query+'&page='+str(pageFrom)
                print url
                request=urllib2.Request(url)
                response=urllib2.urlopen(request)
                pageFrom+=1
                response=response.read().decode('utf-8')
                reg = r'<div class="yt-lockup-content".*?<a href="(.*?)" class.*?>'
                pattern=re.compile(reg)
                href=re.findall(pattern,response)
                for h in href:
                    self.vid.append(h[9:])
                #for a in self.vid:
                    #print a
            print "===============get all vid==============="
            return self.vid
            '''for h in href:
                    URL=self.baseURL+str(h)
                    print URL
                    request1=urllib2.Request(URL)
                    response1=urllib2.urlopen(request1)
                    response1=response1.read().decode('utf-8')
                    reg1 = r'<div class="watch-view-count">(.*?)</div>'
                    reg2 = r'Published on (.*?)</strong>'
                    pattern1=re.compile(reg1)
                    pattern2=re.compile(reg2)
                    self.view.append(re.findall(pattern1,response1))
                    self.date.append(re.findall(pattern2,response1))
            D=zip(self.date,self.view)'''
                
            '''if self.view:
                    for r in self.view:
                        print r
                else:
                    print"none"
                if self.date:
                    for d in self.date:
                        print d
                else:
                    print"none"'''
            
            '''for d in D:
                print d
            return D'''
                    
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"connection failed",e.reason
                return None
'''baseURL='https://www.youtube.com'
query=input("search:")
#query='soccer'
result=youtube(baseURL,query)
pageFrom=1
pageTo=2
response=result.getPage(pageFrom,pageTo)'''
