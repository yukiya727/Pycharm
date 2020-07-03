class masaka_taunts:
    def eng_to_saka(self, words):
        symbol = [
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'p', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        taunt = ""
        for i in range(len(words)):
            for ii in range(len(symbol)):
                if symbol[ii].lower() == words[i].lower():
                    taunt += str(ii+1)
                    taunt += "\n"
        return(taunt)

def masaka_taunt(w):
    words = list(w)
    result = ""
    for i in range(len(words)):
        if words[i] == " ":
            continue
        num = ord(words[i].lower()) - 96
        result += str(num)
        result += "\n"
    return(result)

sentence = input("Please input the word(s) you want to translate to Masaka taunts: ")

print(masaka_taunt(sentence))