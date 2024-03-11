# libraries
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd
from datafunctions import usports_hoop_data

#list of teams who won championshp and appeared in final 8 (replace mbb to wbb for womens)
championship_teams = usports_hoop_data('https://usportshoops.ca/history/champ-years.php?Gender=WBB')
appearance_teams = usports_hoop_data('https://usportshoops.ca/history/champ-appearances.php?Gender=WBB')

temp_df = pd.DataFrame(championship_teams) #championship dataframe
temp_df2 = pd.DataFrame(appearance_teams) #appearance dataframe
temp_df2.columns = ['team_name', 'appearances_count', 'appearances_year'] #rename colums on appearnce dataframe

#merge dataframes so we have championship teams with championship and appearance in final 8 years
merged_df = pd.merge(temp_df, temp_df2, on='team_name', how='left')
merged_df = merged_df.iloc[::-1] #reverse order of row

bgcol = '#fafaf0'
fig, ax = plt.subplots(figsize=(19.20,10.80))                   

#earliest year for men is 1962 and for womens is 1971
earliest_year, latest_year = 1971, 2024
#Iterate through teams
for index, row in merged_df.iterrows():
    # Initialize a list to store team's cumulative performance (appearances + championships) per year
    team_performance = [0] * (latest_year - earliest_year + 1)

    # Update performance for championship years throughout the years
    for i in range(earliest_year, latest_year+1):
        championship_years = row['championship_years']
        championship_appearance = row['appearances_year']
        if i == earliest_year:
            team_performance[i - earliest_year] = 0
        else:
            team_performance[i - earliest_year] += team_performance[i - earliest_year - 1]

        #add large value if team won championship
        if i in championship_years:
            team_performance[i - earliest_year] += 20  

        #add small value if team made final 8
        if i in championship_appearance:
            team_performance[i - earliest_year] += 1
        else:
            if team_performance[i - earliest_year] > 0:
                team_performance[i - earliest_year] -= 1

    championship_years = row['championship_years']
    markers = [0] * len(team_performance)  # Initialize markers with '0'
    
    # Update markers for championship years
    for year in championship_years:
        index = year - earliest_year  # Adjust index based on earliest_year
        markers[index] = index  # Set marker index for championship years
    line_color = "#D1D1D1" #default line color
    mark_title = False
    #figure out how to get top 5 and label them and colors for each team
    if row['team_name'] == 'Laurentian':
        line_color = '#000000'
        mylabel= f"{row['team_name']} - {row['championship_count']} titles"
        mark_title = True
    if row['team_name'] == 'Victoria':
        line_color = '#1b5494'
        mylabel = f"{row['team_name']} - {row['championship_count']} titles"
        mark_title = True
    if row['team_name'] == 'UBC':
        line_color = '#FF0000'
        mylabel = f"{row['team_name']} - {row['championship_count']} titles"
        mark_title = True
    if row['team_name'] == 'SimonFraser':
        line_color = '#612042'
        mylabel = f"{row['team_name']} - {row['championship_count']} titles"
        mark_title = True
    if row['team_name'] == 'Windsor':
        line_color = '#ffb200'
        mylabel = f"{row['team_name']}- {row['championship_count']} titles"
        mark_title = True
    
    if mark_title:
        # Plot the line for the current team
        plt.plot(range(earliest_year, latest_year + 1), team_performance, label=mylabel, color = line_color, lw = 2.1, 
                 marker = 'o', markevery = markers, markersize = 6)
    else:
        plt.plot(range(earliest_year, latest_year + 1), team_performance, color = line_color, alpha=0.7)

#Add labels and title
plt.xlabel('Year')
plt.title('USports Women\'s Basketball Top 5 Most Successful Program', fontweight='bold', fontsize = 20, va= 'top', ha='center')
plt.ylim(bottom=0)
plt.xlim(earliest_year, latest_year)
plt.xticks(range(earliest_year, latest_year+1), fontsize=6, rotation=45, weight='roman')  # Set x-axis labels to years

# Selecting the axis-Y making the right and left axes False 
plt.tick_params(axis='y', which='both', right=False, 
                left=False, labelleft=False) 

# Iterating over all the axes in the figure 
# and make the Spines Visibility as False 
for pos in ['right', 'top', 'left']: 
    plt.gca().spines[pos].set_visible(False) 

# Reverse the order of legend items
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1])

# Reduce white space
plt.subplots_adjust(left=0.03, right=0.96, top=0.9, bottom=0.1)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
image_path = 'USportLogo.png'  # Relative path

# Read the image
image = imread(image_path)

plt.figimage(image, xo = 600, yo = 3000, alpha = 0.7)
fig.text(0.67,0.886,'by OJ Adeyemi', fontsize = 10, fontstyle='oblique', alpha =0.7)
#save figure before showing
plt.savefig('USports_WBB_BestProgram2.png', dpi=300)
#plt.show()
plt.close()

