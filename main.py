import time
import math
from typing import KeysView
from telegram import chat, user
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import respostas as R
from telegram.ext import Updater
import telegram
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


## texto das newsletters ! o primeiro paramentro indica a semana e o segundo a parte da newsletter sendo ilustrado

texto1 = 'O clássico mais citado como livro favorito na nossa pesquisa de hábitos de leitura. \n'
texto1_2= '\n A obra começa quando um aviador tem um problema em seu avião e fica preso no meio do deserto. Logo depois, uma criança, com roupas reais e uma inocência cativante, surge como que por um milagre salvador. É o Pequeno Príncipe, que vem do asteroide B-612, um “planeta” em que só cabe uma pessoa (ele mesmo, rs). Com o aparecimento de uma rosa, que o encanta, mas o assusta ao mesmo tempo, o príncipe foge. Ao longo do livro, ele passa de planeta em planeta, e conhece diversas personagens com personalidades completamente diferentes, até chegar na Terra - e nos levantar questões sobre nossa moral e nossa convivência com o externo.'
texto1_3 = 'As aquarelas originais, já símbolos do livro, são – em minha humilde opinião – maravilhosas, e entram em total contexto com a leveza do Pequeno Príncipe e sua ingenuidade, que nos traz a moral de nossa criança interior.'
texto1_4 ='Talvez o que mais cative na história seja a biografia do autor, Antoine de Saint-Exupéry, e as semelhanças inacreditáveis entre sua vida e a história do piloto do livro (Saint-Exupéry realmente caiu no deserto no Saara... já imaginou?). O autor também tem uma história da vida real que aparece no livro por meio da rosa. Ele teve um romance complicado, com uma mulher de El Salvador, chamada Consuelo. O relacionamento, sempre entre “tapas e beijos”, é tido como inspiração para a história entre a Rosa e o Pequeno Príncipe.'
TextoInicio = 'Olá eu sou o LiteGato_Bot e sou apaixonado por leitura!'
TextoDeBoasVindas= 'Olá eu sou o @LiteGato_Bot 🐱 e sou apaixonado por leitura! 📚 \nMeu trabalho aqui é distribuir as newsletters 📧 da minha mamãe Mariana 👩‍🦰 \nEu posso distribuir a mais nova neslettter ou as versões passadas! Qual vai querer? \n Digite\n /0 para a Nova \n /1 para acessar as versões passadas'
TextoDoFim = 'Pronto essa foi a newsletter da semana escolhida, se quiser ver mais é só digitar /newsletter! 🥰😸😽'

texto2 = 'Bom, vamos lá: De um lado, temos Evelyn Hugo, uma atriz de Hollywood, beirando os 80 anos. Do outro, Monique, uma jornalista que estava estagnada, mas agora conta, com exclusividade, a história de Evelyn e dos sete maridos da atriz, ao que a obra se resume. '
texto2_1 ='Talvez, o ponto mais impactante – destacado em diversas resenhas – seja a forma com que a autora explora a feminilidade e nos faz refletir sobre o papel que a mulher toma, seja na década de 50 ou nos dias de hoje. A obra, além de ser um romance jovem adulto bem escrito, com certeza também é uma fonte para reflexão e indagação.'
texto2_2 ='No podcast Variartes, eles debatem temas cotidianos e incorporam histórias de livros nas conversas. Nesse segundo episódio, com o tema “casamento”, Evelyn Hugo é muito bem citada.'

texto3 = ' Uma obra de angústias, matrimônio e crises. E aqui vai uma sinopse rápida, pra você pegar o contexto:  Bentinho havia sido prometido padre pela mãe, mas também havia tido prometido casamento à Capitu. Nisso, vai ao seminário, mas em uma das visitas à família, decide abandonar a carreira no clero. Depois, se casa, e tem um filho - que nasce (de acordo com as palavras do próprio Bentinho) a cara do seu melhor amigo: Escobar.  Capitu nega, mas já era tarde: o ciúme já tinha tomado conta de tudo.  Intrigas pra lá, discussões pra cá... e ainda se discute se ela traiu ou não traiu. É uma história fantástica, que só você mesmo lendo pra formar sua própria opinião! '
texto3_1='Essa é uma das maiores polêmicas literárias nacionais – se não a maior, e levanta o poder de questionamento a uma narração em primeira pessoa, ainda mais vinda de uma pessoa não tão confiável...\nMas, não acho que fosse isso que Machado quisesse. Tanto que ele morreu sem nunca contar a ninguém quem era o pai de Ezequiel. “Dom Casmurro” vai muito além de uma traição. É um romance quase proibido por ordem divina, com personagens fantásticas e com uma construção impecável. Quando li pela primeira vez, me senti traída junto com Bentinho. Pela segunda, me senti, junto de Capitu, ofendida pela acusação. Machado tem esse dom de te fazer entrar na obra - literalmente fugir da realidade.'


######################


API_KEY = '2034974533:AAHVSm2c-XU7rgLJhdFOirH-oiqCslRkl0Q'
bot = telegram.Bot(token=API_KEY)
try:
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0

print('Bot inicou...')

def get_chat_id(update, context):
  chat_id = -1

  if update.message is not None:
    # from a text message
    chat_id = update.message.chat.id
  elif update.callback_query is not None:
    # from a callback message
    chat_id = update.callback_query.message.chat.id

  return chat_id
def start_command(update, context):
    update.message.reply_text(TextoInicio)

def help_command(update, context):
    update.message.reply_text('Caso precise de ajuda pesquisa no google')

def actual_newsletter(update, context):
    ## atualizar a cada quarta !
    context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Com vocês, uma relação entre as obras de George Orwell e Karl Marx!')
    context.bot.send_message(chat_id = get_chat_id(update, context),text ='Mas, por uma voz diferente.')
    context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Eu sou a Julia Andrade, mas pode me chamar de Ju, e vou ser a redatora dessa semana. Eu sou apaixonada por Literatura desde antes de me entender por gente e durante muito tempo achei que iria para área de Letras, mas atualmente curso História na Universidade Federal de Minas Gerais (UFMG). Vocês podem me encontrar em todas as redes pelo @juliacsandrade.')
    context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Essa semana vamos conversar sobre a obra conhecida como “Revolução dos Bichos 🐷 ”... Na verdade, o autor, George Orwell, prefere que ela seja chamada de “A Fazenda dos Animais”. Sabia dessa? Chegue mais!')
    context.bot.send_message(chat_id = get_chat_id(update, context),text = 'A história é uma fábula, com animais falantes moradores de uma fazenda. Insatisfeito com a forma como são (mal)tratados e (des)cuidados pelo dono da fazenda, o porco mais velho da fazenda, Major, pede que todos os animais se reúnam no celeiro para um anúncio após ter um sonho incomum. No encontro, Major aconselha a união de todos os animais para acabar com a tirania do fazendeiro e criar a primeira fazenda gerenciada e mantida por animais. ')
    context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://i.imgur.com/ym67QTz.gif' )     
    context.bot.send_message(chat_id = get_chat_id(update, context),text ='Pelo título comumente usado na tradução do livro, levamos o leve “spoiler” de que o levante de fato se concretiza, tornando a fazenda, e tudo que ali é produzido, propriedade dos bichos. A fazenda começa a ser administrada principalmente pelos porcos em virtude da suposta “superioridade intelectual” deles nesse contexto. Ao decorrer da narrativa, fica clara a analogia à União Soviética e ao Governo de Stalin, além de alguns conceitos de Marx como a alienação religiosa (representada pelo corvo Moisés) e do trabalho (representada pelo cavalo Sansão).')
    context.bot.send_message(chat_id = get_chat_id(update, context),text ='Muitas vezes os livros de George foram usados como propaganda anticomunista, quando na verdade o autor sempre se declarou socialista em suas posições e quando suas obras mais famosas, A Fazenda dos Animais e 1984, são críticas a governos totalitários. A falta da habilidade de interpretação faz as pessoas passarem cada vergonha... ')
    context.bot.send_message(chat_id = get_chat_id(update, context),text ='Ju Indica!')
    context.bot.send_message(chat_id = get_chat_id(update, context),text ='Caso você tenha se interessado pela obra ou até se você já leu, fica aqui a minha forte recomendação para a leitura do prefácio de Morris Dickstein. Essas poucas páginas fizeram toda a diferença na minha leitura, porque me deram o contexto sobre os pensamentos políticos e pretensões de Orwell, citações de ensaios do autor e que embasavam críticas sutis da fábula e melhor as explorava, interpretações que eu não peguei de primeira leitura. De verdade? Prato cheio, vale muito a leitura. Mas lembre-se: vai estar recheado de “spoilers”, então leia depois de terminar o livro.')
    context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)

def handle_message(update,context):
    mensagem = str(update.message.text).lower()
    user_messages= str(mensagem).lower()
    print(user_messages)
    if user_messages in ('Ola', 'Olá', 'Oi', 'oi','ola','newsletter','newsletters','Newsletters','Newsletter','/start','/newsletter','/Newsletter'):
        context.bot.send_message(chat_id= get_chat_id(update,context), text = TextoDeBoasVindas)
    if user_messages in ('1','/1'):
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Escolha qual semana vai Querer? \n/primeira Pequeno Principe 🤴 \n/segunda Os Sete Maridos de Evelyn Hugo 👰\n/terceira Dom Casmurro 🕴️\n/quarta Capitães da Areia 🪖⏳\n/quinta Harry Potter ⚡🤓') 
    if user_messages in ('0','/0'):
        actual_newsletter(update, context)
    if user_messages in ('/primeira', 'primeira'):
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Essa Semana o tema é o Pequeno Principe 🤴')
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://i.pinimg.com/originals/05/d8/58/05d85847f27bedeffec3bb48c90233c5.gif' ) 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = texto1) 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = texto1_2)
        context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Detalhes, nossos detalhes...')
        context.bot.send_message(chat_id = get_chat_id(update, context), text = texto1_3)
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://capricho.abril.com.br/wp-content/uploads/2019/03/o-pequeno-principe.gif' ) 
        context.bot.send_message(chat_id = get_chat_id(update, context), text='Sobre o autor - e a rosa 🌹')
        context.bot.send_message(chat_id = get_chat_id(update, context), text = texto1_4) 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Mari Indica!') 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Aos que são apaixonados por clássicos que nos fazem retomar a ingenuidade, Meu Pé de Laranja Lima, de José Mauro de Vasconcelos, não pode ficar da lista de leituras, e nem Campo Geral, do Guimarães Rosa.  Ambos são nacionais, com protagonistas crianças e com a visão de mundo típica da ingenuidade das mentes infantis.') 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)
    if user_messages in ('/segunda','segunda'):
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Essa Semana o tema é Os Sete Maridos de Evelyn Hugo 👰')
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://clubedolivrojf.files.wordpress.com/2016/04/rapunzel-books.gif?w=364' ) 
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Reflexões nossas de cada dia')
        context.bot.send_message(chat_id = get_chat_id(update, context), text =  texto2_1)
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Vale a pena conferir!')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = texto2_2)
        context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)
    if user_messages in('/terceira','terceira'):
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Essa Semana o tema é Dom Casmurro 🕴️')
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://img-s1.onedio.com/id-58dd75330a093df01ca2b46c/rev-0/w-900/h-539/f-gif/s-6aae40268f2b916eb197fcc35df1e050c90a7d36.gif' ) 
        context.bot.send_message(chat_id = get_chat_id(update, context),text = texto3)
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'E... traiu ou não?')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = texto3_1)
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://external-preview.redd.it/10Xiqpwr2EarX_nC4Vc4jmDB6BQdxRIS-SRPtLE0fB4.gif?format=mp4&s=e0d6da556f7cf8c3cdc6d87df860f594950feea9' ) 
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Embora haja quem insista...')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'E, com isso, inúmeros pesquisadores até hoje vão atrás de "provas", mensagens subliminares, códigos secretos e tudo mais. Deixo disponível para vocês as que mais achei interessantes!')
        context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Mari Indica!') 
        context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Seguindo a mesma linha da semana passada, acredito que para os que amaram - assim como eu - Dom Casmurro, a melhor recomendação sejam as outras obras de Machado. Deixo aqui as minhas preferidas: Quincas Borba e O Alienista!')
        context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)
    if user_messages in ('/quarta','quarta'):
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Capitães da Areia 🪖⏳')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Os capitães da areia são um bando de meninos de rua que vivem da criminalidade. O livro mostra a essência do indivíduo em uma sociedade que descarta indigentes. Sempre com um olhar anacrônico, Pedro Bala, o líder do grupo, ilustra como o sistema nos encarcera sem nos darmos conta. Embora se mostre “másculo” para os capitães, conhecemos seu lado mais empático pelo romance que ele vive com Dora.\nÉ um livro sobre seres humanos que aprenderam a sobreviver em meio à desigualdade.')
        context.bot.send_photo(chat_id = get_chat_id(update, context), photo = 'https://i.ytimg.com/vi/HT4_SXk4GnI/maxresdefault.jpg')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Pedro Bala, Peter Pan proletário?')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Há umas semanas, li uma matéria que comparava as personagens. Na fantasia de Peter Pan, os meninos órfãos não crescem e permanecem ingênuos, algo que faz sentido para a realidade da Inglaterra do começo do século XX. Aqui no Brasil, Bala também cuida de meninos órfãos, mas que amadurecem rápido, porque aprendem a lidar com a dureza do mundo real. \nDepois que reli Capitães de Areia com esse ponto de vista, não foi difícil perceber a crítica trazida por Jorge Amado, o questionamento social levantado por ele. Deixo aqui o link da matéria para você conferir.')
        context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://media1.giphy.com/media/lDR0wnXboVr8c/giphy.gif?cid=ecf05e4700leqfm871zewz8glf9im5szk3h11c7fcutyj76f&rid=giphy.gif&ct=g')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Mari Indica!')
        context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Para quem gosta de livros críticos, com teor de realidade, eu super recomendo os outros livros de Jorge Amado, e “Vidas Secas”, do Graciliano Ramos (inclusive, “Angústia”, também do Graciliano, é uma boa aposta para entender a decadência da classe média por meio de um protagonista que não consegue agir para mudar apesar de viver constantemente insatisfeito).')
        context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)
    if user_messages in('/quinta', 'quinta'):
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Essa Semana o tema é Harry Potter ⚡🤓')
          context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://hips.hearstapps.com/digitalspyuk.cdnds.net/18/02/1515415098-afecdb0272d74c2336419e4753c2d444.gif' ) 
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Tanto nos livros quanto nos filmes, a trama segue a mesma linha: Harry, aos 11 anos, vivendo sua vida pacata e infeliz com os tios, recebe uma carta de Hogwarts, uma escola de magia e bruxaria, e um convite para estudar lá. Filho de bruxos assassinados pelo Lord Valdemort – que também tentou matar Harry - ele deixa a vida de trouxa e embarca nessa aventura digna de sete livros e oito filmes. Com Rony, um ruivo de uma família super carismática, e Hermione, uma garota extremamente inteligente, muda os conceitos de magia que o mundo bruxo conhece.')
          context.bot.send_animation(chat_id = get_chat_id(update, context), animation = 'https://cdn.mensagenscomamor.com/content/images/m000495051.gif?v=1' ) 
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Assumo que, quando vi os filmes, senti falta do Rony descrito nos livros, acho que dos Weasleys todos, na verdade. Talvez o Rony tenha sido mantido apenas como alívio cômico nos filmes. E os Weasleys ficaram tão superficiais quanto o relacionamento do Harry com a Gina do cinema (nos filmes não dá pra entender de onde surge isso!!! Eles ficam juntos do NADA!). Eu entendo que é uma adaptação e que não daria para colocar tudo (infelizmente), mas faltou um pouco de esforço para manter o Rony nos padrões literários...')
          context.bot.send_animation(chat_id = get_chat_id(update,context), animation = 'https://c.tenor.com/v194NwcjTGEAAAAd/hi-there.gif')
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Mas agora, a mudança mais nada a ver dos livros para o filme foi o temperamento do Dumbledore. Ele passa de uma figura quase que paterna para uma frieza, ele é simplificado à figura de autoridade de Hogwarts. A melhor cena em que a gente pode ver isso é quando ele descobre o nome do Harry no cálice de fogo, e pergunta “calmamente” se ele colocou o nome no cálice! Segue o trecho do filme, haha!')
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'https://www.youtube.com/watch?v=menifzfzBuc&ab_channel=GabrielEduardo')
          context.bot.send_message(chat_id = get_chat_id(update, context),text = 'Mari Indica!')
          context.bot.send_message(chat_id = get_chat_id(update, context), text = 'Juro que tentei não me alongar... mas é complexo não se empolgar falando dessa obra maravilhosa. Minha recomendação é, para quem nunca leu, leia todos os livros! O primeiro livro, “Harry Potter e a Pedra Filosofal” é super curtinho e com uma escrita que te prende do começo ao fim! \nSe você já é fã da saga, “Animais Fantásticos” é do mesmo universo, mas se passa antes dos acontecimentos de Harry Potter. \nMas, para quem já conhece tudo de Harry Potter, minha recomendação é “O Lar da Srta. Peregrine para Crianças Peculiares”, de Ransom Riggs.')
          context.bot.send_message(chat_id = get_chat_id(update, context), text = TextoDoFim)

def error(update, context ):
    print(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('inicio', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling(10)
    updater.idle()

main()




