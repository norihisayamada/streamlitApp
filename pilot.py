import streamlit as st
import pandas as pd
import numpy as np

st.title("📍 東京周辺のランダム地点を地図に表示")

# 東京駅周辺を中心にしたランダムな座標を生成
latitude = 35.681236  # 東京駅の緯度
longitude = 139.767125  # 東京駅の経度

# 50個のランダムな地点を生成
df = pd.DataFrame({
    'lat': np.random.normal(latitude, 0.01, 50),
    'lon': np.random.normal(longitude, 0.01, 50)
})

# 地図にプロット
st.map(df)