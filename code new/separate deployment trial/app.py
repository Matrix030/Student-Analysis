import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import suggestsem3, suggestsem4

app = Flask(__name__)
model1 = pickle.load(open('sem3model.pkl', 'rb'))
model2 = pickle.load(open('sem4model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

# SEM3


@app.route('/sem3')
def sem3():
    return render_template('sem3.html')

# def predict1():
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model1.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('sem3.html', prediction_text='(Previous students)student from sem 3 belongs to class : {}'.format(output), np_array='{}'.format(int_features))

# SEM4


@app.route('/sem4')
def sem4():
    return render_template('sem4.html')

# def predict2():
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model2.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('sem4.html', prediction_text='student from sem 4 belongs to class : {}'.format(output), np_array='{}'.format(int_features))


@app.route('/predictsem3', methods=['POST','GET'])
def predictsem3():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)
    print(int_features)

    output = round(prediction[0], 2)
    print('this is the output',output)
    suggestion = suggestsem3.suggest(int_features,output)
    print(suggestion)
    return render_template('sem3.html', prediction_text='student from sem 3 belongs to class : {}'.format(output), list=suggestion)


@app.route('/predictsem4', methods=['POST'])
def predictsem4():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)

    output = round(prediction[0], 2)
    print('this is the output',output)
    suggestion = suggestsem4.suggest(int_features,output)
    print(suggestion)

    return render_template('sem4.html', prediction_text='student from sem 4 belongs to class : {}'.format(output), list=suggestion)

# @app.route('/predict_apisem3',methods=['POST'])
# def predict_apisem3():
#     data = request.get_json(force=True)
#     prediction = model1.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

# @app.route('/predict_apisem4',methods=['POST'])
# def predict_apisem4():
#     data = request.get_json(force=True)
#     prediction = model2.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)


