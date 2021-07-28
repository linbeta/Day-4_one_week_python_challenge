from bs4 import BeautifulSoup
import urllib.request

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'

# 先將原始網頁資料轉成html文件後，做成BeautifulSoup物件
with urllib.request.urlopen(url) as response:
    html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# 找到網頁中即將上映的每部電影div，用for loop列出每一部電影的中英文片名、期待度、上映日期等資訊：
release_list_element = soup.select(".release_info_text")
for item in release_list_element:
    film_name_ch = item.findChildren("a")[0].text.strip()
    film_name_en = item.findChildren("a")[1].text.strip()
    try:
        expectation = item.findChild(class_="leveltext").text.split()[0]
    except:
        expectation = "無資料"
    release_time = item.findChild(class_="release_movie_time").text
    # print(film_name_ch, film_name_en, expectation, release_time)
    print(f"{film_name_ch} {film_name_en} / 期待度：{expectation} / {release_time}")
    # 如果需要對資料進行處理、排序等，可以用以上film_name, expectation, release_time等變數做成我們需要的資料格式(json或是dataFrame等等)
