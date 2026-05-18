import math
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        cnt = 0
        x = init
        #base case
        if iterations == 0:
            return x

        while cnt < iterations:
            x = x - learning_rate * 2 * x
            cnt += 1
        return round(float(x), 5)