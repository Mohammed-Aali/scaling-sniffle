# text = 'hello my name is slim shady and I would like to eat some fried che ckin if you have some that would be wondorful.'
# text1 = 'hello my name is mohammed and I like women, I find them good looking.'
# text2 = 'jfkldjkjfl'
# print(text2[58:90])
# print(len(text1))
# new_text = list(text)
# print(new_text[58:70])
# result = new_text[58:70].index(' ')
# print(result)
# new_text[result + 58] = '\n'
# print("".join(new_text))

qoute = 'Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult.'
qoute1 = 'Life is short, art long, opportunity fleeting, experience treacherous.'
print(len(qoute1))
if len(qoute) >= 58:
    s = list(qoute)
    n = s[58:].index(' ')
    s[n+58] = '\n'
    new_s = ''.join(s)
    qoute1 = new_s

print(qoute1)
