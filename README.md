# **Portfolio Performance**
*WORK IN PROGRESS*

Django project to track the performance of a stock portfolio - because my broker can't figure that out smh...


## **Goal (for v1)**
I want a crude overview of the perfromance of my/any portfolio (which has to be created on the platform - again, my broker doesn't have an API...).

**The following things should be included:**

* portfolio performance - YTD and overall
* performance of individual positions - YTD and overall
* add/remove positions
* auth

*for now I'll be using the closing prices for all the performance calculations - no realtimeperformance and no accurate opening price*


## **API**
I am using the [twelvedata](https://twelvedata.com/) stock API (free tier).

## **Graphing**
I am using [chart.js](https://www.chartjs.org/) for the graphs.


## TODO:
* position details
	* chart asset/position  ☑️	
	* performacne of asset/position	 ☑️
	* weigted absolut performance (in fiat currancy)
* performance calculation