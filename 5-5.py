subjects = { "mate" : 6, "historia" : 7, "ciencias" : 9 }
total = subjects["mate"] + subjects["historia"] + subjects["ciencias"]
course = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_credits = 0
for subject, credits in subjects.items():
    print(subject, 'tiene', credits, 'créditos')
    total_credits += credits
print('Número total de créditos del curso: ', total)

print(subjects.items())