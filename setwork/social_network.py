users=["rahul","rohit","kohil","rishab","sanju","pandya","siraj"]
rahul_followers=["rohit","kohil","rishab","rahul"]
sanju_followers=["sanju","rohit","kohil"]
#follower_suggestion["sanju","pandya","siraj"]

rahul_follow_suggestion=set(users).difference(set(rahul_followers))
#print(rahul_follow_suggestion)
#mutual_friend=[]
mutual_friends=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_friends)