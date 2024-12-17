list1 = []; list2 = []
with open('day1/input.txt', 'r') as file:
    for line in file:
        a,b = line.strip().split()
        list1.append(int(a))
        list2.append(int(b))
s1,s2 = sorted(list1), sorted(list2)

print(sum([abs(a - b) for a, b in zip(s1, s2)])) #2769675

print(sum(a*s2.count(a) for a in s1)) #24643097