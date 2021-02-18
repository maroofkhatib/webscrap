from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import pandas as pd
import numpy as np

app = Flask(__name__)
api = Api(app)
table = pd.read_csv('./new/articles.csv')

table = table.to_numpy()
l = len(table)

class GetArticle(Resource):

	def post(self):

		requested_data = request.get_json()
		data = requested_data['data'].lower()
		lis = []
		for i in range(l):
			if data in table[i,0].lower():
				dic = {
					
					'text':table[i,1],
					'link':table[i,2],
					'title':table[i,0]
				}
				lis.append(dic)
		
		if lis == []:
			articles = {
				'Articles' : "No match articles found"
			}
		else:
			articles = {
				'Articles' : lis
			}
					
		return jsonify(articles)

api.add_resource(GetArticle, "/getarticle")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)





