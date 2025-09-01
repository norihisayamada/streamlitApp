import streamlit as st
import pandas as pd
import pydeck as pdk
import io

st.title("📶 RSRP付き地点データの地図表示")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    try:
        # ファイル内容を読み取り（文字コードを明示）
        content = uploaded_file.read().decode("utf-8", errors="ignore")
        df = pd.read_csv(io.StringIO(content))

        # カラム名を小文字に統一して標準化
        df.columns = [col.strip().lower() for col in df.columns]
        df = df.rename(columns={
            'latitude': 'lat',
            'longitude': 'lon',
            'lng': 'lon'
        })

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
            st.error(f"カラムが不足しています。現在のカラム: {df.columns.tolist()}")
    except Exception as e:
        st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")
else:
    st.info("CSVファイルをアップロードすると、RSRP付きで地図表示できます。")
