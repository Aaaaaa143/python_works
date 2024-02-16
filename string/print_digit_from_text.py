text=" i have one car 2 bikes and 3 cars"
words=text.split(" ")
for w in words:
    if w.isdigit():
        print(w)
