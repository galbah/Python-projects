import hangman_helper


def update_word_pattern(word, pattern, letter):
    """
    :param word: the word that the user must reveal in the game
    :param pattern: the part of the word that is revealed to the user already
    :param letter: the letter that the user guessed
    :return: the new pattern, after the users guess
    """
    lst_pattern = list(pattern)
    for i in range(0, len(word)):
        if (word[i] == letter):
            lst_pattern[i] = letter
    pattern = ''.join(lst_pattern)
    return pattern


def run_single_game(words_list, score):
    """
    :param words_list: a list of words, the game chooses 1 randomly and the user must guess it
    :param score: the current score that the user has before this round
    :return: the current score after a single game has been played
    """
    word = hangman_helper.get_random_word(words_list)
    pattern = "_" * len(word)
    wrong_guess = list()
    msg = "welcome to the best game in history of games!"
    while True:
        char_counter = 0
        _counter = 0
        if score == 0 :
            msg = "you lost, dont worry its not a big deal, the word was " + word
            break
        hangman_helper.display_state(pattern, wrong_guess, score, msg)
        choice, guess = hangman_helper.get_input()
        if choice == hangman_helper.LETTER :
            if len(guess) != 1 or guess < 'a' or guess > 'z':
                msg = "input was invalid, this time make sure your input is ok!"
                continue
            elif guess in wrong_guess or guess in pattern:
                msg = "this guess was already made, try another one"
                continue
            else:
                score-=1
                for i in range(0, len(word)):
                    if word[i] == guess:
                        char_counter+=1
                if char_counter>0 :
                    pattern = update_word_pattern(word, pattern, guess)
                    score = score+(char_counter*(char_counter+1))//2
                    if pattern == word :
                        msg = "wow! you got it correct! well done!"
                        break
                else:
                    wrong_guess.append(guess)
            char_counter =0
            msg = "another round, good luck!"
            continue
        if choice == hangman_helper.WORD :
            score-=1
            if guess == word:
                for i in range(0,len(pattern)):
                    if pattern[i] == '_' :
                        _counter+=1
                score = score+(_counter*(_counter+1))//2
                msg = "wow! you got it correct! well done!"
                pattern = word
                break
            else:
                msg = "the guess was wrong, good luck this time"
        if choice == hangman_helper.HINT :
            score-=1
            hint = list()
            sec_hint = list()
            hint_length = hangman_helper.HINT_LENGTH
            hint = filter_words_list(words_list, pattern, wrong_guess)
            if len(hint) <= hint_length :
                hangman_helper.show_suggestions(hint)
            else:
                for i in range(0, hint_length):
                    sec_hint.append(hint[(i*len(hint))//hint_length])
                hangman_helper.show_suggestions(sec_hint)
            msg = "another round, good luck!"
    hangman_helper.display_state(pattern, wrong_guess, score, msg)
    return score


def main() :
    """
    the main function, runs game rounds until the user asks to stop
    :return: None
    """
    word_list = hangman_helper.load_words()
    score = run_single_game(word_list, hangman_helper.POINTS_INITIAL)
    games_played = 1
    while True :
        if score > 0 :
            msg = "you played "+ str(games_played)+" games and you have "+str(score)+" points, do you want to play another round?"
            if hangman_helper.play_again(msg) :
                score = run_single_game(word_list,score)
                games_played+=1
            else:
                break
        else:
            msg = "you played "+ str(games_played)+" games and you have "+str(score)+" points, do you want to restart the game?"
            if hangman_helper.play_again(msg):
                score = hangman_helper.POINTS_INITIAL
                score = run_single_game(word_list, score)
                games_played = 1
                continue
            else:
                break


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    :param words: list of words that been used to choose the word
    :param pattern: the current pattern that the user revealed
    :param wrong_guess_lst: all letters that the user guessed that were not in the word
    :return: a list of words that can match the pattern by it length and the revealed letters
    """
    optional_words = list()
    for i in range(0, len(words)) :
        if len(pattern) == len(words[i]) :
            optional_words.append(words[i])
            for j in range(0, len(pattern)) :
                char = pattern[j]
                if words[i][j] in wrong_guess_lst :
                    optional_words.remove(words[i])
                    break
                if char == '_' :
                    continue
                elif char != words[i][j] :
                    optional_words.remove(words[i])
                    break
                if words[i].count(char) != pattern.count(char) :
                    optional_words.remove(words[i])
                    break
    return optional_words


if __name__ == "__main__" :
    main()