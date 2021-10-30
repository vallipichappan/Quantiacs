# Quantiacs

Our objective was to identify an algorithm that could rightly evaluate and pick up on trading signals to let an investor obtain higher returns from their portfolio of futures. This would also directly increase the sharpe ratio, which we used as our evaluation metric. The algorithm would have to place a buy position on the underperforming asset and a sell position on the outperforming asset. Profits are generated when the underperforming stock regains value, and the outperforming stock’s price deflates.

For this task, we explored several types of approaches that involve: technical indicators, macroeconomic indicators, time series forecasting and machine learning. The notebooks in this repo correspond to this. As these groups of approaches are different from each other, we prioritised experimenting with those that were commonly used in the industry, as well as those that had high sharpe ratios in our initial stage of experimentation. We also tried combining methods together like time series approaches with technical indicators. 

The Futures data and Macroeconomics data have been obtained from Quantiacs Toolbox: https://quantiacs.com/documentation/en/user_guide/data.html#futures
