def countword(): 
    fileName=input("enter your file name")
    numberofWords=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print(numberofWords)
countword()