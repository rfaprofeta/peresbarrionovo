#!/usr/bin/python3
import requests, bs4
file=open('dicionario','w')
for i in range(65, 92):

    site = ("https://br.advfn.com/bolsa-de-valores/bovespa/" + str(chr(i)))
    web=requests.get(site)
    websp=bs4.BeautifulSoup(web.content, 'lxml')
    x=[]
    y=[]
    
    now=websp.find_all('td' ,class_='String Column1')
    now2=websp.find_all('td',class_='String Column2 ColumnLast')
    
    
    for link in now:
        x.append(link.getText())
    for link2 in now2:
        y.append(link2.getText())
    n=0
    for math in x:
    	file.write ('"'+ str(x[n])+'"'+":"+'"'+str(y[n])+'"'+",")
    	n+=1
        #file.write ((str(x[n])+':'+str(y[n]))+"\n")
        #n+=1
            