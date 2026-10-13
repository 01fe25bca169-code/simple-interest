def simple_interest(principal,interest,time):
    return(principal*interest*time)/100

if __name__=="__main__":
    p=int(input("Enter principal amount"))
    i=int(input("Enter principal"))
    t=int(input("Enter time in moths"))

    print("Simple interest is:",simple_interest(p,i,t))