competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]

results = [0, 0, 1]


# def tournamentWinner(competitions, results):
#     """
#     Returns the winner of the tournament.
#     :param competitions:
#     :param results:
#     :return:
#     """
#     # Write your code here.
#
#     myDict = {}
#     for i in competitions:
#         for j in i:
#             myDict[j] = 0
#
#     for i in range(0, len(results)):
#         val = competitions[i]
#         if results[i] == 0:
#             myDict[val[1]] += 3
#             myDict[val[0]] += 0
#         else:
#             myDict[val[0]] += 3
#             myDict[val[1]] += 0
#
#     max_value = max(myDict, key=myDict.get)
#     print('max_value')
#     print(max_value)
#     return max_value

def tournamentWinner(competitions, results):
    # Write your code here.
    teamPoints = {}
    currentWinner = '', 0
    for competition, result in zip(competitions, results):
        print(competition)
        print(result)
        winner = competition[not result]
        print('winner: ', winner)
        loser = competition[result]
        print('loser: ', loser)

        if winner not in teamPoints: teamPoints[winner] = 0
        teamPoints[winner] += 3

        print('currentWinner[1]: ', currentWinner[1])
        if teamPoints[winner] > currentWinner[1]:
            currentWinner = winner, teamPoints[winner]

        print('currentWinner:', currentWinner)
    print(teamPoints)
    print(currentWinner[0])
    return currentWinner[0]


tournamentWinner(competitions, results)


