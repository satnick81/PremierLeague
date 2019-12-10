# PremierLeague
EPL Data Set

## Final PBI Report: 
https://msit.powerbi.com/view?r=eyJrIjoiZGQ5OGFmMzItMjM5MS00Mzg4LWExMDgtNGNjNzFhZDRiZWQ5IiwidCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsImMiOjV9

## Architecture: 
Data is passed in through two different web-scrapes and a csv file. The data is processed and transformed in Databricks and loaded into SQL Server where it is loaded into power bi and displayed. 

## Data: 
English Premier League dataset is combined from https://footballapi.pulselive.com/football/stats/player/ as well as historical results from http://www.football-data.co.uk/mmz4281/1920/E0.csv and https://www.oddschecker.com/football/english/premier-league. 

## Logic: 
Most of the logic was scraped from dashee87 GitHub blog that was published here. There was some code refactoring which was used to refine the model to the present-day dataset. The concept is to leverage the popularized Poisson distribution and pass in weekly matches for odd comparison.

https://github.com/dashee87/blogScripts/blob/master/Jupyter/2017-06-04-predicting-football-results-with-statistical-modelling.ipynb. 

There is also data that comes in from the player level and is aggregated in SQL. This aggregated data is then ranked based on team for comparison on specific metrics. 

## Disclaimer: 
The purpose of the dashboard is to grow technical skillset with data science as well as build on Databricks and SQL knowledge. In no way should these results be used for gambling as these results are just displaying the output of a Poisson Distribution.
