s = input("Enter a word :")
m = len(s)
st = 0
for i in range(len(s)//2):
    if s[i]!=s[m-i-1]:
        st  = 1
        break
    
if st:
    print(s, "is not palindromic string")
else:
    print(s, "is palindromic string")

