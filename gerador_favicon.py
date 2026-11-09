from PIL import Image, ImageDraw, ImageFont
import math

def criar_favicon_versao_1():
    # Versão 1: O Fractograma Circular (Arcos concêntricos e rotação autorreferencial)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fundo claymorphism escuro
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Arcos concêntricos autorreferenciais (autopadrão)
    centro = (256, 240)
    raios = [160, 120, 80, 40]
    for i, r in enumerate(raios):
        cor = (88, 166, 255, 255 - i * 40) if i % 2 == 0 else (165, 214, 255, 200)
        draw.arc([centro[0] - r, centro[1] - r, centro[0] + r, centro[1] + r], start=30, end=300, fill=cor, width=10)
        
    # Letras LSC estilizadas ao centro
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 110)
    except IOError:
        fonte = ImageFont.load_default()
        
    draw.text((170, 190), "LSC", fill=(240, 246, 252), font=fonte)
    draw.rounded_rectangle([150, 390, 362, 410], radius=8, fill=(88, 166, 255))
    
    img.save("favicon_v1.png", "PNG")
    print("[Gerado] Versão 1: Fractograma Circular (favicon_v1.png)")

def criar_favicon_versao_2():
    # Versão 2: A Matriz de Tesselação (Grid poligonal e relevo geométrico)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Padrão geométrico modular em relevo (tesselação)
    pontos_hexagono = [(256, 80), (390, 160), (390, 320), (256, 400), (122, 320), (122, 160)]
    draw.polygon(pontos_hexagono, outline=(88, 166, 255, 120), width=6)
    
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 130)
    except IOError:
        fonte = ImageFont.load_default()
        
    draw.text((155, 175), "LSC", fill=(240, 246, 252), font=fonte)
    img.save("favicon_v2.png", "PNG")
    print("[Gerado] Versão 2: Matriz de Tesselação (favicon_v2.png)")

def criar_favicon_versao_3():
    # Versão 3: O Pulso Recursivo (Onda contínua de sinal biomédico / VCG)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Onda recursiva estilo osciloscópio biomédico
    pontos_onda = [
        (60, 260), (120, 260), (160, 340), (200, 140), 
        (240, 360), (280, 200), (320, 280), (380, 260), (450, 260)
    ]
    draw.line(pontos_onda, fill=(88, 166, 255), width=10, joint="curve")
    
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
    except IOError:
        fonte = ImageFont.load_default()
        
    draw.text((180, 340), "L S C", fill=(165, 214, 255), font=fonte)
    img.save("favicon_v3.png", "PNG")
    print("[Gerado] Versão 3: Pulso Recursivo (favicon_v3.png)")

def criar_favicon_versao_4():
    # Versão 4: O Monograma Ortogonal Aninhado (Caixas proporcionais)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Caixas aninhadas (autorreferenciais)
    draw.rounded_rectangle([100, 100, 412, 412], radius=40, outline=(88, 166, 255, 80), width=6)
    draw.rounded_rectangle([140, 140, 372, 372], radius=30, outline=(88, 166, 255, 160), width=8)
    
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
    except IOError:
        fonte = ImageFont.load_default()
        
    draw.text((165, 185), "LSC", fill=(240, 246, 252), font=fonte)
    img.save("favicon_v4.png", "PNG")
    print("[Gerado] Versão 4: Monograma Ortogonal Aninhado (favicon_v4.png)")

def criar_favicon_versao_5():
    # Versão 5: O Nó Topológico (Infinito Modular / Fita contínua)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Anel topológico simétrico
    draw.ellipse([110, 110, 402, 402], outline=(88, 166, 255), width=16)
    draw.arc([150, 150, 362, 362], start=0, end=360, fill=(165, 214, 255, 100), width=8)
    
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 110)
    except IOError:
        fonte = ImageFont.load_default()
        
    draw.text((170, 195), "LSC", fill=(240, 246, 252), font=fonte)
    img.save("favicon_v5.png", "PNG")
    print("[Gerado] Versão 5: Nó Topológico (favicon_v5.png)")

if __name__ == "__main__":
    print("Gerando as 5 versões de design com autopadrão...")
    criar_favicon_versao_1()
    criar_favicon_versao_2()
    criar_favicon_versao_3()
    criar_favicon_versao_4()
    criar_favicon_versao_5()
    print("\nConcluído! Todos os arquivos (favicon_v1.png até favicon_v5.png) foram criados na pasta.")
