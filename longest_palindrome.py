#Given a string which consists of upper or lowercase letters, find the length of the longest palindrome that can be built with those letters
#This is case sensitive so "Aa" Is not a palindrome'

#Example: Input: "abccccdd"

#Output: 7, because "dccaccd" is the longest palindrome of the string which has 7 char's

def longest_palindrome(str):
    letters = {}

    max = 0
    for letter in str:
        if letter in letters:    #if this character has been seen... then....
            letters.pop(letter)
            max += 2
        else:                    #else give that key, which is a character, a value of 1
            letters[letter] = 1

    if letters:
        max += 1
    return max                   # return the max, which is the length of our longest palindrome

print(longest_palindrome("abccccdd"))

#cases: refer, mom, madam, level, kayak, racecar, abccccdd