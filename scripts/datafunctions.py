#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

def usports_team_data(stats_url, no_of_teams):
    '''
    This function takes thr url of the usport's team stats and the number of teams and returns a
    dataframe of the team and their stats removing any rows of team that didnt play that season.
    '''
    #perfrom GET request to the URL and returns the server response to the HTTP request
    page = requests.get(stats_url)
   
    if(page.status_code != 200):
        print("USport's Server did not respond with HTTP request")

    #parse html document
    soup = BeautifulSoup(page.content, 'html.parser')

    #Find the table containing stats
    rows = soup.find_all('tr')
    
    #Intialize lists to store data
    team_names =[]
    games_played = []
    field_goals = []
    field_goal_percentage = []
    three_pointers = []
    three_point_percentage = []
    free_throws = []
    free_throw_percentage = []
    off_rebounds_per_game = []
    def_rebounds_per_game = []
    total_rebounds_per_game = []
    assists_per_game = []
    turnovers_per_game = []
    steals_per_game = []
    blocks_per_game = []
    fouls_per_game = []
    points_per_game = []
    off_efficiency = []
    net_efficiency = []
    field_goals_against = []
    field_goal_against_percentage = []
    three_pointers_against = []
    three_point_against_percentage = []
    off_rebounds_per_game_against = []
    def_rebounds_per_game_against = []
    total_rebounds_per_game_against = []
    rebounds_margin =[]
    assists_per_game_against = []
    turnovers_per_game_against = []
    steals_per_game_against = []
    blocks_per_game_against = []
    fouls_per_game_against = []
    points_per_game_against = []
    def_efficiency = []

    #Loop through each row(skip the first row as it's the header)
    for index, row in enumerate(rows[1:]):

        #exit loop when we reached end of table
        if index >= no_of_teams:
            break

        #Extract team name
        school_name = row.find('td', class_='pinned-col text').text.strip()
        team_names.append(school_name)

        #Extract data from other columns
        columns = row.find_all('td', align = 'center')
        games_played.append(columns[0].text.strip())
        field_goals.append(columns[1].text.strip())
        field_goal_percentage.append(columns[2].text.strip())
        three_pointers.append(columns[3].text.strip())
        three_point_percentage.append(columns[4].text.strip())
        free_throws.append(columns[5].text.strip())
        free_throw_percentage.append(columns[6].text.strip())
        off_rebounds_per_game.append(columns[7].text.strip())
        def_rebounds_per_game.append(columns[8].text.strip())
        total_rebounds_per_game.append(columns[9].text.strip())
        assists_per_game.append(columns[10].text.strip())
        turnovers_per_game.append(columns[11].text.strip())
        steals_per_game.append(columns[12].text.strip())
        blocks_per_game.append(columns[13].text.strip())
        fouls_per_game.append(columns[14].text.strip())
        points_per_game.append(columns[15].text.strip())
        off_efficiency.append(columns[16].text.strip())
        net_efficiency.append(columns[17].text.strip())

     #Loop through defensive stats row (skip first row(header) and second row which contains game played)
    for index, row in enumerate(rows[no_of_teams+2:]):
        
        #exit loop when we reached end of table
        if index >= no_of_teams:
            break

        #Extract data from other columns
        columns = row.find_all('td', align = 'center')
        field_goals_against.append(columns[1].text.strip())
        field_goal_against_percentage.append(columns[2].text.strip())
        three_pointers_against.append(columns[3].text.strip())
        three_point_against_percentage.append(columns[4].text.strip())
        off_rebounds_per_game_against.append(columns[5].text.strip())
        def_rebounds_per_game_against.append(columns[6].text.strip())
        total_rebounds_per_game_against.append(columns[7].text.strip())
        rebounds_margin.append(columns[8].text.strip())
        assists_per_game_against.append(columns[9].text.strip())
        turnovers_per_game_against.append(columns[10].text.strip())
        steals_per_game_against.append(columns[11].text.strip())
        blocks_per_game_against.append(columns[12].text.strip())
        fouls_per_game_against.append(columns[13].text.strip())
        points_per_game_against.append(columns[14].text.strip())
        def_efficiency.append(columns[15].text.strip())  

    data_collected = {
        'Team': team_names,
        'Games Played': games_played,
        'Points/Game': points_per_game,
        'Field Goals': field_goals,
        'Field Goal %': field_goal_percentage,
        '3-points': three_pointers,
        '3-point %': three_point_percentage,
        'Free Throws': free_throws,
        'Free Throw %': free_throw_percentage,
        'Offensive Rebounds/Game': off_rebounds_per_game,
        'Defensive Rebounds/Game': def_rebounds_per_game,
        'Total Rebounds/Game': total_rebounds_per_game,
        'Assists/Game' : assists_per_game,
        'Turnovers/Game': turnovers_per_game,
        'Steals/Game': steals_per_game,
        'Blocks/Game': blocks_per_game,
        'Team Fouls/Game': fouls_per_game,
        'Offensive Efficiency': off_efficiency,
        'Defensive Efficiency': def_efficiency,
        'Net Efficiency': net_efficiency,
        'Field Goals Against': field_goals_against,
        'Field Goals % Against': field_goal_against_percentage,
        '3-points Against': three_pointers_against,
        '3-points % Against ': three_point_against_percentage,
        'Offensive Rebounds/Game Against': off_rebounds_per_game_against,
        'Defensive Rebounds/Game Against': def_rebounds_per_game_against,
        'Total Rebounds/Game Against': total_rebounds_per_game_against,
        'Assists/Game Against': assists_per_game_against,
        'Turnovers/Game Against': turnovers_per_game_against,
        'Steals/Game Against': steals_per_game_against,
        'Blocks/Game Against': blocks_per_game_against,
        'Team Fouls/Game Against': fouls_per_game_against,
        'Points/Game Against': points_per_game_against
    }
    #create dictionary that maps university sports team to respective conference
    team_conference = {
    'Acadia': 'AUS',
    'Alberta': 'CW',
    'Algoma': 'OUA',
    'Bishop\'s': 'RSEQ',
    'Brandon': 'CW',
    'Brock': 'OUA',
    'Calgary': 'CW',
    'Cape Breton': 'AUS',
    'Carleton': 'OUA',
    'Concordia': 'RSEQ',
    'Dalhousie': 'AUS',
    'Guelph': 'OUA',
    'Lakehead': 'OUA',
    'Laurentian': 'OUA',
    'Laurier': 'OUA',
    'Laval': 'RSEQ',
    'Lethbridge': 'CW',
    'MacEwan': 'CW',
    'Manitoba': 'CW',
    'McGill': 'RSEQ',
    'McMaster': 'OUA',
    'Memorial': 'AUS',
    'Mount Royal': 'CW',
    'Nipissing': 'OUA',
    'Ontario Tech': 'OUA',
    'Ottawa': 'OUA',
    'Queen\'s': 'OUA',
    'Regina': 'CW',
    'Saint Mary\'s': 'AUS',
    'Saskatchewan': 'CW',
    'StFX': 'AUS',
    'Thompson Rivers': 'CW',
    'Toronto': 'OUA',
    'Toronto Metropolitan': 'OUA',
    'Trinity Western': 'CW',
    'UBC': 'CW',
    'UBC Okanagan': 'CW',
    'UFV': 'CW',
    'UNB': 'AUS',
    'UNBC': 'CW',
    'UPEI': 'AUS',
    'UQAM': 'RSEQ',
    'Victoria': 'CW',
    'Waterloo': 'OUA',
    'Western': 'OUA',
    'Windsor': 'OUA',
    'Winnipeg': 'CW',
    'York': 'OUA'
    }

    #Create a DataFrame
    df = pd.DataFrame(data_collected)

    # Add a new column based on the dictionary
    df['Conferences'] = df['Team'].map(team_conference)

    #remove rows with null vlaues
    df = df[df['Games Played'] != '-']

    #set index to teams
    df = df.set_index('Team')

    # Convert columns to their respective data types
    df['Games Played'] = df['Games Played'].astype(int)
    df['Field Goals'] = df['Field Goals'].astype(str)
    df['Field Goal %'] = df['Field Goal %'].astype(float)
    df['3-points'] = df['3-points'].astype(str)
    df['3-point %'] = df['3-point %'].astype(float)
    df['Free Throws'] = df['Free Throws'].astype(str)
    df['Free Throw %'] = df['Free Throw %'].astype(float)
    df['Offensive Rebounds/Game'] = df['Offensive Rebounds/Game'].astype(float)
    df['Defensive Rebounds/Game'] = df['Defensive Rebounds/Game'].astype(float)
    df['Total Rebounds/Game'] = df['Total Rebounds/Game'].astype(float)
    df['Assists/Game'] = df['Assists/Game'].astype(float)
    df['Turnovers/Game'] = df['Turnovers/Game'].astype(float)
    df['Steals/Game'] = df['Steals/Game'].astype(float)
    df['Blocks/Game'] = df['Blocks/Game'].astype(float)
    df['Team Fouls/Game'] = df['Team Fouls/Game'].astype(float)
    df['Points/Game'] = df['Points/Game'].astype(float)
    try:
        df['Offensive Efficiency'] = df['Offensive Efficiency'].astype(float)
        df['Defensive Efficiency'] = df['Defensive Efficiency'].astype(float)
        df['Net Efficiency'] = df['Net Efficiency'].astype(float)
    except:
        print(f"Some team's efficiency was not recorded")
    return df

def usports_hoop_data(url):
    """Parse HTML content containing Usports championship data
      Args: html_content :String containing the HTML data
      Returns: a list containing team names, the number of championships won/appearance, and list of years team won/apperance
    """
     #perfrom GET request to the URL and returns the server response to the HTTP request
    page = requests.get(url)
   
    if(page.status_code != 200):
        print("USport's Server did not respond with HTTP request")

    #parse html document
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the table that contains the team, no of championship and year won
    header_row = soup.find_all('table')[2]

    # Find all table rows containing team data (excluding the header)
    team_data_rows = header_row.find_all('tr')
    
     # Extract data for each team
    teams = []

    for row in team_data_rows[1:]:
        cells = row.find_all('td', align = 'center')
        first_cell =(cells[0].text.strip())
        second_cell = (cells[1].text.strip())

        #extract name of team
        team_name = f"".join(filter(lambda x: x.isalpha(), first_cell))
        
        #get list of years team won and no_of champs will be the lenght of the list
        years_won = second_cell.split(',')
        years_won[0] = years_won[0][1:]
        if(len(years_won[0]) > 4):
            years_won[0] = years_won[0][1:]

        championship_years = []
        for value in years_won:
            value = value.strip()
            try:
                int_value = int(value)
            except ValueError:
                # Handle the case where the string cannot be converted to an integer
                print(f"Error: Could not convert '{value}' to an integer.")
                continue  # Skip to the next iteration if conversion fails
            championship_years.append(int_value)

        no_of_champs_won = len(championship_years)

        #dictionary for each team
        team_info = {
            'team_name': team_name,
            'championship_count': no_of_champs_won,
            'championship_years' :championship_years
                    }
        #append each tema dictionary to teams list
        teams.append(team_info)
    
    return teams

#test df from usports (replace MBB to WBB for women's league)
apperance = usports_hoop_data('https://usportshoops.ca/history/champ-appearances.php?Gender=WBB')
print()
championship = usports_hoop_data('https://usportshoops.ca/history/champ-years.php?Gender=WBB')

mens_team = ('https://universitysport.prestosports.com/sports/mbkb/2023-24/teams?sort=&r=0&pos=off', 52)
womens_team = ('https://universitysport.prestosports.com/sports/wbkb/2023-24/teams?sort=&r=0&pos=off', 48)
selected_team = mens_team

df = usports_team_data(selected_team[0], selected_team[1])


#make two seperate functions file one from usports other from usportshoop
#which program has the most pro players from usports hoops
