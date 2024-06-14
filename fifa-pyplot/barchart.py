import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Histogram columns info
# ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,Club,Club Logo,Value,Wage,Special,Preferred Foot,International Reputation,Weak Foot,Skill Moves,Work Rate,Body Type,Real Face,Position,Jersey Number,Joined,Loaned From,Contract Valid Until,Height,Weight,LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,LCB,CB,RCB,RB,Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKHandling,GKKicking,GKPositioning,GKReflexes,Release Clause

fifa = pd.read_csv("fifa_data.csv")

print(fifa[['Name','Release Clause']].head(10))

fifa['Release Clause'] = fifa['Release Clause'].replace({'€': '', 'M': '', 'K': ''}, regex=True).astype(float)

names = fifa['Name'].head(10)
values = fifa['Release Clause'].head(10)

plt.figure(figsize=(12, 5))
plt.bar(names, values)
plt.xlabel('Name')
plt.ylabel('Release Clause (in Millions)')
plt.title('Top 10 Players Release Clauses')
plt.xticks(rotation=45)
plt.show()