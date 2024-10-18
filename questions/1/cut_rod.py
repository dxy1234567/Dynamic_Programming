import numpy as np

N = 10

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def result(res):
    print("The result is: {}".format(res))

def cut_rod(n):
    if n == 1:
        return prices[0]
    dp = np.zeros(n)
    dp[0] = prices[0]

    # 填表 
    for i in range(1, n):
        max = prices[i]
        for j in range(0, i):
            a = dp[i - j - 1]
            b = prices[j]
            q = a + b
            if q > max:
                max = q
        dp[i] = max
    
    result(dp[n - 1])
    return dp[n - 1]

cut_rod(7)