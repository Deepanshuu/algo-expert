competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]

results = [0, 0, 1]


def tournamentWinner(competitions, results):
    # Write your code here.
    myDict = {'HTML': 0, 'C#': 0, 'Python': 0}

    for i in range(0, len(results)):
        val = competitions[i]
        if results[i] == 0:
            myDict[val[1]] += 3
            myDict[val[0]] += 0
        else:
            myDict[val[0]] += 3
            myDict[val[1]] += 0

    max_value = max(myDict, key=myDict.get)
    print('max_value')
    print(max_value)
    return max_value

tournamentWinner(competitions, results)
