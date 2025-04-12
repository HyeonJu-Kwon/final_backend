from app import create_app, db
from app.models.attendance import Attendance

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ DB 테이블 생성 완료!")
