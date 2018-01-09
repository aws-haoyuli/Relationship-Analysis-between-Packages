from urllib.request import urlopen
from urllib.request import Request
import urllib.error
import itertools
import json
import time
import socket 

t_default = 10
socket.setdefaulttimeout(t_default)  

def parse_package(path):
    packages = []
    file = open(path, 'r', encoding='utf-8')
    while 1:
        line = file.readline()
        if not line:
            break
        index = line.find('import')
        if index != -1:
            index1 = line.find('from')
            if index1 != -1:
                index2 = index1+4
                while line[index2] == ' ':
                    index2 = index2+1
                index1 = index2
                while 1:
                    if index2 == len(line) or line[index2] == '\n' or line[index2] == '.' or line[index2] == ' ':
                        break
                    index2 = index2+1
                packages.append(line[index1:index2])
            else:
                index2 = index+6
                while line[index2] == ' ':
                    index2 = index2+1
                index = index2
                while 1:
                    if index2 == len(line) or line[index2] == '\n' or line[index2] == '.' or line[index2] == ',':
                        packages.append(line[index:index2])
                        index2 = line.find(',', index2)
                        if (index2 == -1) :
                            break
                        index2 = index2+1
                        while line[index2] == ' ':
                            index2 = index2+1
                        index = index2
                    index2 = index2+1
    file.close()
    return packages
    

def get_packages(url):
    packages = []
    if url == '':
        return packages
    try:
        req = urlopen(Request(url,headers=headers))
        response = req.read()
        results = json.loads(response.decode('utf-8'))
        req.close()
    except:  
        print('some errors') 
        return packages
    # time.sleep(10)
    for item in results:
        name = item['name']
        typ = item['type']
        if typ == 'file':
            if len(name) > 2 and name[-3] == '.' and name[-2] == 'p' and name[-1] == 'y':
                download = item['download_url']
                try:
                    f = urlopen(download) 
                    data = f.read().decode('utf-8') 
                    f.close()
                except:  
                    print('some errors')
                    return packages
                # time.sleep(10)
                with open('datas/temp/temp.py', 'w', encoding='utf-8') as code:     
                    code.write(data)
                packages = parse_package('datas/temp/temp.py')
                
        elif typ == 'dir':
            packages = packages + get_packages(item['url'])
    packages = list(set(packages))        
    return packages


def get_contributors(url):
    con = []
    try:
        req = urlopen(Request(url,headers=headers))
        response = req.read()
        results = json.loads(response.decode('utf-8'))
        req.close()
    except:  
        print('some errors')
        return con
    # time.sleep(5)
    for item in results:
        con.append(item['login'])
    return con


def get_results(url):
    try:
        req = urlopen(Request(url,headers=headers))
        response = req.read()
        result = json.loads(response.decode('utf-8'))
        req.close()
    except:  
        print('some errors') 
    return result
    

if __name__ == '__main__':
    token_list = [
    '7ebc4cf45af0ba05fd2d8d0a25c84ad14c1d93c6',
    # '01143bdb82b5927fffba8a6952e1781d9c744ebb',
    ]
    token_iter = itertools.cycle(token_list)

    headers = {
           'Authorization': 'token ' + next(token_iter),
           'Content-Type': 'application/json',
           'Accept': 'application/vnd.github.mercy-preview+json',
           # 'Accept': 'application/json'
           }
    pageNum = 10
    
    cnt = 0
    for page in range(1, pageNum+1):
        url = 'https://api.github.com/search/repositories?q=language:Python&page=' + str(page) +'&per_page=100&sort=updated&order=desc'
        results = get_results(url)


        for item in results['items']:
            cnt = cnt+1
            data = {}
            data['name'] = item['name'] 
            data['description'] = item['description']
            data['license'] = item['license']
            data['starNum'] = item['stargazers_count']
            data['folkNum'] = item['forks_count']
            data['watchNum'] = item['watchers_count']
            data['topic'] = item['topics']
            data['contributors'] = get_contributors(item['contributors_url'])
            contentUrl = item['url']+'/contents'
            data['packages'] = get_packages(contentUrl)
            jsonData = json.dumps(data)
            with open('datas/repository'+str(cnt)+'.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)        
