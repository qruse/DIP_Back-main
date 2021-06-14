from flask import request
from module import db
from flask_restful import Resource, reqparse
import pandas as pd
from flask import make_response
import json

class Rec_midaechul_gender_age(Resource):
    def age_gender_search(self,args,dbc):
        try:
            print(args)
            gender = args["gender"]
            age = args["age"]
            topic = args["topic"]
            library_code = args["library_code"]

            if gender=="1":
                gender = "'F'"
            elif gender=="0":
                gender = "'M'"
            elif gender =="":
                gender = "'F','M'"
            else:
                raise ValueError("Only allow 0(M) or 1(F)")

            if age =="":
                age = ",".join(["'%s'"] * 9)
                age = age % tuple([40,  8, 14, 20, 50, 30, 60,  6,  0])

            if topic=="":
                topic = ",".join(["'%s'"] *19)
                topic = topic % tuple(range(19))

            if library_code == "122003":
                library_query = "bukbu=1"
            elif library_code == "127005":
                library_query = "sungseo=1"
            elif library_code == "127002":
                library_query = "dalseochild=1"
            elif library_code == "127001":
                library_query = "dowon=1"
            elif library_code == "127012":
                library_query = "bonly=1"
            else:
                raise ValueError("Only allow [122003,127005,127002,127001,127012]")

            sql = "select * from midaechul_gender_age where gender in (%s) and age in (%s) and %s and topic in (%s);" % (gender, age, library_query,topic)
            row = dbc.executeAll(sql)
            print(row)
            query_data = pd.DataFrame(row, columns=["ISBN", "gender", "age"
                , "bukbu", "dalseochild", "dowon", "bonly","sungseo", "topic","bookname","bookurl"])
            try:
                sample_query = query_data.sample(30)
            except:
                sample_query = query_data.sample(len(query_data))

            result = {}
            #result["result_num"] = len(sample_query)
            result_lst = []
            for ix in range(len(sample_query)):
                row_data = sample_query.iloc[ix]
                result_dict = {"isbn13": row_data["ISBN"],
                               "bookname": row_data["bookname"],
                               "bookImageURL": row_data["bookurl"]}
                result_lst.append(result_dict)
            result["result"] = result_lst
            result = json.dumps(result, ensure_ascii=False, indent=4)
            return make_response(result)
            return result
        except Exception as e:
            return {'error':str(e)}

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('gender',type=str)
            parser.add_argument('age', type=str)
            parser.add_argument('topic', type=str)
            parser.add_argument('library_code', type=str)
            args = parser.parse_args()

            dbc = db.Database()
            result = self.age_gender_search(args,dbc)
            return result
        except Exception as e:
            return {'error':str(e)}