def Copy_textfile(FileName_00, FileName_01):
    with open('apocalypse1.txt', 'r') as file:
        lines = file.read().splitlines()
        lines = [word.replace('Rev','\nRev') for word in lines]
        temp = "".join(lines)
    with open('Copied text.txt','w') as file:
        file.write(temp)


Copy_textfile('apocalypse1.txt','Copied text.txt')