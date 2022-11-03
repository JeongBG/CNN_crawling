import requests
from datetime import datetime
from bs4 import BeautifulSoup

Year=datetime.today().year
Month=datetime.today().month
Day=datetime.today().day

# Year = 2022
# Month = 11
# Day = 3

Year=str(Year)[2:]
Month=str(Month)
Day=str(Day)

Month=Month.zfill(2)
Day=Day.zfill(2)

url='http://transcripts.cnn.com/TRANSCRIPTS/{}/{}/sn.01.html'.format(Year+Month,Day)

resp=requests.get(url)
soup=BeautifulSoup(resp.text, 'lxml')
print('Request code is {}'.format(resp.status_code))

container=soup.find('div', style='padding-left:10px;').find_all('p',class_='cnnBodyText')

contents=''
for i in container:
    contents +='\n'+ i.get_text().strip()

contents=contents.replace("`","'")
contents=contents.replace('   ',' ')
contents = Year + Month + Day + '\n' + contents
file=open('CNN_scripts.txt'.format(Year,Month,Day),'a')
file.write(contents)
file.close()
