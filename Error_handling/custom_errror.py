def review(rating):

    if rating<0:
        raise Exception("too low")
    else:
        print("done!")

try:
  review(-2)
except Exception as e:
    print(e)

print("vokey")
print("hi")