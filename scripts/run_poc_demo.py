import pandas as pd
import time
import os

print("AGENTE CDL - DEMONSTRACAO DA POC")
print("="*60)

planilha_path = "data/fake_data/demonstracao_cdl.xlsx"

if not os.path.exists(planilha_path):
    print(f"Planilha nao encontrada: {planilha_path}")
    exit()

df = pd.read_excel(planilha_path)

print(f"\nTotal de registros: {len(df)}")
print(f"Colunas: {', '.join(df.columns)}")
print()

print("CLIENTES NA PLANILHA:")
print("-"*60)

for i in range(min(3, len(df))):
    row = df.iloc[i]
    print(f"\nCLIENTE {i+1}:")
    print(f"   Nome: {row['Nome_Cliente']}")
    print(f"   Divida: R$ {row['Valor_Divida']:,.2f}")
    print(f"   Telefone: {row['Telefone_Contato']}")
    print(f"   Dias atraso: {row['Dias_Atraso']}")
    
    print(f"   AGENTE: Processando...")
    time.sleep(1)
    
    print(f"   MENSAGEM PRONTA para envio")
    print(f"   Processado com sucesso")

print("\n" + "="*60)
print("RESUMO DA DEMONSTRACAO:")
print()

total_divida = df['Valor_Divida'].sum()

print(f"DIVIDA TOTAL: R$ {total_divida:,.2f}")
print()
print("DISTRIBUICAO DO VALOR RECUPERADO (90%):")
print(f"   Para o comerciante: R$ {total_divida * 0.90:,.2f}")
print(f"   Comissao CDL (3%): R$ {total_divida * 0.03:,.2f}")
print(f"   Comissao Desenvolvimento (5%): R$ {total_divida * 0.05:,.2f}")
print(f"   Comissao Assessor (2%): R$ {total_divida * 0.02:,.2f}")
print()
print("DEMONSTRACAO CONCLUIDA!")
