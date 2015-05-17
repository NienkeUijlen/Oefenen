code=list(input())
codewoord=list(input())

i=0
while i<len(code):
    if 123-ord(codewoord[i%len(codewoord)])+ord(code[i])>122:
        code[i]=chr(97-ord(codewoord[i%len(codewoord)])+ord(code[i]))
    else:
        code[i]=chr(123-ord(codewoord[i%len(codewoord)])+ord(code[i]))
    i=i+1

print(''.join(code))
