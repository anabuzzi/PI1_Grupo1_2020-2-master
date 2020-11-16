dreams = [
  {
  "id": 1,
  "name": "Video-game",
  "price": 2500
  },
  {
  "id": 2,
  "name": "Tênis",
  "price": 300
  },
  {
  "id": 3,
  "name": "Computador",
  "price": 3000
  },
  {
  "id": 4,
  "name": "Bicicleta",
  "price": 1000
  },
  {
  "id": 5,
  "name": "iPhone",
  "price": 4000
  },
  {
  "id": 6,
  "name": "Televisão",
  "price": 1500
  },
  {
  "id": 7,
  "name": "Viagem",
  "price": 5000
  }
]

def get_dreams():
  return dreams
    

def get_dream(id):
  for dream in dreams:
    if dream['id'] == id:
      return dream