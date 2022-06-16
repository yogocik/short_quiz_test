shout_rules = {
    3 : 'tik',
    5 : 'tek'
}

participant_list = ['A','B']

def added_shout_rules(rule:dict) -> None:
    shout_rules.update(rule)

def added_participant(participant:object) -> None:
    participant_list.append(participant)

def start_play(initial_counter:int=1, change_step:int=1, 
               max_counter:int=500, 
               participant:list=participant_list, 
               rules:dict=shout_rules) -> None:
    shout_counter = 0
    max_shout = len(participant) - 1
    while initial_counter <= max_counter:
        shouted_participant = participant[shout_counter]
        added_word = " ".join([val for key, val in rules.items() if initial_counter%key == 0])
        print('{} shouted {} {}'.format(shouted_participant,initial_counter,added_word)) 
        initial_counter+=change_step
        if shout_counter < max_shout:
            shout_counter+=1
        else:
            shout_counter = 0

# Scenario 1 when there are 2 players with 2 rules
print('Scenario 1 with 2 players and 2 rules')
start_play(max_counter=30)
# Scenario 2 when there is 1 player and 1 rule addition
added_shout_rules({7:"tok"})
added_participant('C')
print('Scenario 2 with 3 players and 3 rules')
start_play(max_counter=105)



