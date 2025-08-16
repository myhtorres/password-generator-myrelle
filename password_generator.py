# -----------------------------------------------
# GERADOR DE SENHAS – versão simples 
# -----------------------------------------------
# Objetivo: gerar senhas com letras, números e símbolos,
#           escolhendo o tamanho e quais conjuntos usar.
# Bibliotecas padrão:
# - string: listas de caracteres (letras, dígitos, pontuação)
# - random: sorteio de caracteres
# -----------------------------------------------

import string
import random

def montar_conjunto(usar_maiusculas: bool, usar_numeros: bool, usar_especiais: bool) -> str:
    """Monta a lista de caracteres possíveis a partir das escolhas do usuário."""
    conjunto = string.ascii_lowercase  # sempre inclui minúsculas
    if usar_maiusculas:
        conjunto += string.ascii_uppercase
    if usar_numeros:
        conjunto += string.digits
    if usar_especiais:
        conjunto += string.punctuation
    return conjunto

def gerar_senha(tamanho: int, conjunto: str) -> str:
    """Gera a senha sorteando 'tamanho' caracteres do 'conjunto'."""
    if not conjunto:
        conjunto = string.ascii_lowercase  # fallback simples
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(conjunto)
    return senha

def ler_inteiro_positivo(pergunta: str, minimo: int = 1, maximo: int = 128) -> int:
    """Lê um número inteiro do usuário e valida faixa mínima/máxima."""
    while True:
        valor = input(pergunta).strip()
        if not valor.isdigit():
            print("Digite um número inteiro válido.")
            continue
        numero = int(valor)
        if numero < minimo:
            print(f"Digite um número ≥ {minimo}.")
            continue
        if numero > maximo:
            print(f"Digite um número ≤ {maximo}.")
            continue
        return numero

def ler_sim_nao(pergunta: str) -> bool:
    """Pergunta S/N e retorna True (sim) ou False (não)."""
    while True:
        resp = input(pergunta + " (s/n): ").strip().lower()
        if resp in ("s", "sim"):
            return True
        if resp in ("n", "nao", "não"):
            return False
        print("Responda com 's' para sim ou 'n' para não.")

def menu():
    """Menu simples no terminal."""
    print("\n🔐 GERADOR DE SENHAS (simples) 🔐")
    while True:
        print("\n[1] Gerar nova senha")
        print("[2] Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tamanho = ler_inteiro_positivo("Tamanho da senha (1 a 128): ", 1, 128)
            usar_maiusculas = ler_sim_nao("Incluir letras MAIÚSCULAS?")
            usar_numeros    = ler_sim_nao("Incluir NÚMEROS?")
            usar_especiais  = ler_sim_nao("Incluir SÍMBOLOS?")
            conjunto = montar_conjunto(usar_maiusculas, usar_numeros, usar_especiais)
            senha = gerar_senha(tamanho, conjunto)
            print("\n✅ Senha gerada:")
            print(senha)
        elif opcao == "2":
            print("Até mais! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
