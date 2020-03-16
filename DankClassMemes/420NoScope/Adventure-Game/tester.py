import random
import math

score = 0
sp3 = 0

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
