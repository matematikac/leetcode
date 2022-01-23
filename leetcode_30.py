# s ="barfoothefoobarman"
#  words = ["foo","bar"]


# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]


s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
words_copy = words
print(words_copy)
n = len(words)
position_list =[]

# def check_substring(temp,position):
#     for _ in words:
#         position += 3
#         if position + 3 < len(s):
#             temp = s[0 + position : 3 + position]
#             if temp in words:
#
#                 words.remove(temp)
#     if len(words) == 0:
#         for item in words_copy:
#             words.append(item)
#         return True
#     else:
#         for item in words_copy:
#             print('hy')
#             words.append(item)
#         return False
#
#
# for k in range(0,len(s)-2):
#     temp = s[0+k:3+k]
#     position = k
#     if temp in words:
#         if check_substring(temp, position):
#             print('hello')
#             position_list.append(position)
# print(position_list)