n = int(input())
flows = []

for i in range(n):
    flows.append(int(input()))

while True:
    command = int(input())
    if command == 77:
        break
    if command == 99:
        where = int(input()) - 1
        ratio = int(input())
        flow = flows.pop(where)
        flows.insert(where, flow * ratio / 100)
        flows.insert(where + 1, flow * ((100 - ratio) / 100)) 
    if command == 88:
        where = int(input()) - 1
        flow = flows.pop(where)
        flows[where] = flows[where] + flow

flows = ' '.join(map(str, map(round, flows)))
print(flows)