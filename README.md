Google Slides https://docs.google.com/presentation/d/1g5DSXvWVpdpNWvQIIKLeAP5633_T5m90IMOriAqT248/edit?usp=sharing 

# FinalProject

<img src="https://user-images.githubusercontent.com/115032384/226765988-637d8309-1c3b-44c6-bbe0-49ea84acc7a1.png" width=200>

# Panda Warriors 

Xiaoyi - Team Manager

Wei - Coding Expert

Jess - Visualization Specialist 


# Diabetes Analysis

## Overview
### Topic: Diabetes  
Diabetes is a chronic disease that occurs when the pancreas doesn’t produce enough insulin or the body can’t use it as well as it should. Our bodies break down the food we eat into glucose and gets released into the bloodstream. When blood glucose levels go up, insulin should let the glucose into the body’s cells to be used for energy. When insulin is low, too much glucose stays in the bloodstream and can cause life threatening complications. Diabetes can be caused by genetics or lifestyle factors like eating and exercise habits. Over time, diabetes can lead to other serious problems like kidney disease, heart disease or vision loss.  

There are over 37 million adults in the US living with diabetes and many more that go undiagnosed. We chose this topic to help predict the probability of a person having diabetes using supervised machine learning models.

Note: Reasoning for topic selection is documented in the project proposal and project status is documented in the project proposal and the checklist section. 

## Webpage
   
   * __A Flask app with Neural Network Model has been deployed to an URL using Heroku.__
   
   [Link to Flask App](https://diabetes-model.herokuapp.com/)
   
   <img src="Images/Flask app.PNG" width=200> 
   
## Data source: 

The dataset used for our research was the diabetes_binary_health_indicators_BRFSS2015.csv, extracted from the data pool of health-related telephone survey of 2015 provided by the Behavioral Risk Factor Surveillance System (BRFSS). The data file contains 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced. The original post can be found on Kaggle; please access the following link to the original post.

[Link to Original Post](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

## Questions 
After testing the machine learning models, which model has the highest accuracy? 

What is the correlation between the vector and the target variable? 

## Database and Tables 

Our team used Amazon Web Service to host our database for this project. After building the database, an S3 bucket was created to store the raw data file and relevant tables.

   * __AWS Database__

   <img src="Images/Database.PNG" width=400> 

   * __S3 Bucket__

   <img src="Images/S3_bucket.PNG" width=400> 

   * __Tables Created in Database__

   <img src="Images/Tables.PNG" width=400>
   
## Languages, Tools and Algorithms

   * __Languages:__ Python, HTML

   * __Tools:__ pandas, numpy, scikit-learn, imblearn, sqlalchemy, getpass, collections, tensorflow, os, keras_tuner, keras, pickle, flask, Tableau, AWS, Heroku,  

   * __Algorithms:__ Support Vector Machine, Decision Trees, RandomOverSampler, SMOTE, ClusterCentroids, SMOTEENN, BalancedRandomForestClassifier, EasyEnsembleClassifier, Neural Network Model.

## Data Exploration

   * The diabetes dataset comprises 22 columns containing 21 feature variables and 1 target variable. Our goal is to utilize machine models to predict whether or not a new patient has diabetes. Based on the dataset structure, we proceeded with classification model algorithms to help us predict the discrete outcomes.
   * First, we preprocessed the data by removing invalid inputs and duplicates from the raw data file.  
   * Next, we categorized features from the target by separating the outcome column from the others. In our case, the Diabetes_binary is the target variable; the rest of the columns are the feature variables.
   * Thirdly, we split the dataset into training and testing sets.
   * For particular algorithms, we used Scikit-learn's StandardScaler module to scale data prior to using it to train the model.
   * It is worth noting that our dataset has no categorical data variables. Therefore, there was no need to transform and encode any data variables when we trained the deep learning model.    

## Data Analysis

   * With the preprocessed data, we have trained the following machine learning models:
      * Support Vector Machine Model
      * Decision Trees Model
      * RandomOverSampler Model (Oversampling)
      * SMOTE Model (Oversampling)
      * ClusterCentroids Model (Undersampling)
      * SMOTEENN (Combination of Oversampling and Undersampling)
      * BalancedRandomForestClassifier Model
      * EasyEnsembleClassifier Model
      * Deep Learning Model (with Keras-Tuner)
   * According to the results, the neural network model discovered using Keras-Tuner outperformed the other machine learning models with an accuracy of approximately 0.855. 

## Tableau Analysis

[Link to Tableau Story](https://public.tableau.com/views/Diabetes_Analysis_16786693958130/DiabetesAnalysisStory?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

   Diabetic to Non-Diabetic Patients 

![DiabetictoNonDiabeticPatients](https://user-images.githubusercontent.com/115032384/227278204-16f718a4-66b1-433e-a55c-d9dda0219660.png)


   Cholesterol & Blood Pressure
   
![CholesterolBloodPressure](https://user-images.githubusercontent.com/115032384/227018426-3585ad52-95a3-48a1-b062-bc175108ca78.png)


   Smokers & Alcohol Consumption

![SmokersAlcoholConsumption](https://user-images.githubusercontent.com/115032384/227210547-e1d5fb92-7e5a-47e9-b437-13cc8534d2eb.png)


   Physical Activity by Education

![PhysicalActivity](https://user-images.githubusercontent.com/115032384/227210585-093a4044-65e3-4d01-a056-8a3aaeb6471f.png)


   Fruit & Vegetable Consumption by Income

![FruitVegetableConsumptionbyIncome](https://user-images.githubusercontent.com/115032384/227210635-70d92e11-abb1-420b-acdf-a9c48e24acfd.png)


   Age of Diabetic Patients by Gender

![AgeofDiabeticPatients](https://user-images.githubusercontent.com/115032384/227020416-0e1d3d95-d0fe-4d80-b684-db6f88927755.png)


   Average BMI by Gender 

![AvgBMIbyGender](https://user-images.githubusercontent.com/115032384/227020458-e294c072-f74a-4c17-b830-7ebf9a4f9d10.png)


   Average BMI by Age 

![AvgBMIbyAge](https://user-images.githubusercontent.com/115032384/227020498-fef7d93f-54c8-4ce1-bb73-1395611ad0de.png)

   Dashboard

![DiabetesAnalysisDashboard](https://user-images.githubusercontent.com/115032384/225776918-02587a17-8220-4f48-a5e2-2cb458b14830.png)


## Results 

Multiple supervised machine learning models and deep learning models have been tested. The performance of each model is shown below:

   * __SVM Model__

   <img src="Images/SVM Model.PNG" width=400> 
   
   * __Decision Tree Model__

   <img src="Images/Decision Tree Model.PNG" width=400> 
   
   * __RandomOverSampler Model__

   <img src="Images/RandomOverSampler Model.PNG" width=400>
   
   * __SMOTE Model__

   <img src="Images/SMOTE Model.PNG" width=400>
   
   * __ClusterCentroids Model__

   <img src="Images/ClusterCentroids Model.PNG" width=400>
   
   * __SMOTEENN Model__

   <img src="Images/SMOTEENN Model.PNG" width=400>
   
   * __BalancedRandomForestClassifier Model__

   <img src="Images/BalancedRandomForestClassifier Model.PNG" width=400>
   
   * __EasyEnsembleClassfiler Model__

   <img src="Images/EasyEnsembleClassifier Model.PNG" width=400>
   
   * __Deep Learning Model__

   <img src="Images/Deep Learning Model Summary.PNG" width=400>

   <img src="Images/Deep Learning Model Performance.PNG" width=400>
  
   * __Neural Network Model(Keras-Tuner)__

   <img src="Images/Neural Network Model Hyperparameters.PNG" width=200>
   
   <img src="Images/Neural Network Model Performance.PNG" width=400>
   

## Conculsion

The SVM classifier we tried in the very beginning shows an interesting result: For all testing dataset, it always gives negative results. With about 85% entries in this dataset have negative results, this blind guess on negative can achieve 84.7% accuracy on the testing dataset. This is due to the class imbalance of the source dataset. 
This 84.7% number is set as baseline for the evaluation of the rest of the models.

To account for the class imbalance issue. We tested oversampling, undersampling and combined sampling methods. 
Although the trained model did output both positive and negative results, the accuracy is not good enough compared with the baseline. 

Neural network model discovered from using Keras-Tuner outperformed the other machine learning models with an accuracy of approximately 85.5%. 
The BMI, age & physical health are the most significant risk factors for Diabetes. 

Possible improvement can be:

* Test with larger dataset. With a large dataset, it's possible to train a more sofisticated network and possible to achieve a better accuracy. 
* Incorporate more data columns, there might be other aspects that can affect the diabetes not included in the currect dataset. 

There was a technical challenge encountered when attempting deploy app to the web service, Heroku. The size of the original bundle was 900mb, but the web services limit is 500mb. This was solved by creating a new development environment. After testing the app, the error message showed what libraries were required and followed the instructions to download them. This reduced the bundle size to around 270mb. 