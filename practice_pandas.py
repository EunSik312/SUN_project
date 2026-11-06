
import pandas as pd

# 1. 가상의 반도체 센서 데이터 생성
data = {
    "sensor_001": [10, 12, 9, 11],
    "result": ["PASS", "PASS", "FAIL", "PASS"]
}

# 2. Pandas 데이터프레임 생성
df = pd.DataFrame(data)

# 3. 데이터 출력
print(df)

# 4. 센서 평균 계산
print("센서 평균:", df["sensor_001"].mean())

# 5. 양품과 불량품의 개수 확인
print(df["result"].value_counts())

# 6. 센서 데이터의 최대값과 최소값
print("센서 최대값:", df["sensor_001"].max())
print("센서 최소값:", df["sensor_001"].min())


# 7. 전체 제품 중 불량품의 비율 계산
total_count = len(df) #전체 제품 개수
fail_count = (df["result"] == "FAIL").sum() # 불량 제품인지 확인하고 불량 제품 개수를 계산

fail_rate = (fail_count / total_count) * 100 #불량률 계산

print("전체 제품 수:", total_count)
print("불량품 수:", fail_count)
print("불량률:", fail_rate, "%")
