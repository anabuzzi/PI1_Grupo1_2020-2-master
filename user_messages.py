messages = [
    {
        "label": "type_name",
        "text": "Digite o nome do jogador: "
    },
    {
        "label": "type_name_blank_to_skip",
        "text": "Digite o nome de cada jogador, ou deixe em branco para pular"
    },
    {
        "label": "type_user_dream",
        "text": "Digite o sonho de "
    },
    {
        "label": "sorting_order",
        "text": "Sorteando ordem de jogada..."
    },
    {
        "label": "game_instructions",
        "text": "Preencher com instruções"
    }
]

def get_message(label):
  for message in messages:
    if message['label'] == label:
      return message['text']
