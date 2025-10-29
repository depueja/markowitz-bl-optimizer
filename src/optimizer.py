import cvxpy as cp
import numpy as np
import pandas as pd

def markowitz_optimizer(mean_returns, cov_matrix, risk_aversion=5):
    n = len(mean_returns)
    w = cp.Variable(n)
    risk = cp.quad_form(w, cov_matrix.values)
    ret = mean_returns.values @ w
    prob = cp.Problem(cp.Maximize(ret - risk_aversion*risk), [cp.sum(w) == 1, w >= 0])
    prob.solve()
    return pd.Series(w.value, index=mean_returns.index)

def black_litterman_optimizer(cov_matrix, tickers, Pi, P, Q, omega, tau=0.05, risk_aversion=5):
    Sigma = cov_matrix.values
    P = np.array(P)
    Q = np.array(Q)
    omega = np.array(omega)

    A = np.linalg.inv(tau * Sigma) + P.T @ np.linalg.inv(omega) @ P
    b = np.linalg.inv(tau * Sigma).dot(Pi) + P.T @ np.linalg.inv(omega).dot(Q)
    mu_bl = np.linalg.inv(A).dot(b)
    mu_bl = pd.Series(mu_bl.flatten(), index=tickers)

    n = len(tickers)
    w = cp.Variable(n)
    risk = cp.quad_form(w, Sigma)
    ret = mu_bl.values @ w
    prob = cp.Problem(cp.Maximize(ret - risk_aversion*risk), [cp.sum(w) == 1, w >= 0])
    prob.solve()
    return pd.Series(w.value, index=tickers), mu_bl
