import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="주식 분석기",
    page_icon="📈", 
    layout="wide"
)

STOCKS = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corp.',
    'GOOGL': 'Alphabet Inc.',
    'TSLA': 'Tesla Inc.',
    'NVDA': 'NVIDIA Corp.'
}

def get_stock_data(symbol, period = '1y'):
    try :
        # 해당 심볼의 yf ticker 객체 생성
        ticker = yf.Ticker(symbol)

        # ticker의 기록 데이터 가져오기 기간만큼 
        hist_data = ticker.history(period=period)  # 빈칸을 채우세요

        # 해당 심볼의 기업 정보 가져 오기 
        company_info = ticker.info

        # 데이터가 비어 있지 않았다면 반환 
        if not hist_data.empty:
            return hist_data, company_info 
        else:
            return None, None
    except Exception as e:
        st.error(f"데이터를 가져오는 중 오류 발생: {e}")
        return None, None 





