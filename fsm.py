from transitions.extensions import GraphMachine

from utils import send_text_message
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import re
import datetime
#import urllib
base_url = "https://www.ptt.cc/bbs/Gamesale/index.html"
req = Request('https://www.ptt.cc/bbs/Gamesale/index.html',headers={'User-Agent':'Monzilla/5.0'})
html = urlopen(req).read().decode('utf-8')
game = 'x'
vendor_flag = 0 #0 = PS4 1 = NS
sell_flag = 0 # 1= sell
print(html)
today = datetime.datetime.now()
date = str(today.month) + "/" + str(today.day)
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_instruction(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hello'
            #return True
        return False
    def is_going_to_statePS(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == 'ps4':
                global vendor_flag
                vendor_flag = 0
                return True
            #return text.lower() == 'ps4'
        return False
    def is_going_to_stateNS(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == 'ns':
                global vendor_flag
                vendor_flag = 1
                return True
            #return text.lower() == 'ns'
        return False
    def is_going_to_stateXB(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == 'xbox':
                global vendor_flag
                vendor_flag = 3
                return True
            #return text.lower() == 'ns'
        return False    
    def is_going_to_statePSbuy(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag 
            global sell_flag
            if vendor_flag == 0:
                if text == '徵求':
                    sell_flag = 0
                    return True
            #return text == '徵'
        return False    
    def is_going_to_stateNSbuy(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag 
            global sell_flag
            if vendor_flag == 1:
                if text == '徵求':
                    sell_flag = 0
                    return True
            #return text == '徵'
        return False
    
    def is_going_to_stateNSsell(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag
            global sell_flag
            if vendor_flag == 1:
                if text  == '出售':
                    sell_flag = 1
                    return True
            #return text == '出售'
        return False
    def is_going_to_statePSsell(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag
            global sell_flag
            if vendor_flag == 0:
                if text  == '出售':
                    sell_flag = 1
                    return True
            #return text == '出售'
        return False
    def is_going_to_stateXBbuy(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag 
            global sell_flag
            if vendor_flag == 3:
                if text == '徵求':
                    sell_flag = 0
                    return True
            #return text == '徵'
        return False
    
    def is_going_to_stateXBsell(self, event):
        if event.get("message"):
            text = event['message']['text']
            global vendor_flag
            global sell_flag
            if vendor_flag == 3:
                if text  == '出售':
                    sell_flag = 1
                    return True
            #return text == '出售'
        return False
    def is_going_to_stateNSbuyname(self, event):
        global vendor_flag
        global sell_flag
        if vendor_flag == 1:
            if sell_flag == 0:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False
    def is_going_to_statePSbuyname(self, event):
        global vendor_flag
        global sell_flag
        if vendor_flag == 0:
            if sell_flag == 0:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False
    def is_going_to_stateXBbuyname(self, event):
        global vendor_flag
        global sell_flag
        if vendor_flag == 3:
            if sell_flag == 0:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False
    def is_going_to_stateNSsellname(self, event):
        global vendor_flag
        global sell_flag
        #modify
        if vendor_flag == 1:
            if sell_flag == 1:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False
    def is_going_to_stateXBsellname(self, event):
        global vendor_flag
        global sell_flag
        #modify
        if vendor_flag == 3:
            if sell_flag == 1:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False
    def is_going_to_statePSsellname(self, event):
        global vendor_flag
        global sell_flag
        #modify
        if vendor_flag == 0:
            if sell_flag == 1:
                if event.get("message"):
                    global game
                    game = event['message']['text']
                    print(game)
                    return True
        return False



    def on_enter_instruction(self, event):
        print("I'm entering instruction")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你好!!!我是豬瘟寶寶<3 我可以幫你找到一天內的遊戲價錢資訊<3")  
        responese = send_text_message(sender_id, "請先選擇遊戲主機(NS/PS4/XBOX)")  
        #responese = send_text_message(sender_id, base_url)  
        #self.go_back()
    def on_enter_stateNS(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇要查詢出售價格或是徵求價格")
    def on_enter_statePS(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇要查詢出售價格或是徵求價格")
    def on_enter_stateXB(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇要查詢出售價格或是徵求價格")
    def on_enter_stateNSsell(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")

    def on_enter_stateNSbuy(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")
        #self.go_back()   
    def on_enter_stateXBsell(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")

    def on_enter_stateXBbuy(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")    
    def on_enter_statePSbuy(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")
        #self.go_back() 
    def on_enter_statePSsell(self, event):
        #print("I'm entering state2")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入遊戲名稱")
        #self.go_back() 
    def on_enter_stateNSsellname(self, event):

        out_flag = 0
        sender_id = event['sender']['id']
        global game
        #while
        global date
        print(date)
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:  
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                if d.find ('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'N':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"售") != -1:
                            print("done")
                            print(game)
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"售 價")
                                if start == -1:
                                    start = merchant.find(u"售 　 價")
                                if start == -1:
                                    start = merchant.find(u"【售")
                                    
                                end3 = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"販售者填寫")
                                end2 = merchant.find(u"交易方式")

                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end3 != -1: 
                                        send_text_message(sender_id,merchant[start-2:end3-2])
                                    #print() 
                                    else:
                                        if end != -1:
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
            #else:
                #date_flag=0                            
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'N':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"售") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"售 價")
                                    if start == -1:
                                        start = merchant.find(u"售 　 價")
                                    if start == -1:
                                        start = merchant.find(u"【售")
                                    end3 = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"販售者填寫")
                                    end2 = merchant.find(u"交易方式")

                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end3 != -1: 
                                            send_text_message(sender_id,merchant[start-2:end3-2])
                                        #print() 
                                        else:
                                            if end != -1:
                                                send_text_message(sender_id,merchant[start-2:end-2])
                                            else:
                                                send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")

        self.go_back()
        
    def on_enter_stateNSbuyname(self, event):
        
        out_flag = 0
        sender_id = event['sender']['id']
        global date
        #while
        global game
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:   
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'N':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"徵") != -1:
                            print("done")
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"徵求者填寫")
                                end2 = merchant.find(u"交易方式")
                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end != -1: 
                                        send_text_message(sender_id,merchant[start-2:end-2])
                                    #print() 
                                    else:
                                        send_text_message(sender_id,merchant[start-2:end2-2])
                          
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'N':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"徵") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"徵求者填寫")
                                    end2 = merchant.find(u"交易方式")
                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end != -1: 
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")
        self.go_back() 
    def on_enter_stateXBsellname(self, event):
        out_flag = 0
        sender_id = event['sender']['id']
        global game
        #while
        global date
        print(date)
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:  
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                if d.find ('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'X':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"售") != -1:
                            print("done")
                            print(game)
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"售 價")
                                if start == -1:
                                    start = merchant.find(u"售 　 價")
                                if start == -1:
                                    start = merchant.find(u"【售")
                                    
                                end3 = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"販售者填寫")
                                end2 = merchant.find(u"交易方式")

                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end3 != -1: 
                                        send_text_message(sender_id,merchant[start-2:end3-2])
                                    #print() 
                                    else:
                                        if end != -1:
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
            #else:
                #date_flag=0                            
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'X':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"售") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"售 價")
                                    if start == -1:
                                        start = merchant.find(u"售 　 價")
                                    if start == -1:
                                        start = merchant.find(u"【售")
                                    end3 = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"販售者填寫")
                                    end2 = merchant.find(u"交易方式")

                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end3 != -1: 
                                            send_text_message(sender_id,merchant[start-2:end3-2])
                                        #print() 
                                        else:
                                            if end != -1:
                                                send_text_message(sender_id,merchant[start-2:end-2])
                                            else:
                                                send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")

        self.go_back()
    def on_enter_stateXBbuyname(self, event):
        global game
        out_flag = 0
        sender_id = event['sender']['id']
        global date
        #while
        
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:   
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'X':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"徵") != -1:
                            print("done")
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"徵求者填寫")
                                end2 = merchant.find(u"交易方式")
                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end != -1: 
                                        send_text_message(sender_id,merchant[start-2:end-2])
                                    #print() 
                                    else:
                                        send_text_message(sender_id,merchant[start-2:end2-2])
            
                        #modify: else
            #else:
                #date_flag =0            
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'X':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"徵") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"徵求者填寫")
                                    end2 = merchant.find(u"交易方式")
                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end != -1: 
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")
        self.go_back() 
    def on_enter_statePSsellname(self, event):
        out_flag = 0
        sender_id = event['sender']['id']
        global game
        #while
        global date
        print(date)
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:  
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                if d.find ('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'P':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"售") != -1:
                            print("done")
                            print(game)
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"售 價")
                                if start == -1:
                                    start = merchant.find(u"售 　 價")
                                if start == -1:
                                    start = merchant.find(u"【售")
                                    
                                end3 = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"販售者填寫")
                                end2 = merchant.find(u"交易方式")

                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end3 != -1: 
                                        send_text_message(sender_id,merchant[start-2:end3-2])
                                    #print() 
                                    else:
                                        if end != -1:
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
            #else:
                #date_flag=0                            
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'P':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"售") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"售 價")
                                    if start == -1:
                                        start = merchant.find(u"售 　 價")
                                    if start == -1:
                                        start = merchant.find(u"【售")
                                    end3 = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"販售者填寫")
                                    end2 = merchant.find(u"交易方式")

                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end3 != -1: 
                                            send_text_message(sender_id,merchant[start-2:end3-2])
                                        #print() 
                                        else:
                                            if end != -1:
                                                send_text_message(sender_id,merchant[start-2:end-2])
                                            else:
                                                send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")

        self.go_back()
    def on_enter_statePSbuyname(self, event):
        global game
        out_flag = 0
        sender_id = event['sender']['id']
        global date
        #while
        
        soup = BeautifulSoup(html,'html.parser')
        page_find = BeautifulSoup(html,features='lxml')
        page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
        count_page = 0
        for link in page:
            print(link['href'])
            if count_page == 3:
                url_next = 'https://www.ptt.cc' + link['href']
                #print(html_next)
            count_page = count_page + 1
        #print("HI0")
        #date = "12/19"
        divs = soup.find_all('div','r-ent')
        empty_flag = 0
        date_flag = 0
        print("HI1")
        for d in divs:
            if d.find('div','date').string == date:   
                print("HI2")
                date_flag = 1
                if d.find('a'):
                    href = d.find('a')['href']
                    title = d.find('a').string
                    #print(title[2])
                    print("HI3")
                    if title[1] == 'P':
                        print("HI4")
                        #print("N")
                        #print(title[2])
                        if title.find(u"徵") != -1:
                            print("done")
                            if title.find(game) != -1:
                                empty_flag = 1
                                print("YA")
                                send_text_message(sender_id, title)
                                send_text_message(sender_id,'https://www.ptt.cc' + href)
                                print("GOOD")
                                tmp = 'https://www.ptt.cc' + href
                                req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                merchant = urlopen(req_merchant).read().decode('utf-8')
                                print(merchant)
                                start = merchant.find(u"徵 求 價")
                                end = merchant.find(u"交換物品")
                                end1 = merchant.find(u"徵求者填寫")
                                end2 = merchant.find(u"交易方式")
                                if end1 != -1:
                                    send_text_message(sender_id,merchant[start-2:end1-1])
                                else:
                                    if end != -1: 
                                        send_text_message(sender_id,merchant[start-2:end-2])
                                    #print() 
                                    else:
                                        send_text_message(sender_id,merchant[start-2:end2-2])
            
                        #modify: else
            #else:
                #date_flag =0            
        if date_flag == 0:
            out_flag = 1
        while out_flag == 0:
            req_while = Request(url_next,headers={'User-Agent':'Monzilla/5.0'})
            html_next = urlopen(req_while).read().decode('utf-8')
            soup = BeautifulSoup(html_next,'html.parser')
            page_find = BeautifulSoup(html_next,features='lxml')
            print("NO")
            page = page_find.find_all('a',{'href': re.compile('/bbs/Gamesale/index4*')})
            count_page = 0
            for link in page:
                #print(link['href'])
                if count_page == 3:
                    url_next = 'https://www.ptt.cc' + link['href']
                    print(url_next)
                count_page = count_page + 1

            divs = soup.find_all('div','r-ent')
            #empty_flag = 0
            date_flag = 0
            print("HI1")
            for d in divs:
                print("check date")
                if d.find('div','date').string == date:   
                    print("HI2")
                    date_flag = 1
                    if d.find('a'):
                        href = d.find('a')['href']
                        title = d.find('a').string
                        #print(title[2])
                        print("HI3")
                        if title[1] == 'P':
                            print("HI4")
                            #print("N")
                            #print(title[2])
                            if title.find(u"徵") != -1:
                                print("done")
                                if title.find(game) != -1:
                                    empty_flag = 1
                                    print("YA")
                                    send_text_message(sender_id, title)
                                    send_text_message(sender_id,'https://www.ptt.cc' + href)
                                    print("GOOD")
                                    tmp = 'https://www.ptt.cc' + href
                                    req_merchant = Request(tmp,headers={'User-Agent':'Monzilla/5.0'})
                                    merchant = urlopen(req_merchant).read().decode('utf-8')
                                    print(merchant)
                                    start = merchant.find(u"徵 求 價")
                                    end = merchant.find(u"交換物品")
                                    end1 = merchant.find(u"徵求者填寫")
                                    end2 = merchant.find(u"交易方式")
                                    if end1 != -1:
                                        send_text_message(sender_id,merchant[start-2:end1-1])
                                    else:
                                        if end != -1: 
                                            send_text_message(sender_id,merchant[start-2:end-2])
                                        else:
                                            send_text_message(sender_id,merchant[start-2:end2-2])
                else:
                    date_flag = 0
            if date_flag == 0:
                out_flag = 1
            
        if out_flag ==1:
            if empty_flag == 0:
                send_text_message(sender_id,"not found")
        self.go_back()   
    def on_exit_stateNSbuyname(self):
        print('Leaving state2')
    def on_exit_stateNSsellname(self):
        print('BYE')
    def on_exit_statePSbuyname(self):
        print('BYE')
    def on_exit_statePSsellname(self):
        print('BYE')
    def on_exit_stateXBsellname(self):
        print('BYE')
    def on_exit_stateXBbuyname(self):
        print('BYE')