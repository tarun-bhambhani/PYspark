from bs4 import BeautifulSoup
import requests
import urllib
import matplotlib.pyplot as plt 

#from pyspark import SparkContext

import matplotlib.pyplot as plt


url = 'https://en.wikipedia.org/wiki/Machine_learning#Processes_and_techniques'

#sending a web page request to the required webpage
#storing the request in a variable "r"
r = requests.get(url)

#object conversion to beautifulsoup object
soup = BeautifulSoup(r.content,'lxml')

#Selecting title tag from the soup variable
tit=soup.select('title')
intro = []
intro.append(tit[0].getText());

#finding all paragraph tags
data = soup.find_all('p')

#appending data in a file
for i in data[1:6]:
    intro.append(i.getText())

#print scraped data
intro

#using pyspark  for counting number of occurences of words
from pyspark import SparkContext

sc = SparkContext(appName="WordCountTest")
lines = sc.textFile(data.txt)
words = lines.flatMap(lambda x: x.split(" "))
word_count = words.map(lambda x: (x,1)).reduceByKey(lambda x, y: x+y)
output = word_count.collect()

for pair in output:
    print(pair)
p=word_count(intro[1])

lst = [(k, v) for k, v in p.items()]
lst

#creating file
ax = plt.figure(figsize=(28,8))
plt.bar(range(len(p)), list(p.values()), align='center')
plt.xticks(range(len(p)), list(p.keys()),rotation=90)

#printing graph
plt.show()