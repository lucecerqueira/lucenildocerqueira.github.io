from PIL import Image, ImageDraw, ImageFont

def criar_favicon_v1_avancado():
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fundo Claymorphism escuro refinado
    draw.rounded_rectangle([20, 20, 492, 492], radius=110, fill=(22, 27, 34), outline=(48, 54, 61), width=12)
    
    # Representação de Análise Tempo-Frequência / Espectrograma (Ondas concêntricas e radiais)
    centro = (256, 240)
    
    # Linhas de grade de frequência (concêntricas)
    for r in [60, 110, 160, 210]:
        draw.arc([centro[0] - r, centro[1] - r, centro[0] + r, centro[1] + r], start=0, end=360, fill=(48, 54, 61, 160), width=4)
    
    # Eixos temporais / Vetores de Data Science (cruzamento central)
    draw.line([(256, 40), (256, 440)], fill=(48, 54, 61, 100), width=4)
    draw.line([(40, 240), (472, 240)], fill=(48, 54, 61, 100), width=4)

    # Curva de Sinal / Tempo-Frequência principal em destaque (Azul Técnico)
    pontos_sinal = [
        (70, 240), (120, 240), (150, 160), (190, 320), 
        (230, 120), (280, 360), (320, 180), (370, 240), (440, 240)
    ]
    draw.line(pontos_sinal, fill=(88, 166, 255), width=8, joint="curve")

    # Iniciais LSC estilizadas no topo da grade de processamento
    try:
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 95)
    except IOError:
        fonte = ImageFont.load_default()
        
    # Sombra e texto principal para as iniciais
    draw.text((157, 315), "LSC", fill=(0, 0, 0, 200), font=fonte)
    draw.text((153, 311), "LSC", fill=(240, 246, 252), font=fonte)
    
    # Barra indicadora de Data Science (Processamento de Dados)
    draw.rounded_rectangle([150, 420, 362, 436], radius=6, fill=(88, 166, 255))

    # Salva o arquivo final pronto para o GitHub
    img.save("favicon.png", "PNG")
    print("[Sucesso] Novo favicon V1 (Sinais, Tempo-Frequência e Data Science) gerado como 'favicon.png'!")

if __name__ == "__main__":
    criar_favicon_v1_avancado()