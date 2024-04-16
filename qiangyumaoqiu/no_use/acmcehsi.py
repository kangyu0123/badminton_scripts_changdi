import sys

while True:
    try:
        line1 = sys.stdin.readline().strip()
        N, M = map(int, line1.split())
        line2 = sys.stdin.readline().strip().split(' ')
        scores = []
        for x in line2:
            scores.append(int(x))

        for _ in range(M):
            line_1 = sys.stdin.readline().strip()
            a = int(line_1[2])
            b = int(line_1[4])
            if a > b:
                a, b = b, a
            if line_1[0] == "Q":
                print(max(scores[a-1:b]))
            elif line_1[0] == "U":
                scores[a-1] = b
            else:
                print("输入错误")
                continue
    except:
        break