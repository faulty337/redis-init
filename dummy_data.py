import os
import json
import random

# 데이터 폴더 경로
DATA_FOLDER = "data"

# 폴더가 없으면 생성
os.makedirs(DATA_FOLDER, exist_ok=True)

# 더미 데이터 개수 설정
NUM_FILES = 100  # 원하는 개수로 변경 가능

for i in range(NUM_FILES):
    filename = f"user_{i}.json"
    file_path = os.path.join(DATA_FOLDER, filename)

    # 더미 데이터 생성 (랜덤한 사용자 정보)
    dummy_data = {
        "id": i,
        "name": f"User_{i}",
        "age": random.randint(18, 60),
        "score": random.randint(50, 100),
    }

    # JSON 파일로 저장
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False, indent=2)

print(f"✅ Successfully created {NUM_FILES} dummy JSON files in '{DATA_FOLDER}'")
