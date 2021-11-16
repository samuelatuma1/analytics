from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from assignments_solutions import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get("investmentData")
        data = eval(data)
        investments, available_fund = [data['investments'], data['available_fund']]
        
        analyzed_investments = optimize_investments(investments, available_fund)
        return jsonify(analyzed_investments)
    return render_template("index.html")

