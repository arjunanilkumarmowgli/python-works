def palindrom(n):

    n1=n

    rev=0

    i=0

    while(i<n):
            

            rem=n%10

            rev=rev*10+rem

            n=n//10


    if n1==rev:

            print("the number is a palindrome")