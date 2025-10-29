from src.data_loader import load_data
from src.optimizer import markowitz_optimizer, black_litterman_optimizer
from src.backtest import backtest_rebalance
from src.plotting import plot_cumulative_results

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA"]
start, end = "2020-01-01", "2025-01-01"

# Load data
data, returns = load_data(tickers, start, end)
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Markowitz optimization
opt_weights_mv = markowitz_optimizer(mean_returns, cov_matrix)

# Black-Litterman optimization
w_mkt = [1/len(tickers)]*len(tickers)
delta = 2.5
Pi = delta * cov_matrix.values.dot(w_mkt)

P = [[0]*len(tickers)]
P[0][tickers.index("TSLA")] = 1
P[0][tickers.index("MSFT")] = -1
Q = [0.02]
omega = [[0.0001]]

opt_weights_bl, _ = black_litterman_optimizer(cov_matrix, tickers, Pi, P, Q, omega)

# Backtest portfolios
rebalance_periods = {
    "No Rebalance": returns.index,
    "Monthly": returns.resample('M').mean().index,
    "Quarterly": returns.resample('Q').mean().index
}

cumulative_results = {}
for freq, dates in rebalance_periods.items():
    cumulative_results[f"Markowitz - {freq}"] = backtest_rebalance(opt_weights_mv, returns, dates)
    cumulative_results[f"BL - {freq}"] = backtest_rebalance(opt_weights_bl, returns, dates)

# Plot cumulative portfolios
plot_cumulative_results(cumulative_results)
