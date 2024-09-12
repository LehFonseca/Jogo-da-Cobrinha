import pygame
import random

# Inicialização do pygame
pygame.init()

# Definições de cores
cores = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'vermelho': (213, 50, 80),
    'verde': (0, 255, 0),
    'azul': (50, 153, 213)
}

# Configurações da tela
largura_tela, altura_tela = 600, 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio
relogio = pygame.time.Clock()

# Configurações da cobrinha
tamanho_bloco, velocidade = 20, 15

# Fonte para a pontuação
font_style = pygame.font.SysFont(None, 50)

def mostrar_pontuacao(pontuacao):
    valor = font_style.render(f"Pontuação: {pontuacao}", True, cores['branco'])
    tela.blit(valor, [0, 0])

def desenhar_cobrinha(lista_cobrinha):
    for x, y in lista_cobrinha:
        pygame.draw.rect(tela, cores['verde'], [x, y, tamanho_bloco, tamanho_bloco])

def jogo():
    x1, y1 = largura_tela // 2, altura_tela // 2
    x1_mudanca, y1_mudanca = 0, 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = random.randrange(0, largura_tela - tamanho_bloco, tamanho_bloco)
    comida_y = random.randrange(0, altura_tela - tamanho_bloco, tamanho_bloco)

    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca, y1_mudanca = -tamanho_bloco, 0
                elif evento.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca, y1_mudanca = tamanho_bloco, 0
                elif evento.key == pygame.K_UP and y1_mudanca == 0:
                    x1_mudanca, y1_mudanca = 0, -tamanho_bloco
                elif evento.key == pygame.K_DOWN and y1_mudanca == 0:
                    x1_mudanca, y1_mudanca = 0, tamanho_bloco

        x1, y1 = x1 + x1_mudanca, y1 + y1_mudanca

        if x1 < 0 or x1 >= largura_tela or y1 < 0 or y1 >= altura_tela:
            game_over = True

        tela.fill(cores['azul'])
        pygame.draw.rect(tela, cores['vermelho'], [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        lista_cobrinha.append([x1, y1])
        if len(lista_cobrinha) > comprimento_cobrinha:
            lista_cobrinha.pop(0)

        if [x1, y1] in lista_cobrinha[:-1]:
            game_over = True

        desenhar_cobrinha(lista_cobrinha)
        mostrar_pontuacao(comprimento_cobrinha - 1)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = random.randrange(0, largura_tela - tamanho_bloco, tamanho_bloco)
            comida_y = random.randrange(0, altura_tela - tamanho_bloco, tamanho_bloco)
            comprimento_cobrinha += 1

        relogio.tick(velocidade)

    pygame.quit()

jogo()
