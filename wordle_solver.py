# prereqs

#have all 5 letter words
#only legal guesses

#grey - no, this letter is not in the word
#yellow - yes this letter is in the word but not in the correct spot
#green - the letter is in the word and correct spot

#on first guess eveyr word is valid
    #you can just pick any word
    #will give back grey yellow or green
    #each guess reveals 5 facts

#handling a grey letter
    #if letter is grey
    #for loop over (list_valid)
    #check if it contains grey letter
    #if word has letter
    #take it out of valid word list

#handling a green letter
    #if letter is green
    #for loop over words still allowed
    #eliminate any words not having that letter in the correct position

#handling a yellow letter
    #if yellow letter in word
    #for loop to iterate over whole list of words
    # eliminate any words that do not contain the letter
    #eliminate any words that contain the letter in that spot

#user interface
    #next guess is supplied by the program
    #result is also an input line from the user from wordle

# wget " https://raw.githubusercontent.com/tabatkins/wordle-list/main/words" -outfile "wordle-words.txt"

import random
if __name__ == "__main__":

#means program starts here

    wordfile = open(f'wordle-words.txt', 'r')

    remainingwords = wordfile.read().split()

    current_suggestion = random.choice(remainingwords)

    print(f'Guess 1 is {current_suggestion}')

    userinput = input(f'Result 1 is:')



    if len(userinput) == 5:

        print(userinput)
    else:
       print(f'Please only use 5-letter values.')

       exit(1)

    for position in range(len(userinput)):
        guess_letter = current_suggestion[position]
        guess_result = userinput[position]

        if guess_result == 'G':
            new_guesses = []
            for word in remainingwords:
                if guess_letter in word:
                    continue
                else:
                    new_guesses.append(word)

        remainingwords = new_guesses

        print(f'because position {position} letter {guess_letter} was result {guess_result},')
        print(f'only {len(remainingwords)} remain.')

    current_suggestion = random.choice(remainingwords)

    print(f'Guess 2 is {current_suggestion}')

#dad challenge post leaving me





        #here is where you will put
        #if letter = g
        # if letter = y
        # if letter = e



