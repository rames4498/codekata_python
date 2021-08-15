
a = 0
spec =  "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spec = list(spec)
#print(spec)

def Login():
    m  =  input("Enter your username..")
    n  = input("Enter your password..")
    
    for line in open("dummy.txt", "r").readlines():
        flag  = True
        data  = line.split()
        if m  == data[0] and n == data[1]:
            print("You are successfully logged into your account")
            break
        else:
            flag  =  False
            
    if flag == False:
        print("Your credentials are invalid")



def Register():

    def password(n):
        k,c,d,j = 0,0,0,0
        for b in n:
            if b.isupper():
                k = k+1
            if b.islower():
                c = c+1
            if b.isdigit():
                d = d+1
            if (k and c and d)>0:
                break
        
    
        for s in spec:
            if s in n:
                j = j+1
        if (5<len(n)<15) and ((k and c and d and j) > 0):
            print("Valid password")
            file  =  open("dummy.txt", "a")
            file.write(m)
            file.write(" ")
            file.write(n)
            file.write("\n")
            file.close()
        else:
            print("Invalid password")

    def username(m):
        
       for h in m:
           if h == "@":
               r = m.index(h)
               for l in range(r,len(m)):
                    if m[l] == ".":
                         print("Valid emailid")
                         password(n)
                         break
                    else:
                         global a
                         a = a+1
                         if a == (len(m)-r):
                              print("Invalid emailid")
    m = input("please provide valid mailid: ")
    n = input("please provide valid mailpwd: ")

    username(m)
    
   
print("Welcome....")
print("Choose the option which suits you..")
print("IF YOU ARE A NEW USER Enter 1 to Register")
print("existing user ?, then Enter 2 to Login")

userInput  =  input("Enter your choice..")

if userInput == "1":
    Register()
else:
    Login()
    





     
     
                              


    
