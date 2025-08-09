# Extrator de Dados de Notas Fiscais em PDF para CSV

Este script em Python lê arquivos PDF de notas fiscais, extrai informações relevantes (como número da nota, data de emissão, produtos, quantidade, valores, etc.) e salva os dados em um arquivo CSV.

## 📋 Funcionalidades

- Percorre automaticamente todos os PDFs em uma pasta especificada.
- Extrai:
  - Data de emissão
  - Número da nota fiscal
  - Código do produto
  - Descrição
  - Unidade
  - Quantidade
  - Valor unitário
  - Valor total
- Gera um arquivo `nfs_produtos.csv` com todos os dados consolidados.

## 📂 Estrutura de Saída

O CSV gerado conterá as seguintes colunas:

| Arquivo PDF | Numero NF | Código Produto | Descrição | Unidade | Quantidade | Valor Unitário | Valor Total | Data de Emissão |
|-------------|-----------|----------------|-----------|---------|------------|----------------|-------------|-----------------|

## 📦 Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - "pandas"
  - "pdfplumber"

Instale as dependências com:
---bash---
pip install pandas pdfplumber
