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
- `__init__.py`: Flask 백엔드 초기 구성 업로드: 앱 생성, DB 설정, 블루프린트 등록
- `run.py` : 백엔드 실행용 메인 엔트리포인트


init.db.py = 모든 DB 테이블을 한 번에 생성하는 초기화 스크립트
