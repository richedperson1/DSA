
import matplotlib.pyplot as plt

import numpy as np


def checkingWays(n):
    if n <= 4:
        return 1

    return checkingWays(n-1)+checkingWays(n-4)


ans = []
for i in range(100):
    ans.append(checkingWays(16))


plt.plot(range(100), np.array(ans))
