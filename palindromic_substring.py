import math


s =  "kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"#"aacabdkacaa"#"babad"
print("The lenght of input string s is: {}".format(len(s)))

def is_palindromic(str):
    if len(str) == 2 and str[0] == str [1]:
        return True

    if len(str)%2 != 0:
        lim = math.floor(len(str)/2)
    else:
        lim = int(len(str)/2)

    for index in range(lim):
        if str[index] != str[len(str)-1-index]:
            return False
    else:
        return True

max_palindromic = s[0]
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        substring = s[i:j+1]
        if is_palindromic(substring) and len(max_palindromic) < len(substring):
            max_palindromic = substring

print("The biggest palindromic in string is : {}".format(max_palindromic))