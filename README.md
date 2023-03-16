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


194,377 Patients are non Diabetic & 35,097 patients are Diabetic.

![DiabeticandNonDiabeticPatients](https://user-images.githubusercontent.com/115032384/224593791-4f50f43c-82bf-47bf-9212-50bb4a02e0fc.png)


Gender of All Patients 
128,715 Patients are female & 100,759 are male. 

![GenderofAllPatients](https://user-images.githubusercontent.com/115032384/225178555-343cb5ff-5568-42b3-b371-ab510812705b.png)


Gender of Diabetic Patients 
Of the Diabetic patients, 18,345 are female & 16,752 are male.

![GenderofDiabeticPatients](https://user-images.githubusercontent.com/115032384/225178728-a81f8c10-b000-4212-a721-71ba08a18fd1.png)


Age of Diabetic Patients by Gender
Male and female diabetic patients follow the same age pattern. The amount of diabetic patients jumps up around ages 40-45 and peeks at ages 65-69 for males and females.  

![AgeofDiabeticPatientsByGender](https://user-images.githubusercontent.com/115032384/224593941-8385ed89-34e8-42db-92df-ff0d88c15f1a.png)


Diabetic Patients - Smokers and Alcohol Consumption
Among diabetic patients, there are more smokers. The smokers consumed almost three times more alcohol in the last 30 days than non smokers. 

Non Diabetic Patients - Smokers and Alcohol Consumption
Among non diabetic patients, there are less smokers. The smokers consumed almost two times more alcohol in the last 30 days than non smokers. 

![SmokersAlcoholConsumption](https://user-images.githubusercontent.com/115032384/225178930-4b6a13b5-4fdc-4696-9d08-d1117ed6b623.png)

Income 

![Income](https://user-images.githubusercontent.com/115032384/225179717-70abd8e2-6f03-4553-ab40-484341965503.png)


Physical Activity 

![PhysicalActivity](https://user-images.githubusercontent.com/115032384/225179420-8d7370eb-302b-45b9-b77a-b882014d7e45.png)


Fruit & Vegetable Consumption

![FruitVegetableConsumption](https://user-images.githubusercontent.com/115032384/225179305-ca6a55f4-1e96-44cf-8798-fd428a833f7c.png)


Average BMI by Gender 

![AvgBMIbyGender](https://user-images.githubusercontent.com/115032384/225179178-4e2e2de0-7a88-458b-b5d4-d98137af6e07.png)


Average BMI by Age 
BMI - Body Mass Index is a weight-to-height ration used to indicate if a person is over or underweight. To get the BMI, you divide your weight in kilograms by the square of height in meters. BMI = kg/m2
Overall, diabetic patients have a higher BMI then non diabetic patients. 
Among diabetic and non diabetic patients, ages 18-24 & 70-80+ had the lowest BMI and ages 40-49 had the highest BMI. 
Diabetic Patients
The 18-24 & 60-80+ age ranges have a BMI of 28.073-32.667. The 25-59 age range have a BMI of 33.347-35.065. 
Non Diabetic Patients 
The 18-29 & 70-80+ age ranges have a BMI of 25.765-27.704. The 30-69 age range have a BMI of 28.082-29.026. 

![AvgBMIbyAge](https://user-images.githubusercontent.com/115032384/225179065-159c99ee-a765-45ff-bdb1-cf59543d9b4b.png)



[Link to Tableau Story](https://public.tableau.com/views/Diabetes_Analysis_16786693958130/DiabetesAnalysisStory?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Results 

## Summary 
