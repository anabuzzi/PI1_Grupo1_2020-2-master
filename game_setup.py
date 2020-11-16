from user_messages import get_message as msg
from utils import valid_text
from random import sample
import dreams

MAX_PLAYER_LIMIT = 4
MIN_PLAYER_LIMIT = 2
PLAYER_INITIAL_BALANCE = 50.0


def game_setup():
    nr_match_players = setup_number_match_players()
    players = setup_players(nr_match_players)
    players_ordered = shuffle_player_order(players)
    print(players)
    print(players_ordered)


def setup_number_match_players():
    valid_match_players = False
    while not valid_match_players:
        nr_match_players = int(input("Quantos jogadores para a partida? "))
        if not number_players_valid_for_match(nr_match_players):
            print(f"O número de jogadores deve ser entre {MIN_PLAYER_LIMIT} e {MAX_PLAYER_LIMIT}")
        else:
            valid_match_players = True
    return nr_match_players


def setup_players(nr_match_players):
    players = []
    while len(players) < nr_match_players:
        name = setup_player_name(players)
        dream = setup_player_dream()
        players.append(create_player(name, dream))
    return players


def setup_player_name(players):
    valid_name = False
    while not valid_name:
        name = input(msg("type_name"))
        if player_name_already_exists(name, players):
            print("Nome já selecionado. Por favor, escolha outro nome.")
            continue
        if not valid_text(name):
            name = f"Jogador {len(players) + 1}"
        valid_name = True
    return name


def setup_player_dream():
    print("Sonhos disponíveis para seleção: \n")
    available_dreams = dreams.get_dreams()
    for dream in available_dreams:
        print(f"{dream['id']} - {dream['name']} - Preço: R$ {dream['price']}")

    valid_dream_choice = False
    while not valid_dream_choice:
        dream_choice = int(input("Escolha um sonho: "))
        if not dreams.get_dream(dream_choice):
            print("Sonho inválido. Por favor escolha um sonho válido.")
            continue
        valid_dream_choice = True
    return dreams.get_dream(dream_choice)


def create_player(name, dream):
    return {
        "name": name,
        "dream": dream,
        "balance": PLAYER_INITIAL_BALANCE,
        "board_position": 0,
        "board_turns": 0
    }


def shuffle_player_order(player_list):
    player_order = sample(player_list, len(player_list))
    return player_order


def number_players_valid_for_match(nr_match_players):
    return MIN_PLAYER_LIMIT <= nr_match_players <= MAX_PLAYER_LIMIT


def player_name_already_exists(name, players):
    for player in players:
        if player["name"] == name:
            return True


def calculate_final_score(player):
  if player.balance == player.dream.dream["price"]:
      print(f"{player.name} ganhou o jogo! Sua pontuação é {player.balance}")
