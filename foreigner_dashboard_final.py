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

# Custom CSS (add image center alignment)
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
    /* Center images in markdown */
    .centered-image img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the foreigner data"""
    foreigner_ingu_merged2 = pd.read_csv('foreigner_ingu_merged2.csv')
    return foreigner_ingu_merged2

def centered_image(img, **kwargs):
    from io import BytesIO
    import base64
    buf = BytesIO()
    img.save(buf, format="PNG")
    img_str = base64.b64encode(buf.getvalue()).decode()
    html = f'''
       <div class="centered-image">
           <img src="data:image/png;base64,{img_str}" style="display:block;margin-left:auto;margin-right:auto;max-width:100%;height:auto;" />
       </div>
       '''
    st.markdown(html, unsafe_allow_html=True)

def main():
    # Title
    st.markdown("<h1>🌐 외국인 대상 금융상품 추천 모델 개발 </h1>", unsafe_allow_html=True)
    
    # Load data
    foreigner_ingu_merged2 = load_data()

    # Main dashboard content
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🌎 주제 선정 배경 및 외국인 현황", "🧭 연구방법 및 데이터 수집", "📈 모의 데이터 구축", "💻 금융상품 추천 모델 개발", "📋 분석결과 및 활용방안", "📱 데이터"])
    
    with tab1:
        # # 버튼 생성
        # if st.button('클릭하세요'):
        #     st.success('버튼이 눌렸습니다!')
        #     st.slider('값을 선택하세요')
        page3 = Image.open('page3.png')
        centered_image(page3)
        pie_data = {
            "국적": ["중국", "베트남", "네팔", "우즈베키스탄", "기타 국가"],
            "비율(%)": [33.0, 17.0, 4.5, 4.1, 41.4],
            "인원수(만명)": [45.0, 22.8, 6.0, 5.5, 55.7]
        }
        pie_df = pd.DataFrame(pie_data)

        # 2. 파이차트 만들기 (초록 계열 사용)
        green_colors = [
            "#008060",  # 진초록
            "#06D6A0",  # 밝은 민트
            "#A7F3D0",  # 연한 청록
            "#4CBB17",  # 중간 초록
            "#B7E4C7"   # 아주 밝은 초록
        ]

        # pie chart
        pie_fig = px.pie(
            pie_df,
            names="국적",
            values="비율(%)",
            title="국적별 분포",
            hole=0,
            color_discrete_sequence=green_colors
        )

        # 라벨에 퍼센트 + 인원수 같이 보이도록
        pie_fig.update_traces(
            textposition="inside",
            textinfo="label+percent",
            hovertemplate="<b>%{label}</b><br>비율: %{percent:.1%}<br>인원수: %{customdata}만명",
            customdata=pie_df["인원수(만명)"].values,
        )

        # 3. 화면 배치: 왼쪽 파이차트, 오른쪽 표
        col1, col2 = st.columns([2, 1])

        with col1:
            st.plotly_chart(pie_fig, use_container_width=True)

        with col2:
            st.markdown("#### 세부 데이터")
            st.dataframe(
                pie_df.style.format({
                    "비율(%)": "{:.1f}%",
                    "인원수(만명)": "{:.1f}만명",
                }),
                use_container_width=True,
            )

        page4 = Image.open('page4.png')
        centered_image(page4)
        page5_0 = Image.open('page5_0.png')
        centered_image(page5_0)
        cols = st.columns([2, 1])
        with cols[0]:
            visa_data = {
                "비자 계열": ["F계열(영주권, 결혼이민)", "E계열(취업)", "D계열(유학, 연수)", "H계열(워킹홀리데이, 방문취업)", "기타(Others)"],
                "인원수": [517399, 400033, 250374, 104980, 75840],
                "비율": [35, 27, 20, 10, 5]  # 예시 % (그래프 이미지 스타일과 유사하게)
            }

            visa_df = pd.DataFrame(visa_data)

            # 그래프 객체 생성
            visa_fig = make_subplots(
                specs=[[{"secondary_y": True}]]
            )

            # 막대그래프
            visa_fig.add_trace(
                go.Bar(
                    x=visa_df["비자 계열"],
                    y=visa_df["인원수"],
                    name="인원수",
                    marker_color=["#504A8F", "#2A6777", "#2B8C81", "#82C45D", "#9CD670"],
                    text=visa_df["인원수"],
                    textposition='outside'
                ),
                secondary_y=False,
            )

            # 선그래프 (이중축)
            visa_fig.add_trace(
                go.Scatter(
                    x=visa_df["비자 계열"],
                    y=visa_df["비율"],
                    name="비율 (%)",
                    mode="lines+markers+text",
                    text=visa_df["비율"],
                    textposition="top center",
                    marker=dict(size=8, color="red"),
                    line=dict(color="red", width=2)
                ),
                secondary_y=True,
            )

            visa_fig.update_layout(
                title="비자 계열별 외국인 인원수와 비율",
                xaxis=dict(title="비자 계열"),
                yaxis=dict(title="인원수 (명)", showgrid=True),
                yaxis2=dict(
                    title="비율 (%)",
                    overlaying="y",
                    side="right",
                    showgrid=False,
                    range=[0, 40]
                ),
                template="simple_white",
                width=950,
                height=700
            )

            st.plotly_chart(visa_fig, use_container_width=True)

        with cols[1]:
            page5 = Image.open('page5.png')
            centered_image(page5)
            
        page6 = Image.open('page6.png')
        centered_image(page6)        
        page7 = Image.open('page7.png')
        centered_image(page7)         


     
    with tab2:
        page8 = Image.open('page8.png')
        centered_image(page8)        
        page9 = Image.open('page9.png')
        centered_image(page9)  

    with tab3:
        # st.markdown(f"<h3 style='color:#008486; background-color: #f0f9f8; '>📈 더미데이터 생성</h3>", unsafe_allow_html=True)
        page10 = Image.open('page10.png')
        centered_image(page10) 
        st.markdown("""
        <style>
            div.streamlit-expanderHeader p {
                font-size: 20px !important;   /* 글자 크기 */
                font-weight: 700 !important;  /* 굵기 */
                color: #000000 !important;    /* 색상 */
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("✍️더미데이터 생성 세부 조건")
        with st.expander("더미데이터 생성 조건 (펼치기) 🔻"):

            st.markdown("""
                ### <더미데이터 생성조건>

                #### 1. 고객명  
                - 영문으로 10자 이내  
                - 이름 중복 가능

                #### 2. 비자종류 / 월소득 범위 / 나이  
                | 비자종류 | 월소득 | 나이 |
                |:---|:---|:---|
                | D-1 | 100만원 이하 | 20대 |
                | D-2 | 100만원 이하 | 20대 |
                | D-3 | 100만원 이하 | 30대 |
                | D-4 | 100만원 이하 | 20대 |
                | D-5 | 500-600만원 | 30-50대 |
                | D-6 | 100만원 이하 | 30-50대 |
                | D-7 | 400-500만원 | 30-50대 |
                | D-8 | 300-400만원 | 30-50대 |
                | D-9 | 400-500만원 | 30-50대 |
                | D-10 | 200-300만원 | 20대 |
                | E-1 | 300-400만원 | 40-50대 |
                | E-2 | 200-300만원 | 30-40대 |
                | E-3 | 300-400만원 | 30-50대 |
                | E-4 | 400-500만원 | 30-50대 |
                | E-5 | 500-600만원 | 30-50대 |
                | E-6 | 100-200만원 | 20-50대 |
                | E-7 | 300-400만원 | 20-50대 |
                | E-8 | 200-300만원 | 20-50대 |
                | E-9 | 200-300만원 | 20-50대 |
                | E-10 | 100-200만원 | 20-40대 |
                | F-1 | 100만원 이하 | 20-50대 |
                | F-2 | 300-400만원 | 20-50대 |
                | F-3 | 100만원 이하 | 20-50대 |
                | F-5 | 300-400만원 | 20-50대 |
                | F-6 | 200-300만원 | 20-50대 |
                | H-1 | 100-200만원 | 20-40대 |
                | H-2 | 300-400만원 | 20-40대 |

                | 비자 계열 | 비율  |
                |:-----|:----|
                | F계열 | 5%   |
                | E계열 | 70%  |
                | D계열 | 20%  |
                | H계열 | 5%   |

                #### 3. 국적 / 비율  

                | 국적 | 비율  |
                |:-----|:----|
                | 중국 | 36%   |
                | 베트남 | 20%  |
                | 네팔 | 4%  |
                | 우즈베키스탄 | 4%   |
                | 캄보디아 | 4%   |
                | 인도네시아 | 4%   |
                | 필리핀 | 4%   |
                | 타이 | 3%   |
                | 미얀마 | 3%   |
                | 미국 | 3%   |
                | 몽골 | 3%   |
                | 스리랑카 | 2%   |
                | 일본 | 2%   |
                | 방글라데시 | 2%   |
                | 카자흐스탄 | 1%   |
                | 러시아(연방) | 1%   |
                | 타이완 | 1%   |
                | 파키스탄 | 1%   |
                | 인도 | 1%   |
                | 키르기즈 | 1%   |



                
                nationality_data = {
                    '국적': [
                        '중국', '베트남', '네팔', '우즈베키스탄', '캄보디아', '인도네시아', '필리핀', '타이', 
                        '미얀마', '미국', '몽골', '스리랑카', '일본', '방글라데시', '카자흐스탄', 
                        '러시아(연방)', '타이완', '파키스탄', '인도', '키르기즈'
                    ],
                    '비율(%)': [
                        36, 20, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1
                    ]
                }


                #### 4. 국적별 가입상품 / 손님별 상품 가입 확률  

                - **한국계 중국인, 중국**  
                    - 원화 정기예금 40%, 외화예금 40%, 개인대출 10%, 해외펀드 5%, 국내펀드 5%, 퇴직연금 10%
                    - 외국인 전용보험 50%, 외국인 전용카드 50%
                    - 당발송금: F, E, H 계열만 생성  
                    - 타발송금: D계열만 생성

                - **미국**  
                    - 원화 정기예금 15%, 외화예금 80%, 개인대출 5%, 해외펀드 20%, 국내펀드 10%, 퇴직연금 5%
                    - 외국인 전용보험 30%, 외국인 전용카드 50%
                    - 당발송금: F, E, H 계열만 생성  
                    - 타발송금: D계열만 생성

                - **일본**  
                    - 원화 정기예금 15%, 외화예금 80%, 개인대출 5%, 해외펀드 20%, 국내펀드 10%, 퇴직연금 5%
                    - 외국인 전용보험 30%, 외국인 전용카드 50%
                    - 당발송금: F, E, H 계열만 생성  
                    - 타발송금: D계열만 생성

                - **기타 국가**  
                    - 원화정기예금 5%, 외화예금 90%, 개인대출 5%, 해외펀드 5%, 국내펀드 5%, 퇴직연금 5%
                    - 외국인 전용보험 90%, 외국인 전용카드 50%
                    - 당발송금: F, E, H 계열만 생성  
                    - 타발송금: D계열만 생성

                #### 5. 상품 가입 금액  

                - **A. 원화정기예금**  
                    - 월소득 100-300만원: 가입금액 500만원 이하  
                    - 월소득 300-400만원: 가입금액 1000만원 이하  
                    - 월소득 400만원 초과: 가입금액 3000만원 이하

                - **B. 외화예금(달러)**  
                    - 월소득 100-300만원: 가입금액 1만 달러 이하  
                    - 월소득 300-400만원: 가입금액 2만 달러 이하  
                    - 월소득 400만원 초과: 가입금액 5만 달러 이하

                - **C. 개인대출**  
                    - 월소득 100-300만원: 가입금액 1000만원 이하  
                    - 월소득 300-400만원: 가입금액 3000만원 이하  
                    - 월소득 400만원 초과: 가입금액 5000만원 이하

                - **D. 해외펀드**  
                    - 월소득 100-300만원: 가입금액 500만원 이하  
                    - 월소득 300-400만원: 가입금액 1500만원 이하  
                    - 월소득 400만원 초과: 가입금액 3000만원 이하

                - **E. 국내펀드**  
                    - 월소득 100-300만원: 가입금액 500만원 이하  
                    - 월소득 300-400만원: 가입금액 1500만원 이하  
                    - 월소득 400만원 초과: 가입금액 3000만원 이하

                - **F. 퇴직연금**  
                    - 월소득 100-300만원: 가입금액 100만원 이하  
                    - 월소득 300-400만원: 가입금액 300만원 이하  
                    - 월소득 400만원 초과: 가입금액 500만원 이하

                - **G. 외국인 전용보험 (상해보험 연 납입금)**  
                    - 월소득 모든 구간: 가입금액 3만원

                - **H. 외국인 전용카드 (카드한도, 예금담보 기준 발급)**  
                    - 월소득 100-300만원: 가입금액 200만원 이하  
                    - 월소득 300-400만원: 가입금액 400만원 이하  
                    - 월소득 400만원 초과: 가입금액 500만원 이하

                - **I. 당발송금**  
                    - 월소득 100-300만원: 가입금액 150만원 이하  
                    - 월소득 300-400만원: 가입금액 200만원 이하  
                    - 월소득 400만원 초과: 가입금액 300만원 이하

                - **J. 타발송금**  
                    - 가입금액 300만원 이상 500만원 이하

                #### 6. 송금국가  
                - 해당 행의 **‘국적’** 컬럼값과 동일하게 입력

                """)
        st.markdown("---")
        df_dummy = pd.read_csv('preprocessed_data.csv')
        st.subheader("📖더미데이터 생성 결과")
        st.write(f"총 {len(df_dummy):,} 데이터 생성")
        
        # Column selection
        display_cols = st.multiselect(
            "선택된 컬럼 보기:",
            df_dummy.columns.tolist(),
            default=df_dummy.columns[:].tolist(),
            key="tab2_multiselect"
        )
        
        if display_cols:
            # Sortable data table
            sort_by = st.selectbox("기준 컬럼:", display_cols, index=0, key="tab2_selectbox")
            sort_order = st.radio("정렬 순서:", ["오름차순", "내림차순"], key="tab2_radio")
            
            sorted_df = df_dummy[display_cols].sort_values(
                by=sort_by, 
                ascending=(sort_order == "오름차순")
            )
            st.dataframe(sorted_df, use_container_width=True, height=400)
        else:
            st.dataframe(df_dummy, use_container_width=True, height=400)

        # st.markdown("<h3 style='color:#008486; background-color: #f0f9f8; '>더미 데이터 생성</h3>", unsafe_allow_html=True)
    
    with tab4:
        page11 = Image.open('page11.png')
        centered_image(page11) 
        page12 = Image.open('page12.png')
        centered_image(page12)
        page13 = Image.open('page13.png')
        centered_image(page13) 
        page14 = Image.open('page14.png')
        centered_image(page14) 

        st.markdown("---")
        st.subheader("📑 실제 분석 코드")
        with open("product_recommandation.html", "r", encoding="utf-8") as f:
            html = f.read()

        st.components.v1.html(html, height=900, scrolling=True)

    with tab5:
        page15 = Image.open('page15.png')
        centered_image(page15)
        page16 = Image.open('page16.png')
        centered_image(page16) 
        page17 = Image.open('page17.png')
        centered_image(page17)

    with tab6:
        st.header("📋 분석에 사용한 데이터 ('24 12월말 등록외국인 현황)")
        
        # Data table with search and filter
        # st.subheader("Filtered Dataset")
        # st.write(f"Displaying {len(foreigner_ingu_merged2):,} records")
        
        # Column selection
        display_cols = st.multiselect(
            "지역 선택:",
            foreigner_ingu_merged2.columns.tolist(),
            default=foreigner_ingu_merged2.columns[:8].tolist(),
            key="tab6_multiselect"
        )
        
        if display_cols:
            # Sortable data table
            # sort_by = st.selectbox("Sort by:", display_cols, key="tab6_selectbox")
            # sort_order = st.radio("Sort order:", ["Ascending", "Descending"], key="tab6_radio")
            
            # sorted_df = foreigner_ingu_merged2[display_cols].sort_values(
            #     by=sort_by, 
            #     ascending=(sort_order == "Ascending")
            # )
            
            st.dataframe(foreigner_ingu_merged2, use_container_width=True, height=400)
            
            # Download filtered data
            csv = sorted_df.to_csv(index=False)
            st.download_button(
                label="Download filtered data as CSV",
                data=csv,
                file_name="foreigner_ingu_merged2.csv",
                mime="text/csv"
            )
        else:
            st.dataframe(foreigner_ingu_merged2, use_container_width=True, height=400)
    
    # Footer
    st.markdown("---")
    st.markdown("**Dxp 4조**: **이택인**차장 (강서금융센터지점), **권진**대리 (LS용산타워지점), **김지오**계장 (데이터전략부), **박지영**계장 (IT금융개발부)")

if __name__ == "__main__":
    main()