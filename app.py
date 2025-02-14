from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça São Lourenço', 'Contemporâneo')
restaurante_mexicano = Restaurante('El Kabong', 'Mexicano')
restaurante_sushi = Restaurante('Sushi San', 'Japonês')

bebida_suco_laranja = Bebida('Suco de Laranja', 5.0, 'Grande')
prato_misto_quente = Prato('Misto Quente', 10.0, 'Pão de forma, presunto e queijo')


def main():
    pass

if __name__ == '__main__':
    main()
