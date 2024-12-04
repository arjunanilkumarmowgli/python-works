def poll(age):
    assert age>18,"invalid age"
    print("voted")
def review(rating):
    assert rating>0,"too low"
    assert rating<10,"too high"
    print("rating done")