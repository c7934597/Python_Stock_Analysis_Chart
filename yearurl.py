def twodigit(n):  #將數值轉為二位數字串
    if(n < 10):
        retstr = '0' + str(n)
    else:
        retstr = str(n)
    return retstr

urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017' #網址前半
urltail = '01&stockNo=2317&_=1540489538302'
for i in range(1, 13): #取1到12數字
    url_twse = urlbase + twodigit(i) + urltail #組合網址
    print(url_twse)
    #讀取JSON資料並寫入CSV檔程式碼