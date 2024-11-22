#스트림릿 모듈 호출
import streamlit as st

#데이터 표시 및 시각화
import pandas as pd

#랜덤 수 표시 위해 삽입
import numpy as np

st.title("스파르타코딩클럽 AI 8기 예제")
st.header("지금 스트림릿 예제를 만들고 있습니다.")
st.text("잘 따라오고 계시죠?")

st.markdown("### H3 글씨를 표현합니다.")
st.latex("E = mc^2")

# 버튼

if st.button("버튼을 클릭하세요"):
    st.write("버튼이 눌렸습니다!!!")

# 체크박스 

agree_box = st.checkbox("동의하시겠습니까?")
if agree_box is True:
    st.write("동의하셨습니다!")

# 슬라이더
volume = st.slider("음악 볼륨", 0, 100, 50)
st.write("음악 볼륨은 " + str(volume) + "입니다.")

gender = st.radio("성별", ["남자", "여자", "밝힐 수 없음"])
st.write("성별은 " + gender + "입니다.")

#툴팁
flrower = st.selectbox("좋아하는 꽃", ["해바라기", "장미", "튤립", "유채꽃"])

df = pd.DataFrame({
    "학번" : ["20170321", "20180111", "20192020", "20200589"],
    "이름" : ["김철수", "최영희", "심지수", "이청중"]
})

st.dataframe(df)

# 위 아래 빈 공간
st.empty()
st.container(border=False, height=20)
st.table(df)

#차트그리기 / line_chart = 꺾은 선 그래프
#chart_data = pd.DataFrame( np.random.randn(20, 3), columns=["a", "b", "c"] ) 
#st.line_chart(chart_data)

chart_data = pd.DataFrame({
    "국어": [100, 95, 80],
    "영어": [80, 95, 100],
    "수학": [95, 100, 80]
})
st.line_chart(chart_data)

#라인이 아니라 바 형태로도 가능.
chart_data = pd.DataFrame({
    "국어": [100, 95, 80],
    "영어": [80, 95, 100],
    "수학": [95, 100, 80]
})
st.bar_chart(chart_data)

import streamlit as st
import numpy as np

st.title("간단한 숫자 데이터 분석하기")

# 사용자로부터 숫자 입력받기 / st.text_input
numbers = st.text_input("숫자 리스트를 입력하세요 (쉼표로 구분)", "1,2,3,4,5")  # 플레이스홀더, 기본값
number_list = [float(x) for x in numbers.split(",")]

# 통계 정보 계산
mean_value = np.mean(number_list)
median_value = np.median(number_list)
stdev_value = np.std(number_list)

# 결과 출력 / 포맷스트링
st.write(f"평균값: {mean_value}")
st.write(f"중앙값: {median_value}")
st.write(f"표준편차: {stdev_value}")
