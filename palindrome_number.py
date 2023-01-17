#Given an integer x, return true if x is a palindrome, and false otherwise.
#EX:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


#Convert the number to string and compare it with the reversed string.

def isPalindrome(x: int) -> bool:
	if x < 0:
		return False
	
	return str(x) == str(x)[::-1] #if our input equals our reversed input then its true
print(isPalindrome(121))


