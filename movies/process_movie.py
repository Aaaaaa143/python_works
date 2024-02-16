from json import load
path="C:\\Users\\DHANUJA\\Desktop\\python_works\\movies\\moves.json"
with open(path) as f:
    data=load(f)

print(len(data))

# print titles

print([st.get("Title") for st in data])

# print all director names
print({st.get("Director") for st in data if st.get("Director")!="N/A"})

# or 

all_directors={st.get("Director") for st in data }
all_directors.discard("N/A")
print(all_directors)


# highest IMDB RATING
filtered_rating=[st for st in data if st.get("imdbRating")!="N/A"]
top_movie=max(filtered_rating,key=lambda m:float(m.get("imdbRating")))
print(top_movie.get("Title"))


# print gerners
all_genre=set()
for m in data:
    for gn in m.get("Genre").split():
        all_genre.add(gn.rstrip(","))



# action movies

for mv in data:
    if m.get("Genre").count("Action")>0:
        print(mv.get("Title"))


# movies released before 2014



for mv in data:
    r_date=mv.get("Released")
    year=r_date.split(" ")[-1]
    if year.isdigit():
        if int(year)<2014:
            print(mv.get("Title"))

            