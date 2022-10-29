n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [0]*(n+1)
for a_i in a:
    dp[a_i] = a_i

for i in range(1, n+1):
    m_takahashi = 0
    if dp[i] == 0:
        for a_i in a:
            if a_i > i:
                break
            m_aoki = 0
            for a_j in a:
                if a_j > i-a_i:
                    break
                elif a_j == i-a_i:
                    m_aoki = a_j
                    break
                m_aoki = max(m_aoki, (i-a_i-a_j)-dp[i-a_i-a_j]+a_j)
            m_takahashi = max(m_takahashi, i-m_aoki)
        dp[i] = m_takahashi

print(dp[n])