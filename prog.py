# fizzbizz

def fizzbizz(n):
    for i in range(1,n+1):
        if i%15 == 0:
            print("fizzbizz")
        else:
            if i%5 == 0:
                print("bizz")
            else:
                if i%3 == 0:
                    print("fizz")
                else:
                    print(i)
n=int(input("Enter the number:"))
fizzbizz(n)




# palindrome


def palindrome(pl):
    return pl == pl[::-1]

pl=input("Enter the word: ")
print(palindrome(pl))




# panagram

def panagram(word):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in word.lower():
            return False
        else:
            return True
word=str(input("enter the string:"))

if panagram(word)== True:
    print("yes")
else:
    print("no")
    
panagram(word)



# freq


def freq(s):
    d={}
    s=s.lower()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
s=str(input("Enter the word:"))
print(freq(s))

