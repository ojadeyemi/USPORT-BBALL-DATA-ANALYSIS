# libraries
import matplotlib.pyplot as plt
import pandas as pd
from datafunctions import usports_hoop_data

#list of teams who won championshp and appeared in final 8 (replace mbb to wbb for womens)
championship_teams = usports_hoop_data('https://usportshoops.ca/history/champ-years.php?Gender=MBB')
appearance_teams = usports_hoop_data('https://usportshoops.ca/history/champ-appearances.php?Gender=MBB')

temp_df = pd.DataFrame(championship_teams) #championship dataframe
temp_df2 = pd.DataFrame(appearance_teams) #appearance dataframe
temp_df2.columns = ['team_name', 'appearances_count', 'appearances_year'] #rename colums on appearnce dataframe

#merge dataframes so we have championship teams with championship and appearance in final 8 years
merged_df = pd.merge(temp_df, temp_df2, on='team_name', how='left')
plt.figure(figsize=(19.20,10.80))

earliest_year, latest_year = 1962, 2023

#Iterate through teams
for index, row in merged_df.iterrows():
    # Initialize a list to store team's cumulative performance (appearances + championships) per year
    team_performance = [0] * (latest_year - earliest_year + 1)

    # Update performance for championship years
    for i in range(earliest_year, latest_year+1):
        championship_years = row['championship_years']
        championship_appearance = row['appearances_year']
        if i == earliest_year:
            team_performance[i - earliest_year] = 0
        else:
            team_performance[i - earliest_year] += team_performance[i - earliest_year - 1]

        if i in championship_years:
            team_performance[i - earliest_year] += 15    
        if i in championship_appearance:
            team_performance[i - earliest_year] += 1 

      # Plot the line for the current team
    plt.plot(range(earliest_year, latest_year + 1), team_performance, label=row['team_name'])


# Add labels and title

plt.xlabel('Year')
plt.title('Performance of Teams')
plt.ylim(bottom=0)
plt.xticks(range(earliest_year, latest_year + 1), fontsize=5)  # Set x-axis labels to years
# Selecting the axis-Y making the right and left axes False 
plt.tick_params(axis='y', which='both', right=False, 
                left=False, labelleft=False) 
# Iterating over all the axes in the figure 
# and make the Spines Visibility as False 
for pos in ['right', 'top', 'left']: 
    plt.gca().spines[pos].set_visible(False) 
plt.legend()
plt.show()

#plt.savefig('USportsWBBBestProgram.png', dpi=300)