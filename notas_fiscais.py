import pandas as pd
import pdfplumber
import os   
from datetime import datetime

# Caminho do arquivo
pasta_pdfs = r'C:\Users\mdonovan\OneDrive - Simpress\Documentos\Notas Fiscais'

dados_produtos = []

# for para percorrer todos os pdfs contidos na pasta
for arquivo in os.listdir(pasta_pdfs):
    if arquivo.lower().endswith('.pdf'):
        caminho_pdf = os.path.join(pasta_pdfs, arquivo)

        with pdfplumber.open(caminho_pdf) as pdf:
            data_emissao = ""
            numero_nf = ""
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                linhas = texto.split("\n") # divie em linhas o texto

                for i, linha in enumerate(linhas):
                    if "DATA DE EMISSÃO" in linha.upper():
                        try:
                            data_emissao = linhas[i + 1].strip()
                        except IndexError as e:
                            pass
                    
                    if "SÉRIE" in linha.upper() or "Nº" in linha.upper():
                        for j in range(i+1, min(i+4, len(linhas))):
                            candidato = linhas[j].strip()
                            if candidato.isdigit() and 6 <= len(candidato) <=9:
                                numero_nf = candidato
                                break

                # for para percorer cada linha da NF    
                for linha in linhas:
                    partes = linha.split()

                    try:
                        if(
                            # bloco garantindo que tenha dados suficientes na linha
                            len(partes) >= 8 and
                            partes[-1].replace(",", "").replace(".", "").isdigit() and
                            partes[-2].replace(",", "").replace(".", "").isdigit() and
                            partes[-3].replace(",", "").replace(".", "").isdigit() and
                            partes[-4].replace(",", "").replace(".", "").isdigit() and
                            partes[-5].replace(",", "").replace(".", "").isdigit()
                        ):
                            # Separação dos campos principais
                            codigo_produto = partes[0]
                            valor_total = partes[-6].replace(",", ".")
                            valor_unitario = partes[-7].replace(",", ".")
                            quantidade = partes[-8].replace(",", ".")
                            unidade = partes[-5].replace(',', '')
                            descricao = " ".join(partes[0:-3]) # Descrição está entre código e unidade

                            dados_produtos.append({
                                "Arquivo PDF": arquivo,
                                "Numero NF": numero_nf,
                                "Código Produto": codigo_produto,
                                "Descrição": descricao,  
                                "Unidade": unidade,                              
                                "Quantidade": quantidade,
                                "Valor Unitário": valor_unitario,
                                "Valor Total": valor_total,
                                "Data de Emissão": data_emissao
                            })
                    except Exception as e:
                        continue # try except para ignorar os erros e seguir com a proxima linha

# cria um df com pd, dos dados extradios em CSV
df = pd.DataFrame(dados_produtos)
df.to_csv('nfs_produtos.csv', index=False)
print('\n==Todos os arquivos foram extraidos, verifique o arquivo salvo.==\n')
