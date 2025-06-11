import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
multitap = []
cnt = 0  # 플러그 뽑는 횟수
for i in range(k):
    if lst[i] in multitap:
        continue
    if len(multitap) < n:
        multitap.append(lst[i])
    else:
        for popTap in lst[i:k]:
            if popTap in multitap:
                if multitap[-1] == tap:
                    multitap.remove(tap)
                    cnt+=1
                    break
        
        for tap in multitap:
            if tap in lst[i:k]:
                if multitap[-1] == tap:
                    multitap.remove(tap)
                    cnt+=1
                    break
                
                ccnt+=1
            else:
                multitap.remove(tap)
                cnt+=1
                break
        # if ccnt == n:
        #     for m in lst[k-1:i:-1]:
        #         for tap in multitap:
        #             if m == tap:
        #                 multitap.remove(tap)
        #                 cnt+=1
        #                 ccnt -=1
        #         if ccnt != n:
        #             break
        multitap.append(lst[i])
print(cnt)