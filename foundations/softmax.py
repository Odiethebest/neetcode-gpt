import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        big = max(z)
        exp_z = np.exp(z - big)
        sum_exp = np.sum(exp_z)
        res = np.round((exp_z / sum_exp),4)
        return res
