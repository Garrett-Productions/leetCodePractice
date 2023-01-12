# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(str):
    stack = []
    lookup = {")":"(","}":"{","]":"["}          #this makes our code easy, we dont need a bunch of if else statements. these are key value pairs, and we made our values all the open options
    
    for mark in str:                            #for every parenthesis in our string
        if mark in lookup.values():             #first we ll check to see if its open or closed, which since we made the values all open we know we are accessing the open ones
            stack.append(mark)
        elif stack and lookup[mark] == stack[-1]: #elif make sure the parenthesis are the same and equal the stack, then pop it off
            stack.pop()
        else:                                      #else if there is no stack return False
            return False
    return stack == []                              #this returns weather it's an empty list or not
print(isValid("()"))