number=int(input("Enter The Number:"))
factorial=1
if number==0:
    factorial=1
else:
    for a in range(1,number+1):
       factorial*=a
print(number,"!=",factorial)
  
