def main():
    q = '''people do not live happily ever after even in happy stories, people do not live happily ever after even in happy stories, people do not live happily ever after even in happy stories, people do not live happily ever after even in happy stories, people do not live happily ever after even in happy stories.'''
    
    x = add_new_lines(q, 40)
    print(x)
    

def add_new_lines(string: str, slashed: int) -> str:
    if len(string) <= slashed:
        return string
    s =[]
    for char in string:
        s.append(char)

    initial = slashed
    while True:
        n = string[:slashed].rindex(' ')
        s[n] = '\n'
        slashed += initial
        if len(string) <= slashed:
            return ''.join(s)
        
if __name__ == '__main__':
    main()