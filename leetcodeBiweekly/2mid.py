from typing import List
import bisect

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i: int, delta: int) -> None:
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def sum(self, i: int) -> int:
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    def range_sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Coordinate compression (by value)
        vals = sorted(set(nums))
        idx_of = {v: i for i, v in enumerate(vals)}
        ft = Fenwick(len(vals))

        # Process in decreasing |x| so already-inserted have |b| >= |a|
        order = sorted(range(n), key=lambda i: (abs(nums[i]), i), reverse=True)

        zeros_seen = 0
        ans = 0

        for t in order:
            a = nums[t]
            A = abs(a)

            # Interval 1: [a - A, a + A]
            l1, r1 = a - A, a + A
            li1 = bisect.bisect_left(vals, l1)
            ri1 = bisect.bisect_right(vals, r1) - 1
            c1 = ft.range_sum(li1, ri1)

            # Interval 2: [-a - A, -a + A]
            l2, r2 = -a - A, -a + A
            li2 = bisect.bisect_left(vals, l2)
            ri2 = bisect.bisect_right(vals, r2) - 1
            c2 = ft.range_sum(li2, ri2)

            # Union of the two intervals (they meet only at 0)
            ans += c1 + c2 - zeros_seen

            # Insert current value into the structure
            ft.add(idx_of[a], 1)
            if a == 0:
                zeros_seen += 1

        return ans
