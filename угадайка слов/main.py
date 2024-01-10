import random
word_list = ["помидор","крокодил","машина","человек","ауди","мерседес","дом","паук","шарага","перпендикуляр",
             "окружность","земля","марс","вселеная","школа","университет","колледж","пизда","хуй","пиво",
             "учитель","порно","геморой","частота","шкаф","штанга","яблоко","груша","богатый","ястреб","индивид"]
def get_word():
    return str(random.choice(word_list)).upper()
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def defence_durak(user):
    return user.isalpha()

def play(word):
    print("Добро пожаловать в угадайку слов ! (:")
    s = list("_" * len(word))
    guessed_letters = []
    guessed_words = []
    tries = 6

    while True:
        print(display_hangman(tries))
        user = input("Введите букву или слово").upper()
        print(f"Твои названые буквы {guessed_letters}")
        print(f"Твои названые слова {guessed_words}")
        print("".join(s))

        if (defence_durak(user) == True) and (user not in guessed_letters) and (user not in guessed_words):
            if len(user) == 1:
                if user in word:
                    print(f"Молодец ты угадал/ла букву")
                    id = word.index(user)
                    s[id] = user
                    guessed_letters.extend(user)
                    if (user in word) and (word.count(user)) > 1:
                        ind = [i for i in range(len(word)) if word[i] == user]
                        for i in ind:
                            s[i] = user
                elif tries == 1:
                    print(f"Ты проиграл загаданое слово было {word}")
                    break
                elif user not in word:
                    tries -=1
                    print(f"Ты не угадал/ла букву ): У тебя осталось  {tries} попыток")
                    guessed_letters.extend(user)
            elif len(user) > 1:
                if user == word:
                    print(f"Поздравляю , ты угадал слово {word}")
                    break
                else:
                    print("Нет , это слово не подходит ")
                    guessed_words.append(user)
                    tries -=1
        else:
            print("Ты должен вводить буквы !,и ты не должен повторять буквы или слова которые уже вводил")
play(get_word())