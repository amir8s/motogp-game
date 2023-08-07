import re

def get_input(empty_input):
  while True:  
    value = input(empty_input)
    if value == "":
      print("Input can not be empty!")
      continue
    return value

def get_teams():
  teams = []
  while True:
    try:
      num_teams = int(get_input("Enter number of teams: "))
      break
    except ValueError:  
      print("Invalid input, please enter a number")

  for i in range(num_teams):
    while True:
      team = get_input(f"Enter name for team {i+1}: ")
      if re.fullmatch(r"[a-zA-Z]+", team):
        teams.append(team)
        break
      else:
        print("Invalid team name")
  return teams   
      
def get_players(teams):
  players = []
  for team in teams:
    while True:
      try:
        count = int(get_input(f"Enter number of players for {team}: "))
        break
      except ValueError:
        print("Invalid input, please enter a number")

    team_players = []
    for i in range(count):
      while True:
        player = get_input(f"Enter name for player {i+1} of {team}: ")
        if re.fullmatch(r"[a-zA-Z]+", player):
          team_players.append(player)
          break
        else:
          print("Invalid player name")
    players.append(team_players)
  return players

def get_rounds():
  rounds = []
  while True:
    try:
      rounds_count = int(get_input("Enter number of rounds: "))
      break
    except ValueError:
      print("Invalid input, please enter a number")  

  for r in range(rounds_count):
    while True:
      round = get_input(f"Enter host country for round {r+1}: ")
      if re.fullmatch(r"[a-zA-Z]+", round):
        rounds.append(round)
        break
      else:
        print("Invalid country name")
  return rounds


def calculate_scores(teams, players, rounds):
  scores = [0] * len(teams)
  player_scores = [[0] * len(players[0]) for _ in teams]

  for r, round in enumerate(rounds):
    print(f"\nRound {r+1} hosted in {round}")

    for t, team in enumerate(teams):
      print(f"\n{team} score: {scores[t]}")
      
      for p, player in enumerate(players[t]):
      
        previous_score = player_scores[t][p]
        
        try:
          score = int(get_input(f"Enter score for {player}: "))
          scores[t] += score
          player_scores[t][p] = previous_score + score
        except ValueError:
          print("Invalid input, please enter a number")
          score = int(get_input(f"Enter score for {player}: "))
          scores[t] += score
          player_scores[t][p] = previous_score + score
  return scores, player_scores

def print_scores(teams, scores, players, player_scores):

  print("\nTeam Scores:")
  for t, team in enumerate(teams):
    print(f"{team}: {scores[t]}")
  
  print("\nPlayer Scores:")
  for t, team in enumerate(teams):
    print(f"\n{team}")
    for p, player in enumerate(players[t]):
      print(f"{player}: {player_scores[t][p]}")


teams = get_teams()
players = get_players(teams)
rounds = get_rounds()

scores, player_scores = calculate_scores(teams, players, rounds)
print_scores(teams, scores, players, player_scores)

max_score = 0
champion_player = ""
champion_team = ""

for t, team in enumerate(teams):
  for p, player in enumerate(players[t]):
    if player_scores[t][p] > max_score:
      max_score = player_scores[t][p]
      champion_player = player
      champion_team = team

print(f"\nCongratulations to {champion_player} from {champion_team} for being the champion with {max_score} points!")

