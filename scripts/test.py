#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox #for images of teams
import datafunctions #custom function to get dataframe

mens_team = ('https://universitysport.prestosports.com/sports/mbkb/2023-24/teams?sort=&r=0&pos=off', 52)
womens_team = ('https://universitysport.prestosports.com/sports/wbkb/2023-24/teams?sort=&r=0&pos=off', 48)
selected_team = mens_team

df = datafunctions.usports_team_data(selected_team[0], selected_team[1])
df = df[df['Conferences'] == 'OUA']
# Define a function to get an image from the folder with a zoom factor and make dots transparent with alpha setting to 1
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.06, alpha = 1)

#scatter plot values
x_value = 'Offensive Efficiency'
y_value = 'Defensive Efficiency'

# Create initial plot
bgcol = '#fafaf0'
fig, ax = plt.subplots(figsize=(3,2), dpi=300)
ax.scatter(df[x_value], df[y_value], color='white')
if y_value == 'Defensive Efficiency':
    ax.invert_yaxis() # reverse the y-axis

#label graph
plt.title('2023-2024 OUA Men\'s BasketBall Regular Season Efficiency Landscape',fontsize = 5,fontstyle='oblique',weight='bold')
fig.text(0.77,0.89,'by OJ Adeyemi', fontsize = 3, fontstyle='oblique', alpha =0.7)

# Create arrow patches lines for averages
style = patches.ArrowStyle('Fancy', head_length=1, head_width=1.5, tail_width=0.5)
harrow = patches.FancyArrowPatch((df[x_value].min()-0.01, df[y_value].mean()), (df[x_value].max()+0.01, df[y_value].mean()), 
                                arrowstyle=style, color='#c2c1c0', linewidth=0.5)
varrow = patches.FancyArrowPatch((df[x_value].mean(), df[y_value].max()+0.01),(df[x_value].mean(), df[y_value].min()-0.01), 
                                 arrowstyle=style, color='#c2c1c0', linewidth=0.5)

# Add arrow patches to the axes to be drawn
plt.gca().add_patch(harrow)
plt.gca().add_patch(varrow)

# Draw dashed lines from top-left to bottom-right
plt.plot([df[x_value].min(), df[x_value].max()], [df[y_value].min(), df[y_value].max()], '--', color='#c2c1c0', alpha = 0.5,linewidth=0.4)  # Top-left to bottom-right

# Set labels and title
plt.xlabel('X-axis')
# Add text next to the lines
plt.text(df[x_value].max(), df[y_value].mean(), x_value, 
          horizontalalignment='right', verticalalignment='bottom', rotation=0, color='#c2c1c0', fontsize=4)
plt.text(df[x_value].mean(), df[y_value].min(), y_value, 
          horizontalalignment='right', verticalalignment='top', rotation=90, color='#c2c1c0', fontsize=4)
plt.text(df[x_value].min()+0.001, df[y_value].min()+0.01, 'Positive Teams', alpha = 0.5,
          horizontalalignment='left', verticalalignment='bottom', rotation=-30, color='#c2c1c0', fontsize=2)
plt.text(df[x_value].min()+0.001, df[y_value].min()+0.005, 'Negative Teams', alpha = 0.5,
          horizontalalignment='left', verticalalignment='top', rotation=-30, color='#c2c1c0', fontsize=2)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)

# Remove plot spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

for index,x, y in zip(df.index, df[x_value], df[y_value]):
    # Get the image file name from the team name
    try:
        file = 'team_logos/' + index + '.png'
        # Create an annotation box with the image
        ab = AnnotationBbox(getImage(file), (x, y), frameon=False)
        # Add the annotation box to the axis
        ax.add_artist(ab)
    except:
        print(index) #team photo needs to be updated which is Guelph

# Find the index of the team with best off and best defense
best_off_team = df[x_value].idxmax()
best_def_team = df[y_value].idxmin()
worst_off_team = df[x_value].idxmin()
worst_def_team = df[y_value].idxmax()

# Get the coordinates of the team with best off and best defense
best_off_x = df.loc[best_off_team, x_value]
best_off_y = df.loc[best_off_team, y_value]
best_def_x = df.loc[best_def_team, x_value]
best_def_y = df.loc[best_def_team, y_value]
worst_off_x = df.loc[worst_off_team, x_value]
worst_off_y = df.loc[worst_off_team, y_value]
worst_def_x = df.loc[worst_def_team, x_value]
worst_def_y = df.loc[worst_def_team, y_value]

# Add text under the scatter plot
plt.text(best_off_x, best_off_y+0.015, 'Best Offense!', fontsize=2, verticalalignment='bottom',horizontalalignment='center', color = '#512888',fontweight='bold')
plt.text(best_def_x, best_def_y-0.011, 'Best Defence!', fontsize=2, verticalalignment='bottom',horizontalalignment='center', color = '#651d32',fontweight='bold')
plt.text(worst_off_x, worst_off_y+0.016, 'Worst Offense!', fontsize=2, verticalalignment='bottom',horizontalalignment='center', color = '#ffd105')
plt.text(worst_def_x, worst_def_y+0.01, 'Worst Defence!', fontsize=2, verticalalignment='bottom',horizontalalignment='center', color = '#bd2f19')

#manually added text for OUA Men's League
plt.text(best_def_x, 0.871, 'Record: 19-3', fontsize=2, horizontalalignment='center', color='#651d32',fontweight='bold')
plt.text(1.058, 0.8819, 'Record: 19-3', fontsize=2, horizontalalignment='center', color='#febe10',fontweight='bold')
plt.text(1.0579, 0.888, 'Beat Ottawa Twice!', fontsize=2, horizontalalignment='center', color='#febe10',fontweight='bold')
plt.text(1.007, 0.96, 'Carelton Era Over?', fontsize=2, horizontalalignment='center', color='#00000d', fontweight='bold',alpha =0.8)
plt.text(1.014, 0.909, 'Still runs Toronto', fontsize=2, horizontalalignment='center', color='#003594',fontweight='bold')
plt.text(0.983, 0.945, 'Most Improved!', fontsize=2, horizontalalignment='center', color='#005185',fontweight='bold')
plt.text(1.03, 1.008 ,'All Offense\nPractice Cone Defence', fontsize=5, horizontalalignment='center', color='#c2c1c0', alpha=0.3)


plt.show()

