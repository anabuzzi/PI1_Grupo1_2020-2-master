import game_setup as setup
from user_messages import get_message as msg


def main():
  print(msg("type_name_blank_to_skip"))
  setup.game_setup()
  print(msg("sorting_order"))

main()
