import pandas as pd
import matplotlib.pyplot as plt
import os

arquivo = "data/Pesquisa de atendimento_Vaga Estágio.xlsx"
os.makedirs("outputs", exist_ok=True)

def ler_dados():
    df_reclamacoes = pd.read_excel(arquivo, sheet_name="BASE - RECLAMAÇÕES")
    df_reclamacoes.columns = [col.strip().upper() for col in df_reclamacoes.columns]
    df_gerentes = pd.read_excel(arquivo, sheet_name="BASE - GERENTE E ÁREA")
    df_gerentes.columns = [col.strip().upper() for col in df_gerentes.columns]
    df_reclamacoes["GERENTE RESPONSÁVEL"] = df_reclamacoes["PRODUTO"].map(
        dict(zip(df_gerentes["PRODUTO"], df_gerentes["GERENTE RESPONSÁVEL"]))
    )
    return df_reclamacoes

def separar_avaliacoes(df):
    bem_avaliados = df[df["NOTA DO ATENDIMENTO (0 A 10)".upper()] >= 6]
    mal_avaliados = df[df["NOTA DO ATENDIMENTO (0 A 10)".upper()] <= 5]
    return bem_avaliados, mal_avaliados

def calcular_media_por_gerente(df):
    media = (
        df.groupby("GERENTE RESPONSÁVEL")["NOTA DO ATENDIMENTO (0 A 10)".upper()]
        .mean()
        .sort_values(ascending=True)
        .to_dict()
    )
    return media

def gerar_grafico(media_por_gerente):
    plt.figure(figsize=(8, 4))
    bars = plt.barh(list(media_por_gerente.keys()), list(media_por_gerente.values()), color="#ff6200")
    plt.xlabel("Média da Nota", color="#333")
    plt.title("Média de Avaliação por Gerente", color="#333", pad=12)
    for i, (gerente, media) in enumerate(media_por_gerente.items()):
        plt.text(media + 0.1, i, f"{media:.2f}", va="center", fontsize=10, color="#333")
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.savefig("outputs/media_por_gerente.png", dpi=300, bbox_inches="tight")
    plt.show()

def salvar_excel(media_por_gerente, bem_avaliados, mal_avaliados):
    with pd.ExcelWriter("outputs/resultados.xlsx") as writer:
        pd.DataFrame(
            {"GERENTE RESPONSÁVEL": list(media_por_gerente.keys()), "MÉDIA NOTA": list(media_por_gerente.values())}
        ).to_excel(writer, sheet_name="Média por gerente", index=False)
        bem_avaliados.to_excel(writer, sheet_name="Bem avaliados", index=False)
        mal_avaliados.to_excel(writer, sheet_name="Mal avaliados", index=False)

def imprimir_resultados(total_atendimentos, media_geral, media_por_gerente, bem_avaliados, mal_avaliados):
    print("\n=== RESULTADOS GERAIS ===")
    print(f"Total de atendimentos: {total_atendimentos}")
    print(f"Média geral das notas: {media_geral:.2f}\n")
    print("=== MÉDIA POR GERENTE ===")
    for gerente, media in media_por_gerente.items():
        print(f"{gerente}: {media:.2f}")
    print("\n=== GERENTES BEM AVALIADOS ===")
    print(bem_avaliados[["GERENTE RESPONSÁVEL", "NOTA DO ATENDIMENTO (0 A 10)".upper(), "JUSTIFICATIVA DA NOTA".upper()]])
    print("\n=== GERENTES MAL AVALIADOS ===")
    print(mal_avaliados[["GERENTE RESPONSÁVEL", "NOTA DO ATENDIMENTO (0 A 10)".upper(), "JUSTIFICATIVA DA NOTA".upper()]])

def main():
    df = ler_dados()
    total_atendimentos = len(df)
    media_geral = df["NOTA DO ATENDIMENTO (0 A 10)".upper()].mean()
    bem_avaliados, mal_avaliados = separar_avaliacoes(df)
    media_por_gerente = calcular_media_por_gerente(df)
    gerar_grafico(media_por_gerente)
    salvar_excel(media_por_gerente, bem_avaliados, mal_avaliados)
    imprimir_resultados(total_atendimentos, media_geral, media_por_gerente, bem_avaliados, mal_avaliados)

if __name__ == "__main__":
    main()
