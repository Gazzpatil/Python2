#non repeating character in a string


#take user input

string = "gazzpatil"
for i in string:
    #initializing a count variable
    count=0
    for j in  string:
        #check for repeated characters
        if i==j:
            count+=1
        #if character is found more than one time
        # break the loop
        if count>1:
            break
if count==1:
    print(i,end="")    