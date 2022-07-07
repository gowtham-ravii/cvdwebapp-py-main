# heart-disease-prediction
Cardiovascular diseases (which often leads to heart failures) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of global deaths.
The dataset consists of 12 variables/features, and 1 output variable/target variable. Let us examine the role of each feature in determining if a person is likely to have heart failure or not:

Age: This variable shows the patient’s age
Anemia: is the decrease in red blood cells or hemoglobin
Creatinine_phosphokinase: is the level of creatine kinase in the blood. This enzyme is important for muscle function.
Diabetes: is a chronic disease that causes high blood sugar
Ejection fraction: is the percentage of blood leaving the heart at each contraction
High blood pressure: is blood pressure that is higher than normal
Platelets: are tiny blood cells that help your body form clots to stop bleeding
Serum creatinine: is the level of serum creatinine in the blood
Serum sodium: is the level of serum sodium in the blood
Sex: gender of the patient
Time: This captures the time of the event
Death event: which is the predictor variable.

Step 1: Import Libraries
Step 2: Import the Dataset
Step 3: Data Cleaning and EDA
I use Matplotlib to visualize the distribution of the target variable (Death_event). From the visualization, we can see that a greater percentage of the patients had a failed heart.
Hera are the exploratory analysis:
![image](https://user-images.githubusercontent.com/100552250/177739439-2f277368-bf77-40cc-b9ac-305134cbc921.png)
![image](https://user-images.githubusercontent.com/100552250/177739482-4b72a19d-695a-4308-bfb2-ab96922ec19d.png)
# Min, max and average of the age variable:
Min age:  29
Max age:  77
Average age:  54.43333333333333
![image](https://user-images.githubusercontent.com/100552250/177739680-86bde4c6-c8da-4286-bdf0-3e7c61f1d340.png)
![image](https://user-images.githubusercontent.com/100552250/177739733-93221196-cf8c-4347-968e-03de91033416.png)
![image](https://user-images.githubusercontent.com/100552250/177739754-f075c081-68c4-457b-af1e-0ba0df0be9b4.png)
![image](https://user-images.githubusercontent.com/100552250/177739809-784b185b-6383-4c2f-b6c9-41f8eae22b6a.png)
![image](https://user-images.githubusercontent.com/100552250/177739830-a41fb6f1-8fa8-427a-b799-e72ce0119a08.png)
![image](https://user-images.githubusercontent.com/100552250/177739853-7f1d76d4-f013-4261-8396-1c0c7bccd2d5.png)
![image](https://user-images.githubusercontent.com/100552250/177739885-a3c9e71b-e96b-4cbb-833f-e5bc949215e8.png)
![image](https://user-images.githubusercontent.com/100552250/177739929-40de0793-47bb-4f7d-8642-b9454f4fad64.png)
![image](https://user-images.githubusercontent.com/100552250/177740055-535c60f2-3db9-4cf0-8e40-3d93e5740ba4.png)
![image](https://user-images.githubusercontent.com/100552250/177740089-6a3f27b6-63bc-404d-9c9f-14db974d4da1.png)
![image](https://user-images.githubusercontent.com/100552250/177740131-cb9ef812-79b3-4e02-9ef7-f0ca418313e0.png)
![image](https://user-images.githubusercontent.com/100552250/177740163-ae97b56a-f818-4de4-8768-2ef653b32b08.png)
![image](https://user-images.githubusercontent.com/100552250/177740189-39a3e34b-87d3-4103-b82c-81c55dd90cd8.png)
![image](https://user-images.githubusercontent.com/100552250/177740242-08d3a93f-c2c0-4156-8427-bb2084b8b396.png)
![image](https://user-images.githubusercontent.com/100552250/177740280-0ad2cec1-e7a8-40a3-9198-c75d4fcafb59.png)
![image](https://user-images.githubusercontent.com/100552250/177740332-b1487e87-4a8e-4e8b-96ac-bd95e184836b.png)
![image](https://user-images.githubusercontent.com/100552250/177740389-b4768045-6cad-4b64-9515-30b950a2fc99.png)
Modeling
For the model development part, I will use the following models: i) support vector macine, ii) random forest, iii) Ada Boost, iv) Gradient boosting for evaluating cardiovacular risk prediction using set of predictor variables defined/examined above.

Steps to go:

Prepare data for ML
Train and evaludate model
Examine the important features of the model
Save the model
WE NOW USE MACHINE LEARNING ALGORITHMS AND THE PREDICTIONS FOUND ARE,
SVC

classification_report :
              precision    recall  f1-score   support

           1       0.71      0.90      0.79        30
           2       0.81      0.54      0.65        24

    accuracy                           0.74        54
   macro avg       0.76      0.72      0.72        54
weighted avg       0.76      0.74      0.73        54


confusion_matrix :
[[27  3]
 [11 13]]

-----

RandomForestClassifier

classification_report :
              precision    recall  f1-score   support

           1       0.76      0.73      0.75        30
           2       0.68      0.71      0.69        24

    accuracy                           0.72        54
   macro avg       0.72      0.72      0.72        54
weighted avg       0.72      0.72      0.72        54


confusion_matrix :
[[22  8]
 [ 7 17]]

-----

AdaBoostClassifier

classification_report :
              precision    recall  f1-score   support

           1       0.75      0.80      0.77        30
           2       0.73      0.67      0.70        24

    accuracy                           0.74        54
   macro avg       0.74      0.73      0.73        54
weighted avg       0.74      0.74      0.74        54


confusion_matrix :
[[24  6]
 [ 8 16]]

-----

GradientBoostingClassifier

classification_report :
              precision    recall  f1-score   support

           1       0.79      0.73      0.76        30
           2       0.69      0.75      0.72        24

    accuracy                           0.74        54
   macro avg       0.74      0.74      0.74        54
weighted avg       0.74      0.74      0.74        54


confusion_matrix :
[[22  8]
 [ 6 18]]
PLOTTING FAETURE IMPORTANCE
Feature: age, Score: 0.06003
Feature: sex, Score: 0.01170
Feature: cp, Score: 0.28587
Feature: trestbps, Score: 0.03719
Feature: chol, Score: 0.06027
Feature: fbs, Score: 0.00082
Feature: restecg, Score: 0.00376
Feature: thalach, Score: 0.06526
Feature: exang, Score: 0.02465
Feature: oldpeak, Score: 0.13452
Feature: slope, Score: 0.04946
Feature: ca, Score: 0.17047
Feature: thal, Score: 0.09600
![image](https://user-images.githubusercontent.com/100552250/177740982-dd0e44d7-e2c8-4174-9290-ef15d0657c6a.png)
AND WE WILL HAVE OUR OUTPUT IN THE FORM OF FLASK AND THE SCREENSHOTS OF THE PREDICTED WEBPAGE ARE ATTACHED FOR REFRENCES.
![2022-07-07](https://user-images.githubusercontent.com/100552250/177744616-83ec9f99-1adb-46e1-8c96-115183272894.png)
![2022-07-07 (1)](https://user-images.githubusercontent.com/100552250/177744710-6254bb7a-4970-4450-9ee8-792c5422304a.png)
THANK YOU

