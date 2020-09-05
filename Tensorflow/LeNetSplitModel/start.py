import os
print("Please Enter Your Choice\n")
while True:
    print("================================")
    print("1 Training (using MNIST datasets) \n")
    print("2 Guess the number in 'text.png' \n")
    print("3 Quit ")
    opt = int(input())
    if opt== 1 :
        os.system("python train.py")
    elif opt== 2 :
        os.system("python classify.py")
    else :
        exit()

