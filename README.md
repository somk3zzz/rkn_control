# Контроль качества блокировки сайтов 
Для выгрузки файлов взял за основу ```extfilter_maker.pl```
Правим под себя строчку в ```extfilter_maker.conf```
```
[DB]
### адрес сервера mysql
host = 'ip_address_db'
### имя пользователя
user = 'zapret'
### пароль
password = '123321'
### имя БД
name = 'rkn'
```
# Эксплуатация 
```sh
pip install -r req.txt
```
#
Запускается так : ``` python3 rkn_check.py -t 50 -f contrib/domains -m 'TTK :: Доступ к ресурсу ограничен' -o test_file.txt &```
#
```-f``` - путь к файлу
#
```-t``` - количество потоков
#
```-m``` - маркер. В качестве маркера входит title заглушки
#
```-o test_file.txt``` - выходной файл со списко сайтов не прошедших проверку
#

Для более быстрой проверки я использовал количество потоков 100. Прилизительно от 186354 , это 3732 записей на поток
