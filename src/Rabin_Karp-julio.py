'''
Rabin Karp
'''

class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rk_aux(word, text):
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return print(None)
    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    #word_hash.move_window()
    cc = 0
    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                cc = cc + 1
        rolling_hash.move_window()
    if not cc:
        return None
    return cc


'''
Input: words - variavel do tipo list - palavras/entidades a serem buscadas
       texts - variavel do tipo list - com textos onde as words serão procuradas
Output: 'texto:', num ,'- palavra:', a palavra ,'- quantidade:', num de vezes que aconteceu

'''

def rabin_karp(words,texts):
    if words == [] or texts == []:
        return None
    for ii in range(len(words)):
        for jj in range(len(texts)):
            if rk_aux(words[ii],texts[jj]) != None:
                print('texto:',str(jj),'- palavra:',str(words[ii]),'- quantidade:',str(rk_aux(words[ii],texts[jj])))


TEXTOS = ["Joao Marcos foi a praia no sabado","Apesar da chuva Julio Cesar saiu e foi ver Bruno.Julio Cesar e Bruno sao loucos",
          "Julio e Joao sairam","Joao, Marcos e Bruno da Silva"]
PALAVRAS = ["Julio Cesar","Joao","Joao Marcos","Bruno da Silva"]

rabin_karp(PALAVRAS,TEXTOS)


'''
exemplo em que as palavras sao maiores que o texto
'''

TEXTOS = ["Joao Marcos foi a praia no sabado","Apesar da chuva Julio Cesar saiu e foi ver Bruno",
          "Julio e Joao sairam","Joao e Marcos"]
PALAVRAS = ["Julio Cesar de azevedo vieira","Joao da silva sauro","Joao Marcos dos santos augusto","Bruno da Silva"]


rabin_karp(PALAVRAS,TEXTOS)
