# a,b=map(int,input().split())

# if a*b%2==0:
#   print("Even")
  
# else:
  
#   print("Odd")


s=input()
sum=0
for i in range(len(s)):
  sum+=int(s[i])

print(sum)