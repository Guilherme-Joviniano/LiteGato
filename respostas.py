# Primeiro formatar todos os texots das newsletters
# Segundo aprender a mandar imagens e gifs ! 


from typing import KeysView
from telegram import user
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

texto1 = 'Hoje, o tema é O Pequeno Príncipe.  \n O clássico mais citado como livro favorito na nossa pesquisa de hábitos de leitura. \n'
texto1_2= '\n A obra começa quando um aviador tem um problema em seu avião e fica preso no meio do deserto. Logo depois, uma criança, com roupas reais e uma inocência cativante, surge como que por um milagre salvador. É o Pequeno Príncipe, que vem do asteroide B-612, um “planeta” em que só cabe uma pessoa (ele mesmo, rs). Com o aparecimento de uma rosa, que o encanta, mas o assusta ao mesmo tempo, o príncipe foge. Ao longo do livro, ele passa de planeta em planeta, e conhece diversas personagens com personalidades completamente diferentes, até chegar na Terra - e nos levantar questões sobre nossa moral e nossa convivência com o externo.'

def respostas(input_texto):
    user_messages = str(input_texto).lower()
    if user_messages in ('Ola', 'Olá', 'Oi', 'oi','ola'):
        return 'Olá eu sou o @LiteGato_Bot 🐱 e sou apaixonado por leitura! 📚 \nMeu trabalho aqui é distribuir as newsletters 📧 da minha mamãe Mariana 👩‍🦰 \nEu posso distribuir a mais nova neslettter ou as versões passadas! Qual vai querer? \n Digite\n [0] para a Nova \n [1] para acessar as versões passadas'
    if user_messages in ('Tchau', 'tchau', 'bye'):
        return 'Já vai? 🙀😿'
