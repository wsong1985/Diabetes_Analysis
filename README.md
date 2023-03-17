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

Total Number of Patients

![NumberofPatients](https://user-images.githubusercontent.com/115032384/224593519-e49babfe-c817-4113-b8a0-4088b1fa34e8.png)


Diabetic to Non-Diabetic Patients

![DiabetictoNonDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773453-4dbb5714-a1dc-473e-be0f-ae13e31208d6.png)


Gender of All Patients 

![GenderofAllPatients](https://user-images.githubusercontent.com/115032384/225773817-7ea078ae-ed36-4803-9fd3-e36e00152e58.png)


Gender of Diabetic Patients 

![GenderofDiabeticPatients](https://user-images.githubusercontent.com/115032384/225773833-31e06d92-a619-4618-a9ee-ad6eafb8d081.png)


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

## Summary 
