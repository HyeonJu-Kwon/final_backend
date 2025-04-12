from flask import Blueprint, request, jsonify, session
from app.models.attendance import Attendance
from app.models.user import User
from app import db
from datetime import datetime
from sqlalchemy import and_
from functools import wraps

bp = Blueprint('attendance', __name__, url_prefix='/api')

# ✅ 세션 기반 인증 데코레이터
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'message': '로그인이 필요합니다.'}), 401
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': '사용자를 찾을 수 없습니다.'}), 404
        return f(user, *args, **kwargs)
    return decorated

# ✅ 출석 등록 (중복 방지 포함)
@bp.route('/attendance', methods=['POST'])
@login_required
def record_attendance(current_user):
    status = request.json.get('status', '출석')
    today = datetime.utcnow().date()

    existing = Attendance.query.filter(
        and_(
            Attendance.user_id == current_user.id,
            db.func.date(Attendance.timestamp) == today
        )
    ).first()

    if existing:
        return jsonify({'message': '오늘은 이미 출석을 등록했습니다.'}), 409

    new_record = Attendance(
        user_id=current_user.id,
        status=status,
        timestamp=datetime.utcnow()
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message': '출석 등록 완료!', 'status': status}), 201

# ✅ 본인 출석 목록 조회
@bp.route('/attendance/history', methods=['GET'])
@login_required
def attendance_history(current_user):
    records = Attendance.query.filter_by(user_id=current_user.id).order_by(Attendance.timestamp.desc()).all()

    history = [
        {
            'date': record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'status': record.status
        }
        for record in records
    ]

    return jsonify({'attendance': history}), 200

# ✅ 관리자 전체 출석 기록 조회
@bp.route('/admin/attendance/all', methods=['GET'])
@login_required
def admin_attendance_all(current_user):
    if current_user.email != 'admin@admin.com':
        return jsonify({'message': '관리자 권한이 없습니다.'}), 403

    records = Attendance.query.order_by(Attendance.timestamp.desc()).all()

    all_data = [
        {
            'user_id': record.user_id,
            'timestamp': record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'status': record.status
        }
        for record in records
    ]

    return jsonify({'attendance': all_data}), 200

