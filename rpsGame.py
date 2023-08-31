import random
rpsChoices = ["Rock","Paper","Scissors"]
playerPoints = 0
cpuPoints = 0
def rpsGame():
    
    cpuDecision = random.choice(rpsChoices)
    playerDecision = input('Rock (0), Paper (1) or Scissors? (2): ')
    playerDecision = int (playerDecision)
    #logic for player choosing Rock
    if playerDecision == 0:
        if cpuDecision == rpsChoices[0]:
            print('Both rock, it\'s a tie!')
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        elif cpuDecision == rpsChoices[1]:
            print('CPU chose Paper, so CPU wins.')
            cpuPoints = cpuPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        else:
            print('CPU chose Scissors, so you win!')
            playerPoints = playerPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
    #logic for player choosing Paper
    elif playerDecision == 1:
        if cpuDecision == rpsChoices[0]:
            print('CPU chose Rock, so you win!')
            playerPoints = playerPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        elif cpuDecision == rpsChoices[1]:
            print('Both Paper, it\'s a tie!')
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        else:
            print('CPU chose Scissors, so CPU wins.')
            cpuPoints = cpuPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
    #logic for player choosing Scissors
    elif playerDecision == 2:
        if cpuDecision == rpsChoices[0]:
            print('CPU chose Rock, so CPU wins.')
            cpuPoints = cpuPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        elif cpuDecision == rpsChoices[1]:
            print('CPU chose Paper, so you win!')
            playerPoints = playerPoints + 1
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
        else:
            print('Both Scissors, it\'s a tie!')
            print('Player: ', playerPoints, ' CPU: ', cpuPoints)
            rpsGame();
    #logic for player choosing an invalid input
    else:
        print('Invalid input.')
        rpsGame();
rpsGame();
    
