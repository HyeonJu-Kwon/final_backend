from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print(" db 테이블 생성 완료")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

