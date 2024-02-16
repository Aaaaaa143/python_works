f_news=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\latest_news.txt")
f_stop=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\stopword.txt")

stop_words={line.strip("\n") for line in f_stop}
news_words=set()

for line in f_news:
    words=line.split()
    for w in words:
        news_words.add(w)                            

print(news_words.difference(stop_words))


