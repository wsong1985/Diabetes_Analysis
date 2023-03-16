# Final_Project_Group4

# Diabetes Analysis

## Overview
### Topic: Diabetes  
Diabetes is a chronic disease that occurs when the pancreas doesn’t produce enough insulin or the body can’t use it as well as it should. Our bodies break down the food we eat into glucose and gets released into the bloodstream. When blood glucose levels go up, insulin should let the glucose into the body’s cells to be used for energy. When insulin is low, too much glucose stays in the bloodstream and can cause life threatening complications. Diabetes can be caused by genetics or lifestyle factors like eating and exercise habits. Over time, diabetes can lead to other serious problems like kidney disease, heart disease or vision loss.  

There are over 37 million adults in the US living with diabetes and many more that go undiagnosed. We chose this topic to help predict the probability of a person having diabetes using supervised machine learning models.

Note: Reasoning for topic selection is documented in the project proposal and project status is documented in the project proposal and the checklist section. 

## Data source: 

The dataset used for our research was the diabetes_binary_health_indicators_BRFSS2015.csv, extracted from the data pool of health-related telephone survey of 2015 provided by the Behavioral Risk Factor Surveillance System (BEFSS). The data file contains 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced. The original post can be found on Kaggle; please access the following link to the original post.

[link to the original post](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

## Questions 
After testing the maching learning models, which model has the highest accuracy? 

What is the correlation between the vector and the target variable? 

## Checklist

   * __AWS Database - Completed__
   <img src="Images/Database.PNG" width=400> 

   * __S3 Bucket - Completed__
   <img src="Images/S3_bucket.PNG" width=400> 

   * __Tables Created in Database - Completed__
   <img src="Images/Tables.PNG" width=400> 

   
## Webpage
   
   * __A Flask app with Deep Machine Learning has been completed and deployed to an URL using Heroku.__
   
   [link to the Flask app](https://diabetes-model.herokuapp.com/)
   
   <img src="Images/best_dml_model_by_keras_tuner.PNG" width=400>    

## Tableau Analysis

There are 229,474 patients in this dataset. 

![NumberofPatients](https://user-images.githubusercontent.com/115032384/224593519-e49babfe-c817-4113-b8a0-4088b1fa34e8.png)


Diabetic to Non-Diabetic Patients
194,377 Patients are non Diabetic & 35,097 patients are Diabetic.

![DiabetictoNonDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773453-4dbb5714-a1dc-473e-be0f-ae13e31208d6.png)


Gender of All Patients 

![GenderofAllPatients](https://user-images.githubusercontent.com/115032384/225773817-7ea078ae-ed36-4803-9fd3-e36e00152e58.png)


Gender of Diabetic Patients 

![GenderofDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773833-31e06d92-a619-4618-a9ee-ad6eafb8d081.png)


Age of Diabetic Patients by Gender

![AgeofDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773864-94730b88-0aaf-4b3e-989e-9c1e969cef0b.png)


Smokers and Alcohol Consumption

![SmokersAlcoholConsumption](https://user-images.githubusercontent.com/115032384/225178930-4b6a13b5-4fdc-4696-9d08-d1117ed6b623.png)

Income 

![Income](https://user-images.githubusercontent.com/115032384/225179717-70abd8e2-6f03-4553-ab40-484341965503.png)


Physical Activity 

![PhysicalActivity](https://user-images.githubusercontent.com/115032384/225179420-8d7370eb-302b-45b9-b77a-b882014d7e45.png)


Fruit & Vegetable Consumption

![FruitVegetableConsumption](https://user-images.githubusercontent.com/115032384/225179305-ca6a55f4-1e96-44cf-8798-fd428a833f7c.png)


Average BMI by Gender 

![AvgBMIbyGender](https://user-images.githubusercontent.com/115032384/225774978-a57c4b46-e462-452f-a2ee-1914a35dea1d.png)


Average BMI by Age 

![AvgBMIbyAge](https://user-images.githubusercontent.com/115032384/225774955-e3ee5e57-84a0-430e-bec5-6f21b526b51e.png)


[Link to Tableau Story](https://public.tableau.com/views/Diabetes_Analysis_16786693958130/DiabetesAnalysisStory?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Results 

## Summary 
