import streamlit as st
import pandas as pd
import numpy as np

st.title("📍 柳井湊周辺のランダム地点を地図に表示")

# 東京駅周辺を中心にしたランダムな座標を生成
latitude = 33.957268  # 柳井港の緯度
longitude = 132.134044  # 柳井港の経度

# 50個のランダムな地点を生成
df = pd.DataFrame({
    'lat': np.random.normal(latitude, 0.01, 50),
    'lon': np.random.normal(longitude, 0.01, 50)
})

# 地図にプロット

st.map(df)
