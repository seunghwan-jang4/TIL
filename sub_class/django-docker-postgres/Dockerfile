# Dockerfile 
FROM python:3.9 # 파이썬의 버전

# 작업 디렉토리 설정 
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 복사
COPY . .

# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]