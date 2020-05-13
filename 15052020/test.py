last_word_list=('1','a','2','b','b','b','b','c')
uniq_last_word_list=('1','a','b','c')
uniq=()
len_l_w=len(last_word_list)
len_q_l_w=len(uniq_last_word_list)
for last_word_list in uniq_last_word_list:
    if last_word_list in uniq:
        uniq.count(last_word_list)
print(uniq)


words = "слово1 слово2 слово1 слово3 слово2 Вася слово1"
word_list = words.split()
  
from collections import defaultdict
word_count_dict = defaultdict(int)
  
for word in word_list:
    print(word, word_count_dict[word])
    word_count_dict[word] += 1
print(word_count_dict)