import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

# Título do app
st.title("Dashboard de Colaboração TA")

# Dados fornecidos
ta_nome_data = {
    "344064338": "Não registrado",
    "344173283": "Roberto",
    "344296283": "Ernandes, John",
    "344332960": "Roberto, Sales, Valter",
    "344340339": "Rafael",
    "344343917": "Felipe",
    "344355040": "Não registrado",
    "344382179": "Roberto",
    "344553101": "Rafael",
    "344564763": "Sales, Ernandes",
    "344596251": "Felipe",
    "344600233": "Felipe, Ernandes",
    "344605925": "Sales",
    "344641897": "Felipe, Ernandes",
    "344653864": "Sozinho",
    "344811053": "Isaque, Eduardo Silve",
    "344821039": "Ernandes",
    "344829300": "Rafael, Felipe"
}

# Contar ocorrências individuais de nomes
nome_counter = Counter()
for nomes in ta_nome_data.values():
    for nome in map(str.strip, nomes.split(',')):
        if nome:
            nome_counter[nome] += 1

# Separar "Não registrado" e "Sozinho" para colocar no final
especial = {k: nome_counter.pop(k) for k in ["Não registrado", "Sozinho"] if k in nome_counter}

# Ordenar os nomes por frequência decrescente
sorted_nomes = sorted(nome_counter.items(), key=lambda x: x[1], reverse=True)

# Adicionar os especiais ao final
sorted_nomes.extend(especial.items())

# Separar nomes e contagens
nomes, contagens = zip(*sorted_nomes)

# Calcular total de TAs
total_tas = len(ta_nome_data)

# Exibir gráfico com matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(nomes, contagens, color='skyblue')
ax.set_title(f"Colaboração TA (Total de TAs: {total_tas})")
ax.set_xlabel("Nome")
ax.set_ylabel("Quantidade de TAs")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
