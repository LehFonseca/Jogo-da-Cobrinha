import pygame
import time
import random

# Inicialização do pygame
pygame.init()

# Definições de cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Configurações da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio
relogio = pygame.time.Clock()

# Configurações da cobrinha
tamanho_bloco = 20
velocidade = 15

# Fonte para a pontuação
font_style = pygame.font.SysFont(None, 50)

def nossa_pontuacao(pontuacao):
    valor = font_style.render("Pontuação: " + str(pontuacao), True, branco)
    tela.blit(valor, [0, 0])

def nossa_cobrinha(tamanho_bloco, lista_cobrinha):
    for x in lista_cobrinha:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def jogo():
    game_over = False
    game_close = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            tela.fill(azul)
            nossa_pontuacao(comprimento_cobrinha - 1)
            mensagem = font_style.render("Você perdeu! Pressione Q para sair ou C para jogar novamente", True, vermelho)
            tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_close = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobrinha = []
        cabeca_cobrinha.append(x1)
        cabeca_cobrinha.append(y1)
        lista_cobrinha.append(cabeca_cobrinha)
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]

        for x in lista_cobrinha[:-1]:
            if x == cabeca_cobrinha:
                game_close = True

        nossa_cobrinha(tamanho_bloco, lista_cobrinha)
        nossa_pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobrinha += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()


