from  urllib import request
from bs4 import BeautifulSoup

def grapDoubanMovieTop250(url):
   page = request.urlopen(url)
   contents = page.read()
   soup = BeautifulSoup(contents,"html.parser")
   print(u'               �����ӰTOP250:\n ��� \tӰƬ��\t  ���� ')
   for tag in soup.find_all('div', class_='item'):
      m_order=tag.em.get_text()
      #print m_order
      m_name=tag.span.get_text()
      #print m_name

      m_url=tag.a["href"]
      #print m_url
      print ("%s %s %s" %(m_order, m_name,m_url))
if __name__ == '__main__':
     grapDoubanMovieTop250('http://movie.douban.com/top250?')