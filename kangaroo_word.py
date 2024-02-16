source_word="chicken"
target_word="hen"
is_kangaroo_word=True

source_word_lst=[]
target_word_lst=[]
for ch in source_word:
    source_word_lst.append(ch)
for ch in target_word:
    if source_word_lst.count(ch)>0:
        source_word_lst.remove(ch)
    else:
        is_kangaroo_word=False
        break
print(is_kangaroo_word)
 