# Anemia Sense: Leveraging Machine Learning For Precise Anemia Recognitions

 Author: Bandana Shaw\
 Date: 2024-08-02\
 Version: 1.0\


Project Description:

Anemiasense leverages machine learning algorithms to provide precise recognition and management of anemia, a condition characterized by a deficiency of red blood cells or hemoglobin. Here are three general scenarios illustrating its use case:
Scenario 1: Early Detection and Diagnosis:
Anemiasense utilizes machine learning models trained on vast datasets of blood parameters and patient profiles to detect early signs of anemia. By analyzing key indicators such as hemoglobin levels, red blood cell counts, and other relevant biomarkers, the system can flag potential cases for further investigation by healthcare professionals. Early detection enables timely interventions and treatment plans, improving patient outcomes.
Scenario 2: Personalized Treatment Plans
Machine learning algorithms in Anemiasense can analyze diverse patient data, including genetic factors, lifestyle habits, and medical history, to generate personalized treatment plans. By considering individual variations and responses to different treatments, the system helps healthcare providers tailor interventions for optimal results. This personalized approach enhances the effectiveness of anemia management and reduces the risk of complications.
Scenario 3:Remote Monitoring and Follow-Up
Anemiasense supports remote monitoring of patients with anemia through wearable devices or digital health platforms. Machine learning algorithms continuously analyze real-time data such as hemoglobin levels, activity levels, and medication adherence to provide insights to both patients and healthcare providers. This remote monitoring capability facilitates proactive management, enables timely adjustments to treatment regimens, and reduces the need for frequent in-person visits, particularly beneficial for patients in rural or underserved areas.


The Anemiasense system was completed in the following steps:
 **Data Collection & Preparation**\
Data collection is fundamental to machine learning, providing the raw material for training algorithms and making predictions. This process involves gathering relevant information from various sources such as databases, surveys, sensors, and web scraping. The quality, quantity, and diversity of collected data significantly impact the performance and accuracy of ML models.

Data Collection: There are many popular open sources for collecting the data. Eg: kaggle.com, UCI repository, etc. In this project, we have used .csv data. This data is downloaded from kaggle.com.

Reading the data : Our dataset format is in .csvc. We can read the dataset with the help of pandas. 
In pandas, we have a function called read_csv() to read the dataset. As a parameter, we give the directory of the CSV file.

Data Preparation : Before we can use our data to teach our machine-learning model, we need to clean it up. That means we have to deal with missing information, like when there's no data for some entries. We also have to figure out what to do with categories, like types of stages and outliers, which are really unusual data points. This activity includes the following steps. 
            Handling missing values 
            Handling imbalanced data 
            
To handle imbalanced data we have use undersampling. Undersampling addresses imbalanced data by reducing instances in overrepresented classes, achieving class balance. It mitigates model bias towards majority classes.