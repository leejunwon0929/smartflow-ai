# 🚦 SmartFlow AI — 지능형 도시 교통 관리 시스템

> AI 기반 도시 교통 흐름 최적화 시스템 기획 및 인터랙티브 시뮬레이션

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

---

## 📋 프로젝트 구성

| 파일 | 설명 |
|------|------|
| `app.py` | Streamlit 메인 앱 (뉴스 + 시뮬레이터 탭) |
| `news.html` | 뉴스 형식 기획 보도 페이지 |
| `index.html` | AI 교통 시뮬레이션 대시보드 |
| `requirements.txt` | Python 의존성 |
| `.streamlit/config.toml` | Streamlit 테마 설정 |

## 🚀 로컬 실행

```bash
pip install streamlit
streamlit run app.py
```

## 🌐 Streamlit Cloud 배포

1. 이 저장소를 GitHub에 push
2. [share.streamlit.io](https://share.streamlit.io) 접속
3. GitHub 연동 후 이 저장소 선택
4. Main file: `app.py` 설정 후 Deploy

## ✨ 주요 기능

- 📰 AI 교통 관리 시스템 뉴스 기사 (TechNews Korea 형식)
- 🚦 실시간 교통 시뮬레이션 (5×4 교차로 격자 도시)
- 🤖 AI 신호 최적화 모드 (강화학습 기반)
- ⚠️ 사고 발생 및 우회 경로 시뮬레이션
- 🚑 응급차 우선 신호 제어 시뮬레이션
- 🚗 출퇴근 혼잡 시뮬레이션
