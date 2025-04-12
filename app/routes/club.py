# app/routes/club.py

from flask import Blueprint, make_response
from app.models.club import Club
import json

bp = Blueprint('club', __name__)

# 한글 응답용 JSON 함수
def json_response(data, status=200):
    response = make_response(json.dumps(data, ensure_ascii=False))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response, status

@bp.route('/api/clubs', methods=['GET'])
def get_clubs():
    clubs = Club.query.all()
    return json_response([club.to_dict() for club in clubs])

