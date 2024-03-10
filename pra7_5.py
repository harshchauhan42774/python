d={'gujarat':'ghandhinagar','up':'lakhnav','mp':'bhopal','maharastra':'mumbai','panjab':'chandigdh','hariyana':'chandigdh','telengana':'hydrabad','tamil nadu':'chennai','kerela':'trivendru','bihar':'patna','wb':'kolkata'}
st=input("Enter state:")
while(True):
    cap=input("Enter capital of " + st +":")
    if(d[st]==cap):
        print("correct..")
        break
    
    else:
        print("incorrect try one more time")

