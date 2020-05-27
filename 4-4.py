winners = []
for i in range(1,6):
    winner = int(input("introduce al ganador " + str(i) + ": "))
    winners.append(winner)
winners.sort()
print(winners)
