import datetime
import pytz
import calendar
import fp_date

cdt = datetime.datetime.now().date()
str_cdt=cdt.strftime("%d.%m")
print(str_cdt)
#заношу в виде строки
date_to_str=str(cdt)
#меняю в строке  - на _
clear_str=date_to_str.replace('-',' ')
#разбиваю на отдельные слова
slice_str=clear_str.split()
#cоздаю новую дату +2 дня к ней
creat_date=datetime.datetime(int(slice_str[0]),int(slice_str[1]),int(slice_str[2])+2)
print("созданная дата 17.00 : ",creat_date)

# через dimedelta
td=datetime.timedelta(minutes=3)
print("отнимаем от созаднной даты 3 минуты(td) : ",creat_date-td)

#из строки делаем время
strptime=datetime.datetime.strptime('1803191327','%d%m%y%H%M')
print("из строки далем время",strptime)

#____
import sys
print(sys.path)
print(calendar.__file__)

print(fp_date.count_lines())
print(fp_date.last_word_on_line(6666))
print(fp_date.def_counter(fp_date.get_ip(1)))