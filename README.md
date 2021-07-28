# 挑戰 #04：靜態網頁爬蟲實作（基礎）

這個挑戰對我來說算是簡單，順便複習了一下BeautifulSoup中一些常用的指令。

在這次的挑戰中，我原本想針對需要的資料個別存成List在依照順序印出，但因為有幾部片沒有期待度的資料，如果分欄位取得資料會出問題，所我我後來改成針對每部電影為單位，去抓出這部片的中英文名、期待度、上映日期等資料。
在for loop中以取得的電影使用.findChild()及.findChildren()方法，去抓出每一部片的片名及期待度等資料。

因為有些期待度欄位空白，故使用try/except來將沒有資料的欄位填入"無資料"

## 輸出結果如下圖

![output.png](https://github.com/linbeta/Day-4_one_week_python_challenge/blob/main/output.PNG)
