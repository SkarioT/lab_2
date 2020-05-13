def gener():
    counter = 1
    while counter<20:
        #проверка на остаток от деления
        if (counter%3) == 0:
            print("Василий")
            #увеличиваем что бы не дублировалось следующее значение
            counter+=1
        yield counter
        counter += 1

for i in gener():
    print(i)


print("Use gener v2\n",'-'*40)
# v2
def gener2():
    counter = 1
    while counter<20:
        #проверка на остаток от деления
        if (counter%3) == 0:
            yield 'Василий'
            counter+=1
            #увеличиваем что бы не дублировалось следующее значение
        yield counter
        counter += 1



for i in gener2():
    print(i)