# Given an array of ints, every int appears twice except for one, return the one number that only appears once 
# we can store all items we see in an empty dictionary, and if we see it again we can delete it... So if we se it twice, it gets deleted, 
# if only once then we'll still have it


def single_num(nums):
    count = {}

    for n in nums:
        if n not in count:          #if the num is not in count, set the count equal to something, but it doesnt really matter
            count[n]= 1             #it does not matter about the value we give it because we are only looking to store it and then access the key!
        else:
            del count[n]            #else, if we have seen it already then delete it

    return list(count.keys())[0]    #lets turn it into a list to extract it
print(single_num(nums = [2,2,1]))