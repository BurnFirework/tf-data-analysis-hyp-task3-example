import pandas as pd
import numpy as np

from scipy.stats import ttest_ind


chat_id = 860138765

def solution(x: np.array, y: np.array) -> bool:
    imp_crit = 0.04
    t, p_value = ttest_ind(x, y, equal_var=False)
    return p_value < imp_crit
