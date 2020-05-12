fp=open('1.txt','r')
fp2=open('fp2.txt','w+')

print("содержимое fp(1.txt)",fp.read())
print("содержимое fp2(fp2.txt)",fp2.read())
fp.seek(0)
fp2.seek(0)
fp_1=fp.read()
fp_2=fp2.read()
fp_2=fp_1

print("содержимое fp_2\n",fp_2)


fp2.seek(0)
fp.seek(0)

fp2_list_all_lines=fp.readlines()
fp2_list_one_line=fp2_list_all_lines[0].split() #развибка первой строки на отдлельыне слова
seen =[]
for line in fp2_list_all_lines:
    if line not in seen:
        seen.append(line)
print("содержимое fp2_list после сохронения",seen)
fp2.seek(0)
i=0
while i < len(seen):
    seen_list=seen[i]
    i+=1
    fp2.write(seen_list)

print("содержимое seem : ",len(seen))
print("содержимое seem_list : ",seen_list)
fp.close()
fp2.close()

fp_show=open('fp2.txt')
fp_show_str=fp_show.readline()
print(fp_show_str)