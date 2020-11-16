from random import randint
import dreams
from user_messages import get_message as msg


TOTAL_BOARD_POSITIONS = 20


def end_balance(current_balace, question_money):
    balance_change = float(question_money)
    if question_money != 0:
        current_balace += balance_change
    return current_balace


def move_player(player):
  player["board_position"] += dice_roll()


def player_board_turn(player):
  if player["board_position"] > TOTAL_BOARD_POSITIONS:
    player["board_turns"] += 1
    player["board_position"] -= TOTAL_BOARD_POSITIONS


def dice_roll():
  return randint(1, 6)

def show_positive_event(positive_event_list):
  print(positive_event_list[randint(len(min(positive_event_list)), len(max(positive_event_list)))])

def show_negative_event(negative_event_list):
  print(negative_event_list[randint(len(min(negative_event_list)), len(max(negative_event_list)))])

def show_board_position_event(player):
  if player["board_position"] != 0:
    if player["board_position"] % 2 == 0:
      show_positive_event()
    else:
      show_negative_event()
