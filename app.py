from flask import Flask, jsonify,request
import json
from datetime import datetime

api=Flask(__name__)

with open("amazon_comments_scrapping.json","r") as f :
    data=json.load(f)
month = { "jan" : 1, "feb" : 2, "mar" : 3, "apr": 4, "may" : 5, "jun" : 6,"jul" :7 ,"aug" : 8,"sep" : 9, "oct" : 10,"nov" :11,"dec" : 12}
for i in data :
    temp=i["Date"].split(" ")
    i["date"]=datetime(i["year"],i["month"],int(temp[0]))
@api.route('/api/customer/all',methods=['POST'])
def display() :
    return jsonify(data)

@api.route('/api/results',methods=['POST'])
def results() :
    input= request.get_json()
    color=input['Color']
    size=str(input['Size'])+'GB'
    rating=input['Rating']
    verified=input['Verified']
    sentiment=input['Sentiment']
    from_date=input['From date']
    fd=datetime(int(from_date[-4:]),month[from_date[:3].lower()],int(from_date[4:6]))
    to_date=input['To date']
    td=datetime(int(to_date[-4:]),month[to_date[:3].lower()],int(to_date[4:6]))
    results = [res for res in data if res['sentimentValue']> float(sentiment) and res["Colour"]== color and res['size']  == size and res['Verification'] == verified and res['Rating'] == rating and res['date'] >= fd and res['date'] <= td] 

    return jsonify(results)
    
if __name__=='__main__' :
    api.run(debug=True)
