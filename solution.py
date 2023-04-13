import pandas as pd
import numpy as np

from scipy.stats import ttest_1samp


chat_id = 860138765

def solution(x: np.array) -> bool:
    max_cost = 300
    imp_crit = 0.04
    t, p_value = ttest_1samp(x, max_cost)
    return (p_value < imp_crit)
