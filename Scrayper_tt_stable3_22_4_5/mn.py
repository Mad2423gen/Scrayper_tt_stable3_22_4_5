# 更新：2022-01-17@楽街の最初のPRページを削除
# 更新：2022年1月18日Gmail不具合修正
# 更新：2022-02-08ドライバーがバージョンが上がると
# 対応しなくなるのでwebdriver-manager導入
# 2022-04-02　RAINSオプション追加
#

import os
import datetime
import shutil
import time
import re
from time import sleep
from selenium import webdriver
import selenium
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
# RAINS関数追加
# import rains_scray as rains


# 変数定義===================================================
path = os.getcwd()
data_dir = path + "/data"
data_old_dir = "/data2"
send_file_dir = "/data3"
chrome_driver_path = "./chromedriver"
send_file = "data3/send_record.txt"



# ここから本体===============================================

# time.sleep(2000)



# =========================================================
# ファイル書き込み
# 書き換え
def write_w(bunshyou_text, file_name):
    with open(file_name, "w",encoding="utf-8_sig") as bun:
        bun.write(bunshyou_text)
# 追記
def write_a(bunsyou_text,file_name):
    with open(file_name,"a",encoding="utf-8_sig") as bun:
        bun.write(bunsyou_text)
# 件名抽出、保存
def kenmei_selection(title_xpath, write_file_path):
    tags = driver.find_elements_by_xpath(title_xpath)
    for tag in tags:
        write_a(tag.text + "\n", write_file_path)
# URLを抽出、保存
def url_selection(url_xpath,save_url_file):
    urls = driver.find_elements_by_xpath(url_xpath)
    for url in urls:
        if "https" in url.get_attribute("href"):
            write_a(url.get_attribute("href") + "\n",
            save_url_file)
# リストから１行呼び出し
def file_open_lines(filename):
    filename_str = str(filename)
    f = open(filename_str,"r",encoding="utf-8")
    lines = f.readlines()
    f.close()
    return lines
# リストの指定行削除（gyou_numberは最初なら0を、最後なら-1を入れる）
def delite_line(filename,gyou_number):
    ff = open(filename,"r",encoding="utf-8")
    dellines = ff.readlines()
    ff.close()
    del dellines[gyou_number]
    write_w("",filename)
    for delline in dellines:
        write_a(delline,filename)
#　10件以上削除(10以上削除
def del_outrange(filename):
    ff = open(filename,"r",encoding="utf-8")
    dellines = ff.readlines()
    ff.close()
    # 新着11件以上削除
    del dellines[10:]
    write_w("",filename)
    for delline in dellines:
        write_a(delline,filename)
# =========================================================

# ==========================================================
# ノーマル作動時のワークフロー
# 送信物件検索、記録部
# １サイトごとにループ処理
# サイトから新規情報を読み込む
# 旧ファイルと新規情報を比較する
# 差分を抽出
# 記録する
# 新ファイルを旧ファイルへコピー
# LINEに送信(但し、中身があれば）
# Emailに送信(但し、中身があれば）
# 送信ファイルを消去(但し、中身があれば）
# ==========================================================
#
# # 健美家１===================================================
# URL及びxpathとファイルパス
kenbika_url1 = "https://www.kenbiya.com/pp2_3_4/kw=%E6%BB" \
               "%8B%E8%B3%80/ "
title_xpath_kenbika1 = "//div/ul/li/a/ul/li/ul/li/h3"
url_xpath_kenbika1 = "//section/div/div/ul/li/a"
kenbika_bukkenfile1 = "./data/kenbika_bukken1.txt"
kenbika_urlfile1 = "./data/kenbika_url1.txt"

# # 新着保存・送信ファイル消去
write_w("",kenbika_bukkenfile1)
write_w("",kenbika_urlfile1)

# 新着読み込み・保存

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(kenbika_url1)
sleep(5)
kenmei_selection(title_xpath_kenbika1,kenbika_bukkenfile1)
url_selection(url_xpath_kenbika1,kenbika_urlfile1)
driver.quit()
# 最初のPR行削除
delite_line(kenbika_bukkenfile1,1)
delite_line(kenbika_urlfile1,1)


# 旧ファイルと差分を比較
new_title_files = file_open_lines(kenbika_bukkenfile1)
new_url_files = file_open_lines(kenbika_urlfile1)
old_title_files = file_open_lines("data2/kenbika_bukken1.txt")
old_url_files = file_open_lines("data2/kenbika_url1.txt")

# 差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【建美家・新着物件(滋賀)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_title_files):
    if not n_file in old_title_files:
        write_a(n_file + new_url_files[i] + "\n",send_file)
        print(n_file + new_url_files[i])

#新ファイルを古ファイル用としてdata2フォルダに保存
old_title = "./data2/kenbika_bukken1.txt"
old_url = "./data2/kenbika_url1.txt"
write_w("",old_title)
write_w("",old_url)
shutil.copy(kenbika_bukkenfile1,old_title)
shutil.copy(kenbika_urlfile1,old_url)
#
# 建美家１処理終==============================================

# 健美家2====================================================
# 1.URL及びxpathとファイルパス
kenbika_url2 ="https://www.kenbiya.com/pp2_3_4/" \
              "kw=%E4%B8%89%E9%87%8D/"
title_xpath_kenbika2 = "//div/ul/li/a/ul/li/ul/li/h3"
url_xpath_kenbika2 = "//section/div/div/ul/li/a"
kenbika_bukkenfile2 = "data/kenbika_bukken2.txt"
kenbika_urlfile2 = "data/kenbika_url2.txt"

# 2.新着保存・送信ファイル消去
write_w("",kenbika_bukkenfile2)
write_w("",kenbika_urlfile2)

# 3.新着読み込み・保存
# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(kenbika_url2)
sleep(5)
kenmei_selection(title_xpath_kenbika2,kenbika_bukkenfile2)
url_selection(url_xpath_kenbika2,kenbika_urlfile2)
driver.quit()
# 最初のPR行削除
delite_line(kenbika_bukkenfile2,1)
delite_line(kenbika_urlfile2,1)

# 4.旧ファイルと差分を比較
new_title_files = file_open_lines(kenbika_bukkenfile2)
new_url_files = file_open_lines(kenbika_urlfile2)
old_title_files = file_open_lines("./data2/"
                                  "kenbika_bukken2.txt")
old_url_files = file_open_lines("./data2/kenbika_url2.txt")

# 5.差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【建美家・新着物件(三重)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_title_files):
    if not n_file in old_title_files:
        write_a(n_file + new_url_files[i] + "\n",send_file)
        print(n_file + new_url_files[i])

# 6.新ファイルを古ファイル用としてdata2フォルダに保存
old_title = "./data2/kenbika_bukken2.txt"
old_url = "./data2/kenbika_url2.txt"
write_w("",old_title)
write_w("",old_url)
shutil.copy(kenbika_bukkenfile2,old_title)
shutil.copy(kenbika_urlfile2,old_url)

# 建美家２処理終==============================================

# 楽待１=====================================================
# 1.URL及びxpathとファイルパス
rakumachi_url1 = "https://www.rakumachi.jp/syuuekibukken/" \
                 "area/prefecture/dimAll/" \
                 "?realtor_id=&pref%5B%5D=25&area=&line=&st=" \
                 "&limit=20&keyword=&newly=&price_from=" \
                 "&price_to=&gross_from=&gross_to=" \
                 "&dim%5B%5D=1001&dim%5B%5D=1002&dim%5B%5D=" \
                 "1003&year_from=&year_to=&b_area_from=" \
                 "&b_area_to=&houses_ge=&houses_le=&min=" \
                 "&l_area_from=&l_area_to=&ex_real_search="

title_xpath_rakumachi1 = "//form/div/div/div/p"
rakumachi_titlefile1 = "data/rakumachi_title1.txt"
rakumachi_urlfile1 = "data/rakumachi_url1.txt"
main_url = "https://www.rakumachi.jp/syuuekibukken"

# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(rakumachi_url1)
time.sleep(3)
res = driver.page_source.encode('utf-8')
soup = BeautifulSoup(res, 'html.parser')
driver.quit()

# 3.新着読み込み・保存
# 楽待１_件名抽出
write_w("",rakumachi_titlefile1)
titles = soup.find_all("p", class_="propertyBlock__name")
for title in titles:
    # kenmei = title.get_text()
    with open(rakumachi_titlefile1,"a",encoding='utf-8_')\
            as raku:
        raku.write(title.get_text() + "\n")

# 楽待１URL抽出
# 特定の文字に挟まれたURLを抽出（属性が呼び出せないので）
html = str(soup)
url_strs = re.findall(r'syuuekibukken(.+)html',html)
write_w("",rakumachi_urlfile1)
for url in url_strs:
    with open(rakumachi_urlfile1,'a',encoding='utf-8_sig') as st:
        st.write("https://www.rakumachi.jp" + url + "html" + "\n")

# 新着10件以降削除
del_outrange(rakumachi_urlfile1)
del_outrange(rakumachi_titlefile1)
# 最初のPR行削除
delite_line(rakumachi_urlfile1,0)
delite_line(rakumachi_titlefile1,0)

# 4.旧ファイルと差分を比較

#新・旧ファイル読み込み

o_rakumachi_titlefile1 = "data2/rakumachi_title1.txt"
o_rakumachi_urlfile1 = "data2/rakumachi_url1.txt"
new_title_files = file_open_lines(rakumachi_titlefile1)
new_url_files = file_open_lines(rakumachi_urlfile1)
old_title_files = file_open_lines(o_rakumachi_titlefile1)
old_url_files = file_open_lines(o_rakumachi_urlfile1)


# # 5.差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【楽待・新着物件(滋賀)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_title_files):
    if not n_file in old_title_files:
        write_a(n_file + new_url_files[i] + "\n",send_file)
        print(n_file + new_url_files[i])

# 6.新ファイルを古ファイル用としてdata2フォルダに保存
old_title = "./data2/rakumachi_title1.txt"
old_url = "./data2/rakumachi_url1.txt"
write_w("",old_title)
write_w("",old_url)
shutil.copy(rakumachi_titlefile1,old_title)
shutil.copy(rakumachi_urlfile1,old_url)

# 楽待１処理終================================================

# 楽待２=====================================================

# 1.URL及びxpathとファイルパス
rakumachi_url2 = "https://www.rakumachi.jp/syuuekibukken/" \
                 "area/prefecture/dimAll/?realtor_id=&area=" \
                 "&line=&st=&limit=20&keyword=" \
                 "%E4%B8%89%E9%87%8D&newly=&price_from=" \
                 "&price_to=&gross_from=&gross_to=" \
                 "&dim%5B%5D=1001&dim%5B%5D=1002&dim%5B%5D=" \
                 "1003&year_from=&year_to=&b_area_from=" \
                 "&b_area_to=&houses_ge=&houses_le=&min=" \
                 "&l_area_from=&l_area_to=&ex_real_search="

# title_xpath_rakumachi2 = "//form/div/div/div/p"
rakumachi_titlefile2 = "data/rakumachi_title2.txt"
rakumachi_urlfile2 = "data/rakumachi_url2.txt"
main_url = "https://www.rakumachi.jp/syuuekibukken"

# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(rakumachi_url2)
time.sleep(3)
res = driver.page_source.encode('utf-8')
soup = BeautifulSoup(res, 'html.parser')
driver.quit()

# 3.新着読み込み・保存
# 楽待2_件名抽出
write_w("",rakumachi_titlefile2)
titles = soup.find_all("p", class_="propertyBlock__name")
for title in titles:
    # kenmei = title.get_text()
    with open(rakumachi_titlefile2,"a",encoding='utf-8_sig')\
            as raku:
        raku.write(title.get_text() + "\n")

# 楽待2URL抽出
# 特定の文字に挟まれたURLを抽出（属性が呼び出せないので）
html = str(soup)
url_strs = re.findall(r'syuuekibukken(.+)html',html)
write_w("",rakumachi_urlfile2)
for url in url_strs:
    with open(rakumachi_urlfile2,'a',encoding='utf-8_sig') as st:
        st.write("https://www.rakumachi.jp" + url + "html" + "\n")

# # 新着10件以降削除
del_outrange(rakumachi_urlfile2)
del_outrange(rakumachi_titlefile2)
# 最初のPR行削除
delite_line(rakumachi_urlfile2,0)
delite_line(rakumachi_titlefile2,0)

# 4.旧ファイルと差分を比較

#新・旧ファイル読み込み
o_rakumachi_titlefile2 = "data2/rakumachi_title2.txt"
o_rakumachi_urlfile2 = "data2/rakumachi_url2.txt"
new_title_files = file_open_lines(rakumachi_titlefile2)
new_url_files = file_open_lines(rakumachi_urlfile2)
old_title_files = file_open_lines(o_rakumachi_titlefile2)
old_url_files = file_open_lines(o_rakumachi_urlfile2)

# 5.差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【楽待・新着物件(三重)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_url in enumerate(new_url_files):
    if not n_url in old_url_files:
        write_a(n_url + new_title_files[i] + "\n",send_file)
        print(n_url + new_title_files[i])

# 6.新ファイルを古ファイル用としてdata2フォルダに保存
old_title = "./data2/rakumachi_title2.txt"
old_url = "./data2/rakumachi_url2.txt"
write_w("",old_title)
write_w("",old_url)
shutil.copy(rakumachi_titlefile2,old_title)
shutil.copy(rakumachi_urlfile2,old_url)

# 楽待２処理終================================================

#ニフティ不動産1==============================================
#　大津・近江
# # 1.URL及びxpathとファイルパス
nifty_xpath = "//div/div/div/h2/p/a"
nifty_titlefile1 = "data/nifty_title1.txt"
nifty_urlfile1 = "data/nifty_url1.txt"
# main_url =
nifty_url1 = "https://myhome.nifty.com/chuko/ikkodate" \
             "/kinki/shiga/?cities=otsushi," \
             "omihachimanshi,kusatsushi,moriyamashi," \
             "rittoshi,kokashi,yasushi," \
             "konanshi&subtype=buh&b2=15000000&b6=20" \
             "&isFromSearch=1 "

# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(nifty_url1)
time.sleep(5)
driver.find_element_by_id("ex13").click()
time.sleep(5)
# ページソース再取得
res = driver.page_source.encode('utf-8')
# soup = BeautifulSoup(res, 'html.parser')

# # 2.新着保存・送信ファイル消去
write_w("",nifty_titlefile1)
write_w("",nifty_urlfile1)

 # 3.新着読み込み・保存
# xpath = "//div/div/div/h2/p/a"
elems = driver.find_elements_by_xpath(nifty_xpath)
# for elem in elems:
#     print(elem.text)
#     print(elem.get_attribute("href"))

for elem in elems:
    el_title = elem.text
    el_url = elem.get_attribute("href")
    with open(nifty_urlfile1,"a",encoding="utf-8_sig") as u:
        u.write(el_url + "\n")
    with open(nifty_titlefile1,"a",encoding="utf-8_sig") as ti:
        ti.write(el_title + "\n")

# 4.旧ファイルと差分を比較
# 新・旧ファイル読み込み
o_nifty_titlefile1 = "data2/nifty_title1.txt"
o_nifty_urlfile1 = "data2/nifty_url1.txt"
new_title_files = file_open_lines(nifty_titlefile1)
new_url_files = file_open_lines(nifty_urlfile1)
old_title_files = file_open_lines(o_nifty_titlefile1)
old_url_files = file_open_lines(o_nifty_urlfile1)

# # 5.差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【ニフティ不動産・新着物件(大津・近江)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_title_files):
    if not n_file in old_title_files:
        write_a(n_file + new_url_files[i] + "\n",send_file)
        print(n_file + new_url_files[i])

# 6.新ファイルを古ファイル用としてdata2フォルダに保存
old_title = "./data2/nifty_title1.txt"
old_url = "./data2/nifty_url1.txt"
write_w("",old_title)
write_w("",old_url)
shutil.copy(nifty_titlefile1,old_title)
shutil.copy(nifty_urlfile1,old_url)
driver.quit()
#ニフティ不動産１終了==========================================

#ニフティ不動産２=============================================
#　甲賀市・湖南市
# 1.URL及びxpathとファイルパス
nifty_xpath = "//div/div/div/h2/p/a"
nifty_titlefile2 = "data/nifty_title2.txt"
nifty_urlfile2 = "data/nifty_url2.txt"
nifty_url2 = "https://myhome.nifty.com/tochi/kinki/shiga" \
             "/?b50=200&b6=20&cities=kokashi,konanshi," \
             "kusatsushi,moriyamashi,omihachimanshi," \
             "otsushi,rittoshi," \
             "yasushi&sort2=lotSize2-desc&subtype=bes" \
             "&sort1=money1-asc "

# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)
driver.get(nifty_url2)
time.sleep(5)
driver.find_element_by_id("ex13").click()
time.sleep(5)
# ページソース再取得
res = driver.page_source.encode('utf-8')
# soup = BeautifulSoup(res, 'html.parser')

# # 2.新着保存・送信ファイル消去
write_w("",nifty_titlefile2)
write_w("",nifty_urlfile2)

 # 3.新着読み込み・保存

elems = driver.find_elements_by_xpath(nifty_xpath)

for elem in elems:
    el_title = elem.text
    el_url = elem.get_attribute("href")
    with open(nifty_urlfile2,"a",encoding="utf-8_sig") as u:
        u.write(el_url + "\n")
    with open(nifty_titlefile2,"a",encoding="utf-8_sig") as ti:
        ti.write(el_title + "\n")

# 4.旧ファイルと差分を比較
# 新・旧ファイル読み込み
o_nifty_titlefile2 = "data2/nifty_title2.txt"
o_nifty_urlfile2 = "data2/nifty_url2.txt"
new_title_files2 = file_open_lines(nifty_titlefile2)
new_url_files2 = file_open_lines(nifty_urlfile2)
old_title_files2 = file_open_lines(o_nifty_titlefile2)
old_url_files2 = file_open_lines(o_nifty_urlfile2)

# # 5.差分を抽出・送信用ファイルに記録（data3のファイル）
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【ニフティ不動産・新着物件(甲賀市・湖南市)】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_title_files2):
    if not n_file in old_title_files2:
        write_a(n_file + new_url_files2[i] + "\n",send_file)
        print(n_file + new_url_files2[i])

# 6.新ファイルを古ファイル用としてdata2フォルダに保存
old_title2 = "./data2/nifty_title2.txt"
old_url2 = "./data2/nifty_url2.txt"
write_w("",old_title2)
write_w("",old_url2)
shutil.copy(nifty_titlefile2,old_title2)
shutil.copy(nifty_urlfile2,old_url2)
driver.quit()
# ニフティ不動産２終了==========================================
#
# アットホーム１==============================================
from selenium.webdriver.support.ui import Select

ahtome_url_top = "https://toushi-athome.jp/"
athome_url = "https://toushi-athome.jp/bklist?ITEM=ei&ART=42"

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome("./chromedriver")
driver.get(athome_url)
time.sleep(10)
driver.find_element_by_link_text("滋賀").click()
time.sleep(3)
driver.find_element_by_xpath("//div/div/div[2]"
                             "/ul/li[1]/img").click()
time.sleep(3)
driver.find_element_by_id("GROUP_00370")
time.sleep(3)
chk_shiga = driver.find_element_by_css_selector\
    ("input[name='GROUP'][value='00370']")
chk_shiga.click()
time.sleep(4)
driver.find_element_by_xpath("//li[9]/img[1]").click()
time.sleep(4)
element = driver.find_element_by_id("sortcombo_1")
select_num = Select(element)
select_num.select_by_value("33")

time.sleep(10)

at_titlefile1= "data/at_title1.txt"
at_urlfile1 = "data/at_url1.txt"
old_at_titlefile1 = "data2/at_title1.txt"
old_at_urlfile1 = "data2/at_url1.txt"

# 新着読み込み
write_w("",at_titlefile1)
write_w("",at_urlfile1)
at_css = "p.station > a"

elems = driver.find_elements_by_css_selector(at_css)
for elem in elems:
    atitle = elem.text
    aurl = elem.get_attribute("href")
    write_a(atitle + "\n",at_titlefile1)
    write_a(aurl + "\n",at_urlfile1)
# 登録件数ファイル10件以上削除
del_outrange(at_titlefile1)
del_outrange(at_urlfile1)

# ファイル比較
# 新旧ファイル呼び出し
ct = len(old_at_titlefile1)

if ct == 0:
    shutil.copy(at_titlefile1,old_at_titlefile1)
    shutil.copy(at_urlfile1,old_at_urlfile1)

new_at_titlefiles1 = file_open_lines(at_titlefile1)
new_at_urlfiles1 = file_open_lines(at_urlfile1)
old_at_titlefiles1 = file_open_lines(old_at_titlefile1)
old_at_urlfiles1 = file_open_lines(old_at_urlfile1)

# 新旧比較、差分抽出、メッセージ記録
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【アットホーム(滋賀)新着物件】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_at_urlfiles1):
    if not n_file in old_at_urlfiles1:
        write_a(new_at_titlefiles1[i] + n_file+ "\n",send_file)
        print(new_at_titlefiles1[i] + n_file)
# 新ファイルを旧ファイルへコピー
write_w("",old_at_titlefile1)
write_w("",old_at_urlfile1)
shutil.copy(at_titlefile1,old_at_titlefile1)
shutil.copy(at_urlfile1,old_at_urlfile1)

driver.quit()

# アットホーム１終了===========================================

# アットホーム２==============================================

ahtome_url_top = "https://toushi-athome.jp/"
athome_url = "https://toushi-athome.jp/bklist?ITEM=ei&ART=42"


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome("./chromedriver")
driver.get(athome_url)

time.sleep(5)
driver.find_element_by_link_text("三重").click()
time.sleep(3)
driver.find_element_by_xpath("//div/div/div[2]"
                             "/ul/li[1]/img").click()
time.sleep(3)
driver.find_element_by_id("GROUP_00360")
time.sleep(3)
chk_shiga = driver.find_element_by_css_selector\
    ("input[name='GROUP'][value='00360']")
chk_shiga.click()
time.sleep(4)
driver.find_element_by_xpath("//li[9]/img[1]").click()
time.sleep(4)
element = driver.find_element_by_id("sortcombo_1")
select_num = Select(element)
select_num.select_by_value("33")

time.sleep(10)

at_titlefile2= "data/at_title2.txt"
at_urlfile2 = "data/at_url2.txt"
old_at_titlefile2 = "data2/at_title2.txt"
old_at_urlfile2 = "data2/at_url2.txt"

# 新着読み込み
write_w("",at_titlefile2)
write_w("",at_urlfile2)
at_css = "p.station > a"

elems = driver.find_elements_by_css_selector(at_css)
for elem in elems:
    atitle = elem.text
    aurl = elem.get_attribute("href")
    write_a(atitle + "\n",at_titlefile2)
    write_a(aurl + "\n",at_urlfile2)
# 登録件数ファイル10件以上削除
del_outrange(at_titlefile2)
del_outrange(at_urlfile2)

# ファイル比較
# 新旧ファイル呼び出し
ct = len(old_at_titlefile2)

if ct == 0:
    shutil.copy(at_titlefile2,old_at_titlefile2)
    shutil.copy(at_urlfile2,old_at_urlfile2)

new_at_titlefiles2 = file_open_lines(at_titlefile2)
new_at_urlfiles2 = file_open_lines(at_urlfile2)
old_at_titlefiles2 = file_open_lines(old_at_titlefile2)
old_at_urlfiles2 = file_open_lines(old_at_urlfile2)

# 新旧比較、差分抽出、メッセージ記録
dt_now = datetime.datetime.now() #日付と時刻の表示
print("【アットホーム(三重)新着物件】" + dt_now.strftime
('%Y年%m月%d日 %H:%M:%S') + "\n")
for i,n_file in enumerate(new_at_urlfiles2):
    if not n_file in old_at_urlfiles2:
        write_a(new_at_titlefiles2[i] + n_file + "\n",send_file)
        print(new_at_titlefiles2[i] + n_file)
# 新ファイルを旧ファイルへコピー
write_w("",old_at_titlefile2)
write_w("",old_at_urlfile2)
shutil.copy(at_titlefile2,old_at_titlefile2)
shutil.copy(at_urlfile2,old_at_urlfile2)

driver.quit()
# ==================================================================================================



# ==================================================================================================
# RAINS 処理開始

# RAINS 追加　2022-04-02
# 引数、戻り値なし、WEBサイトの時間内の範囲で動作し、該当データがある場合、
# 'send_record.txt'に勝手に書き込む
# 修正などがある場合はすべて　’rains_scray.py’　に記述すること。

# rains.rains_function()

# import time
# import datetime
import difflib
# import re
# import os
import csv
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())

# RAINS アカウント情報 ==============================================

rains_id = '125100372700'  # ID
rains_passwd = 'cosei0304'  # Password

# ログインページURL
rains_top_url = "https://system.reins.jp/login/main/KG/GKG001200"

# 検索項目（ドロップダウンバリュー）
sd1 = [
    "//option[. = '01:■三重四日市　外全']",
    "//option[. = '02:■滋賀１棟']",
    "//option[. = '03:　三重県桑名市']",
    "//option[. = '04:　滋賀県戸建て']",
    "//option[. = '05:　滋賀土地']",
    "//option[. = '06:　京都市内１棟']"
]

# 動作テスト用ドロップダウンリスト
# sd2 = [
#     "//option[. = '01:■三重四日市　外全']",
#     "//option[. = '02:■滋賀１棟']",
#     "//option[. = '03:　三重県桑名市']"]

# ドロップダウンリスト指定
selects_dropdown = sd1

# =================================================================
# ログインページ用
def scrowd_login():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(rains_top_url)
    time.sleep(5)
    # ID入力
    driver.find_element(By.ID, "__BVID__13").click()
    time.sleep(0.3)
    driver.find_element(By.ID, "__BVID__13").send_keys(rains_id)
    time.sleep(0.3)
    # PASSWORD入力
    driver.find_element(By.ID, "__BVID__16").click()
    time.sleep(0.3)
    driver.find_element(By.ID, "__BVID__16").send_keys(rains_passwd)
    time.sleep(0.3)
    # 「ガイドラインを尊守します」チェックボックスクリック
    driver.find_element(By.CSS_SELECTOR,
                        ".b-custom-control-lg > .custom-control-label").click()
    time.sleep(0.3)
    # ログインボタン
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(5)

# =================================================================
# 本ページ処理用
def mainpage_scrowl(select_page_one):
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # 以下メインページ=================================================================

    # 売買物件検索
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div['
                                 '1]/button').click()
    time.sleep(4)
    # 「検索条件を表示」クリック
    driver.find_element(By.CSS_SELECTOR,"span.align-middle").click()
    time.sleep(0.2)
    # 「保存した検索条件の選択」クリック
    dropdown = driver.find_element(By.CSS_SELECTOR,'select.p-selectbox-input.custom-select')
    time.sleep(0.2)
    # セレクトボックス内の保存条件をクリック
    dropdown.find_element(By.XPATH, select_page_one).click()
    time.sleep(0.1)
    # 「読込」ボタンクリック
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/'
                                  'div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button').click()
    time.sleep(1.5)
    # ポップアップメニュー　クリック
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/footer/button').click()
    time.sleep(0.5)
    # 下部「検索」ボタンクリック
    driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.p-frame-footer > div > div > div "
                                         "> div > div:nth-child(4) > button").click()
    time.sleep(3)

    # ============================================================
    # 記録用要素抽出

    # 検索ページ項目
    pagename = select_page_one.split(':')[-1].replace("']","")

    # 新着データ取得
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    # 物件番号
    bukken_nums = driver.find_elements(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div['
                                               '2]/div/div/div[2]/div[2]/div/div[4]')
    # 物件種目
    bukken_object_typies = driver.find_elements(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div['
                                                        '2]/div/div/div[2]/div[2]/div/div[5]')
    # 価格
    bukken_plicies = driver.find_elements(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div['
                                                  '2]/div/div/div[2]/div[2]/div/div[9]')


    for i, num in enumerate(bukken_nums):
        # 物件データとしてまとめる
        bukken_data = [num.text, pagename.replace("\u3000",""),
                       bukken_object_typies[i].text, bukken_plicies[i].text]
        # 物件データをCSVへ記録
        with open('new_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(bukken_data)


# =================================================================
# ファイルの増減を抽出
def sabun_select(new, last):
    # ファイル差分抽出
    file1 = open(last) #  前回のリスト
    file2 = open(new) # 今回のリスト
    diff = difflib.Differ()
    output_diff = diff.compare(file1.readlines(), file2.readlines())

    # 差分の結果を抽出
    to_message = []
    for data in output_diff:
        # リストの増分のみ抽出
        if data[0:1] in ['+']:
            # print(data.replace('+', '').replace('"', ''))
            to_message.append(data.replace('+', '').replace('"', '').replace('\n', ''))

    file1.close()
    file2.close()

    return to_message


def write_a(bunsyou_text, file_name):
    with open(file_name, "a", encoding="utf-8_sig") as bun:
        bun.write(bunsyou_text)


# =================================================================

def rains_function():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    send_file = 'data3/send_record.txt'

    # 接続可能時間帯の判断
    dt = datetime.datetime.today()
    print('只今の時間：{}時'.format(dt.hour))
    if 7 <= int(dt.hour) <= 23:
        # 前回のファイルを旧ファイルに変更
        if os.path.isfile('new_data.csv'):
            os.rename('new_data.csv', 'last_data.csv')
        # ログインページオープン
        # scrowd_login()
        # 本ページ処理
        for name in selects_dropdown:
            scrowd_login()
            print('RAINS・カテゴリ『{}』開始'
                  .format(name.split(':')[-1].replace("']", "")
                          .replace(' ', '')))
            mainpage_scrowl(name)
        driver.close()

        file_new = 'new_data.csv'
        file_last = 'last_data.csv'
        # 差分抽出
        to_message = sabun_select(file_new, file_last)

        for ms in to_message:
            msg = "RAINS物件 {}".format(ms.replace(',', '  ', 3)) + '\n'
            print(msg)

            write_a(msg, send_file)

        # 今回のファイルを旧ファイルに変更
        os.remove('last_data.csv')

    # サイト時間外についての処理
    else:
        print('WEB受付時間外により処理をスキップ')
        pass




rains_function()





# ==================================================================================================
# ==================================================================================================


# 送信==============================================================================================

adfile = "address.txt"

def read_text(file):
    with open(file,"r",encoding="utf-8") as tx:
        text = tx.readline()
    return str(text)

to_address = read_text(adfile)


# 新着があれば送信
print("LINE,Email メッセージ送信")


# Emails
import smtplib, ssl
from email.mime.text import MIMEText

# Gmail設定
my_account = 'tartnesssectional6@gmail.com'
my_password = 'bnF8D2JxEjrUZh'

def send_gmail(msg):
    """
    引数msgをGmailで送信
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
    # ログ出力
    server.set_debuglevel(0)
    # ログインしてメール送信
    server.login(my_account, my_password)
    server.send_message(msg)

def make_mime(mail_to, subject, body):
    """
    引数をMIME形式に変換
    """
    msg = MIMEText(body, 'plain') #メッセージ本文
    msg['Subject'] = subject #件名
    msg['To'] = mail_to #宛先
    msg['From'] = my_account #送信元
    return msg

def send_my_message(msg):
    """
    メイン処理
    """
    # MIME形式に変換
    # 送信したい宛先を指定
    msg = make_mime(
        mail_to=to_address,
        subject='不動産最新情報',
        body= msg)
    # gmailに送信
    send_gmail(msg)



# 送信部分
    # send_my_message()
if os.path.isfile(send_file):
    f = open(send_file, "r", encoding="utf-8")
    mail_msgs = str(f.read())
    print(mail_msgs)
    f.close()
    send_my_message(mail_msgs)

# =================================================================================================

# LINE


tkfile = "talken.txt"
talken_id = read_text(tkfile)

def line_send(l_str):
    import requests

    url = "https://notify-api.line.me/api/notify"
    access_token = talken_id
    # access_token = "uA3Ycd7MdjNMVCcWZDWWqNZfJhcdXSmQ9alzY1VLxHp"
    headers = {
        'Authorization': 'Bearer ' + access_token}
    message = l_str
    payload = {'message': message}
    r = requests.post(url, headers=headers,
                      params=payload, )

if os.path.isfile(send_file):
    f = open(send_file, "r",encoding="utf-8")
    line_msgs = f.read()
    print(line_msgs)
    f.close()
    line_send(line_msgs)

if os.path.isfile(send_file):
    os.remove(send_file)
if os.path.isfile("data3/line_msg.txt"):
    os.remove("data3/line_msg.txt")
if os.path.isfile("data3/msg.txt"):
    os.remove("data3/msg.txt")

# 送信終了==========================================================================================




