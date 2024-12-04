from json import load
f=open("C:\\pythonworks\\dataset\\books.json")
data=load(f)
# for book in data:
    # print(book)

all_titles=[book.get("title") for book in data]
# print(all_titles)

#book with page<250
page_filter=[book.get("title")for book in data if book.get("pages")<250]
#print(page_filter)

#print all genres
all_genres=[book.get("genre")for book in data ]

#print(set(all_geners))
genre_count={genre:all_genres.count(genre) for genre in all_genres}
#print(genre_count)


# print costly book
costly_book=max(data,key=lambda d:d.get("price"))
#print(costly_book)

#author with more than one book 
all_author=[book.get("author") for book in data]

author_count={auth:all_author.count(auth) for  auth in all_author}
print([ k for k,v in author_count.item])

