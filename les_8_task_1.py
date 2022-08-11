# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

friends = int(input('How many friends you met: '))

graph = []

for i in range(friends):
    row = [1] * friends
    row[i] = 0
    graph.append(row)

print(*graph, sep = '\n')

handshakes = 0

for row in graph:
    for i in row:
        handshakes += 1

print(f'Total handshakes: {handshakes}')
