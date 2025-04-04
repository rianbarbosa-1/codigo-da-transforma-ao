print('olá mundo')
caixa= 'caneta' 

print(caixa)

nome='rian'
idade=15
altura=1.73
estudante=True

print(f'nome:{nome},idade:{idade},{altura},altura,{estudante}estudante ')

mensagem = "python é divertido"   
print(mensagem.strip())  
print(mensagem.lower()) 
print(mensagem.upper())
nome=input("qual e o seu nome?")
print(f'ola{nome},seja bem vindo a introducao python')


from datetime import datetime

nome=input("qual o seu nome?")
agora=datetime.now()
hora_atual=agora.strftime("%H:%M")
print(f'ola,{nome}!agora sao {hora_atual}.')