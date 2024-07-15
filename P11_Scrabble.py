# P11 Scrabble

# data
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1 map letters to points
letter_to_point = {letters:points for letters, points in zip(letters, points)}

#print(letter_to_point)

# 2 add blank tiles
letter_to_point[" "] = 0
print(letter_to_point)

# 3, 4, 5, 6 define function for calculate word's points
def score_word(word):
  point_total = 0
  for letter in word.upper():
    if letter not in letter_to_point:
      point_total += 0
    else:
      point_total += letter_to_point[letter]
  return point_total

# 7, 8 test function
score1 = score_word("ฟฟฟฟ")
#print(score1)
score2 = score_word("BROWNIE")
#print(score2)
score3 = score_word("AaBbCc")
#print(score3)

# 9 map player to words
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# 10, 11, 12, 13 calculate point
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# 14 print the result
# print(player_to_points)

# 15 define function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    print("This player doesn't exist!")

# test play_word function
##print(player_to_words)
##play_word("player1", "CODE")
##play_word("player2", "CODE")
##print(player_to_words)

# define point update function
def update_point_totals(target_dict):
  score_board = {}
  for player, words in target_dict.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    score_board[player] = player_points
  return score_board

# test update_point_totals function
print("Turn 1", player_to_words)
print("Turn 1 Points", player_to_points)
print("Turn 2 Start")
play_word("player1", "CODE")
print("Turn 2", player_to_words)
print("Turn 2 Points", update_point_totals(player_to_words))