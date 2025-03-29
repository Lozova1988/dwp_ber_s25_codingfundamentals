scores = [15, 19, 17, 12, 17, 13]
print(scores[0])


print(scores[len(scores)-1])

print(max(scores))
print(min(scores))

scores.append(21)
print(scores)

scores.sort()
print(scores)

while 17 in scores:
    scores.remove(17)
    print(scores)

scores.pop(3)
print(scores)