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

quote = 'Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult. And for those reasons life should be appreciated'
quote1 = """When fast food is not a treat but a dietary staple,
the children surf the internet all day
in dark corners of the room and are bombarded
with latest gadgets. Things replace parental
standards."""
print(len(quote))
print(len(quote1))
print(quote[40:45])

if 58 < len(quote):
    slashed = 45
    s = []
    for char in quote:
       s.append(char)
    for char in s[slashed:]:
        try:
            n = s[slashed:].index(' ')
        except:
            continue
        s[n+slashed] = '\n'
        new_s = ''.join(s)
        slashed+=45
        if slashed > len(s):
            break


print(''.join(s))
print(new_s)
