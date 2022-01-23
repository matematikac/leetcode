#only digits from 2 to 9 can be in combination for a phone number, maximal length of 4
digits = "234"

elements = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],['m', 'n', 'o'],['p', 'q', 'r','s'],['t', 'u', 'v'],['w', 'x', 'y','z']]

dictionary = {key: elements[key-2] for key in range(2,10)}

result = []

if len(digits) == 1:
    for i in range( len ( dictionary [ int (digits[0]) ] ) ):
        result.append(dictionary [ int (digits[0]) ][i])
elif len(digits) == 2:
    for i in range( len ( dictionary [ int (digits[0]) ] ) ):
        for j in range( len( dictionary [ int (digits[1]) ] ) ):
            result.append(dictionary [ int (digits[0]) ][i]+dictionary [ int (digits[1]) ][j])
elif len(digits) == 3:
    for i in range( len ( dictionary [ int (digits[0]) ] ) ):
        for j in range( len( dictionary [ int (digits[1]) ] ) ):
            for k in range(len(dictionary[int(digits[2])])):
                result.append(dictionary [ int (digits[0]) ][i]+dictionary [ int (digits[1]) ][j]+dictionary [ int (digits[2]) ][k])
elif len(digits) == 4:
    for i in range( len ( dictionary [ int (digits[0]) ] ) ):
        for j in range( len( dictionary [ int (digits[1]) ] ) ):
            for k in range(len(dictionary[int(digits[2])])):
                for s in range(len(dictionary[int(digits[3])])):
                    result.append(dictionary [ int (digits[0]) ][i]+dictionary [ int (digits[1]) ][j]+dictionary [ int (digits[2]) ][k]+dictionary [ int (digits[3]) ][s])


print(result)