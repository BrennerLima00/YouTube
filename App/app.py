import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("Analisando os dados...")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['England','Germany','Italy','Spain','France'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2021/2022','2020/2021','2019/2020'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'England':
    league = 'E0'
  if selected_league == 'Germany':
    league = 'D1'
  if selected_league == 'Italy':
    league = 'I1'
  if selected_league == 'Spain':
    league = 'SP1'
  if selected_league == 'France':
    league = 'F1'
   
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df), unsafe_allow_html=True)


df_2 = pd.read_excel('https://github.com/futpythontrader/YouTube/blob/main/x_FutPythonTrader_Base_de_Dados_Temporadas_Passadas_x.xlsx?raw=true')
# Carregando Dataframe
df = pd.read_excel('https://github.com/futpythontrader/YouTube/blob/main/x_FutPythonTrader_Base_de_Dados_Temporada_Atual_x.xlsx?raw=true')
# Solicitando ao usuário que escolha o time da casa e o time visitante
home_team = input("Escolha o time da casa: ")
away_team = input("Escolha o time visitante: ")

# Filtro para jogos do time escolhido como mandante e o outro time como visitante
df_home = df[(df["Home"] == home_team) & (df["Away"] == away_team)]

# Filtro para jogos do time escolhido como visitante e o outro time como mandante
df_away = df[(df["Home"] == away_team) & (df["Away"] == home_team)]

# Concatenando Dataframes
df_confrontos = pd.concat([df_home, df_away, df_2])

# Média de escanteios dos últimos 5 jogos do time escolhido como mandante
home_corners_mean = df[df["Home"] == home_team][-5:]["FT_Corners_H"].mean()

# Média de escanteios dos últimos 5 jogos do time escolhido como visitante
away_corners_mean = df[df["Away"] == away_team][-5:]["FT_Corners_A"].mean()

# Média de escanteios dos últimos 5 confrontos entre os times escolhidos
confronto_corners_mean = df_confrontos["FT_Corners_H"].mean()

# Média de gols dos últimos 5 jogos do time escolhido como mandante
home_goals_mean = df[df["Home"] == home_team][-5:]["FT_Goals_H"].mean()

# Média de gols dos últimos 5 jogos do time escolhido como visitante
away_goals_mean = df[df["Away"] == away_team][-5:]["FT_Goals_A"].mean()

# Média de gols dos últimos 5 confrontos entre os times escolhidos
confronto_goals_mean = df_confrontos["FT_Goals_H"].mean()

# Divisão de gols e escanteios por "2"|
#away_goals_mean = df[df["Away"] == away_team][-5:]["FT_Goals_A"]

#df_away = df[(df["Home"] == away_team) & (df["Away"] == home_team)]



# Imprimindo resultados
print(f"Média de escanteios dos últimos 5 jogos do Time 1 como mandante: {home_corners_mean}")
print(f"Média de escanteios dos últimos 5 jogos do Time 2 como visitante: {away_corners_mean}")
print(f"Média de escanteios dos últimos 5 confrontos entre Time 1 e Time 2: {confronto_corners_mean}")
print(f"Média de gols dos últimos 5 jogos do Time 1 como mandante: {home_goals_mean}")
print(f"Média de gols dos últimos 5 jogos do Time 2 como visitante: {away_goals_mean}")
print(f"Média de gols dos últimos 5 confrontos entre Time 1 e Time 2: {confronto_goals_mean}")




