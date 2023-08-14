limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disc => Programação de Computadores
    @Autor => Wenes Aquino -> 2º Períldo
"""#-----------------------------------------------------------

"""
1 lat = 18 lt
1 lt  = 3m^2 => 18lt = (54m^2)
1 lat = (R$ 80,00)
"""

area = float(input("Digite o tamanho da área: "))

quantidade_lata = area / 54
preco_total = 80 * quantidade_lata

print(f"""
      Orçamento de Tintas:
      
      Total Latas = {quantidade_lata}
      Volor Total = R$ {preco_total}
""")