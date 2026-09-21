import os
import gspread
import pandas as pd
from dotenv import load_dotenv

#  CARREGAR CONFIGURAÇÕES
load_dotenv()
credenciais = os.getenv("GOOGLE_CREDENTIALS")
planilha_id = os.getenv("GOOGLE_SHEETS_ID")
gc = gspread.service_account(filename=credenciais)
planilha = gc.open_by_key(planilha_id)
print("Conexão realizada com sucesso!")
print("Nome da planilha:", planilha.title)

# LER A ABA ALUNOS
aba = planilha.worksheet("Alunos")
dados = aba.get_all_records()
df = pd.DataFrame(dados)
print("\nlido todos os dados da planilha:")
print(df)

pendentes = df[df["Status"] == "Pendente"]
print("Alunos pendentes:")
print(pendentes)

# Verificador de aba pendente
try:
    aba_pendentes = planilha.worksheet("Pendentes")

except gspread.WorksheetNotFound:
    aba_pendentes = planilha.add_worksheet(
        title="Pendentes",
        rows=100,
        cols=10
    )
# ENVIAR O RESULTADO PARA A SEGUDA ABA
valores = [
    pendentes.columns.tolist()] + pendentes.values.tolist()

aba_pendentes.clear()

aba_pendentes.update(
    "A1",
    valores
)

print("\n================================")
print("Processo concluído!")
print("================================")
print("A aba 'Pendentes' foi atualizada.")