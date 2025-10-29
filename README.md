# Markowitz vs Black-Litterman Portfolio Optimizer

This project implements and compares **Markowitz Mean-Variance Optimization** and **Black-Litterman Portfolio Optimization** for a custom set of stocks. It demonstrates portfolio construction, backtesting, and performance analysis using Python.

---

## 📊 Features

- Download historical stock price data via **Yahoo Finance** (`yfinance`).  
- Calculate **daily and monthly returns**, mean returns, and covariance matrix.  
- **Markowitz Optimization:** Compute optimal weights for maximum return given a risk aversion parameter.  
- **Black-Litterman Optimization:** Incorporate subjective market views into portfolio weights.  
- Backtest portfolios with **different rebalancing frequencies**: no rebalance, monthly, quarterly.  
- Visualize cumulative portfolio value and compare risk-return metrics.  
- Generate performance summary tables including:
  - Annualized Return  
  - Annualized Volatility  
  - Sharpe Ratio  
  - Max Drawdown  

---

## 🛠️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/<your-username>/markowitz-bl-optimizer.git
cd markowitz-bl-optimizer
python -m pip install -r requirements.txt
