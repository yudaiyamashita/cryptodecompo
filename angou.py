input_line = input()
i, string = input_line.split()
i = int(i)
arr = list(string)
abc = list("abcdefghijklmnopqrstuvwxyz")
text = input() 
for j in range(i):
    m = text.maketrans(string,"abcdefghijklmnopqrstuvwxyz")
    text = text.translate(m)
print(text)