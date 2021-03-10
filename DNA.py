import time

Turns = int(input("How many strands do you want?\n>>>"))

c="#"
s=" "

def bids(a,b,c="",d=""):
    return(a+b+c+d)

def strand():
    print(bids(s*19,c))
    print(bids(s*17,c*4))
    print(bids(s*16,c*6))
    print(bids(s*14,c*2,s*6,c*2))
    print(bids(s*12,c*14))
    print(bids(s*11,c*2,s*12,c*2))
    print(bids(s*11,c*16))
    print(bids(s*12,c*2,s*10,c*2))
    print(bids(s*14,c*10))
    print(bids(s*16,c*2,s*2,c*2))
    print(bids(s*17,c*4))
    print(bids(s*18,c*2))

for i in range(Turns):    
     time.sleep(0.3)
     strand()
print(" ")