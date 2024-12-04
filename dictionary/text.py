words=["hello","hai","hello","this","is","this","is","hello"]
#word freq
word_ferquency={w:words.count(w) for w in words }
print(word_ferquency)

#recursive_word
recursive_words=[k for k,v in word_ferquency.items() if v>1]
print(recursive_words)
#non recursive word
none_recursive_words=[k for k,v in word_ferquency.items() if v==1]
print(none_recursive_words)