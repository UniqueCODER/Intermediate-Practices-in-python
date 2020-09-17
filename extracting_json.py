import json
import urllib.request
url=input('Enter a URL: ')
u=urllib.request.urlopen(url)
dat=u.read()
data=json.loads(dat)

sum=0
for tags in data['comments']:
    sum+=tags['count']
print (sum)

#print(sum(nested_dict['count'] for nested_dict in js['comments'])
