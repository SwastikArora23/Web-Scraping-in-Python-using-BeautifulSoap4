import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import pandas as pd


class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = 'http://galaxytoyotaservice.com'

client_response = Client(url)
source = client_response.mainFrame().toHtml()




        
sauce = urllib.request.urlopen('http://galaxytoyotaservice.com')

soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.title.string)

#print(soup.p)

#print(soup.find_all('p'))

#for paragraph in soup.find_all('p'):
#    print(paragraph.text)

#print(soup.get_text())

#for url in soup.find_all('a'):
#    print(url.get('href'))

nav = soup.nav

#print(nav)

#for url in nav.find_all('a'):
#    print(url.get('href'))

#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)

#for div in soup.find_all('div', class_='body'):
#    print(div.text)

#table = soup.table
#table = soup.find('table')
#print(table)

js_test = soup.find('p', class_='jstest')
print(js_test.text)

#table_rows = table.find_all('tr')

#for tr in table_rows:
#    td = tr.find_all('td')
#    row = [i.text for i in td]
#    print(row)

#dfs = pd.read_html('http://galaxytoyotaservice.com', header=0)
#for df in dfs:
#    print(df)

