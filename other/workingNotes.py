# working Notes

"""
scale up strategy -> waiting momentum end to change params in christy_v1
trade phoebe other factors

main
1) backtest phoebe good endpoint_list
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
"""