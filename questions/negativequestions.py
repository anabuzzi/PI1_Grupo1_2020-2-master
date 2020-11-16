negativequestions= [
  {
  "id": 1,
  "question": "Fernanda ficou pensando durante o dia sobre o uso do dinheiro e ao encontrar seu amigo Bruno, este estava se organizandso justamente sobre a questão do dinheiro dinheiro. Contou a Fernanda que ajuda seu pai na loja da família e que por esta ajuda seu pai resolveu dar uma mesada em dinheiro no valor de R$ 150,00. Porém, ele devem planejar como gastá-la, pois nenhum outro dinheiro será dado ao longo do mês e ele devera cuidar de seus próprios gastos. Despesas: Compras na cantina da escola R$3,00 por dia (segunda á sexta), ônibus escolar R$1,40 dia e volta, balas e doces 3x por semana, R$2,00 - passeio no shopping 1x nom mês R$20,00. O dinheiro que Bruno recebe de mesada será suficiente para seus gastos durante o mês, considerando que todas as semanas ele gasta a mesma quantia?",
  "answer": "Não",
  "score": 50
  },
  {
  "id": 2,
  "question": "Quais desses gastos você deveria repensar nos gastos semanais para cumprir com as prioridades. 1- compras no shopping 2-alimentação 3-transporte escolar. Digite o número correspondente:",
  "answer": 1,
  "score": 100
  },
  {
  "id": 3,
  "question": "Seu video-game estragou. O conserto custa R$300,00 - Você precisa completar tarefas em casa para ganhar ajuda financeira da família. Quais dessas tarefas você cumpriria? 1- Andar de skate, 2 - Fazer pequenas tarefas em casa e ajudar minha família, 3 - Pedir dinheiro emprestado sem saber se consigo pagar, 4 - Chamar amigos para ir ao shopping e pensar nisso depois. Digite o número correspondente:",
  "answer": 2,
  "score": 200
  },
  {
  "id": 4,
  "question": "Você perdeu 100 pontos por não ter guardado o troco de lanche. Pense no seu sonho!",
  "score": -100
  },
   {
  "id": 5,
  "question": "Você guardou R$150,00 reais esse mês, mas precisará gastar R$100,00 com os cuidados do seu bichinho de estimação.",
  "score": -100
  } 

]

def get_questions():
  return negativequestions
    

def get_questions(id):
  for question in negativequestions:
    if question['id'] == id:
      return question

