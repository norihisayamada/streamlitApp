#import streamlit as st
#import pandas as pd
#import numpy as np

#st.title("📍 柳井湊周辺のランダム地点を地図に表示")

# 東京駅周辺を中心にしたランダムな座標を生成
#latitude = 33.957268  # 柳井港の緯度
#longitude = 132.134044  # 柳井港の経度

# 50個のランダムな地点を生成
#df = pd.DataFrame({
 #   'lat': np.random.normal(latitude, 0.01, 50),
  #  'lon': np.random.normal(longitude, 0.01, 50)
#})

# 地図にプロット
#st.map(df)

#******************************************************************************#
###  ファイルを選択　　###
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("📶 RSRP付き地点データの地図表示")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep="\t")  # タブ区切りに対応


    # 必須カラムの確認
    if {'lat', 'lon', 'rsrp'}.issubset(df.columns):
        st.success("ファイルを読み込みました。地図にプロットします。")

        # pydeckでマップ表示
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position='[lon, lat]',
            get_color='[255 - abs(rsrp), abs(rsrp), 100, 160]',  # RSRPの強さで色分け
            get_radius=30,
            pickable=True
        )

        tooltip = {
            "html": "<b>RSRP:</b> {rsrp}<br/><b>Lat:</b> {lat}<br/><b>Lon:</b> {lon}",
            "style": {"backgroundColor": "navy", "color": "white"}
        }

        view_state = pdk.ViewState(
            latitude=df['lat'].mean(),
            longitude=df['lon'].mean(),
            zoom=16,
            pitch=0
        )

        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=view_state,
            layers=[layer],
            tooltip=tooltip
        ))
    else:
        st.error("ファイルに 'lat', 'lon', 'rsrp' カラムが含まれていません。")
else:
    st.info("CSVファイルをアップロードすると、RSRP付きで地図表示できます。")





