# working Notes

"""
main
1) order_history
- order_times -> how many times get cancelled -> filled
- min, max and avg order_times
* seems cannot find cancelled order (GTX order hit market order stuffs)
* be careful with manual order adjustment

2) trade history
- order_slippage (trade_price - theo_price)
* be careful with manual order adjustment

3) result_df last column
- some data do not finish its resolution (kline, volatility index, ...)
- therefore, the last column should be eliminated
- be careful, if last_column deleted -> not latest_data -> cant get latset backtest_df for positioning

4) data optimization
- if data smaller than 3-year history -> do not download and skip

5) (glassnode data) - del data for useless symbol and exchange_list as well
--------------------------------------------------
1) optimize current strategy (celesty, claire)
- celesty + claire (resampled to 8hrs) -> if (index + funding) > futures -> long/ short
- claire - try 12h-resolution close position

2) big backtest on phoebe -> running
--------------------------------------------------
waiting team
1) copy SingleResult from server to local   -> waiting backend get ready
2) deploy celesty for binance coinm_futures -> waiting tbackend get ready
3) copy trading repo from tc to local       -> waiting tbackend get ready
4) adjust notional to aware of MDD of each strategy -> waiting backend get ready
5) calculate exchange/ total performance -> waiting main acc details
6) short-cut = ctrl + b + [
--------------------------------------------------
other (data)
1) get_data for dataScrapper
2) data standardization
3) path standardization
4) checker optimization
- 4.1) coinm_futures with contractType
- 4.2) funding_rate upper/ lower limit from exchange API
- 4.3) N.A for data
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

- BTC, ETH, DOGE, AVAX, GRT only
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

5. bvol analysis (waiting answer from calvin)
--------------------------------------------------
other (analysis)
1) finalize pnlAnalyzer
--------------------------------------------------
other (team)
1) change to notional value instead of base_qty -> will do so in the next version
2) refactor/ restructure trading system -> waiting okex onboard
"""