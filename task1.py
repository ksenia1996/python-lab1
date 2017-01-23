import re 
import requests 
s=[] 
str1='http://www.mosigra.ru/'
j=1
k=1
i=1
s.insert(1,'')
while k<10:
	response = requests.get(str1) 
	a=re.findall(r'(\w*@\w*[.]\w*)',str(response.content)) 
	a=set(a)
	b=re.findall(r'http:\/\/www\.mosigra\.ru\/[\w\d:#@%\/;$~_?\+-=\/\.&]*',str(response.content)) 
	b=set(b)
	for word in b:
		if str1.rfind(word)!=-1:
			str1=word
	for word in a:
		t=0
		for n in range(1,i):
			if word==s[n]:
				t=1
		if t==0:
			s.insert(i,word)
			i=i+1
	k=k+1
	
s.pop(1)
print(s)