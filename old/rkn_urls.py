# -*- coding: UTF-8 -*-
import sys
import requests
import threading
import argparse
from datetime import datetime, timedelta
from lxml.html import fromstring
from lxml.etree import ParseError
from lxml.etree import ParserError

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-t', '--thread')
    parser.add_argument ('-f', '--file', default='contrib/urls')
    return parser

def funcname(s,n):
    not_blockd = []
    error_404_list = 0
    error_403_list = 0
    count_blocked = 0
    count_all = 0
    conn_error = 0
    for i, x in enumerate(open(items.file)):
        if i >= int(s) and i <= int(n):
            try:
                url = str(x)[:-1]
                response = requests.head('http://'+url, timeout=3)
                #response = requests.head(url, timeout=3)
                count_all = int(count_all) + 1
                if response.status_code == 301:
                    count_blocked = int(count_blocked) + 1
                elif response.status_code == 404:
                    error_404_list = int(error_404_list) + 1
                elif response.status_code == 403:
                    error_403_list = int(error_403_list) + 1
                else:
                    try:
                        r = requests.get('http://'+url, timeout=2.5)
                        tree = fromstring(r.content)
                        text = tree.findtext('.//title')
                        tag = 'TTK :: Доступ к ресурсу ограничен'
                        if text != tag:
                            not_blockd.append(x)
                    except (ParserError, ParseError):
                        not_blockd.append(x)
            except requests.exceptions.ConnectionError:
                count_all = int(count_all) + 1
                conn_error = int(conn_error) + 1
            except requests.exceptions.Timeout:
                count_all = int(count_all) + 1
                conn_error = int(conn_error) + 1
            except requests.exceptions.RequestException:
                count_all = int(count_all) + 1
                conn_error = int(conn_error) + 1
    print('********************************************************************')
    print(threading.currentThread().getName() + ': thread end...')
    print('Проверено записей: '+str(count_all))
    #print('C ошибкой 404 : '+str(error_404_list)+' | с ошибкой подключения : '+str(conn_error)+' | с ошибкой 403 : '+str(error_403_list))
    print('Не прошли проверку : ',len(not_blockd))
    for item in not_blockd:
        out_f.write(item)


if __name__ == '__main__':
    #Аргумент '-t', '--thread'
    parser = createParser()
    items = parser.parse_args(sys.argv[1:])

    count = len(open(items.file).readlines())
    print('Процесс запусщен : ',datetime.strptime(str(datetime.now())[:-7], "%Y-%m-%d %H:%M:%S"))
    print('Записей найдено : ',count)
    drop = int(items.thread)
    ln = 0
    x = int(count/int(drop))+1
    out_f = open('nb_test','w+')
    for i in range(int(drop)):
        my_thread = threading.Thread(target=funcname, name='Thread_'+str(i+1), args=(int(ln),int(ln+x+1)))
        my_thread.start()
        print('Thread '+str(i+1) + ' : thread start...')
        ln = int(ln+x+1)
    my_thread.join()

