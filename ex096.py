def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno com as dimensões {largura}m e {comprimento}m é de: {area}m²')

lar = float(input('Largura do terreno (m): '))
comp = float(input('Comprimento do terreno (m): '))
área(lar, comp)
