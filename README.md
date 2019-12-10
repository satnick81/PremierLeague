# PremierLeague
EPL Data Set

Architecture: 
Data is passed in through two different webscrapes and a csv file. THe data is processed and transformed in Databricks and loaded into SQL Server where it is loaded into power bi and displayed. 

Data: 
English Premier League dataset is combined from https://translations.platform.pulselive.com/ as well as historical results from http://www.football-data.co.uk/mmz4281/1920/E0.csv and https://www.oddschecker.com/football/english/premier-league. 

Logic: 
Most of the logic was scraped from dashee87 github blog that was published here. There was some code refractoring which was used to refine the model to the present day dataset. The concept is to leverage the popularized Poisson distribution and pass in weekly matches for odd comparison. https://github.com/dashee87/blogScripts/blob/master/Jupyter/2017-06-04-predicting-football-results-with-statistical-modelling.ipynb. There is also data that comes in from the player level and is aggregated in sql. This aggregated data is then ranked based on team for comparison on specific metrics. 

Disclaimer: 
The purpose of the dashboard is to grow technical skillset with data science as well as build on Databricks and SQL knowledge. In no way should these results be used for gambling as these results are just displaying the output of a Possion Distribution. 
