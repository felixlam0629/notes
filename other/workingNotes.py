# working Notes

"""
main
update phoebe script
add christyResult

# optimize strategy model/ type params

2.1 price_data (sd, different resolution, momentum only)
- binance
scrapping: /
waiting: 5m, 15m, 30m, 1h, 2h, 4h
backtesting:
finished: 24h, 12h, 8h, 6h

- bybit
scrapping: 5m
waiting: 1h, 30m, 15m
backtesting:
finished: 2h, 4h, 6h, 12h, 24h

top
1) Backtest glassnode
1.1 resampling/ different resolution (method: past mean, past total, now_data) -> 12h, 8h, 6h, 4h, 2h, 1h

now_data
- backtested: 12h, 8h, 6h
- running: 4h

1.2 different model
* rmb Signal.py changed in non-24h backtesting



2) Backtest trading_idea
2.3 taker buy/sell volume (sd, different resolution, momentum, reversion)
--------------------------------------------------
"""