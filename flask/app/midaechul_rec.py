from flask import request
from module import db
from flask_restful import Resource, reqparse
import pandas as pd
from flask import make_response
import json
import numpy as np
class Rec_midaechul(Resource):
    def rec_isbn13_search(self,args,dbc):
        try:
            isbn_lst = args["isbn13"].split(",")
            where_query = ",".join(["'%s'"] * len(isbn_lst))
            where_query = where_query % tuple(isbn_lst)
            sql = "select * from midaechul_rec where isbn13 in (%s);" % (where_query)
            row = dbc.executeAll(sql)

            query_data = pd.DataFrame(row, columns=["ISBN", "ISBN_neighbor_0", "ISBN_neighbor_1", "ISBN_neighbor_2"
                , "bookImageURL_0", "bookImageURL_1", "bookImageURL_2"
                , "bookname_0", "bookname_1", "bookname_2"])

            query1 = query_data[["ISBN", "ISBN_neighbor_0", "bookImageURL_0", "bookname_0"]].values
            query2 = query_data[["ISBN", "ISBN_neighbor_1", "bookImageURL_1", "bookname_1"]].values
            query3 = query_data[["ISBN", "ISBN_neighbor_2", "bookImageURL_1", "bookname_2"]].values
            query_data = pd.DataFrame(np.concatenate([query1, query2, query3], axis=0),
                                      columns=["ISBN", "ISBN_neighbor", "bookImageURL", "bookname"])
            query_data = query_data.drop_duplicates()

            final_query = query_data.iloc[:1]

            for ix, row_data in query_data.iterrows():
                isbn = row_data["ISBN_neighbor"]
                if isbn in final_query["ISBN_neighbor"].tolist():
                    continue
                else:
                    final_query = final_query.append(row_data)
            query_data = final_query.iloc[:30]

            result = {}
            result_lst = []
            for ix, row in query_data.iterrows():
                result_dict = {"bookImageURL": row["bookImageURL"],
                               "bookname": row["bookname"],
                               "isbn13": row["ISBN_neighbor"]}
                result_lst.append(result_dict)
            if len(result_lst)==0:
                raise ValueError
            result["result"] = result_lst

            result = json.dumps(result, ensure_ascii=False, indent=4)
            return make_response(result)
        except Exception as e:
            return {'error':str(e)}

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('isbn13',type=str)
            args = parser.parse_args() # example input 11111,22222,33333.//

            dbc = db.Database()
            result = self.rec_isbn13_search(args,dbc)
            return result
        except Exception as e:
            return {'error':str(e)}