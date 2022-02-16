import random
from hangman_art import stages , logo
from hangman_words import word_list


print(logo)
print("\n\n\n")

answer = random.choice(word_list)
is_win = False 
finalans = ""
deadline = 0
# print(answer)
for j in range(0 , len(answer)):
    finalans += "_"
# print(finalans)
print("Welcome to the Hangman Game!!")
print("\n\nINSTRUCTIONS :")
print("\nGuess the below word and SAVE the hostage ")
print("For each wrong move,this man is going one step forward to HELL!!")

finalans1 = list(finalans)
print(finalans1)
print("\n\n")


while not is_win and deadline < 6 :
#for checking wether the guess is correct and update the word
    guess = input("Guess a letter: ").lower()
    for i in range (0,len(answer)) :
        if answer[i] == guess :
            finalans1[i] = guess
    count = finalans1.count(guess)
    finalans2= "".join(finalans1)
#informing whether thier guess is correct or not  
    if count ==0 :
        print("Your guess is wrong")
        deadline += 1
        print(finalans2)
    else :
        print("Your guess is correct")
        print(finalans2)
#printing player stage 
    print(stages[6-deadline])
#finding wether the player was won or not
    for i in range(0,len(finalans1)):
        if finalans2 == answer :
            is_win = True

    if is_win and deadline <6 :
        print("You win")
    elif deadline >=6:
        print(".....GAME OVER.....") 
        print("The Hostage was KILLED....")
        print(f"The correct word is {answer}")
    


    
    




input()