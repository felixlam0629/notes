# working Notes

"""
trade phoebe other factors

main
1) backtest phoebe good endpoint_list
- backtest
2) trade phoebe good endpoint_list

3) adopt different model to backtestEngine
* rmb Signal.py changed in non-24h backtesting

Optimization for 25Q1
- Resampling
- Modelling

waiting
- glassnode resampling
(method: past mean, past total, now_data) -> 12h, 8h, 6h, 4h, 2h, 1h
- optimize phoebe current endpoint (resampling only)
- backtest taker buy/sell volume (sd, different resolution, momentum, reversion)
--------------------------------------------------
other

Backtest

(MP issue)
 1 BacktestProcessor -> put into BacktestEngine
 2 BacktestProcessor -> stay remaining function the same

(Folder issue)
 1 Issue: various model in a folder, a good and a bad -> deleted the whole folder LMAO

 1 Solution: always put symbol at the last (BTC…)

Questions
Data
 1 How to fill? As 1) you dun know which row is missed, 2) you dun know how many rows is missed

Backtest
 1 Modelling -> params how to set?
 2 Open/ exit logic -> other than 1) > ut// <lt, 2) flat-at-0, anymore?

Notes
1 Handle skewness data
root, log, yeo-johnson, rank, box-cox

 1 Validation method
walk-forward, split, k-fold

 1 Params
Window: 151, threshold 1
Window: 129, threshold 0.8

With 0.5 equal weigting

Trading_idea
(From 22Q3 Stefan)
Coinbase premium
 1 coinbase/ binance spot
 2 BTC 1h/ 15m
 3 ETH 1h/ 15m
 4 SOL 1h (1.7)
 5 XRP 1h (2.6)
 6 DOGE 1h
 7 Some z, some pRank, some with/ without price filter
 8 forgot one important point, must flat-at-0
 9 the heatmap completely different

(From 22Q4 Nelson)
Funding rate spread between exchange
Money flow
Open interest pct change spread
Liquidation spread


waiting to-add in the future
1) position_sizing (0.1, 0.25, 0.5, etc...)
2) leverage (1x, 2x, 3x, etc...)
3) tp/sl/ trailing tp/ sl
4) entry/ exit timing (based on time instead of magnitude)
5) risk management (max_trade per day, max_mdd per strat)
6) time-based fliters (trading hours/ days -> all, asia, ny, london)
7) market regime classification (IV, HV, trend_strength, )
"""