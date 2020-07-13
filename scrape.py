import bs4
import pandas as pd
from selenium import webdriver
import random
import bisect

driver = webdriver.Chrome(executable_path=r"C:\Users\Hp\Python\chromedriver.exe")



ques_num = [268,35,43,208,181,139,85,60,82,39,55,50,57,9,4,19,25,128]
l = []
for i in range(len(ques_num)):
    if(i==0):
        l.append(ques_num[0])
    else:
        l.append(l[i-1]+ques_num[i])
       
index = random.randint(0,l[len(l)-1]-1)
x = bisect.bisect_right(l,index,0,len(l))
x = x+1
print(x)
#print(l)
url = ""
if(x==1):
  url = "https://leetcode.com/tag/array/"
elif(x==2):
  url = "https://leetcode.com/tag/heap/"
elif(x==3):
  url= "https://leetcode.com/tag/graph/"
elif(x==4):
    url = "https://leetcode.com/tag/dynamic-programming/"
elif(x==5):
    url = "https://leetcode.com/tag/string/"
elif(x==6):
    url = "https://leetcode.com/tag/tree/"
elif(x==7):
    url = "https://leetcode.com/tag/binary-search/"
elif(x==8):
    url = "https://leetcode.com/tag/two-pointers/"
elif(x==9):
    url = "https://leetcode.com/tag/greedy/"
elif(x==10):
    url = "https://leetcode.com/tag/linked-list/"
elif(x==11):
    url = "https://leetcode.com/tag/backtracking/"
elif(x==12):
    url = "https://leetcode.com/tag/bit-manipulation/"
elif(x==13):
    url = "https://leetcode.com/tag/stack/"
elif(x==14):
    url = "https://leetcode.com/tag/queue/"
elif(x==15):
    url = "https://leetcode.com/tag/binary-search-tree/"
elif(x==16):
    url = "https://leetcode.com/tag/divide-and-conquer/"
elif(x==17):
    url = "https://leetcode.com/tag/sliding-window/"
elif(x==18):
    url = "https://leetcode.com/tag/hash-table/"    
    
print(url)
driver.get(url)

content = driver.page_source

soup = bs4.BeautifulSoup(content,'html.parser')

tag_list = soup.find_all('div',class_='title-cell__ZGos')
y = random.randint(0,len(tag_list)-1)
val = tag_list[y].find('a',href=True)
print("leetcode.com"+val['href'])

