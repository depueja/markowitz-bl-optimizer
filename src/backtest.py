import numpy as np
import pandas as pd

def backtest_rebalance(weights, returns_df, rebalance_dates):
    """
    Compute cumulative portfolio value with optional rebalance dates.
    """
    cumulative = [100]
    current_weights = np.array(weights)
    reb_flags = returns_df.index.isin(rebalance_dates)

    for i in range(len(returns_df)):
        if reb_flags[i]:
            current_weights = np.array(weights)
        port_ret = np.dot(returns_df.iloc[i].values, current_weights)
        cumulative.append(cumulative[-1] * (1 + port_ret))

    return pd.Series(cumulative[1:], index=returns_df.index)
