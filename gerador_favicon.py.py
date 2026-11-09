from PIL import Image, ImageDraw, ImageFont
import os

def criar_favicon():
    # Dimensões de alta resolução para nitidez em telas Retina (512x512 pixels)
    tamanho = 512
    img = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Cores baseadas no estilo Claymorfismo / Dark Mode do seu portfólio
    cor_fundo = (22, 27, 34)       # #161b22 (Tom escuro principal)
    cor_borda = (48, 54, 61)       # #30363d (Borda sutil)
    cor_destaque = (88, 166, 255)  # #58a6ff (Azul técnico)
    cor_texto = (240, 246, 252)    # #f0f6fc (Texto claro)

    # Desenha o fundo arredondado (estilo card moderno)
    padding = 20
    raio_borda = 110
    draw.rounded_rectangle(
        [padding, padding, tamanho - padding, tamanho - padding],
        radius=raio_borda,
        fill=cor_fundo,
        outline=cor_borda,
        width=12
    )

    # Adiciona as iniciais "LC" (Lucenildo Cerqueira) estilizadas
    # Se você tiver uma fonte TrueType (.ttf) instalada no Linux, pode substituir None
    try:
        # Tenta carregar uma fonte padrão do sistema Linux Mint
        fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 190)
    except IOError:
        fonte = ImageFont.load_default()

    # Desenha o texto centralizado
    texto = "LC"
    # Calcula o tamanho do texto para centralização perfeita
    bbox = draw.textbbox((0, 0), texto, font=fonte)
    largura_texto = bbox[2] - bbox[0]
    altura_texto = bbox[3] - bbox[1]
    
    x = (tamanho - largura_texto) / 2 - bbox[0]
    y = (tamanho - altura_texto) / 2 - bbox[1] - 10

    # Sombra sutil para dar profundidade (efeito tátil)
    draw.text((x + 6, y + 6), texto, fill=(0, 0, 0, 180), font=fonte)
    # Texto principal
    draw.text((x, y), texto, fill=cor_texto, font=fonte)

    # Detalhe técnico minimalista (linha de destaque inferior)
    draw.rounded_rectangle(
        [150, 390, 362, 410],
        radius=8,
        fill=cor_destaque
    )

    # Salva em formato PNG de alta qualidade para o favicon
    nome_arquivo = "favicon.png"
    img.save(nome_arquivo, "PNG")
    print(f"[Sucesso] Favicon gerado e salvo como '{nome_arquivo}' na pasta atual!")

if __name__ == "__main__":
    criar_favicon()