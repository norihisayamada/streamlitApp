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
###  ファイルを選択　　###
import streamlit as st
import pandas as pd
import numpy as np

st.title("📍 柳井港周辺の地点を地図に表示")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVまたはJSONファイルをアップロードしてください", type=["csv", "json"])

# ファイルがアップロードされた場合
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            df = pd.read_json(uploaded_file)

        # 必須カラムの確認
        if {'latitude', 'longitude'}.issubset(df.columns):
            st.success("ファイルを読み込みました。地図にプロットします。")
            st.map(df)
        else:
            st.error("ファイルに 'lat' と 'lon' カラムが含まれていません。")
    except Exception as e:
        st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")
else:
    st.info("ファイルが未アップロードのため、ランダム地点を表示します。")

    # 柳井港周辺のランダムな座標を生成
    latitude = 33.957268
    longitude = 132.134044

    df = pd.DataFrame({
        'lat': np.random.normal(latitude, 0.01, 50),
        'lon': np.random.normal(longitude, 0.01, 50)
    })

    st.map(df)

