from random import randint
# Zasady
title = 'Koło niefortuny!'.upper()
print('=' * 30)
print(title)
print('=' * 30)
print('''Zgaduj po jednej literze na raz. Aby kupić samogłoskę, musisz mieć $500.
Jeśli sądzisz, że znasz całe słowo lub zsanie, wpisz \'bingo\' i wciśnij enter, potem podaj słowo lub zdanie.
Otrzymasz wtedy wartość każdej litery a samogłośki za darmo.''')
print('=' * 30)

amounts = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0

# Lista liter do zdjęcia z tablicy po poprawnym trafieniu
alphabet = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
# Kategorie, słowa i frazesy
categories = {'Kolory': ['biel', 'czerń', 'czerwień', 'błękit', 'brąz', 'zieleń', 'fiolet', 'granat'],
              'Przysłowia polskie': ["Z osła konia wyścigowego nie zrobisz", "spokojnie jak na wojnie",
                                     "chcieć to móc", "cała mądrość nie mieści się w jednej głowie",
                                     "cel uświęca środki", "chciwy dwa razy traci",
                                     "chłop potęgą jest i basta", "ciągnie wilka do lasu",
                                     "cierpliwością i pracą ludzie się bogacą", "co ma piernik do wiatraka",
                                     "co nagle to po diable", 'czyny przemawiają głośniej niż słowa'],
              'Gwiazdy Hollywood\'u': ['jean-claude van damme', 'sylvester stallone', 'sharon stone', 'tom cruise',
                         'robert de niro', 'al pacino', 'westley snipes', 'jennifer aniston',
                           'julia roberts', 'courtney cox', 'sean connery', 'morgan freeman'],
              'Poeci polscy': ['Julian Tuwim', 'Jan Brzechwa', 'Maria Konopnicka', 'Aleksander Fredro',
                               'Wanda Chotomska', 'Cyprian Kamil Norwid', 'Adam Mickiewicz'],
              'Państwa': ['argentyna', 'wybrzeże kości słoniowej', 'zjednoczone emiraty arabskie',
                          'szwajcaria', 'watykan', 'polska', 'wielka brytania', 'australia']
              }

# Losowy wybór kategorii
category = randint(0, (len(categories) - 1))
# Wypisz kategorię
print('Kategoria:', '{', list(categories.keys())[category], '}')
# Losowy wybór słowa lub zdania
word = (categories[list(categories.keys())[category]][
    randint(0, (len(list(categories[list(categories.keys())[category]])) - 1))]).upper()
wordCount = len(word) - word.count(" ") - word.count("-")
wordRange = wordCount in range(22, 92)
wordLastLetter = int(repr(wordCount)[-1])
wordTeens = wordCount not in range(5, 22)

if wordCount in range(2, 5) or wordLastLetter == 2 and wordTeens \
        or wordLastLetter == 3 and wordTeens \
        or wordLastLetter == 4 and wordTeens:
    print('Na', wordCount, 'litery')
else:
    print('Na', wordCount, 'liter')

# Wypełnienie słowa lub zdania podkreślnikami
Word = []
for char in word:
    if char.isalpha():
        Word.append('_')
    else:
        Word.append(char)


# Funkja drukująca słowo lub zdanie
def printWord(word):
    for char in word:
        print(char, end=' ')
    print()


printWord(Word)

# Lista samogłosek
vowels = ['A', 'E', 'I', 'O', 'U']

# Zgaduj zgadula, do bólu
while True:
    while True:
        # Losowy wybór wygranej za odgadniętą literę
        amount = amounts[randint(0, (len(amounts) - 1))]
        print('Otrzymasz $' + str(amount), 'za poprawną literę')
        print('Zapłacisz $500 za samogłoskę')
        guess = input('Zgaduj, podaj literę: \n').upper()
        # Jeśli gracz che odgadnąć całość od razu
        if guess == 'BINGO':
            while True:
                correct = 0
                guess = input().upper()
                for letter in range(len(guess)):
                    if guess[letter] == word[letter]:
                        correct += 1
                    else:
                        break
                if correct == len(guess):
                    for letter in range(len(guess)):
                        if guess[letter] == word[letter]:
                            if not Word[letter].isalpha():
                                Word[letter] = guess[letter]
                                if guess[letter] not in vowels and guess[letter].isalpha():
                                    total += amount
                else:
                    print('Niestety nie, to nie jest dobra odpowiedź!')
                    printWord(Word)
                    break
                if '_' not in Word:
                    print('-' * 30)
                    printWord(Word)
                    break
                else:
                    for char in range(len(Word)):
                        if word[char] == guess:
                            Word[char] = guess
                print('$' + str(total))
                printWord(Word)
                if '_' not in Word:
                    break
            break
        # Jeśli gracz poda już wcześniej podaną literę
        elif guess not in alphabet:
            print('Już użyłeś/aś tej litery!')
            print('Posiadasz: $' + str(total))
        # Jeśli samogłoska, zabierz graczowi $500
        elif guess in vowels:
            if total >= 500:
                alphabet.remove(guess)
                for char in range(len(Word)):
                    if word[char] == guess:
                        total -= 500
                        Word[char] = guess
            # Brak środków na zakup samogłoski
            else:
                print('Za mało pieniędzy')
            print('Posiadasz: $' + str(total))
            print('-' * 30)
            printWord(Word)
            if '_' not in Word:
                break
        # Jeśli do tej pory wszystko jest False, zdejmij literę z alfabetu i wstaw ją do szukanego hasła
        else:
            alphabet.remove(guess)
            for char in range(len(Word)):
                if word[char] == guess:
                    Word[char] = guess
                    total += amount
            print('Posiadasz: $' + str(total))
            printWord(Word)
            if '_' not in Word:
                break
    # Całe słowo lub zdanie odgadnięte, koniec gry.
    if '_' not in Word:
        print('Brawo!')
        print('Twoja wygrana: $' + str(total))
        print('=' * 30)
        break