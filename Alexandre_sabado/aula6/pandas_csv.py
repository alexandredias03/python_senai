import pandas as pd
import matplotlib.pyplot as plt



# criar os dados para o nosso dataframe

dados = {
    "Nome": ["Arthur", "Maria", "Mateus", "Carlos", "Bruna", "Diogo"],
    "Idade": [28, 22, 18, 35, 20, 31],
    "Cidade":["Cotia","Carapikuiba","Cotia","Osasco","Cotia","Osasco"]
}

df = pd.DataFrame(dados)
# Exibir o DataFrame
print(df)

# Salvar DataFrame no CSV
df.to_csv("pandas_dados.csv", index=False)
# visualizar em data frame o CSV
df_csv = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["Idade"] > 25 ]
print(df_filtrado) # Todas as pessoas com menos de 25 anos não aparecem

df_ordenado = df.sort_values(by="Idade", ascending=False)
print(df_ordenado) # Do maior para o menor (Decrescente)

# Exibir estatisticas
print(df.describe())

# Media por cidade, coluna idade
media_cidade = df.groupby("Cidade")["Idade"].mean()
print(media_cidade)

# Criando grafico
# df.plot(kind="pie", x="Nome", y="Idade", color="black" )
# plt.title("Idade das pessoas")
# plt.xlabel("Nome")
# plt.ylabel("Idade")
# plt.show()

df.boxplot(column="Idade", by="Cidade", grid=False)
plt.title("Distribuição de Idades por Cidades")
plt.xlabel("Cidade")
plt.ylabel("Idade")

plt.show()