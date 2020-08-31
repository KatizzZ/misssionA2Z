import random
import json
import os

def shuffle_dictinary(d):
    dict_list = list(d.items())
    random.shuffle(dict_list)
    return dict(dict_list)

teams_and_states = {
    'Rhino Hurricanes':'Uttar_Pradesh',
    'Black Bullets':'Uttar_Pradesh',
    'Thunder Commandos':'Uttar_Pradesh',
    'Midnight Stars':'J_K',
    'Rocky Assassins':'Delhi',
    'Real Madrid':'Delhi',
    'Flying Xpress':'Delhi',
    'The Showstoppers':'Delhi',
    'Skull Fireballs':'Goa',
    'Retro Heroes':'Haryana',
    'Venomous Sharks':'Haryana',
    'Wolfsburg':'Haryana',
    'Knockout Busters':'Madhya_Pradesh',
    'Spirit Blockers':'Andra_Pradesh',
    'Wind Kamikaze Pilots':'Kerala',
    'Retro Chuckers':'Uttarakhand',
    'Silver Wasps':'Uttarakhand',
    'Venomous Cyborgs':'West_Bengal',
    'Quicksilver Ninjas':'Sikkim',
    'Demolition Piledrivers':'Rajasthan',
    'Lions':'Punjab',
    'Raging Spanners':'Himachal_Pradesh',
    'Poison Spiders':'Odisha',
    'Killer Stars':'Nagaland',
    'Knockout Busters':'Madhya_Pradesh'
}
super_eight_qualifiers = {
  'Striking Sharpshooters': 'Delhi',
  'Blue Bombers': 'Haryana',
  'Blue Geckos': 'Madhya_Pradesh',
  'Midnight Miners': 'Uttar_Pradesh',
  'Alpha Blockers': 'Rajasthan',
  'Tornado Geckos': 'Punjab',
  'Muffin Racers': 'Maharashtra',
  'Black & White Gangstaz': 'Andra_Pradesh'
}

teams_and_states = shuffle_dictinary(teams_and_states)
super_eight_qualifiers = shuffle_dictinary(super_eight_qualifiers)

Groups,i = {},0
for first_team,first_team_state in super_eight_qualifiers.items():
    individual_group = {}
    individual_group[first_team] = super_eight_qualifiers[first_team]
    number_of_teams = 0
    teams_and_states_copy = teams_and_states
    while number_of_teams < 3:
        for team,state in teams_and_states_copy.items():
            if state not in  ([] for state in individual_group.values()) and teams_and_states[team] != '':
                individual_group[team] = state
                teams_and_states[team] = ''
                number_of_teams+=1
            if number_of_teams >= 3:
                break
        number_of_teams+=1
    Groups['Group {}'.format(chr(ord('A')+i))] = individual_group
    i+=1
    # Groups.append(individual_group)

with open('xmpl.json', "w") as file:
    # dct,i={},0
    # for d in Groups:
    #     # chr(ord('A')+i) way to incement character in python
    #     group = 'Group {}'.format(chr(ord('A')+i))
    #     dct[group]=d
    #     i+=1
    file.write(json.dumps(Groups))
    file.close()

print('output file xmpl.json is saved at directory {}'.format(os.getcwd()))
