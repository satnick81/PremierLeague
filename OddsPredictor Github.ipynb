import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson,skellam
# importing the tools required for the Poisson regression model
import statsmodels.api as sm
import statsmodels.formula.api as smf
import urllib.request
from bs4 import BeautifulSoup

epl_full = pd.read_csv("http://www.football-data.co.uk/mmz4281/2021/E0.csv")
epl = epl_full[['HomeTeam','AwayTeam','FTHG','FTAG']]
epl = epl.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
n_columns = 0
n_rows=0
goal_model_data = pd.concat([epl[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(
            columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}),
           epl[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(
            columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data, 
                        family=sm.families.Poisson()).fit()
pd.DataFrame(columns = range(0,5), index= range(0,n_rows))

poisson_model.summary()
import urllib.request
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.oddschecker.com/football/english/premier-league"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need
soup = BeautifulSoup(data , "lxml")
table = soup.find_all('table')[0]


    # Find number of rows and columns
# we also find the column titles if we can
for row in table.find_all('tr'):

    # Determine the number of rows in the table
    td_tags = row.find_all('p')
    if len(td_tags) > 0:
        n_rows+=1
        if n_columns == 0:
            # Set the number of columns for our table
            n_columns = len(td_tags)

df = pd.DataFrame(columns = range(0,6),
                  index= range(0,n_rows))
row_marker = 0
identity = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('p')
    for column in columns:
        df.iat[row_marker,column_marker] = column.get_text()
        column_marker += 1
        
    if len(columns) > 0:
        df.iat[row_marker,column_marker] = identity
        identity += 1
        row_marker += 1
        
header = ['hometeam','awayteam','homeodds','drawodds','awayodds', 'id']
df.columns=(header)
df = df[1:11]
hometeam = []
awayteam = []
homeodds = []
drawodds = []
awayodds = []
id = []

all_names = list(set(epl["HomeTeam"]))

for homename in list(df['hometeam']):
    for cleanname in all_names:
        if homename[:6] == cleanname[:6]:
            hometeam.append(cleanname)
        if homename == 'Man Utd' and homename[:5] == cleanname[:5]:
            homename.append(cleanname)
            
for awayname in list(df['awayteam']):
    for cleanname in all_names:
        if awayname[:6] == cleanname[:6]:
            awayteam.append(cleanname)
        if awayname == 'Man Utd' and awayname[:5] == cleanname[:5]:
            awayteam.append(cleanname)
            
for (hometeam_v, awayteam_v, home_fraction, draw_fraction, away_fraction, ids) in zip(df['hometeam'],df['awayteam'],df['homeodds'],df['drawodds'],df['awayodds'], df['id']):
    for cleanname in all_names:
        if homename[:6] == cleanname[:6]:
            homeodd_raw = eval(home_fraction)
            homeodds_v = (1/(homeodd_raw+ 1))
            homeodds.append(homeodds_v)
            drawodd_raw = eval(draw_fraction)
            drawodd_raw_v = (1/(drawodd_raw+ 1))
            drawodds.append(drawodd_raw_v)
            awayodds_raw = eval(away_fraction)
            awayodds_v = (1/(awayodds_raw+ 1))
            awayodds.append(awayodds_v)
            id.append(ids)
        elif homename == 'Man Utd' and homename[:5] == cleanname[:5]:
            homeodd_raw = eval(home_fraction)
            homeodds_v = (1/(homeodd_raw+ 1))
            homeodds.append(homeodds_v)
            drawodd_raw = eval(draw_fraction)
            drawodd_raw_v = (1/(drawodd_raw+ 1))
            drawodds.append(drawodd_raw_v)
            awayodds_raw = eval(away_fraction)
            awayodds_v = (1/(awayodds_raw+ 1))
            awayodds.append(awayodds_v)
            id.append(ids)

percentagedf = pd.DataFrame(list(zip(hometeam, awayteam, homeodds, drawodds,awayodds,id)),columns=['hometeam','awayteam','homeodds','drawodds','awayodds', 'id'])
def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam,'opponent': awayTeam,'home':1},index=[1]))
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam, 
                                                            'opponent': homeTeam,'home':0},
                                                      index=[1]))
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))

hometeam = []
awayteam = []
home_prob = []
draw_prob = []
away_prob = []
idprob = []

for (ht,at) in zip(percentagedf.iloc[:, 0], percentagedf.iloc[:, 1]):
    odds_matrix = simulate_match(poisson_model, ht, at, max_goals = 10)
    home_probability = np.sum(np.tril(odds_matrix, -1))
    draw_probability = np.sum(np.diag(odds_matrix))
    away_probability = np.sum(np.triu(odds_matrix, 1))
    hometeam.append(ht)
    awayteam.append(at)
    home_prob.append(home_probability)
    draw_prob.append(draw_probability)
    away_prob.append(away_probability)
    idprob.append(ids)
    ids +=1

percentile_list = pd.DataFrame( {'id': idprob,'hometeam': hometeam, 'awayteam': awayteam, 'home_prob': home_prob,'draw_prob': draw_prob, 'away_prob': away_prob})

Total_Odds = percentile_list.merge(percentagedf, left_index=True, right_index=True)
Total_Odds
