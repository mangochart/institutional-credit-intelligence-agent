import pandas as pd

print("CRIANDO PLANILHA PARA A POC DA CDL...")
print()

dados_poc = {
    "Nome_Cliente": ["Joao Silva - Mercado Central", "Maria Santos - Loja de Roupas", "Carlos Oliveira - Auto Pecas", "Ana Costa - Restaurante", "Roberto Lima - Farmacia"],
    "Valor_Divida": [2850.50, 1500.00, 3890.75, 2250.00, 1800.50],
    "Telefone_Contato": ["11999990001", "11999990002", "11999990003", "11999990004", "11999990005"],
    "Dias_Atraso": [45, 30, 90, 60, 15],
    "Status": ["Em aberto", "Em aberto", "Negociando", "Em aberto", "Atrasado"]
}

df = pd.DataFrame(dados_poc)
caminho_planilha = "data/fake_data/demonstracao_cdl.xlsx"
df.to_excel(caminho_planilha, index=False)

print(f"PLANILHA CRIADA: {caminho_planilha}")
print()
print("CONTEUDO DA PLANILHA:")
print("="*60)
print(df.to_string())
print()
print("RESUMO FINANCEIRO:")
print(f"   Total de clientes: {len(df)}")
print(f"   Divida total: R$ {df['Valor_Divida'].sum():,.2f}")
print(f"   Media por cliente: R$ {df['Valor_Divida'].mean():,.2f}")
