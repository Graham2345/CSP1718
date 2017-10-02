team_name = "Team Cardi"
startegy_name = 'I Can Get Em Both Ion Wanna Choose'
strategy_description = 'Use the inverse average of their moves against them, unless its always betray'
def move (my_history, their_history, my_score, their_score):
    numbs = their_history.count('b')
    if (float(sum(numbs)) / max(len(round))) = 1
        return 'b'
    else
        if (float(sum(their_history)) / max(len(round))) < .5
        return 'b'
    else
        return 'c'