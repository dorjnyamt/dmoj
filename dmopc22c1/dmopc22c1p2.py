from itertools import combinations

n, npair = map(int, input().split())
people = list(map(int, input().split()))
pairs = []
for i in range(npair):
    pair = set(map(int, input().split()))
    pairs.append(pair)