num=int(input("Enter any number !"));
for i in range(1, num):
    if(num%i==0):
        print(num,"="+"is not a prime number");
        break
        
    else:
        print(num,"=" + "is a prime number");
              
    
