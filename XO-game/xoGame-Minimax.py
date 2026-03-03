import math

# Tuole to store wining positions.
win_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)
)

def check_winner(current_mesh):
  for wp in win_positions:
    if all(current_mesh[pos] == "O" for pos in wp):
      return "O"
    if all(current_mesh[pos] == "X" for pos in wp):
      return "X"
  if not any(x.isdigit() for x in current_mesh):
    return "Draw"
  return None

def minimax(current_mesh, depth, isMaximizingPlayer):
  winner = check_winner(current_mesh)

  if winner == "O":
    return 10 - depth
  if winner == "X":
    return depth - 10
  if winner == "Draw":
    return 0

  if isMaximizingPlayer:
    maxEval = -math.inf
    for i in range(9):
      if current_mesh[i].isdigit():
        temp = current_mesh[i]
        current_mesh[i] = "O"
        eval = minimax(current_mesh, depth+1, False)
        current_mesh[i] = temp
        maxEval = max(maxEval, eval)
    return maxEval

  else:
    minEval = math.inf
    for i in range(9):
      if current_mesh[i].isdigit():
        temp = current_mesh[i]
        current_mesh[i] = "X"
        eval = minimax(current_mesh, depth+1, True)
        current_mesh[i] = temp
        minEval = min(minEval, eval)
    return minEval

def get_best_move(current_mesh):
  best_score = -math.inf
  best_move = -1
  for i in range(9):
    if current_mesh[i].isdigit():
      temp = current_mesh[i]
      current_mesh[i] = "O"
      score = minimax(current_mesh, 0, False)
      current_mesh[i] = temp
      if score > best_score:
        best_score = score
        best_move = i + 1
  return best_move

def game(player):
  #display current mesh
  print("\n", " | ".join(mesh[:3]))
  print("---+---+---")
  print("", " | ".join(mesh[3:6]))
  print("---+---+---")
  print("", " | ".join(mesh[6:]))

  # Loop until player valid input cell number.
  while True:
    if player == "X":
      try:
        ch = int(input(f"Enter player {player}'s choice : "))
        if str(ch) not in mesh:
          raise ValueError
        break
      except ValueError:
        print("Invalid position number.")
    else:
      ch = get_best_move(mesh)
      print(f"Computer's choice: {ch}")
      break

  mesh[ch-1] = player
  for wp in win_positions:
    if all(mesh[pos] == player for pos in wp):
      return wp
  return None

player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")

for i in range(9):
  won = game(player)
  if won:
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))
    print(f"Player {player} won! ***")
    break
  player = player1 if player == player2 else player2
else:
  # 9 moves without a win is a draw.
  print("Game ends in a draw.")