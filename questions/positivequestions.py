positivequestions= [
  {
  "id": 1,
  "question": "Um amiguinho de Joãozinho estava com uma grande dúvida: Ele queria saber quanto gastaria para poder comprar 6 pacotinhos de figurinhas para completar seu álbum. Joãozinho que é muito bom em matemática perguntou: Quanto custa cada pacotinho de figurinhas? O amiguinho respondeu: Cada pacote de figurinhas custa R$0,30. Quanto o amiguinho do Joãozinho vai gastar ?",
  "answer": 1.80,
  "score": 180
  },
  {
  "id": 2,
  "question": "Se ao comprar 6 pacotinhos de figurinhas por R$0,30 cada um, o amigo de Joãozinho gastará R$1,80. Qual será o troco do amiguinho de Joãozinho entregando R$5,00?",
  "answer": 3.20,
  "score": 320
  },
  {
  "id": 3,
  "question": "Mariana é uma trabalhadora brasileira que como tantos outros está emergindo. Arranjou um emprego, abriu uma conta no Banco do Povão e já conseguiu o seu primeiro cartão de crédito. Seu salário mensal é de R$2.000,00 mensais e seus gastos mensais contam com conta de luz R$82,00 - conta de água R$45,80 - cartão de crédito com a fatura fixa em R$1.200,85 - despesas com combustível R$500,00 e ainda despesas de alimentação no valor de R$525,00 mensais. O salário líquido de Mariana pagará todas as despesas? Considerando que você tenha um amigo que receba um salário de R$2.000,00 e tenha as despesas abaixo. Quanto faltaria para quitar as despesas? Salário: R$2.000,00 - Despesas: Luz  R$82,00 - Água R$45,80 -  Cartão de Crédito R$1.200,85 - Combustível R$500,00 - Alimentação: R$525,00",
  "answer": 353.65,
  "score": 353
  },
  {
  "id": 4,
  "question": "Felício ganha mesada todo mês de alguns de seus familiares. Para começar, Felício precisa se organizar com os valores recebidos. Ele deve saber direitinho quanto está recebendo por mês. Ele ganha R$10,00 de mesada do seu pai;  R$10,00 de mesada da vovó; Além disso, a cada dois meses Felício recebe um bônus por cumprir algumas tarefas da casa no valor de R$82,00. Felício deseja muito comprar uma bicicleta no valor de R$650,00 e ainda adicionar alguns itens opcionais no valor de R$250,00. Quanto tempo Felício precisará guardar dinheiro para conseguir alcançar o seu sonho de comprar uma bicicleta (em meses)?",
  "answer": 16,
  "score": 180
  },
   {
  "id": 5,
  "question": "Juliana guardou o troco do lanche em seu cofrinho durante 30 dias. Todos os dias colocou R$1,10 centavos. Quanto Juliana terá guardado no final do mês?",
  "answer": 33,
  "score": 33
  } 

]

def get_questions():
  return positivequestions
    

def get_questions(id):
  for question in positivequestions:
    if question['id'] == id:
      return question

