def long_string(str):
# Given a string str, find the length of the longest substring without repeating characters
#Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#were gonna need a variable to store the longets substring "sofar", a variable to store the current substring, and a pointer to restart, 
#a dictionary to see if we've already checked these values
#we ll make this a while loop so we can exit when we meet our requirement so we'll create an iterator variable
    current, start, sofar = 0,0,0
    lookup = {}
    i = 0
    N = len(str)
    
    while i < N:
        if str[i] not in lookup:
            current +=1
        else:
            start = max(start, lookup[str[i]])
            current = i - start
        lookup[str[i]]= i
        sofar = max(current, sofar)
        i+=1
    return sofar
#print(long_string("abaaaa"))






print(long_string("abaaaa"))