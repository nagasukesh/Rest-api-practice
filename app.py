from flask import Flask, jsonify
import json

api=Flask(__name__)

with open("amazon_comments_scrapping.json","r") as f :
    data=json.load(f)

@api.route('/api/customer/all',methods=['POST'])
def display() :
    return jsonify(data)

@api.route('/api/results',methods=['POST'])
def results() :
    result = [res for res in data if res['sentimentValue']> 0.6 and res["Colour"]=="SpaceGrey" and res['size']  == '256GB' and res['Verification'] == 'False' and res['sentimentValue'] > 0.6 and (res['Date'] >='3 March 2018, .' or res['Date'] <= '3 March 2019, .' )]
    return jsonify(result)


if __name__=='__main__' :
    api.run(debug=True)
