class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
     
        b = 2 * k + 1
        def ceil_div(a: int, b: int) -> int:
            return (a + b - 1) // b
        return ceil_div(n, b) * ceil_div(m, b)
