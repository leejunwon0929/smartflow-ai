import streamlit as st
import pathlib

st.set_page_config(
    page_title="SmartFlow AI | 지능형 도시 교통 관리",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stTabs { background: #060a14; }
.stTabs [data-baseweb="tab-list"] {
    background: #0b1120;
    padding: 6px 20px 0;
    border-bottom: 1px solid rgba(0,229,255,0.18);
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    color: #64748b !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 8px 22px !important;
    border-radius: 6px 6px 0 0 !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    color: #00e5ff !important;
    background: rgba(0,229,255,0.08) !important;
    border-bottom: 2px solid #00e5ff !important;
}
div[data-testid="stTabContent"] { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# app.py 위치 기준으로 HTML 파일 경로 설정 (Streamlit Cloud 경로 문제 방지)
BASE      = pathlib.Path(__file__).parent
NEWS_PATH = BASE / "news.html"
SIM_PATH  = BASE / "index.html"

news_html = NEWS_PATH.read_text(encoding="utf-8")
sim_html  = SIM_PATH.read_text(encoding="utf-8")

news_html = news_html.replace(
    '<a class="demo-btn" href="index.html" target="_blank">▶ 시뮬레이터 실행하기</a>',
    '<span style="display:inline-block;padding:10px 28px;'
    'background:linear-gradient(135deg,#00e5ff,#3b82f6);color:#000;'
    'font-family:Outfit,sans-serif;font-weight:800;font-size:0.85rem;border-radius:6px;">'
    '🚦 상단 \'AI 시뮬레이터\' 탭을 클릭하세요</span>'
)

tab1, tab2 = st.tabs(["📰  뉴스 기사", "🚦  AI 시뮬레이터"])

with tab1:
    st.components.v1.html(news_html, height=5600, scrolling=True)

with tab2:
    st.components.v1.html(sim_html, height=760, scrolling=False)
