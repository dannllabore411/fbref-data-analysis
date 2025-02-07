import timeit
import numpy as np
import pandas as pd
import streamlit as st
import scipy.stats as stat
import plotly.express as px
import warnings
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance 
time_start = timeit.default_timer()
# CHOSEN VARIABLES
LEFT = ["Player", "Nation", "Pos", "Squad", "Comp", "Age", "Born", "Playing Time Min"]
DEF = ["Tackles Tkl%", "Foul Prev%", "Deep DAs", "High DAs", "Tackles TklW", "Int", "Tackles Def 3rd", "Tackles Mid 3rd", "Tackles Att 3rd"]
AER = ["Aerial Duels Won", "Aerial Duels Won%"]
PAS = ["Short Cmp%", "Medium Cmp%", "Long Cmp%", "Total Cmp", "Total PrgDist", "Progression PrgP", "%Short Att", "%Medium Att", "%Long Att"]
CAR = ["Take-Ons Succ%", "Carries Carries", "Carries PrgDist", "Carries PrgC"]
CRE = ["xAG", "Expected A-xAG", "SCA SCA", "KP", "1/3", "PPA", "CrsPA"]
SHO = ["Expected np:G-xG", "Expected npxG/Sh", "Expected npxG", "Standard Gls", "Standard Sh"]
TOU = ["Touches %Def Pen", "Touches %Def 3rd", "Touches %Mid 3rd", "Touches %Att 3rd", "Touches %Att Pen"]
DEFq = ["Tackles Tkl%", "Foul Prev%", "Deep DAs", "High DAs", "Tackles TklW", "Int", "Aerial Duels Won%"]
PASq = ["Short Cmp%", "Medium Cmp%", "Long Cmp%", "Total Cmp", "Total PrgDist", "Progression PrgP"]
CARq = ["Take-Ons Succ%", "Carries Carries", "Carries PrgDist", "Carries PrgC"]
CREq = ["xAG", "Expected A-xAG", "SCA SCA", "KP", "1/3"]
SHOq = ["Expected np:G-xG", "Expected npxG/Sh", "Expected npxG", "Standard Gls"]
order = [DEF, AER, PAS, CAR, CRE, SHO, TOU]; order = sum(order, [])
order_m = [DEFq, PASq, CARq, CREq, SHOq]; order_m = sum(order_m, [])
# FOR RADAR
DF = ["Deep DAs", "Aerial Duels Won%", "High DAs", "Tackles Tkl%", "Total Cmp", "Progression PrgP", "Carries PrgC", "CrsPA"]
DM = ["High DAs", "Tackles Tkl%", "Total Cmp", "Progression PrgP", "Carries PrgC", "CrsPA", "KP"]
MF = ["High DAs", "Tackles Tkl%", "Total Cmp", "Progression PrgP", "Carries PrgC", "Take-Ons Succ%", "CrsPA", "KP", "xAG"]
AM = ["High DAs", "Total Cmp", "Progression PrgP", "Carries PrgC", "Take-Ons Succ%", "CrsPA", "KP", "xAG", "Expected npxG"]
FW = ["High DAs", "Progression PrgP", "Carries PrgC", "Take-Ons Succ%", "KP", "xAG", "Expected npxG", "Expected np:G-xG"]
# READING DATA, INITIAL FILTERS AND CLEANUP
df = pd.read_csv("2324_top_8_raw.csv", low_memory=False, encoding="utf-8")
df = df.loc[df["Playing Time Min"] > 360]
df = df.loc[df["Pos"] != "GK"]
df = df.reset_index(drop = True)
df = df.fillna(0)
df.loc[(df["Pos"] == "DF,FW"), "Pos"] = "DF"
df.loc[(df["Pos"] == "DF,MF") | (df["Pos"] == "MF,DF"), "Pos"] = "DM"
df.loc[(df["Pos"] == "FW,MF") | (df["Pos"] == "MF,FW"), "Pos"] = "AM"
df.loc[(df["Pos"] == "FW,DF"), "Pos"] = "FW"
# COMPARISON
data_c = df[order].copy().astype(float)
comp_std = StandardScaler().fit_transform(data_c)
comp_norm = stat.norm.cdf(comp_std)*100
data_comp = pd.DataFrame(comp_norm, columns=data_c.columns)
# METRICS
data_m = df[order_m].copy().astype(float)
met_std = StandardScaler().fit_transform(data_m)
met_norm = stat.norm.cdf(met_std)*100
data_met = pd.DataFrame(met_norm, columns=data_m.columns)
# DISPLAY
data = df[order].copy().astype(float)
arr_std = data.copy()
arr_std["Pos"] = df["Pos"]
zscore = lambda x: (x - x.mean())/x.std()
arr_std = arr_std.groupby(arr_std["Pos"]).transform(zscore)
arr_norm = stat.norm.cdf(arr_std)*100
data_norm = pd.DataFrame(arr_norm, columns=arr_std.columns)
# UI
title = "Football Player Profile App - Big 8 European Leagues"
st.set_page_config(
    layout="wide",
    page_icon="⚽",
    page_title=title
)
st.title(title)
with st.sidebar:
    leagues = sorted(df["Comp"].unique())
    league = st.selectbox("Select a league: ", leagues)
    clubs = sorted(df.loc[df["Comp"] == league, "Squad"].unique())
    club = st.selectbox("Select a club: ", clubs)
    players = sorted(df.loc[(df["Comp"] == league) & (df["Squad"] == club), "Player"].unique())
    player = st.selectbox("Select a player: ", players)

player_index = df.index[(df['Player'] == player) & (df['Squad'] == club)].to_list()[0]
player_profile = df[["Player", "Pos", "Age", "Squad", "Nation", "Comp", "Playing Time Min"]].iloc[player_index,:]
col_top = st.columns((1,3), gap="small")
with col_top[0]:
    st.markdown("<h4>" + player_profile["Player"] + "</h4>" + str(player_profile["Age"]) + " | " + player_profile["Pos"] + " | " + player_profile["Nation"]
                + " | " + player_profile["Squad"] + " (" + str(player_profile["Comp"]).split(" ")[0] + ")",
                unsafe_allow_html=True)
with col_top[1]:
    player_metrics = pd.DataFrame(data_m[(df['Player'] == player) & (df['Squad'] == club)])
    player_metrics.loc[len(player_metrics)] = met_norm[player_index,:]
    col_metrics = st.columns(6, vertical_alignment='center', gap='small')
    with col_metrics[0]:
        player_touches = pd.DataFrame(df[(df['Player'] == player) & (df['Squad'] == club)][TOU].transpose().iloc[::-1])
        heatmap = px.imshow(player_touches, text_auto=True, aspect="auto")
        st.markdown("# 👤")
        #st.plotly_chart(heatmap)
    with col_metrics[1]:
        st.metric("Defending", round(40 + 0.6*player_metrics.loc[1, DEFq].mean()))
    with col_metrics[2]:
        st.metric("Passing", round(40 + 0.6*player_metrics.loc[1, PASq].mean()))
    with col_metrics[3]:
        st.metric("Carrying", round(40 + 0.6*player_metrics.loc[1, CARq].mean()))
    with col_metrics[4]:
        st.metric("Creation", round(40 + 0.6*player_metrics.loc[1, CREq].mean()))
    with col_metrics[5]:
        st.metric("Shooting", round(40 + 0.6*player_metrics.loc[1, SHOq].mean()))

tab1, tab2 = st.tabs(["Player Profile", "Similar Players"])
with tab1: 
    player_key_stats = pd.DataFrame(data[(df['Player'] == player) & (df['Squad'] == club)])
    player_key_stats.loc[len(player_key_stats)] = arr_norm[player_index,:]
    key_variables = eval(player_profile["Pos"]) 
    with st.popover("Change variables", use_container_width=True):
        key_variables = st.multiselect(
        "Add or remove variables:",
        order, key_variables)   
    col_bot = st.columns((12,13), gap="small")
    with col_bot[0]:
        st.markdown("#### RADAR CHART (KEY STATS)")
        player_key_stats = player_key_stats[key_variables]
        player_key_stats = player_key_stats.transpose()
        player_key_stats.columns = ["Value", "Percentile"]
        #del player_key_stats["Value"]
        radar = px.line_polar(player_key_stats, 
                              r="Percentile", theta=player_key_stats.index, 
                              line_close=True, range_r=[0,100])
        radar.update_traces(fill='toself')
        st.plotly_chart(radar, theme="streamlit", use_container_width=True, key = 1)        
        
    with col_bot[1]:
        st.markdown("#### KEY STATS")
        player_stats = pd.DataFrame(data[(df['Player'] == player) & (df['Squad'] == club)])
        player_stats.loc[len(player_stats)] = arr_norm[player_index,:]
        player_stats = player_stats.transpose()
        player_stats.columns = ["Value", "Percentile (relative to position)"]
        st.dataframe(player_key_stats, width=500, column_config={
                        "Percentile": st.column_config.ProgressColumn(
                            "Percentile",
                            format="%.0f",
                            min_value=0,
                            max_value=100,
        )})

with tab2:
    col_bot2 = st.columns((12,13), gap="small")
    with col_bot2[0]:
        st.markdown("#### 2023-24 ALL STATS")
        player_stats = pd.DataFrame(data[(df['Player'] == player) & (df['Squad'] == club)])
        player_stats.loc[len(player_stats)] = arr_norm[player_index,:]
        player_stats = player_stats.transpose()
        player_stats.columns = ["Value", "Percentile (relative to position)"]
        st.dataframe(player_stats, width=500, column_config={
                        "Percentile (relative to position)": st.column_config.ProgressColumn(
                            "Percentile (relative to position)",
                            format="%.0f",
                            min_value=0,
                            max_value=100,
        )})
    with col_bot2[1]:
        st.markdown("#### SIMILAR PLAYERS TO " + player + ":")
        distances = distance.cdist([comp_norm[player_index,:]], comp_norm, "cosine")[0]
        output_table = df[["Player", "Pos", "Age", "Squad", "Nation"]]
        output_table = output_table.assign(Similarity = distances)
        st.dataframe(output_table.sort_values('Similarity').head(11), use_container_width=True)
        st.write("(From Europe's top 8 leagues, min. 360 minutes played 2023-24)")

time_stop = timeit.default_timer()
st.write("Time: ", time_stop-time_start)