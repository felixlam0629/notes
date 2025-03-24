# working Notes

"""
to-do today
- add how to deal with method, model, close

waiting
- run all exchangeData for testing new dataScrapper

prod
- strategy weighting -> ask how to do strategy weigting

1) backtest glassnode good endpoint_list
2) trade glassnode good endpoint_list
3) resample glassnode good endpoint_list
4) backtest binance, bybit funding_rate, basis
5) create straetgy pool
6) check correlation among strategy (in fixed resolution)

when tried...
1) refactor everything...
2) ask questions for the whole system (backtest/ prod)
--------------------------------------------------
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

glassnode
["v1-metrics-addresses-active_count.csv",
                             "v1-metrics-addresses-count.csv",
                             "v1-metrics-addresses-loss_count.csv",
                             "v1-metrics-addresses-profit_count.csv",

                             'v1-metrics-addresses-min_100k_usd_count.csv',
                             'v1-metrics-addresses-min_100_count.csv',
                             'v1-metrics-addresses-min_100_usd_count.csv',
                             'v1-metrics-addresses-min_10k_count.csv',
                             'v1-metrics-addresses-min_10k_usd_count.csv',
                             'v1-metrics-addresses-min_10_count.csv',
                             'v1-metrics-addresses-min_10_usd_count.csv',
                             'v1-metrics-addresses-min_1k_count.csv',
                             'v1-metrics-addresses-min_1k_usd_count.csv',
                             'v1-metrics-addresses-min_1m_usd_count.csv',
                             'v1-metrics-addresses-min_1_count.csv',
                             'v1-metrics-addresses-min_1_usd_count.csv',
                             'v1-metrics-addresses-min_point_1_count.csv',
                             'v1-metrics-addresses-min_point_zero_1_count.csv',

                             'v1-metrics-addresses-supply_balance_0001_001.csv',
                             'v1-metrics-addresses-supply_balance_001_01.csv',
                             'v1-metrics-addresses-supply_balance_01_1.csv',
                             'v1-metrics-addresses-supply_balance_100_1k.csv',
                             'v1-metrics-addresses-supply_balance_10k_100k.csv',
                             'v1-metrics-addresses-supply_balance_10_100.csv',
                             'v1-metrics-addresses-supply_balance_1k_10k.csv',
                             'v1-metrics-addresses-supply_balance_1_10.csv',
                             'v1-metrics-addresses-supply_balance_less_0001.csv',
                             'v1-metrics-addresses-supply_balance_more_100k.csv',
                             'v1-metrics-addresses-supply_distribution_relative.csv',

                             'v1-metrics-entities-active_count.csv',
                             'v1-metrics-entities-active_count_pit.csv',
                             'v1-metrics-entities-min_1k_count.csv',
                             'v1-metrics-entities-min_1k_count_pit.csv',

                             'v1-metrics-entities-supply_balance_0001_001.csv',
                             'v1-metrics-entities-supply_balance_0001_001_pit.csv',
                             'v1-metrics-entities-supply_balance_001_01.csv',
                             'v1-metrics-entities-supply_balance_001_01_pit.csv',
                             'v1-metrics-entities-supply_balance_01_1.csv',
                             'v1-metrics-entities-supply_balance_01_1_pit.csv',
                             'v1-metrics-entities-supply_balance_100_1k.csv',
                             'v1-metrics-entities-supply_balance_100_1k_pit.csv',
                             'v1-metrics-entities-supply_balance_10k_100k.csv',
                             'v1-metrics-entities-supply_balance_10k_100k_pit.csv',
                             'v1-metrics-entities-supply_balance_10_100.csv',
                             'v1-metrics-entities-supply_balance_10_100_pit.csv',
                             'v1-metrics-entities-supply_balance_1k_10k.csv',
                             'v1-metrics-entities-supply_balance_1k_10k_pit.csv',
                             'v1-metrics-entities-supply_balance_1_10.csv',
                             'v1-metrics-entities-supply_balance_1_10_pit.csv',
                             'v1-metrics-entities-supply_balance_less_0001.csv',
                             'v1-metrics-entities-supply_balance_less_0001_pit.csv',
                             'v1-metrics-entities-supply_balance_more_100k.csv',
                             'v1-metrics-entities-supply_balance_more_100k_pit.csv',

                             'v1-metrics-derivatives-options_25delta_skew_1_month-deribit.csv',
                             'v1-metrics-derivatives-options_25delta_skew_1_week-deribit.csv',
                             'v1-metrics-derivatives-options_25delta_skew_3_months-deribit.csv',
                             'v1-metrics-derivatives-options_25delta_skew_6_months-deribit.csv',
                             'v1-metrics-derivatives-options_25delta_skew_all-deribit.csv',
                             'v1-metrics-derivatives-options_atm_implied_volatility_1_month-deribit.csv',
                             'v1-metrics-derivatives-options_atm_implied_volatility_1_week-deribit.csv',
                             'v1-metrics-derivatives-options_atm_implied_volatility_3_months-deribit.csv',
                             'v1-metrics-derivatives-options_atm_implied_volatility_6_months-deribit.csv',
                             'v1-metrics-derivatives-options_atm_implied_volatility_all-deribit.csv',

                             'v1-metrics-derivatives-options_volume_put_call_ratio-aggregated.csv',
                             'v1-metrics-derivatives-options_volume_put_call_ratio-deribit.csv',
 ]

/v1/metrics/derivatives/futures_estimated_leverage_ratio

short_liqudiation_usd (bybit)
top_long_short_acc_ratio (binance)

+v1+metrics+market+realized_volatility_...

v1_metrics_supply_active_1w_1m_
v1_metrics_supply_active_1y_2y_***
v1_metrics_supply_active_3m_6m_
v1_metrics_supply_active_1m_3m_

/v1/metrics/breakdowns/mvrv_by_age
/v1/metrics/breakdowns/mvrv_by_wallet_size
v1/metrics/indicators/mvrv_account_based
BTC_v1_metrics_market_mvrv_more_155_
BTC_v1_metrics_market_mvrv_
BTC_v1_metrics_market_mvrv_more_155_


BTC_v1_metrics_blockchain_utxo_profit_count_
BTC_v1_metrics_derivatives_futures_open_interest_cash_margin_sum_
BTC_v1_metrics_distribution_balance_exchanges_
BTC_v1_metrics_distribution_balance_exchanges_relative_
BTC_v1_metrics_indicators_cdd90_account_based_age_adjusted_pit_
BTC_v1_metrics_indicators_cdd90_account_based_age_adjusted_
BTC_v1_metrics_indicators_cdd90_age_adjusted_
BTC_v1_metrics_indicators_liveliness_
BTC_v1_metrics_indicators_mvrv_account_based_pit_
BTC_v1_metrics_indicators_hodler_net_position_change_
BTC_v1_metrics_indicators_net_unrealized_profit_loss_
BTC_v1_metrics_indicators_net_unrealized_profit_loss_account_based_
BTC_v1_metrics_indicators_nupl_more_155_
BTC_v1_metrics_indicators_nvts_
BTC_v1_metrics_indicators_sol_1h_
BTC_v1_metrics_indicators_unrealized_profit_
BTC_v1_metrics_indicators_unrealized_profit_account_based_
BTC_v1_metrics_indicators_unrealized_loss_
BTC_v1_metrics_market_marketcap_usd_
BTC_v1_metrics_market_realized_volatility_3_months_
BTC_v1_metrics_supply_active_more_1y_percent_
BTC_v1_metrics_supply_liquid_sum_pit_
BTC_v1_metrics_transactions_transfers_volume_exchanges_net_
BTC_v1_metrics_transactions_transfers_volume_from_exchanges_mean_
BTC_v1_metrics_transactions_transfers_volume_exchanges_net_

]

"""