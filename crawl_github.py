from urllib.request import urlopen
from urllib.request import Request
import urllib.error
import itertools
import json
import time
import socket 

t_default = 10
socket.setdefaulttimeout(t_default)  


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
    '01143bdb82b5927fffba8a6952e1781d9c744ebb',
    ]
    token_iter = itertools.cycle(token_list)

    headers = {
           'Authorization': 'token ' + next(token_iter),
           'Content-Type': 'application/json',
           'Accept': 'application/vnd.github.mercy-preview+json',
           # 'Accept': 'application/json'
           }
    starBound = 10000000
    pageNum = 10
    cnt = 0
    for num in range(1, 51):
        for page in range(1, pageNum+1):
            url = 'https://api.github.com/search/repositories?q=language:Python+stars:<=' + str(starBound) + '&page=' + str(page) +'&per_page=100&sort=stars&order=desc'
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
                jsonData = json.dumps(data)
                if page == 10 and cnt % 100 == 0:
                    starBound = data['starNum'] - 1
                with open('datas2/repository'+str(cnt)+'.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f)        
            