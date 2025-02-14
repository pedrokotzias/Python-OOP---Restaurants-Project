from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça São Lourenço', 'Contemporâneo')
restaurante_mexicano = Restaurante('El Kabong', 'Mexicano')
restaurante_sushi = Restaurante('Sushi San', 'Japonês')

restaurante_mexicano.alternar_estado()
restaurante_praca.avaliar('José', 5)
restaurante_praca.avaliar('Maria', 4)
restaurante_praca.avaliar('João', 3)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
