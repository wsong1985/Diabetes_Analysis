import flask
import pickle
import numpy as np
import pandas as pd
from keras.models import load_model

# Load in the pre-trained model.
model = load_model('diabetes_model.h5')

# Use pickle to load in the pre-trained scaler.
with open('dlm_X_scaler.pkl', 'rb') as file:
    dlm_X_scaler=pickle.load(file)

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
        input_variables = pd.DataFrame([[highbp, highchol, cholcheck, smoker, stroke, 
                                         heartdiseaseorattack, physactivity, fruits, veggies, 
                                         hvyalcoholconsump, anyhealthcare, nodocbccost, genhlth, 
                                         diffwalk, sex, education, income]],
                                        columns=['HighBP', 'HighChol', 'CholCheck', 'Smoker','Stroke', 
                                                'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                                                'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
                                                'DiffWalk', 'Sex', 'Education', 'Income'],
                                       dtype=float)
        
        input_variables_2 = pd.DataFrame(0, index=range(1), columns=['BMI_23.0', 'BMI_24.0','BMI_25.0', 'BMI_26.0', 'BMI_27.0', 
                                                'BMI_28.0', 'BMI_29.0', 'BMI_30.0','BMI_100.0', 
                                                'MentHlth_0.0', 'MentHlth_1.0', 'MentHlth_2.0','MentHlth_3.0', 
                                                'MentHlth_5.0', 'MentHlth_10.0', 'MentHlth_15.0','MentHlth_30.0', 
                                                'MentHlth_100.0', 
                                                'PhysHlth_0.0', 'PhysHlth_1.0','PhysHlth_2.0', 'PhysHlth_3.0', 
                                                'PhysHlth_5.0', 'PhysHlth_10.0','PhysHlth_15.0', 'PhysHlth_30.0', 
                                                'PhysHlth_100.0', 
                                                'Age_6.0','Age_7.0', 'Age_8.0', 'Age_9.0', 'Age_10.0', 'Age_11.0', 
                                                'Age_12.0','Age_13.0', 'Age_100.0'])

        bmi_str = 'BMI_' + str(round(int(bmi))) +'.0'
        menthlth_str = 'MentHlth_' + str(round(int(menthlth))) +'.0'
        physhlth_str = 'PhysHlth_' + str(round(int(physhlth))) +'.0'
        age_str = 'Age_' + str(round(int(age))) + '.0'

        if bmi_str in input_variables_2.columns:
            input_variables_2[bmi_str] = 1
        else:
            input_variables_2['BMI_100.0'] = 1

        if menthlth_str in input_variables_2.columns:
            input_variables_2[menthlth_str] = 1
        else:
            input_variables_2['MentHlth_100.0'] = 1

        if physhlth_str in input_variables_2.columns:
            input_variables_2[physhlth_str] = 1
        else:
            input_variables_2['PhysHlth_100.0'] = 1

        if age_str in input_variables_2.columns:
            input_variables_2[age_str] = 1
        else:
            input_variables_2['Age_100.0'] = 1

        print(input_variables.shape)
        print(input_variables_2.shape)

        input_variables = input_variables.merge(input_variables_2, left_index =True, right_index = True)

        # # Scale the input variables
        input_array = input_variables.loc[0,:].to_numpy().reshape(1,-1)
        input_array_scaled = dlm_X_scaler.transform(input_array)

        # test_input_array = ([[1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 5, 1, 0, 5,
        # 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        # 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
        # 0, 0, 0, 0, 0]])
        # test_input_array_scaled = dlm_X_scaler.transform(input_array)
        
        # Get the model's prediction
        prediction = (model.predict(input_array_scaled) > 0.5).astype("int32")
        # print(f'Input Variables: {input_array}')
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
