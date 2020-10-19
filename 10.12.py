import random
from collections import Counter
n = 5
m = 5
matrix = [[random.randrange(0, 10) for y in range(n)] for x in range(m)]
print(*matrix, sep='\n')
most_common = [(i, Counter(x).most_common(1)[0]) for i, x in enumerate(matrix, start=1)]
print(*sorted(most_common, key=lambda x: int(x[1][1]), reverse=True), sep='\n')
