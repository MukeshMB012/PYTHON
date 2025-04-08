#Exercise 3 solution
#Kon Banega Crorepati
questions= [["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],
            ["What is the capital of India: ", "1. Delhi ", "2.Mumbai", "3.Kolkata", "4.Benguluru"],]

level= [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0, len(questions)):
   
    print(f"Question for prize money {level[i]} is in front of your screen")
    print(questions[i])
    ans= int(input("Enter your option(1-4) or enter 0 to quit: "))
    if(ans==0):
        if(i<4):
            money = 0
            
        elif(4<=i<9):
            money=10000
        elif(9<=i<14):
            money= 320000
        else:
            money=10000000 
        


    elif(ans==1):
        print(f"Correct answer, you have won Rupees{level[i]}")

    else:
        print(f"Wrong answer, Better luck next time, but you have won Rupees{} ")    



        if(i<4):
            money = 0
        elif(4<=i<9):
            money=10000
        elif(9<=i<14):
            money= 320000
        else:
            money=10000000 
            print(f"Your game has been quit as per your request and you have won Rupees{} ")