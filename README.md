# PremierLeague
EPL Data Set

## Report
https://app.powerbi.com/view?r=eyJrIjoiZGNmYTk3MGQtZjNmMC00MjI1LTg0YzUtOThhNDMyOTA0YWE0IiwidCI6ImU3NDk4YmMzLWE3MWEtNGI2MC05ZWU5LWM2Y2QyYjFjMmYxNiIsImMiOjN9

## Architecture: 
Data is extracted and transformed using a python script prior to loading directly into Power Bi.

## Data: 
English Premier League dataset is combined from https://footballapi.pulselive.com/football/stats/player/ as well as historical results from http://www.football-data.co.uk/mmz4281/1920/E0.csv and https://www.oddschecker.com/football/english/premier-league. 

## Logic: 
By leveraging dashee87 blog post, which utilizes a Poisson distribution, I can get the expected value by comparing the result probability from the poisson distribution against the expected value of the Bet365. 

https://github.com/dashee87/blogScripts/blob/master/Jupyter/2017-06-04-predicting-football-results-with-statistical-modelling.ipynb. 

## Disclaimer: 
The purpose of the dashboard is to grow technical skillset with data science as well as build on Databricks and SQL knowledge. In no way should these results be used for gambling.
