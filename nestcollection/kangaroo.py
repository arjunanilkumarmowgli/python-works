source="CHICKEN"

target="HEN"

charcarte_count={ch:source.count(ch) for ch in source}
is_kangroo=True

for ch in target:
    if ch in target and charcarte_count.get(ch)>0:
        charcarte_count[ch]-=1
    else:
        is_kangroo=False
        break
print(is_kangroo)