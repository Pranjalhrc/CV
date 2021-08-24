def prime():
    n=eval(input('enter the number='))
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,'is  a composite no.')
            break
        else :
            print(n,'is a prime no.')
            break
    if n==0:
        print('0 is a prime number')
    elif n==1:
        print('1 is not a primr number nor composite number')
            
k=int(input('No of times you want to check the number='))
for i in range(1,k+1):
    prime()
