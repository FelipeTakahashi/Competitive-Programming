amount_people = int(input())
s_size, m_size = [], []

requested = [int(a) for a in input().split()]

for i in range(len(requested)):
    if (requested[i] == 1):
        s_size.append(requested[i])
    if (requested[i] == 2):
        m_size.append(requested[i])

s_needed = int(input())
m_needed = int(input())

if (s_needed == len(s_size) and m_needed == len(m_size)): print("S")
else: print("N")
