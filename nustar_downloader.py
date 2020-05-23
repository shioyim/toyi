url = "https://heasarc.gsfc.nasa.gov/FTP/nustar/data/obs/00/1/"
project_name = "10012001002"

parent_url = url + project_name


from bs4 import BeautifulSoup
import requests
import os

def task (url,p='.'):
    html = requests.get(url)
    bs = BeautifulSoup(html.text)
    subdirectorys = []
    a_list = bs.findAll("a")
    for i in a_list:
        if i.text[-1] == "/":
            subdirectorys.append(i.attrs["href"])
        else:
            if i.attrs["href"][0] not in  "/?":    
                os.system("wget -P %s"%p  + " " +url + "/" + i.text)
    return subdirectorys


if __name__ == "__main__":
    subdirectorys = task(parent_url)                
    for i in subdirectorys:
        p = i[:-1]
        os.mkdir(p)
        task(parent_url + "/" +i[:-1],p=p)



