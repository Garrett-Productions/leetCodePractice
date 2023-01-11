def rometoint(str):
    #if there are multiple files in oine repository it is because aI have been practicing!
    roman_map={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    for i in range(len(str)):
        if i + 1 < len(str) and roman_map[str[i]]< roman_map[str[i+1]]:
            result -= roman_map[str[i]]
        else:
            result += roman_map[str[i]]

    return result
rometoint('MCIX')