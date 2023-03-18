#백준 n7568 silver5
#덩치

#2:41 시작
#정렬한담에 해시로 해야되나? 하다가 정렬 기준등등 생각이 안나서 그냥 단순하게 한 사람마다 다른 모든 사람 일일히 체크하기로
#3:00 통과
import sys

def big() :
    N = int(input())
    people = []
    for i in range(N) :
        w, t = map(int, sys.stdin.readline().split())
        people.append([w,t])
    bigppl = []
    for i in range(len(people)) :
        p_w = people[i][0]
        p_t = people[i][1]
        pp = people.copy()
        pp.remove(people[i])
        big = 1
        for w,t in pp :
            if (w - p_w)*(t - p_t)>0 and w - p_w >=0 :
                big += 1
        bigppl.append(big)
    return ' '.join(list(str(i)for i in bigppl))
print(big())