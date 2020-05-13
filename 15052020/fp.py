# парсим файл логов:
# 1) подсчёт кол-во строк 
# 2) подсчёт уникальных IP
# 3) подсчёт браузеров(cколько запросов от Safari и от Firefox)

with open('1.txt','r') as fp:
    myfile_lines=fp.readlines()
    fp.seek(0)
    myfile_read=fp.read()

#функция полсчтёта кол-во строк
def count_lines():
    coun_str_in_file=(myfile_read.count('\n'))+1 #+1 т.к. в текущем файле последняя строка не имеет перенос
    return coun_str_in_file

print("кол-во строк : ",count_lines())

#фукция для получения IP из N строки. Мали ли, пригодиться посмотреть IP в конкретной строке
def get_ip(number_line):
    #берём n строку из листа и заносим в отдельную строку
    list_to_str=myfile_lines[int(number_line)]
    #полученную строку разделяю на отдельный слова
    split_str=list_to_str.split()
    #заношу в переменную 1 слово( по логам 1 слово всегда == IP)
    rez_ip_in_line=split_str[0]
    return rez_ip_in_line

#функция получает все IP присутствующие в файле.
def all_ip_on_list():
    rez_list=list()
    i=0
    while i < count_lines():
        #rez=get_ip(i)
        rez_list.append(get_ip(i))
        i+=1
    return rez_list

print("кол-во ВСЕХ уникальных IP: ",len(all_ip_on_list()))


uniq_ip=[]
for line in all_ip_on_list():
    if line not in uniq_ip:
        uniq_ip.append(line)

print("кол-во уникальных IP: ",len(uniq_ip))






