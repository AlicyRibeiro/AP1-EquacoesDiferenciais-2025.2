import os
from pathlib import Path

# Listar todos os notebooks na pasta atual
notebooks = list(Path('.').glob('*.ipynb'))

if not notebooks:
    print(" Nenhum notebook encontrado na pasta atual!")
    print(f"Pasta atual: {os.getcwd()}")
else:
    print(f" Notebooks encontrados:")
    for nb in notebooks:
        print(f"  - {nb.name}")
    
    # Converter o primeiro notebook encontrado
    notebook = notebooks[0]
    print(f"\n Convertendo: {notebook.name}")
    
    import subprocess, sys
    subprocess.run([
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        str(notebook)
    ])
    print(f"Conversão concluída: {notebook.stem}.html") 



#python exportar.py

"""
Professor, inicialmente enfrentei dificuldades técnicas ao tentar exportar o notebook para HTML devido a problemas de 
compatibilidade entre o Python 3.13 e as ferramentas de conversão por isso fiz esse arquivo. Após diversas tentativas e soluções alternativas, 
consegui gerar o arquivo HTML solicitado. Estou entregando tanto o arquivo .ipynb quanto sua versão em .html, ambos contendo todas
as questões resolvidas, código executado, resultados completos e gráficos. Os arquivos podem ser abertos diretamente no VS Code,
Jupyter Notebook ou qualquer navegador web (no caso do HTML).

"""