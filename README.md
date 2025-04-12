## 주요 디렉토리

| 폴더 | 설명 |
|------|------|
| `app/` | 사용자, 동아리, 출석 등 라우터 및 모델 |
| `flask_session/` | 세션 설정 |
| `utils/` | 유틸 함수 모음 |
| `wsgi.py` | 배포용 진입점 |
| `requirements.txt` | 패키지 목록 |

---

##  업로드 파일 요약
app 파일
- `routes/` : 사용자, 출석 등 REST API 정의
- `models/` : SQLAlchemy 모델 (User, Attendance 등)
- `config.py` : DB 연결, 시크릿 키 등 설정
- `init_db.py` : create_all()로 테이블 자동 생성
- `run.py` : 백엔드 실행용 메인 엔트리포인트
