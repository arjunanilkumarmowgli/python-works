text="ABABBCCDDEEH"
#character_frequeny become more than 1 or more and  count in dispaly on output 
character_frequeny={ch:text.count(ch)for ch in text}
print(character_frequeny)
for k,v in character_frequeny.items():
    if v==1:
       print(k)

non_recuresive_character=[k for k,v in character_frequeny.items() if v==1]
print(non_recuresive_character)
