# waiting Notes

"""
to-do list (data)
1) get_data for dataScrapper
2) data standardization
3) path standardization
4) checker optimization
- 4.1) coinm_futures with contractType
- 4.2) funding_rate upper/ lower limit from exchange API
- 4.3) N.A for data

5) storing optimization
- if data smaller than 3-year history -> do not download and skip

6) glassnode optimization
= del data for useless symbol and exchange_list as well
--------------------------------------------------
to-do list (backtest)
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

4. bvol analysis (waiting answer from calvin)

5. single para_dict vs full_para_dict vs all_para_combination in backtestEngine
--------------------------------------------------
to-do list (correlation)
1) optimize correlationChecker
- by symbol
- by single symbol in single strategy
--------------------------------------------------
to-do list (analysis)
1) finalize pnlAnalyzer
--------------------------------------------------
to-do list (team)
2) refactor/ restructure trading system -> waiting dex onboard
"""