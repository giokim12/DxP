import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="4조",
    page_icon="4️⃣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #000000;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #f0f9f8;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .stSelectbox > div > div > div > div {
        background-color: #f0f9f8;

    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the foreigner data"""
    foreigner_ingu_merged2 = pd.read_csv('foreigner_ingu_merged2.csv')
    return foreigner_ingu_merged2

def main():
    # Title
    st.markdown("<h1 style='color:#008486; background-color: #f0f9f8; '>🌐 외국인 대상 금융상품 추천 모델 개발 </h1>", unsafe_allow_html=True)
    
    # Load data
    foreigner_ingu_merged2 = load_data()

    # Main dashboard content
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🌎 주제 선정 배경 및 외국인 현황", "🧭 연구방법 및 데이터 수집", "📈 모의 데이터 구축", "💻 금융상품 추천 모델 개발", "📋 분석결과 및 활용방안", "📱 데이터"])
    
    with tab1:

        page3 = Image.open('page3.png')
        st.image(page3)
        pie_data = {
            "국적": ["중국", "베트남", "네팔", "우즈베키스탄", "기타 국가"],
            "비율(%)": [33.0, 17.0, 4.5, 4.1, 41.4],
            "인원수(만명)": [45.0, 22.8, 6.0, 5.5, 55.7]
        }
        pie_data = pd.DataFrame(pie_data)

        # 2. 파이차트 만들기 (초록 계열 사용)
        green_colors = [
            "#008060",  # 진초록
            "#06D6A0",  # 밝은 민트
            "#A7F3D0",  # 연한 청록
            "#4CBB17",  # 중간 초록
            "#B7E4C7"   # 아주 밝은 초록
        ]

        fig = px.pie(
            pie_data,
            names="국적",
            values="비율(%)",
            title="국적별 분포",
            hole=0,
            color_discrete_sequence=green_colors
        )

        # 라벨에 퍼센트 + 인원수 같이 보이도록
        fig.update_traces(
            textposition="inside",
            textinfo="label+percent",
            hovertemplate="<b>%{label}</b><br>비율: %{percent:.1%}<br>인원수: %{customdata}만명",
            customdata=pie_data["인원수(만명)"],
        )

        # 3. 화면 배치: 왼쪽 파이차트, 오른쪽 표
        col1, col2 = st.columns([2, 1])

        with col1:
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### 세부 데이터")
            st.dataframe(
                pie_data.style.format({
                    "비율(%)": "{:.1f}%",
                    "인원수(만명)": "{:.1f}만명",
                }),
                use_container_width=True,
            )
        inbank_data = pd.DataFrame({
            "테이블명": ["고객정보", "수신상품 가입내역", "당발송금거래 ", "타발송금거래"],
            "컬럼명": ['고객번호, 고객명, 국적, 비자종류, 나이, 월소득, 주소', '고객번호, 계좌번호, 가입상품종류, 상품가입금액, 가입일자', '고객번호, 송금종류, 송금국가, 송금금액, 송금목적, 지정항목', '고객번호, 송금종류, 송금국가, 송금금액, 송금목적, 지정항목']
        })

        st.table(inbank_data)  
        page4 = Image.open('page4.png')
        st.image(page4)
        page5 = Image.open('page5.png')
        st.image(page5)        
        page6 = Image.open('page6.png')
        st.image(page6)        
        page7 = Image.open('page7.png')
        st.image(page7)         



        
        st.markdown("---")
     
        
   
    
    with tab2:
        page8 = Image.open('page8.png')
        st.image(page8)        
        page9 = Image.open('page9.png')
        st.image(page9)  
        
    


    with tab3:
        st.header("📈 검증용 모의 데이터 구축")        
        st.subheader("Filtered Dataset")
        st.markdown(f"<h3 style='color:#008486; background-color: #f0f9f8; '>데이터 구조 및 설계 </h3>", unsafe_allow_html=True)
        page10 = Image.open('page10.png')
        st.image(page10) 
        with st.expander("더미데이터 생성 조건 (펼치기)"):
            st.markdown("""
                ## (1) 고객명 / 비자종류 / 월소득 범위 / 나이
                - 고객명: 영문 10자 이내 (중복 가능)

                ### D계열  
                - D-1 / 100만원 이하 / 20대  
                - D-2 / 100만원 이하 / 20대  
                - D-3 / 100만원 이하 / 30대  
                - D-4 / 100만원 이하 / 20대  
                - D-5 / 500~600만원 / 30~50대  
                - D-6 / 100만원 이하 / 30~50대  
                - D-7 / 400~500만원 / 30~50대  
                - D-8 / 300~400만원 / 30~50대  
                - D-9 / 400~500만원 / 30~50대  
                - D-10 / 200~300만원 / 20대  

                ### E계열  
                - E-1 / 300~400만원 / 40~50대  
                - E-2 / 200~300만원 / 30~40대  
                - E-3 / 300~400만원 / 30~50대  
                - E-4 / 400~500만원 / 30~50대  
                - E-5 / 500~600만원 / 30~50대  
                - E-6 / 100~200만원 / 20~50대  
                - E-7 / 300~400만원 / 20~50대  
                - E-8 / 200~300만원 / 20~50대  
                - E-9 / 200~300만원 / 20~50대  
                - E-10 / 100~200만원 / 20~40대  

                ### F계열  
                - F-1 / 100만원 이하 / 20~50대  
                - F-2 / 300~400만원 / 20~50대  
                - F-3 / 100만원 이하 / 20~50대  
                - F-5 / 300~400만원 / 20~50대  
                - F-6 / 200~300만원 / 20~50대  

                ### H계열  
                - H-1 / 100~200만원 / 20~40대  
                - H-2 / 300~400만원 / 20~40대  

                ### 비자 비율
                - F계열 5% / E계열 70% / D계열 20% / H계열 5%  

                ---

                ## (3) 국적 비율
                - 중국 36%  
                - 베트남 20%  
                - 네팔 4%  
                - 우즈베키스탄 4%  
                - 캄보디아 4%  
                - 인도네시아 4%  
                - 필리핀 4%  
                - 타이 3%  
                - 미얀마 3%  
                - 미국 3%  
                - 몽골 3%  
                - 스리랑카 2%  
                - 일본 2%  
                - 방글라데시 2%  
                - 카자흐스탄 1%  
                - 러시아(연방) 1%  
                - 타이완 1%  
                - 파키스탄 1%  
                - 인도 1%  
                - 키르기즈 1%  

                ---

                ## (4) 국적별 상품 가입 확률
                (여기에 동일한 방식으로 이어서 붙여주세요)

                """)

        df_dummy = pd.read_csv('preprocessed_data.csv')
        st.write(f"Displaying {len(df_dummy):,} records")
        
        # Column selection
        display_cols = st.multiselect(
            "Select columns to display:",
            df_dummy.columns.tolist(),
            default=df_dummy.columns[:].tolist(),
            key="tab2_multiselect"
        )
        
        if display_cols:
            # Sortable data table
            sort_by = st.selectbox("Sort by:", display_cols, index=0, key="tab2_selectbox")
            sort_order = st.radio("Sort order:", ["Ascending", "Descending"], key="tab2_radio")
            
            sorted_df = df_dummy[display_cols].sort_values(
                by=sort_by, 
                ascending=(sort_order == "Ascending")
            )

            
        st.dataframe(df_dummy, use_container_width=True, height=400)

        st.markdown("<h3 style='color:#008486; background-color: #f0f9f8; '>더미 데이터 생성</h3>", unsafe_allow_html=True)
    
    

    with tab4:
        page11 = Image.open('page11.png')
        st.image(page11) 
        page12 = Image.open('page12.png')
        st.image(page12)
        page13 = Image.open('page13.png')
        st.image(page13) 
        page14 = Image.open('page14.png')
        st.image(page14) 


        with open("product_recommandation.html", "r", encoding="utf-8") as f:
            html = f.read()

        st.components.v1.html(html, height=900, scrolling=True)

     
    
    with tab5:
        page15 = Image.open('page15.png')
        st.image(page15)
        page16 = Image.open('page16.png')
        st.image(page16) 
        page17 = Image.open('page17.png')
        st.image(page17)


    with tab6:
        st.header("📋 Data Table")
        
        # Data table with search and filter
        st.subheader("Filtered Dataset")
        st.write(f"Displaying {len(foreigner_ingu_merged2):,} records")
        
        # Column selection
        display_cols = st.multiselect(
            "Select columns to display:",
            foreigner_ingu_merged2.columns.tolist(),
            default=foreigner_ingu_merged2.columns[:8].tolist(),
            key="tab6_multiselect"
        )
        
        if display_cols:
            # Sortable data table
            sort_by = st.selectbox("Sort by:", display_cols, key="tab6_selectbox")
            sort_order = st.radio("Sort order:", ["Ascending", "Descending"], key="tab6_radio")
            
            sorted_df = foreigner_ingu_merged2[display_cols].sort_values(
                by=sort_by, 
                ascending=(sort_order == "Ascending")
            )
            
            st.dataframe(sorted_df, use_container_width=True, height=400)
            
            # Download filtered data
            csv = sorted_df.to_csv(index=False)
            st.download_button(
                label="Download filtered data as CSV",
                data=csv,
                file_name="foreigner_ingu_merged2.csv",
                mime="text/csv"
            )
    
    # Footer
    st.markdown("---")
    st.markdown("**Dxp 4조**: **이택인**차장 (강서금융센터지점), **권진**대리 (LS용산타워지점), **김지오**계장 (데이터전략부), **박지영**계장 (IT금융개발부)")

if __name__ == "__main__":
    main()
