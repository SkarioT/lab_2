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
        rez_list.append(get_ip(i))
        i+=1
    return rez_list

#print("кол-во ВСЕХ IP: ",len(all_ip_on_list()))

#функция возвращает уникальные значения( как для IP(первых слов) так и для браузеров(последних слов))
def uniq(function_name):
    uniq=[]
    for line in function_name:
        if line not in uniq:
            uniq.append(line)
    return uniq

print("кол-во уникальных IP: ",len(uniq(all_ip_on_list())))

#функция получает последнее слово в N cтроке
def last_word_on_line(line_number):
    list_to_str=myfile_lines[line_number]
#полученную строку разделяю на отдельные слова
    split_str=list_to_str.split()
#заношу в переменную длинну строки
    len_str=len(split_str)-1
    #заношу в переменную ПОСЛЕДНЕЕ СЛОВО 
    rez_last_word_in_line=split_str[len_str]
    return rez_last_word_in_line

#функция возвращает лист состоящий из последних слов
def def_last_word_list():
    rez_list_browser_list=list()
    i=0
    while i < count_lines():
        rez_list_browser_list.append(last_word_on_line(i))
        i+=1
    return rez_list_browser_list
# 1 cпособ подсчтета браузеров(конечных слов), используя counter 
def def_counter ():
    from collections import Counter
    cnt = Counter()
    for word in def_last_word_list():
        cnt[word] += 1
    return cnt



print("Печать результато полученых спомощью counter : ",def_counter())
fp2 = open('browser_list.txt','w')
fp2.write(str(def_counter()))
fp2.close()






