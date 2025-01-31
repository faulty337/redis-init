# 🚀 Redis 초기 데이터 삽입 자동화

이 프로젝트는 **Redis에 초기 데이터를 자동으로 삽입**하는 방법을 제공합니다.  
비동기 파일 읽기를 활용하여 `.data/` 폴더 내 파일을 빠르게 Redis에 저장합니다.

---

## 📦 프로젝트 개요

- Redis 실행 시 **초기 데이터 세팅을 자동화**합니다.
- `.data/` 폴더 내 JSON 파일을 **비동기(Async) 방식으로 Redis에 저장**합니다.
- **Docker 환경**에서도 Redis 데이터 초기화를 자동으로 수행할 수 있습니다.

---

## ⚙️ 환경 설정

### **🔹 1️⃣ 필수 요구 사항**
이 프로젝트를 실행하려면 다음 환경이 필요합니다.

- Python 3.8+
- Redis 6.0+
- `pip` (Python 패키지 관리자)
- (선택) Docker & Docker Compose
- 

### **🔹 2️⃣ Python 패키지 설치**
```bash
pip install redis aiofiles
```


### **🔹 3️⃣ (선택) Docker **
기본적인 Redis 이미지를 이용한 Docker compose 파일을 제공합니다.
Redis가 존재하지 않거나 테스트 환경이 필요할 경우 실행해야 합니다.
```bash
docker compose up -d
```
