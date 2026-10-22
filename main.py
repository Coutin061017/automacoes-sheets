"""Filtra alunos pendentes no Google Sheets e atualiza a aba Pendentes."""

import os
from pathlib import Path

import gspread
import pandas as pd
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent


def carregar_configuracao():
    """Valida as configurações antes de conectar ou alterar qualquer planilha."""
    load_dotenv(BASE_DIR / ".env")
    nome_credenciais = os.getenv("GOOGLE_CREDENTIALS", "").strip()
    planilha_id = os.getenv("GOOGLE_SHEETS_ID", "").strip()

    if not nome_credenciais or not planilha_id:
        raise ValueError("Configure GOOGLE_CREDENTIALS e GOOGLE_SHEETS_ID no .env local.")

    credenciais = Path(nome_credenciais)
    if not credenciais.is_absolute():
        credenciais = BASE_DIR / credenciais
    if not credenciais.is_file():
        raise FileNotFoundError("Arquivo de credenciais não encontrado. Confira GOOGLE_CREDENTIALS.")

    return credenciais, planilha_id


def preparar_valores(dados):
    """Filtra pendências, mantendo o cabeçalho mesmo quando não há resultados."""
    if not dados:
        raise ValueError("A aba 'Alunos' está vazia. Nada foi alterado.")

    df = pd.DataFrame(dados)
    if "Status" not in df.columns:
        raise ValueError("A coluna obrigatória 'Status' não foi encontrada. Nada foi alterado.")

    filtro = df["Status"].astype(str).str.strip().str.casefold() == "pendente"
    pendentes = df.loc[filtro].fillna("")
    valores = [df.columns.tolist()] + pendentes.values.tolist()
    return valores, len(pendentes)


def executar():
    credenciais, planilha_id = carregar_configuracao()
    cliente = gspread.service_account(filename=str(credenciais))
    planilha = cliente.open_by_key(planilha_id)

    aba_alunos = planilha.worksheet("Alunos")
    valores, quantidade = preparar_valores(aba_alunos.get_all_records())

    try:
        aba_pendentes = planilha.worksheet("Pendentes")
    except gspread.WorksheetNotFound:
        aba_pendentes = planilha.add_worksheet(
            title="Pendentes", rows=max(100, len(valores)), cols=max(10, len(valores[0]))
        )

    # Evita erro quando uma atualização exige mais linhas/colunas que a aba atual.
    if aba_pendentes.row_count < len(valores) or aba_pendentes.col_count < len(valores[0]):
        aba_pendentes.resize(
            rows=max(aba_pendentes.row_count, len(valores)),
            cols=max(aba_pendentes.col_count, len(valores[0])),
        )

    aba_pendentes.clear()  # Remove resultados antigos antes de gravar a lista atual.
    aba_pendentes.update(range_name="A1", values=valores)
    print(f"Planilha atualizada com sucesso: {quantidade} aluno(s) pendente(s).")


def main():
    try:
        executar()
    except (ValueError, FileNotFoundError, gspread.exceptions.GSpreadException) as erro:
        print(f"Erro: {erro}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
