def longestCommonPrefix(strs):
# find the longest common prefix string amongst an array of prefix strings, if there is no common prefix return an empty string

    if len(strs) == 0: #edge case
        return("")
    if len(strs) == 1: #edge case
        return(strs[0])
    pref = strs[0]      #save the first word in the list as longrst prefix to make comparison, this is your initial prefix
    plen = len(pref)    #this keeps track of that variable, pref, lengths.
                        #loop through the rest of the array and make comparisons

    for s in strs[1:]:  #we dont need the first value in our array so we slice it so we start at the 1st position and not the 0 position because the 0 position is already stored
        while pref != s[0:plen]:
            pref = pref[0:(plen-1)]
            plen -= 1

            if plen == 0:
                return("")
    return(pref)
print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))