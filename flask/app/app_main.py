
# About Flask and Flask_restful Library
from flask import Flask, render_template,request
from flask_restful import Api
from flask import session
from datetime import timedelta
#from flask_jwt_extended import JWTManager, jwt_required

#from flask_cors import CORS, cross_origin

from midaechul_rec import Rec_midaechul # 대출 추천 유사 미대출 도서 추천
from midaechul_gender_age import Rec_midaechul_gender_age # 성별,연령,토픽별 미대출 도서 추천

app = Flask(__name__)
#app.config['JWT_SECRET_KEY'] = 'secret'
#app.config['JSON_AS_ASCII'] = False
#app.secret_key = 'secret'

api = Api(app)

#jwt = JWTManager(app)

api.add_resource(Rec_midaechul,'/midaechul/similar') # midaechul_rec.py
api.add_resource(Rec_midaechul_gender_age,'/midaechul/gender-age') # midaechul_gender_age.py

#CORS(app, resources={r'*': {'origins': '*'}})
"""
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
"""
@app.route("/")
def hello():
    return render_template('/index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)