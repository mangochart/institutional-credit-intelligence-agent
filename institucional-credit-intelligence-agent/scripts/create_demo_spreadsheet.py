import pandas as pd

print("📊 CRIANDO PLANILHA PARA A POC DA CDL...")
print()

# Dados de exemplo para demonstração
dados_poc = {
    "Nome_Cliente": [
        "João Silva - Mercado Central", 
        "Maria Santos - Loja de Roupas", 
        "Carlos Oliveira - Auto Peças",
        "Ana Costa - Restaurante",
        "Roberto Lima - Farmácia"
    ],
    "Valor_Divida": [2850.50, 1500.00, 3890.75, 2250.00, 1800.50],
    "Telefone_Contato": ["11999990001", "11999990002", "11999990003", "11999990004", "11999990005"],
    "Dias_Atraso": [45, 30, 90, 60, 15],
    "Status": ["Em aberto", "Em aberto", "Negociando", "Em aberto", "Atrasado"],
    "Ultimo_Contato": ["15/01/2024", "20/01/2024", "05/01/2024", "10/01/2024", "25/01/2024"]
}

df = pd.DataFrame(dados_poc)

# Salva a planilha
caminho_planilha = "data/fake_data/demonstracao_cdl.xlsx"
df.to_excel(caminho_planilha, index=False)

print(f"✅ PLANILHA CRIADA: {caminho_planilha}")
print()
print("📋 CONTEÚDO DA PLANILHA:")
print("="*60)
print(df.to_string())
print()
print("💰 RESUMO FINANCEIRO:")
print(f"   • Total de clientes: {len(df)}")
print(f"   • Dívida total: R$ {df['Valor_Divida'].sum():,.2f}")
print(f"   • Média por cliente: R$ {df['Valor_Divida'].mean():,.2f}")
print()
print("🎯 PARA A DEMONSTRAÇÃO DA CDL:")
print("   • O agente vai ler ESTA planilha")
print("   • Vai identificar automaticamente as colunas")
print("   • Vai simular o envio de mensagens")
print("   • Vai mostrar o potencial de recuperação")