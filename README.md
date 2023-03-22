# FinalProject

<img src="https://user-images.githubusercontent.com/115032384/226765988-637d8309-1c3b-44c6-bbe0-49ea84acc7a1.png" width=200>

# Panda Warriors 

# Diabetes Analysis

## Overview
### Topic: Diabetes  
Diabetes is a chronic disease that occurs when the pancreas doesn’t produce enough insulin or the body can’t use it as well as it should. Our bodies break down the food we eat into glucose and gets released into the bloodstream. When blood glucose levels go up, insulin should let the glucose into the body’s cells to be used for energy. When insulin is low, too much glucose stays in the bloodstream and can cause life threatening complications. Diabetes can be caused by genetics or lifestyle factors like eating and exercise habits. Over time, diabetes can lead to other serious problems like kidney disease, heart disease or vision loss.  

There are over 37 million adults in the US living with diabetes and many more that go undiagnosed. We chose this topic to help predict the probability of a person having diabetes using supervised machine learning models.

Note: Reasoning for topic selection is documented in the project proposal and project status is documented in the project proposal and the checklist section. 

## Webpage
   
   * __A Flask app with Neural Network Model has been deployed to an URL using Heroku.__
   
   [link to the Flask app](https://diabetes-model.herokuapp.com/)
   
   <img src="Images/Flask app.PNG" width=200> 
   
## Data source: 

The dataset used for our research was the diabetes_binary_health_indicators_BRFSS2015.csv, extracted from the data pool of health-related telephone survey of 2015 provided by the Behavioral Risk Factor Surveillance System (BEFSS). The data file contains 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced. The original post can be found on Kaggle; please access the following link to the original post.

[link to the original post](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

## Questions 
After testing the maching learning models, which model has the highest accuracy? 

What is the correlation between the vector and the target variable? 

## Database and Tables

   * __AWS Database__
   <img src="Images/Database.PNG" width=400> 

   * __S3 Bucket__
   <img src="Images/S3_bucket.PNG" width=400> 

   * __Tables Created in Database__
   <img src="Images/Tables.PNG" width=400>
   
## Languages, Tools and Algorithms

   * __Languages:__ Python, HTML

   * __Tools:__ pandas, numpy, scikit-learn, imblearn, sqlalchemy, getpass, collections, tensorflow, os, keras_tuner, keras, pickle, flask, AWS, Heroku 

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

Age of Diabetic Patients by Gender

![AgeofDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773864-94730b88-0aaf-4b3e-989e-9c1e969cef0b.png)


Smokers & Alcohol Consumption

![SmokersAlcoholConsumption](https://user-images.githubusercontent.com/115032384/225789059-7dc24710-e27b-4211-955e-433ce3e96dd8.png)


Physical Activity by Education

![PhysicalActivity](https://user-images.githubusercontent.com/115032384/225775635-1e7f24c7-ebcb-45a7-b849-de60b4223746.png)


Fruit & Vegetable Consumption by Income

![FruitVegetableConsumptionbyIncome](https://user-images.githubusercontent.com/115032384/225788358-41eed264-90b8-4439-aff1-f1e30fcd6aec.png)


Average BMI by Gender 

![AvgBMIbyGender](https://user-images.githubusercontent.com/115032384/225789941-af0844b6-e90d-43d1-8e0c-a86036f6115e.png)


Average BMI by Age 

![AvgBMIbyAge](https://user-images.githubusercontent.com/115032384/225788322-a78d20b1-efe0-4467-a988-9cf8cd9907a4.png)


Diabetes Analysis Dashboard

![DiabetesAnalysisDashboard](https://user-images.githubusercontent.com/115032384/225776918-02587a17-8220-4f48-a5e2-2cb458b14830.png)


[Link to Tableau Story](https://public.tableau.com/views/Diabetes_Analysis_16786693958130/DiabetesAnalysisStory?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Results 

Multiple supervised machine learning models and deep machine learning models have been tested. The performance of each model is shown below:

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

There was a technical challenge encountered when attempting deploy app to the web service, Heroku. The size of the original bundle was 900mb, but the web services limit is 500mb. This was solved by creating a new development environment. After testing the app, the error message showed what libraries were required and followed the instructions to download them. This reduced the bundle size to around 270mb. 
If we had a resource with more detailed data to create more accurate machine learning models to predict the probability of a patient having diabetes. 
Neural network model discovered from using Keras-Tuner outperformed the other machine learning models with an accuracy of approximately 0.855. 
The BMI, age & physical health are the most significant risk factors for Diabetes. 
