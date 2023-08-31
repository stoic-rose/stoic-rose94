import random
rpsChoices = ["Rock","Paper","Scissors"]

def rpsGame():
    cpuDecision = random.choice(rpsChoices)
    playerDecision = input('Rock (0), Paper (1) or Scissors? (2)')
    if playerDecision == 0:
        if cpuDecision == rpsChoices[0]:
            print('Both rock, it\'s a tie!')
        elif cpuDecision == rpsChoices[1]:
            print('CPU chose Paper, so CPU wins.')
        else:
            print('CPU chose Scissors, so you win!')
    elif playerDecision == 1:
        if cpuDecision == rpsChoices[0]:
            print('CPU chose Rock, so you win!')
        elif cpuDecision == rpsChoices[1]:
            print('Both Paper, it\'s a tie!')
        else:
            print('CPU chose Scissors, so CPU wins.')
    elif playerDecision == 2:
        if cpuDecision == rpsChoices[0]:
            print('CPU chose Rock, so CPU wins.')
        elif cpuDecision == rpsChoices[1]:
            print('CPU chose Paper, so you win!')
        else:
            print('Both Scissors, it\'s a tie!')
    else:
        print('Invalid input.')
        rpsGame();
rpsGame();
