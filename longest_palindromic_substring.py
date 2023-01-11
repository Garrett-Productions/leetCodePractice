#Given a string, return the longest palindromic substring
#palindrome remains the same forward to backwards

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

#whats the most brute force way I could do this? I could store all substrings starting from position 0
#whats the most efficient way to do this?
#We could check each character and look to the left and right and check the characters, that way whatever character we are currently on is the center, time complexity is 0(n)2
#what edge case are we missing? odd length and even length

#put the if statement inside the while loop for most efficient usage


def long_palindrome(str):
    result = ''
    resLen = 0
    
    #odd length palindromes first, setting our two pointers
    for i in range(len(str)):
        left, right = i, i
        while left >= 0 and right < len(str) and str[left] == str[right]:
            if( right - left + 1) > resLen:
                resLen = right - left + 1
                result = str[left:right+1]
            left -=1
            right += 1
    #even length palindromes ya?
        left, right = i, i + 1
        while left >= 0 and right < len(str) and str[left] == str[right]:
            if(right - left + 1) > resLen:
                resLen = right - left + 1
                result = str[left:right+1]
            left -+1
            right+=1
    return result
print(long_palindrome('babad'))