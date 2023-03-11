import flask
import pickle
import pandas as pd
from sklearn import preprocessing

# Use pickle to load in the pre-trained model.
with open(f'diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])

def main():
    #  Render the initial form, to get input
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    # Extract the input
    if flask.request.method == 'POST':
        highbp = flask.request.form['HighBP']
        highchol = flask.request.form['HighChol']
        cholcheck = flask.request.form['CholCheck']
        bmi = flask.request.form['BMI']
        smoker = flask.request.form['Smoker']
        stroke = flask.request.form['Stroke']
        heartdiseaseorattack = flask.request.form['HeartDiseaseorAttack']
        physactivity = flask.request.form['PhysActivity']
        fruits = flask.request.form['Fruits']
        veggies = flask.request.form['Veggies']
        hvyalcoholconsump = flask.request.form['HvyAlcoholConsump']
        anyhealthcare = flask.request.form['AnyHealthcare']
        nodocbccost = flask.request.form['NoDocbcCost']
        genhlth = flask.request.form['GenHlth']
        menthlth = flask.request.form['MentHlth']
        physhlth = flask.request.form['PhysHlth']
        diffwalk = flask.request.form['DiffWalk']
        sex = flask.request.form['Sex']
        age = flask.request.form['Age']
        education = flask.request.form['Education']
        income = flask.request.form['Income']

        # Create a dataframe for the model
        input_variables = pd.DataFrame([[highbp, highchol, cholcheck, bmi, smoker, stroke, heartdiseaseorattack, 
                                         physactivity, fruits, veggies, hvyalcoholconsump, anyhealthcare, 
                                         nodocbccost, genhlth, menthlth, physhlth, diffwalk, sex, age, education, 
                                         income]],
                                       columns=['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
                                                'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                                                'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
                                                'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
                                                'Income'],
                                       dtype=float)
        
        # Normalize the input variables
        input_array = preprocessing.normalize([input_variables.loc[0,:].to_numpy()]).reshape(1,-1)
        
        # Get the model's prediction
        prediction = model.predict(input_array)[0]
        print(f'Input Variables: {input_array}')
        print(f'Prediction: {prediction}')

        test_result = "No"

        if prediction == 1:
            test_result = "Yes"

        # Render the form again to output the prediction
        return flask.render_template('main.html',
                                     result=test_result,
                                     )


if __name__ == '__main__' :
    app.run()
