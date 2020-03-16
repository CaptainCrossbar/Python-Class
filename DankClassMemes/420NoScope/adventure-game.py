#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : adventure-game.py
# Author : CaptainCrossbar
# Creation Date : 05 - March - 2020
# Last Modified : 12 - March - 2020
# Description : A game that takes you on a series of adventures where it will ask
# to do do something and input your findings to progress.
#
###############################################################################
"""

#import statements
import time

#main function
def main():
    pass

#function for the intro to the game
def intro():
    while True:
        print('Would you like to go on an adventure?')
        x = input()
        if x == 'yes' or x == 'Yes' or x == 'YES' or x == 'y' or x == 'Y':
            print('Congrats love! You have chosen wisely. We will begin shortly.')
            break
        elif x == 'no ' or x == 'No' or x == 'NO' or x == 'n' or x == 'N':
            print('What you dont want to go on an adventure!? what are you a panzy, mate. You have done mugged me off')
            time.sleep(5)
            print('Ill give you another shot. Hopefully you make the right call')
            time.sleep(.99)
            continue
        elif x == '69':
            print('Noice! You my good sir or ma am are a person of amazing quailty. Please input either yes or no tho next time')
            time.sleep(.69)
            continue
        elif x == '420':
            print('Ayy my mans. You blaze it up, dont you? But guess what! You just won a random a UA')
            time.sleep(.69)
            continue
        else:
            print('I like your style but please input a yes or a no')
            x = input()
            if x == 'yes' or x == 'Yes' or x == 'YES' or x == 'y' or x == 'Y':
                print('We will begin shortly, mate')
                break
            else:
                print('Youse mugged us off for the last time...')
                print(' ')
                time.sleep(4.20)
                print('uuuuuuuuuuuuuuuWWWWWWWWWWWWWWWuuuuuuuuuuuuuuu')
                print(' ')
                continue

#intro()

#function for adventure 1
#Intro to Pete
def adventure1():
    time.sleep(.69)
    print('Your first adventure is a recon challenge. In this adventure you will be asked to'
    'find a certain key word or phrase that will unlock your next adventure. Are you ready?')
    print('***Note you will need access to the internet to complete this adventure***')
    x = input()
    if x == 'yes' or x == 'Yes' or x == 'YES' or x == 'y' or x == 'Y':
        print('Your first adventure is as follows: \n'
        'First you will need to guess my name. I am dark as night and strike fear into my enemies.'
        'I clean up the streets but normally at night. Whats my name? \n')
        name = input()
        if name == 'batman' or x == 'Batman' or x == 'BATMAN':
            print('Congrats on completing the first part of this. Now on to the next part. \n'
            'Next you need to watch a video. How you watch is up to you. Dont find the right one and you may not get this challenge. \n'
            'The video you must find is a song. It is a silly song that has two people in it. They sing about cool guys...'
            ' Hopefully you think that is enough of a hint but if not ill point you oin the right direction with, one of the singers is Andy Sandburg \n'
            '...After Watching the video, who is walking away in a hat?')
            mark = input()
            if mark == 'mark walburg' or mark == 'Mark Walburg':
                print('Cool guys dont look at expolsions. They walk away, in slow motion.'
                'Whose go time to watch an explosion, when they got cool guy errands they got to walk to. \n\n'
                'Next question: Who had the best explosion scene? Hint: it may or may not be related to a previous question... ')
                joker = input()
                if joker == 'joker' or joker == 'Joker' or joker == 'JOKER' or joker == 'the joker' or joker == 'The Joker' or joker == ' THE JOKER':
                    print('Ayy you got it. Heather Ledger was by far the best joker character!\n'
                    'The final question of the quest is what ') #batman vs bane

        else:
            print('Thats not my name. Hint: Peters nickname at school his first year was my name')


    else:
        print('Whats the matter? You get scared?')
    pass

#function for adventure 2
#Its Hockey Night tonight
def adventure2():
    print('Congradulations on finishing your first adventure.')
    pass

#function for adventure 3
#The West Point of the South aka the better school
def adventure3():
    print('Congradulations on finishing your second adventure.')
    pass

#function for adventure 4
#From Russia with Love
def adventure4():
    print('Поздравляю с завершением третьего приключения.')
    pass

#function for adventure 5
#Its show time
def adventure5():

    #variables for adventure 5
    score = 0
    sp1 = 0
    sp2 = 0
    sp3 = 0
    sp4 = 0
    sp5 = 0
    attempts = 9
    t = 5

    print('Congratulations on finishing your fourth adventure.')

    time.sleep(5)

    print('\nI hope you are ready for your fifth adventure... \n')

    time.sleep(1)

    #countdown loop to start the adventure
    while t >= 0:
        print(t, end='...\n')
        time.sleep(1)
        t -= 1
    print('\n \nHERE WE GOOOOOOO! \n \n \n')

    #wait 3 seconds before displaying adventure opening statement
    time.sleep(3)

    #adventure opening statement
    print("In this adventure, you will be quizzed on some tv and movie knowledge."
    " Dont worry, my friend this won't be too bad. You've made it this far havent you?"
    " We will start slow and easy and progressively get a bit harder."
    " Oh I forgot to mention this but you will be scored in this challenge :)\n")

    #question set 1
    #loop to go through the question set
    while True:
        print('The first challenge is, how many seasons are they currently in The Expanse?')
        user = input()
        if user == '4':
            #adds points to score for correct answer
            score += 10
            sp1 += 10
            print('\nStarted you off easy there :)\n')
            print('Your next question is, what is this quote from?')

            #loop to keep the second question going if user gets it wrong
            while True:
                print("\nI bet you're the kind of guy that would f-ck a person in the ass and not even have the goddamn common courtesy to give him a reach-around."
                "I'll be watching you.\n")
                user = input()
                if user == 'Full Metal Jacket' or user == 'full metal jacket' or user == 'FULL METAL JACKET' or user == 'fmj' or user == 'FMJ':
                    #adds points to score for correct answer
                    score += 10
                    sp1 += 10
                    print('\nAwesome Job! Glad you got that one. Your next question is the last for this set.')
                    print('\nThis question is two parts \n')

                    #loop to keep the third question going if user gets it wrong
                    while True:
                        print("First question is, Who has a meme run named after them?\n")
                        user = input()
                        if user == 'Naruto' or user == 'naruto' or user == 'NARUTO':
                            #adds points to the score for correct answer
                            score += 5
                            score += 5
                            print('The second question is:')
                            time.sleep(3)
                            #loop to keep the second part of question 3 going if user gets it wrong
                            while True:
                                print("What is the creature's name that resides inside him?")
                                user = input()
                                if user == 'kurama' or user == 'Kurama' or user == 'KURAMA':
                                    #adds points to the score for correct answer
                                    score += 5
                                    score += 5
                                    print('Congratulations on completing this set of questions. You will be moving onto a slightly harder set of questions next :)'
                                    ' The next set will be related to a certain genre of movies. So grad your rifle and lets move out')
                                    #should exit the loop (ie question set)
                                    break
                                elif user == 'nine tails fox' or user == 'Nine Tails Fox' or user == 'NINE TAILS FOX':
                                    print('I guess you got it but I was really looking for his name. I will give you another chance to get it so you can claim the points')
                                    time.sleep(2)

                                    #loop to keep part two going if user inputs nickname of the character and not the desired answer
                                    while True:
                                        print("\n What is the creature's name that resides inside him?")
                                        user = input()
                                        if user == 'kurama' or user == 'Kurama' or user == 'KURAMA':
                                            #adds points to the score for correct answer
                                            score += 5
                                            score += 5
                                            print('Congratulations getting it on your second guess. You have successfully completed this set of questions.'
                                            ' You will be moving onto a slightly harder set of questions next :)'
                                            ' The next set will be related to a certain genre of movies. So grad your rifle and lets move out')
                                            #should exit the loop (ie the question set)
                                            break
                                        else:
                                            #subtracts points to the score for incorrect answer
                                            score -= 1
                                            sp1 -= 1
                                            print("You're getting there. Keep trying!")
                                            #should keep going through this portion of the loop
                                            continue
                                    break
                            else:
                                #subtracts points to the score for incorrect answer
                                score -= 1
                                sp1 -= 1
                                print('\n Ill throw you a bone, He is a sometimes called the evil fox spirit')
                                #should keep going through this portion of the loop
                                continue

                            break
                    else:
                        #subtracts points to the score for incorrect answer
                        score -= 1
                        sp1 -= 1
                        print('\n Hint, He is a character from a popular anime show and characters do hands signs in the show to do certain actions')
                        #should keep going through this portion of the loop
                        continue

                    break
                else:
                    #subtracts points to the score for incorrect answer
                    score -= 1
                    score -= 1
                    print('Its a classic vietnam movie')
                    print('I am also judging your skills and ability to look/recon on the interwebs')
                    #should keep going through this portion of the loop
                    continue
            break

        else:
            print('This was supposed to be an easy question even if you dont watch the show...')
            #should keep going through this portion of the loop
            continue

        break


    #question set 2 war movies
    print("\nYour score after the first part of this adventure is ", score)
    print("\nThe next set of questions will be tougher...\n \n \n")
    while True:
        print('The second challenge is,\nWhat movie is this picture from? \n ')

        #Opens an image for the question
        from PIL import Image
        im = Image.open(r)
        im.show()

        user = input()

        #
        if user == '':
            score += 15
            sp2 += 15

            #
            while True:
                print('')

                if:
                    score += 15
                    sp2 += 15

                else:
                    score -= 2
                    sp2 -= 2

                    print('')

                    break
        else:
            print('')

        break


    '''
    #question set 3 comedies
    while True:
        print('The third challenge is, in what movie is  ')

    #question set 4 chuck
    while True:
        print('The fourth challenge is, in what show is  ')

    #question set 5 gg
    while True:
        print('The fifth challenge is, in what show is  ')

    #question set 6
    while True:
        print('Your final challenge for this adventure is,   ')
    '''
adventure5()
    #pass

#function for adventure 6
#The kights who say Knee
def adventure6():
    print('Congradulations on finishing your fifth adventure.')
    pass

#function for adventure 7
#Best beer in the world
def adventure7():
    print('Herzlichen Glückwunsch zum Abschluss Ihres sechsten Abenteuers.')
    pass

#function for adventure 8
#City of love (Pari)
def adventure8():
    print('Félicitations pour avoir terminé votre septième aventure.')
    pass

#function for adventure 9
#Barcalona is king
def adventure9():
    print('Felicitaciones por terminar su octava aventura.')
    pass

#function for adventure 10
#Italian job
def adventure10():
    print('Congratulazioni per aver terminato la tua nona avventura.')
    pass

###############################################################################################################################################################
#Add-ons to the game
###############################################################################################################################################################

#function for the last decison the user makes
def finaldecision():
    pass

#function to create and display an ascii art of Dio
def DioASCiiArt():
    pass
