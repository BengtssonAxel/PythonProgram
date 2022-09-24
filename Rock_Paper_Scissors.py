import random
from re import S

validStart = True
playerScore = 0
aiScore = 0

def AiChoice():
    aiRandom = random.randint(0, 2)

    match aiRandom:
        case 0:
            return 'R'
        case 1:
            return 'P'
        case 2: 
            return 'S'

def Comparitor(playerMove, aiMove):
    print('')
    caseSelector = 0

    if playerMove == aiMove:
        caseSelector = 0
    elif playerMove == 'R' and aiMove == 'S':
        caseSelector = 1
    elif playerMove == 'P' and aiMove == 'R':
        caseSelector = 1
    elif playerMove == 'S' and aiMove == 'P':
        caseSelector == 1
    else:
        caseSelector = 2

    match caseSelector:
        case 0:
            print('Great minds think alike and none of us scored a point! Let us go again!')
            return
        case 1:
            global playerScore 
            playerScore += 1
            print('Well fuck! you won a point but it is not over yet!')
            return
        case 2:
            global aiScore 
            aiScore += 1
            print('You suck! I won a point! HAHAHAHAHA')
            return

def ScorePrinter():
    global playerScore
    global aiScore
    print('')
    print('Current score:')
    print('Player: ' + str(playerScore))
    print('Devil:  ' + str(aiScore))
    print('First to 5 wins!')
    print('')
    if playerScore == 5 or aiScore == 5:
        return False
    else:
        return True

print('I welcome you to a battle of Rock, Paper, Scissors!')
play = input('Would you like to challenge me to a battle? ').lower()
print('')

if play != "yes":
    print("HAHA you whimp! You did not dare to challenge me!")
    quit()
else:
    print('Here are some rules: ')
    print('For ROCK you will write "R"')
    print('For PAPER you will write "P"')
    print('Aaaand for SCISSORS you will write.... "S"')
    print('')
    while validStart:
        playerMove = input('So... what will be your first move then? ').upper()
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            validStart = False
            Comparitor(playerMove, AiChoice())
        else:
            print('That is not a legit move! Try again!')

print('Now we have stared! May the best player win! HOHAWAHA')
while ScorePrinter():
    playerMove = input('What will your next move be? ').upper()
    if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
        Comparitor(playerMove, AiChoice())
        print('')
    else:
        print('That is not a legit move! Try again!')

if playerScore == 5:
    print('Well you won and can keep your fucking soul...')
else:
    print('I fucking won! Now give me your soul and fuck off!')