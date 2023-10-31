# fizzbizz code

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
                    

# palindrome code

def palindrome(pl):
    return pl == pl[::-1]



#panagram code

def panagram(word):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in word.lower():
            return False
        else:
            return True

#freq code

def freq(s):
    d={}
    s=s.lower()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


if __name__ == "__main__":
    n=int(input("Enter a number:"))	
    fizzbizz(n)
    pl=input("Enter the word to check palindrome:")
    print(palindrome(pl))
    word=input("Enter the string to check panagram:")
    print(panagram(word))
    s=input("Enter the word to check frequency:")
    print(freq(s))

