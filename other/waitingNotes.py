# waiting Notes

"""
to-do list (prod)
1) Feedback Loop
- track predictions vs outcomes (after strat pool introdcted)

2) Execution Quality Analysis
- add slippage tracking and execution quality metrics

3) Consolidate messageHandling
- message including order, trade, position, signal, performance, etc...

to-do list (data)
1) get_data for dataScrapper
2) data standardization
4) checker optimization
- 4.1) coinm_futures with contractType
- 4.2) funding_rate upper/ lower limit from exchange API
- 4.3) N.A for data
--------------------------------------------------
to-do list (backtest)
1. magnitude calculation method
- 1) iv * open_interest
- make the open_interest -> change % to normalize it
- 2) iv * volume (sd_normalized)
rationale: if both call iv increases and volume sudden increaded -> most of them are retail investors
rationale: if call iv increases, volume did not changed          -> market maker increases iv -> some of them might be institutional investors
- 3) iv * put_call ratio
--------------------------------------------------
"""