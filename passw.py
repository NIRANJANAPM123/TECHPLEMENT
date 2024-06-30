import string
length=int(input("Enter the length of password"))
upper=input("do you need uppercase letter").lower()
lower=input("do you need lowercase letter").lower()
digit=input("do you need digit").lower()
sym=input("do you need symbols").lower()

index=length

chr=''
     
l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l3=['1','2','3','4','5','6','7','8','9','0']
l4=['*','/','-','+','<','>','%','#','@','!','^','&','(',')','{','}','|']
while(len(chr)<length):
         if upper=="yes":
             index=(index+length)%len(l1)
             chr+=l1[index]  
             index+=1
             
         if lower=="yes":
             index=(index+length)%len(l2)
             chr+=l2[index] 
             index+=1
             
         if digit=="yes":
              index=(index+length)%len(l3)
              chr+=l3[index]    
              index+=1
              
         if sym=="yes":
             index=(index+length)%len(l4)
             chr+=l4[index]   
             index+=1
             

         elif upper==lower==digit==sym=="no":
             print("not possible")

print("password",chr[0:length])  
                 
        

    

    
        
    



