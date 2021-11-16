import pprint
import requests
from bs4 import BeautifulSoup
#############
# 1. 미드 대본 수집
#############
url='https://fangj.github.io/friends/season/0101.html'
result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')

sentence_list = doc.select('p>font')
print(sentence_list)
for i,sentence in enumerate(sentence_list):
    print('=================')
    sentence_text = sentence.get_text().strip()
    start_idx = sentence_text.find(':')
    clean_sentence = sentence_text[start_idx+2:]
    pprint.pprint('1>{}'.format(clean_sentence))

#############
#2. 단어만 추출(전처리)
##############

##################
#3.빈도수 순으로 나열 및 시각화
###################