#reversing an array without a built in method

#we can do this by manipulating our range function to step in reverse order
def reverse_list(list):
    rev_list = []
#we must know how range works, meaning, our 3 parameters explain the start, end, and step
#we need to start at the last indice position so i can do this by setting our start point to -1
    for i in range(len(list)-1, -1,-1):
        #print(i)
        rev_list.append(list[i])
    return rev_list
print('after reversing',reverse_list([1,2,3,4,5,6,7,8,100]))

