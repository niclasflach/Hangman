import random
import os

def main(args=None):
    
    def get_hangman_art():
        '''
        Hämta ASCII art från filen hangman.art och lägger den i en lista som returneras
        '''
        art_file = open("hangman.art","r")
        art = art_file.read()
        return art.split(',')
    
    
    def get_word():
        '''
        Funktion som öppnar filen svenska-ord.txt och läser in den till data variabeln.
        Splittar upp den vid radavslut till en lista
        tar en slumpvis medlem i listan och returnerar som sträng
        '''
        text_file = open("svenska-ord.txt", "r", encoding='utf-8') #öppnar ord-filen
        data = text_file.read() #läser in filens innehåll till data
        word_list = data.split('\n') #splittar till lista vid rad-avslut
        number_of_words = len(word_list) #tar reda på antalet ord i listan
        return random.choice(word_list) #tar ett slumpvis ord ur listan
     
        
    def rita_bild(gissning):
        os.system('cls')
        print(hangman[gissning])
    
    bokstaver = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö']
    spelar = True
    poäng = 0
    hangman = get_hangman_art()
    gissning = 0
    ordet = get_word()
    maskerat = '_'* len(ordet) # Gör en maskerad sträng med samma längd som ordet
    resultat_gissning = []
    while spelar: #kör tills spelar sätts till False
        #Printa Galge i ASCII art
        rita_bild(gissning)
        #Printa en lista med bokstäver som finns kvar att gissa på
        print(*bokstaver)
        #print(ordet) # För debug, Printar rätt svar
        print(maskerat)
        print(resultat_gissning)
        print(f'poäng: {poäng}')
        resultat_gissning = []
        bokstav = input("vilken bokstav gissar du på: ")
        if bokstav == 'sluta':
            spelar = False
        resultat_gissning = []
        #lägga in try här
        if bokstav in bokstaver and len(bokstav) == 1:
            bokstaver.remove(bokstav)
            if bokstav not in list(ordet):
                gissning = gissning + 1
            for i in range(0, len(ordet)):
                if ordet[i] == bokstav: #kollar om bokstaven finns i ordet på plats [i]
                    resultat_gissning.append(i + 1) # lägger till bokstaven i lista om så är fallet
                    temp_lista = list(maskerat) # gör om maskerat till temporär lista för att kunna ändra enskilda tecken
                    for letter in resultat_gissning:
                        temp_lista[i] = bokstav #ändrar dom träffade bokstäverna till den gissade bokstaven
                    maskerat = "".join(temp_lista)# gör om den temporära listan till en sträng igen och färdig för printning
        if ordet == maskerat: # Då borde man gissat hela ordet
            poäng += 1 #Öka poäng ett snäpp
            gissning = 0
            ordet = get_word()
            maskerat = '_'* len(ordet) # Gör en maskerad sträng med samma längd som ordet
            bokstaver = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö']
        if gissning > 5:
            print('Du klarade inte ordet! Du är hängd')
            print(f'Ordet som du misslyckades på är {ordet}')
            val = input('för att avsluta spelet, skriv sluta annars trycker du enter')
            if val.lower() == 'sluta':
                spelar = False
            gissning = 0
            ordet = get_word()
            maskerat = '_'* len(ordet) # Gör en maskerad sträng med samma längd som ordet
            bokstaver = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö']
        
        
    
if __name__ == "__main__":
    main()