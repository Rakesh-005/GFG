from math import log, floor, ceil

class Solution:
    def nearestPower(self, N, M):
        if N <= 1:
            return 1

        low_exp = floor(log(N, M))
        high_exp = ceil(log(N, M))

        low_power = M ** low_exp
        high_power = M ** high_exp

        # Compare distances
        dist_low = abs(low_power - N)
        dist_high = abs(high_power - N)

        if dist_low < dist_high:
            return low_power
        elif dist_high < dist_low:
            return high_power
        else:
            return max(low_power, high_power)  # return greater if tie
