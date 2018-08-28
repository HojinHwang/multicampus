# lotto1.py
# 1. 1 ~ 45 중 6개 뽑기, range(1,46), sample
# 2. 정렬, sorted
# 3. 5게임, while
# 4. 합계가 100 ~ 170 사이만 사용

import random
cnt = 0
while cnt < 5:
    myballs = sorted(random.sample(range(1,46), 6))
    if 100 <= sum(myballs) <= 170:
        print(myballs)
        cnt += 1

