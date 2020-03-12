""" following code is a program Quiz-Game in python.
    it contains 4 categories with 5 questions each.
    categories are: World-Quiz, Time-Quiz, Sports-Quiz, History-Quiz.

    programmer: maverick sonawane
    github: mavericksonawane
    email : mavericksonawane@gmail.com

    ************************* MAYUR SONAWANE ********************************
    Scores will be recorded, make every option Count ...
        ENJOY :)
#BeAMaverick
"""

print("*** Yo! Welcome to the most HARD quiz-game in the word by maverick-sonawane***")
name = input(' WHATS YOUR NAME ? \n:')
print('WELCOME,', name)
ans = input('Are you ready?  (y/n): ')
score = 0
total_q = 5

if ans.lower() == 'y':
    print('On which topic would you like to test your brain? ')
    ans = input('a. World \nb. Time \nc. Sports  \nd. History \n(a/b/c/d): \n')

    if ans.lower() == 'a':
        print('** Welcome To The World-quiz** \n Their are 5 questions, Try to score max ')

        # 1
        print('1. How many people are left handed in the World ? ')
        ans = input('a. 23% b. 11%  c. 37% d. 52%  \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 11%')

        print('2. Which is the coldest place in the World  ?')
        ans = input('a. Iceland b. Himalayas c. Antarctica d. North-Pole \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Antarctica')

        print('3. What is the AGE of the Earth ?')
        ans = input('a. 2.62billlions b. 4.98billions c. 3.71billions d.4.54billions \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 4.54billions')

        print('4. How many spoken languages are there in the World ?')
        ans = input('a. 6500 b. 10216 c. 9514 d. 720 \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 6500')

        print('5. Which is the smallest country in the World ?')
        ans = input('a. Nauru b. Tuvalu c. Vatican-City d. Liechtenstein \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Vatican-City')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Einstein !!! ")
        elif Marks > 50:
            print("You Played Well")
        elif Marks < 30:
            print("You Know Nothing Jon Snow :(")
        print("Goodbye", name, ". It was nice having you :)")

    # 2
    elif ans.lower() == 'b':
        print('** Welcome To The Time-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. How many SECONDS are there in a year ?')
        ans = input('a. 31,556,000 b. 30,489,580 c. 25,752,203 d. 36,158,495 \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 31,556,000')

        print('2. What is the lifespan of a squirrel ? (years)')
        ans = input('a. 15 b. 10 c. 9 d. 30 \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 9')

        print('3. Hpw many hours a night Einstein slept ?')
        ans = input('a. 12 b. 15 c. 24 d. 10 \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 10')

        print('4. On average, How many times human BLINK a day ?')
        ans = input('a. 30,000 b. 25,000 c. 20,000 d. 0 \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 25,000')

        print('5. The average person has over how many DREAMS a year ?')
        ans = input('a. 2,567 b. 1,460 c. 2,141 d. 9,999 \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1,460')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Einstein !!! ")
        elif Marks > 50:
            print("You Played Well")
        elif Marks < 30:
            print("You Know Nothing Jon Snow :(")
        print("Goodbye", name, ". It was nice having you :)")

    # 3
    elif ans.lower() == 'c':
        print('** Welcome To The Sport-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. The Olympic flag was designed in ?')
        ans = input('a. 1915 b. 1925 c. 1913 d. 1900 \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1913')

        print('2. Which is most FOLLOWED sport ?')
        ans = input('a. Golf b. Soccer c. Base-Ball d. Wresling \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Soccer')

        print('3. Volley was invented in year ?')
        ans = input('a. 1895 b.1901 c. 1925 d. 1702 \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1895')

        print('4. The average golf ball has how many DIMPLES ?')
        ans = input('a. 308 b. 452 c. 336 d. 999 \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 336')

        print('5. Olympic has how many SPORTS ?')
        ans = input('a. 20 b. 29 c. 54 d. 28 \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 28')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Einstein !!! ")
        elif Marks > 50:
            print("You Played Well")
        elif Marks < 30:
            print("You Know Nothing Jon Snow :(")
        print("Goodbye", name, ". It was nice having you :)")

    # 4
    elif ans.lower() == 'd':
        print('** Welcome To The History-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. What was Sir Issac Newtons age when he discovered the LAW of GRAVITY ?')
        ans = input('a. 19 b. 23 c. 25 d. 21 \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 23')

        print('2. How many years Leonardo Da Vinci took to paint MONA LISA ?')
        ans = input('a. 18 b.15 c. 10 d. 2 \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 10')

        print('3. The $ sign was introduced in ?')
        ans = input('a. 1788 b. 1821 c. 1762 d. 1811 \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1788')

        print('4. Which country first used PAPER MONEY ?')
        ans = input('a. Germany b. USA c. Russia d. China \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is China')

        print('5. Disneyland Opened in year ?')
        ans = input('a. 1902 b. 1916 c. 1898 d. 1955 \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1955')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Einstein !!! ")
        elif Marks > 50:
            print("You Played Well")
        elif Marks < 30:
            print("You Know Nothing Jon Snow :(")
            print("Goodbye", name, ". It was nice having you :)")

if ans.lower() == 'n':
    print("Sad to see you leave :(")





















