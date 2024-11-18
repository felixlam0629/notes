# working Notes

"""
main
1) transfer bybit fund to binance 4th sub-acc for phoebe (waiting team onboard 4th acc)
--------------------------------------------------
1) optimize current strategy (celesty, claire)
- celesty + claire (resampled to 8hrs) -> if (index + funding) > futures -> long/ short

2) big backtest on the following strategy
- phoebe - all endpoints -> updating all data

check strategy crystal

--------------------------------------------------
2) develop new strategies (from glassnode only)
- futures - open_interest (cash-margin, crypto-margin, perp, ...), volume (...)
--------------------------------------------------
(analysis)
- bvol analysis
- check monthly pnl
--------------------------------------------------
(optimization)
- within-resolution close position
- timezone





team
1) change to notional value instead of base_qty -> will do so in the next version
2) adjust notional to aware of MDD of each strategy (some > 100%...)
2) refactor/ restructure trading system -> waiting okex onboard
--------------------------------------------------
other (data)
1) get_data for dataScrapper
2) data standardization
3) path standardization
4) checker optimization
- 4.1) coinm_futures with contractType
- 4.2) funding_rate upper/ lower limit from exchange API
- 4.3) N.A for data

5) deribit data scripts
problem: data is not trustable to use atm LMAO
--------------------------------------------------
other (backtest)
1) SingleResult function -> update data with trading symbol_list too
- including 1) kline, 2) index_kline, 3) funding_rate

3) backtest_df data visualization
- visualize data with time -> check data quality

4) backtest analysis
- pnl (long, short) distribution -> check if one-off -> affecting the whole result
- monthly pnl distribution -> check if one-off

5) claire -> across exchange??
--------------------------------------------------
other (analysis)
1) post-trade analysis (from exchange UI)
- order -> 1) order_time (delay), 2) order_slippage
- trade -> 1) trdae_time (waiting), 2) trade_slippaage
- performace -> 1) each exchange, 2) each account, 3) each strategy, 4) each symbol

2) post-trade analysis from UI
--------------------------------------------------
optimization (backtest)
1. magnitude calculation method
- 1) iv * open_interest
- make the open_interest -> change % to normalize it
- 2) iv * volume (sd_normalized)
rationale: if both call iv increases and volume sudden increaded -> most of them are retail investors
rationale: if call iv increases, volume did not changed          -> market maker increases iv -> some of them might be institutional investors
- 3) iv * put_call ratio

2. funding_rate with multi- factor (glassnode)
- as funding_rate is testified to be a profitable strategy
- therefore, focos on magnitude calculation method with

phrase 1
- BTC, ETH, BNB, DOGE, AVAX, GRT, LDO, LINA only
- 8h (resampled from 1h)
- all exchanges except ftx

phrase 2
- BTC, ETH, BNB, DOGE, AVAX, GRT, LDO, LINA only
- 8h (resampled from 1h)
- funding_rate * open_interest/ volume? maximize the retail effect on funding_rate/ position
- funding_rate * estimated leverage ratio?

3. how to use bvol?
- realized that when the market does not move/ boring -> funding_rate as well
- no movement in funding_rate -> no signal from celesty
-> higher bvol -> start celesty?
-> lower bvol -> momentum strategy~~?

thought
1) lower volatility -> less retail investor participation
2) higher volatility -> more retail investors -> alpha for CTA
"""