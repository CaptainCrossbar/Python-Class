#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : adventure-game.py
# Author : CaptainCrossbar
# Creation Date : 05 - March - 2020
# Last Modified : 16 - March - 2020
# Description : A game that takes you on a series of adventures where it will ask
# to do do something and input your findings to progress.
#
###############################################################################
"""

#import statements
import time
import math
import random

#main function
def main():
    #list adventures out, prompt user to pick an adventure
    #has to comlete a series of 3 or more adventures to get to final challenge
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
    hockey_bank = ["The word Hockey was first used in what year?",
    "Ice Hockey was included for the first time in the Olympics in which year?",
    "Which teams are included in the Big Six hockey teams?",
    "Which team of the NHL won back to back Stanley Cup titles?",
    "Which player holds the record for the most goals scored in one NHL game?",
    "Before Steve Yzerman who was the captain of the Detriot Red Wings?",
    "Who was the first player in hockey history to win an Olympic Gold Medal and a Stanley Cup in the same year?",
    "What year did the Stanley Cup have no winner? And what was the cause?"]

    hockey_lst = hockey_bank

    hockey_ans = ["1773",
    "1920 Summer Olympics",
    "Canada, Czech Republic, Finland, Russia, Sweden, and the United States",
    "Ottawa Senators",
    "Joe Malone",
    "Danny Gare",
    "Ken Morrow",
    "1919 influenza epidemic"]

    hockey_ans_lst = hockey_ans

    hockey_chirps = ["What's that? Roll down your window, I can't hear you.",
    "Hey man, does your coach know you're out here?",
    "Hey stripes, the whistle ain't a dick, get it out of your mouth.",
    "Hey tendie, your legs are so wide open you make Jenna Jameson look like a saint.",
    "Funny, I heard you were the worst player on your last team too."]

    while hockey_lst > 0:

        r = random.randint(0, len(hockey_lst)- 1)

        print(hockey_lst[r])

        user = input().lower()
        print('\n')

        if user == hockey_ans_lst[r]:
            print('He shots, he scores. Keep firing top ched there big boy\n \n')
        else:
            chirp = random.randint(0, len(hockey_chirps))
            print(hockey_chirps[chirp],'\n\n')

        hockey_lst.remove(hockey_lst[r])
        hockey_ans_lst.remove(hockey_ans_lst[r])
    pass

#function for adventure 3
#
def adventure3():
    print('Congradulations on finishing your second adventure.')
    pass

#function for adventure 4
#From Russia with Love
def adventure4():
    print('Поздравляю с завершением третьего приключения.')
    #this adventure is done in the fight night.py game
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
    bq = 0
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
    #print("In this adventure, you will be quizzed on some tv and movie knowledge."
    #" Dont worry, my friend this won't be too bad. You've made it this far havent you?"
    #" We will start slow and easy and progressively get a bit harder."
    #" Oh I forgot to mention this but you will be scored in this challenge :)\n")


    #question set 1 random
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
                        user = input()time.sleep(3)
                            print('')
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
                        #should keep going throutime.sleep(3)
                            print('')gh this portion of the loop
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
    #print("\nYour score after the first part of this adventure is ", score)
    #print("\nThe next set of questions will be tougher...\n \n \n")
    #loop for question 1
    while True:
        print('The second challenge is,\nWhat movie is this picture from? \n ')

        #Opens an image for the question
        from PIL import Image
        im = Image.open(r"platoon-question.jpg")
        im.show()

        user = input()

        #Question 1 answer checker: Platoon
        if user == 'Platoon' or user == 'platoon':
            score += 15
            sp2 += 15

            time.sleep(3)
            print('Congrats on gettting that one. It is a pretty famous scene nut if you didnt not know that it probably was a bit challenging')

            #loop for question 2
            while True:
                time.sleep(3)
                print('\n \nYour next question is similar to the first. What is this image from?')

                from PIL import Image
                im1 = Image.open(r"apoc-now.jpg")
                im1.show()

                user = input()

                #question 2 answer checker: we were soliders
                if user == 'Apocalypse Now' or user == 'apocalyse now':
                    score += 15
                    sp2 += 15

                    print('Bonus question time!!!!\n\n\n')
                    time.sleep(2)
                    print('What is a famous quote that the man standing said at some point in the movie?')

                    user = input()

                    #bonus question checker
                    if user == 'I love the smell of napalm in the morning. You know, one time we had a hill bombed, for 12 hours. When it was all over, I walked up. We didn’t find one of ’em, not one stinkin’ dink body. The smell, you know that gasoline smell, the whole hill. Smelled like victory.':
                        score += 30
                        sp2 += 0
                        bq = 1

                        print('\n \nI am impessed. Didnt think you were going to get that. It was a rather long one to type out but dammmm do I love that smell')

                    #condition if bonus answer was wrong
                    else:
                        print('Sorry the correct answer was: \n \n \n')
                        time.sleep(2)
                        print('I love the smell of napalm in the morning. You know, one time we had a hill bombed, for 12 hours. When it was all over, I walked up. We didn’t find one of ’em, not one stinkin’ dink body. The smell, you know that gasoline smell, the whole hill. Smelled like victory.')


                    #loop for question 3
                    while True:
                        #bnous question answered corrctly
                        if bq == 1:
                            print('Knarly mate!! Very impressive you got both of those!')

                        #bonus question answered incorrectly
                        else:
                            print('One for two aint bad bruv. Keep up the good work')

                        time.sleep(3)
                        print('The next question will follow the same format as previous questions. \n'
                        'What movie is this picture from?')

                        from PIL import Image
                        im1 = Image.open(r"we-were-soldiers.jpg")
                        im1.show()

                        user = input()

                        if user == 'We Were Soldiers' or user == 'we were soldiers':
                            score += 10
                            sc3 += 10

                            #loop for question 4
                            while True:
                                print('Nice one there! Keep it up! Almost to the end of this question set!!')
                                time.sleep(2)
                                print('Your fourth question is gonna follow the same format... Shocker XD')

                                from PIL import Image
                                im1 = Image.open(r"dirty-dozen.jpg")
                                im1.show()

                                user = input()

                                #answer checker for question for
                                if user == 'The Dirty Dozen' or user == 'the dirty dozen':
                                    score += 15
                                    sp4 += 15

                                    #loop for question five
                                    while True:
                                        print('Smashing! You made it to the last question in this set. I hope you are ready')
                                        time.sleep(2)
                                        print('For this one, I will be nice and provide you a hint with image')

                                        from PIL import Image
                                        im1 = Image.open(r"kellys-heroes.jpg")
                                        im1.show()

                                        #hint for last question
                                        print('Hint:\n \n ')
                                        time.sleep(2)
                                        print("Don't hit me with those negative waves so early in the morning")

                                        user = input()

                                        #answer checker for question 5
                                        if user == 'Kellys Heroes' or user == 'kellys heroes' or user == "Kelly's Heroes" or user == "kelly's heroes":
                                            score += 20
                                            sp5 += 20

                                            print('Congratulations on successfully making it through this set of questions.'
                                            ' I hopeyou enjoyed these questions and it has inspired you to watch the movies')

                                            #should exit question 5 loop
                                            break

                                        #wrong answer for question 5
                                        else:
                                            #deducts point from score
                                            score -= 2
                                            score -= 2

                                            print('Sorry, that was not it. Maybe you should try looking up war movies')

                                            #repeat question 5 again
                                            continue

                                    #should exit to the question 4 loop
                                    break

                                #wrong answer for question 4
                                else:
                                    #deducts points for wrong input
                                    sorce -= 2
                                    sp4 -= 2

                                    print('Sorry that was incorrect. Maybe this will getcha dropped in the right lz.'
                                    'They are war gaming in preparation for their top secret mission and oh they may be dirty')

                                    #repeat question 4 again
                                    continue

                            #should exit to the question 3 loop
                            break

                        #wrong answer for question 3
                        else:
                            #deducts points for wrong answer
                            score -= 2
                            sp3 -= 2

                            print()
                            #repeat question 3 again
                            continue
                    #should exit to the question 2 loop
                    break
            #wrong answer for question 2
            else:
                score -= 2
                sp2 -= 2

                print('Come on now. This was uspposed to be easy. It is an iconic image from a famous war movie. Maybe charlie does surf then...'
                'and just may you cant ride the valkeryies')

                #repeat question 2 again
                continue

            #should exit to the question 1 loop
            break

        #wrong answerfor question 1
        else:
            print('I get it, you dont watch war movies. How do you except to lead you joes if you havent seen them...'
            ' Or so said some crusty old MSG I once knew')
            continue
        #should exit the question set 2 loop
        break


    #question set 3 comedies


    #print("\nYour score after the first part of this adventure is ", score)
    #print("\nThe next set of questions will be tougher...\n \n \n")

    question3_bank = ["I want you to round up every vicious criminal and gunslinger in the West. Take this down: 'I want rustlers, cut-throats, murderers, bounty hunters, desperadoes, mugs, pugs, thugs, nit-wits, half-wits, dim-wits, vipers, snipers, con-men, Indian agents, Mexican bandits, muggers, buggerers, bush-whackers, horn-swagglers, horse-thieves, bull-dykes, train-robbers, bank-robbers, ass-kickers, shit-kickers, and Methodists! Ha, ha, ha, ha!",
    "What makes you think she's a witch?\nWell, she turned me into a newt!\nA newt?\nI got better.\nBurn her anyway!\n",
    "Hey, don't knock masturbation. It's sex with someone I love.",
    "Joey, do you like movies about gladiators?",
    "We Romans are rich. We've got a lot of gods. We've got a god for everything. The only thing we don't have a god for is premature ejaculation, but I hear that that's coming quickly.",
    "Look, there is a woman in a car. Can we follow her? And maybe make the sexy-time with her?!"
    ]
    question3_list = question3_bank
    answer3_bank = ["blazing saddles",
    "monty python",
    "annie hall",
    "airplane!",
    "history of the world part 1",
    "borat"
    ]
    answer3_list = answer3_bank

    for i,x in enumerate(question3_list):
        attempt = 4
        print("What movie is this line from?\n\n" + question3_list[i])

        user = input()

        if user == answer3_list[i]:
            score += 10
            sp3 += 10
            print('\nCongrats on getting that right! Here comes the next one!')
        else:
            while user != answer3_list[i] and attempt > 0:
                attempt -= 1
                score -= 1
                if sp3 > 0:
                    sp3 -= 1
                print('Nice try but not quite the answer. You have' ,attempt, "attempts left.")
                print("\n\nWhat movie is this line from?\n" + question3_list[i])
                user = input()
            if attempt == 0:
                print('You have run out of attempts for this question. Dont worry, a new one is coming :)')



    #question set 4 Star Wars
    question4_bank = ["What were Luke's aunt and uncle's job on Tatooine?",
    "In how many languages is C-3P0 fluent?",
    "Who actually shot first?",
    "Which species stole the plans to the Death Star?",
    "Which bounty hunter in The Empire Strikes Back is wearing an old costume from a Doctor Who episode?",
    "What odds does C-3P0 give Han for successfully navigating the asteroid field?",
    "Darth Vader's chestpiece has some writing on it. What does it translate to?"
    ]
    question4_list = question4_bank
    answer4_bank = ["moisture farmers",
    "more than 6 million",
    "han Solo",
    "bothans",
    "bossk",
    "3720 to 1",
    "His deeds will not be forgiven, until he merits."
    ]
    answer4_list = answer4_bank

    for i,x in enumerate(question4_list):
        attempt = 4
        print("What movie is this line from?\n\n" + question4_list[i])

        user = input()

        if user == answer3_list[i]:
            score += 10
            sp4 += 10
            print('\nCongrats on getting that right! Here comes the next one!')
        else:
            while user != answer3_list[i] and attempt > 0:
                attempt -= 1
                score -= 1
                if sp4 > 0:
                    sp4 -= 1
                print('Nice try but not quite the answer. You have' ,attempt, "attempts left.")
                print("\n\nWhat movie is this line from?\n" + question4_list[i])
                user = input()
            if attempt == 0:
                print('You have run out of attempts for this question. Dont worry, a new one is coming :)')

    #question set 5 gg
    question5_bank = ["Don Corleone meets three men at his daugther's wedding reception. Who was the one that just wanted to thank him for being invited?",
    "A bomb goes off in the opening scene of the movie. Who is holding it when it goes off?",
    "Al Capone does murder one person somewhere in the movie. During this scene, what is his weapon of choice?",
    "He puts one of yours in the hospital, you put one of his in the ________.",
    "Who issues Frank Nitti a gun license?",
    " What is the last line of the movie, Untouchables?"]
    question5_list = question5_bank
    answer5_bank = ["luca brasi",
    "a little girl",
    "baseball bat",
    "morgue",
    "mayor of chicago",
    "i think ill have a drink"
    ]
    answer5_list = answer5_bank

    tc = 0

    for i,x in enumerate(question5_list):
        attempt = 4
        print("Read the question and give an answer. First time go's get more points than re-trains :p\n\n" + question5_list[i])

        user = input()

        if user == answer5_list[i]:
            score += 10
            sp5 += 10
            print('\nCongrats on getting that right! Here comes the next one!')
        else:
            while user != answer5_list[i] and attempt > 0:
                attempt -= 1
                score -= 1
                if sp5 > 0:
                    sp5 -= 1
                print('Nice try but not quite the answer. You have' ,attempt, "attempts left.")
                print("\n\nWhat movie is this line from?\n" + question5_list[i])
                user = input()
            if attempt == 0:
                print('You have run out of attempts for this question. Dont worry, a new one is coming :)')

        #question set 6

    print('You have made it to the final shallenge of the adventure. Congratulations!\n\n')

    questions_bank = ["I'm a mog - half man, half dog. I'm my own best friend.",
    "And all the while you’re just really wondering are we gonna get hopped up enough to make some bad decisions? Perhaps play a little game called 'just the tip.' Just for a second, just to see how it feels. Or, ouch, ouch, you’re on my hair.",
    "We've been goin' about this all wrong. This Mr. Stay-Puffs' okay! He's a sailor, he's in New York. We get this guy laid, we won't have any trouble!",
    "Disturbin' the peace? I got thrown out of a window! What's the f--kin' charge for getting pushed out of a moving car, huh? Jaywalking? This is bulls--t.",
    "But where in New York can one find a woman with grace, elegance, taste and culture? A woman suitable for a king.\n""Queens!",
    "The royal penis is clean, your Highness!",
    "There's no reason to become alarmed, and we hope you'll enjoy the rest of your flight. By the way, is there anyone on board who knows how to fly a plane?",
    "Oh, and this one time, at band camp, I stuck a flute in my pussy...",
    "What? Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no!",
    "That is my least vulnerable spot.",
    "It's just a flesh wound.",
    "I'm about to do to you what Limp Bizkit did to music in the late '90s",
    "Greater good?' I am your wife! I'm the greatest good you're ever gonna get!",
    "We get the warhead and we hold the world ransom for…. One million dollars",
    "Leave the gun. Take the cannoli.",
    "Bears. Beets. Battlestar Galactica.",
    "I never thought I’d say this, but I think I ate too much bone marrow",
    "The Almighty tells me he can get me out of this mess, but he's pretty sure you're fucked.",
    "Out here, due process is a bullet!",
    "I could have killed 'em all, I could kill you. In town you're the law, out here it's me. Don't push it. Don't push it or I'll give you a war you won't believe. Let it go. Let it go.",
    "Remember Sully when I promised to kill you last? I lied.",
    "Lighten up, Francis.",
    "My name is Gunnery Sergeant Highway. I've drunk more beer, banged more quiff, pissed more blood, and stomped more ass than all of you numb-nuts put together.",
    "A gun is a tool, Marian; no better or no worse than any other tool: an ax, a shovel or anything. A gun is as good or as bad as the man using it. Remember that.",
    "Dying ain't much of a living, boy.",
    "We'll give you a fair trial, followed by a first-class hanging!",
    "Well, if you’re waitin’ for a woman to make up her mind, you may have a long wait.",
    "When you hang a man, you better look at him.",
    "I’ve killed everything that walks or crawls at one time or another. And I’m here to kill you, Little Bill, for what you done to Ned.",
    "You see, in this world, there’s two kinds of people, my friend; those with loaded guns and those who dig. You dig."]

    answers_bank = ["spaceballs",
    "wedding crashers",
    "ghostbusters",
    "beverly hills cops",
    "coming to america",
    "coming to america",
    "airplane",
    "american pie",
    "animal house",
    "casablanca",
    "monty python",
    "dead pool",
    "the incredibles",
    "austin powers international man of mystery",
    "the godfather",
    "the office, jim",
    "the office, dwight",
    "braveheart",
    "the green berets",
    "rambo",
    "commando",
    "stripes",
    "heart break ridge",
    "shane",
    "the outlaw josey wales",
    "silverado",
    "pale rider",
    "hang 'em high",
    "unforgiven",
    "the good, the bad, the ugly"]

    questions_list = questions_bank
    answers_list = answers_bank

    test_counter = 0
    tests_left = 6

    print('In this challenge, you will be presented with a series of questions that you will have to answer.'
          'Theses questions are from movies and shows. Lets see if you can name the movie or show they are from.\n\n\n')

    while test_counter < 6:
        tests_left -= 1

        r = random.randint(0, len(questions_list)- 1)

        print('What movie or show is this quote from: "',questions_list[r],'"?')


        user = input().lower()
        print('\n')

        if user == answers_list[r]:
            score += 10
            sp6 += 10
            print('Thats Correct! Moving on to the next question...\n \n')
        else:
            if score > 0:
                score -= 1
            if sp6 > 0:
                sp6 -= 1
            print('\nSorry that was incorrect. Dont let it bother you! you still have ', tests_left, " questions left before you finish this challenge.")

        questions_list.remove(questions_list[r])
        answers_list.remove(answers_list[r])

        test_counter += 1
    print('you have completed this question set and have completed the adventure. congrats!')


#function for adventure 6
#The kights who say Knee, an adventure into memes
def adventure6():
    print('Congradulations on finishing your fifth adventure.')

    meme_lst1 = []
    animeme = []
    meme_lst2 = []


    pass

#function for adventure 7
#Best beer in the world
def adventure7():
    print('Herzlichen Glückwunsch zum Abschluss Ihres sechsten Abenteuers.')

    #find beers and provide description of their taste
    #have user input the beer name based of taste description
    pass

#function for adventure 8
#City of love (Pari)
def adventure8():
    print('Félicitations pour avoir terminé votre septième aventure.')
    #ask questions based on rom coms and display memes for right and wrong answers
    pass

#function for adventure 9
#Barcalona is king
def adventure9():
    print('Felicitaciones por terminar su octava aventura.')
    #
    pass

#function for adventure 10
#Italian job
def adventure10():
    print('Congratulazioni per aver terminato la tua nona avventura.')
    #
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

#write a function to rickroll scrubs
#b"import webbrowser\nwebbrowser.open('https://www.youtube.com/watch?v=oHg5SJYRHA0',new=1)"
