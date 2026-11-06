
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
