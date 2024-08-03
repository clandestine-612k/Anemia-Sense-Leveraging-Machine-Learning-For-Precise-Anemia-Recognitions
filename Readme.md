# Anemia Sense: Leveraging Machine Learning For Precise Anemia Recognitions

 Author: Bandana Shaw\
 Date: 2024-08-02\
 Version: 1.0


Project Description:

Anemiasense leverages machine learning algorithms to provide precise recognition and management of anemia, a condition characterized by a deficiency of red blood cells or hemoglobin. Here are three general scenarios illustrating its use case:
Scenario 1: Early Detection and Diagnosis:
Anemiasense utilizes machine learning models trained on vast datasets of blood parameters and patient profiles to detect early signs of anemia. By analyzing key indicators such as hemoglobin levels, red blood cell counts, and other relevant biomarkers, the system can flag potential cases for further investigation by healthcare professionals. Early detection enables timely interventions and treatment plans, improving patient outcomes.
Scenario 2: Personalized Treatment Plans
Machine learning algorithms in Anemiasense can analyze diverse patient data, including genetic factors, lifestyle habits, and medical history, to generate personalized treatment plans. By considering individual variations and responses to different treatments, the system helps healthcare providers tailor interventions for optimal results. This personalized approach enhances the effectiveness of anemia management and reduces the risk of complications.
Scenario 3:Remote Monitoring and Follow-Up
Anemiasense supports remote monitoring of patients with anemia through wearable devices or digital health platforms. Machine learning algorithms continuously analyze real-time data such as hemoglobin levels, activity levels, and medication adherence to provide insights to both patients and healthcare providers. This remote monitoring capability facilitates proactive management, enables timely adjustments to treatment regimens, and reduces the need for frequent in-person visits, particularly beneficial for patients in rural or underserved areas.


The Anemiasense system was completed in the following steps:\

 **Data Collection & Preparation**\
Data collection is fundamental to machine learning, providing the raw material for training algorithms and making predictions. This process involves gathering relevant information from various sources such as databases, surveys, sensors, and web scraping. The quality, quantity, and diversity of collected data significantly impact the performance and accuracy of ML models.

1. Data Collection: There are many popular open sources for collecting the data. Eg: kaggle.com, UCI repository, etc. In this project, we have used .csv data. This data is downloaded from kaggle.com.

2. Reading the data : Our dataset format is in .csvc. We can read the dataset with the help of pandas. 
In pandas, we have a function called read_csv() to read the dataset. As a parameter, we give the directory of the CSV file.

3. Data Preparation : Before we can use our data to teach our machine-learning model, we need to clean it up. That means we have to deal with missing information, like when there's no data for some entries. We also have to figure out what to do with categories, like types of stages and outliers, which are really unusual data points. This activity includes the following steps. 
            Handling missing values 
            Handling imbalanced data 
            
To handle imbalanced data we have use undersampling. Undersampling addresses imbalanced data by reducing instances in overrepresented classes, achieving class balance. It mitigates model bias towards majority classes.

**Exploratory Data Analysis**
Exploratory data analysis (EDA) is a crucial step in understanding the characteristics of the data.

1. Descriptive Statistical : Descriptive analysis is to study the basic features of data with the statistical process. Here pandas have a worthy function called describe. With this described function we can understand the unique, top and frequent values of categorical features. And we can find mean, std, min, max, and percentile values of continuous features.

2. Visual analysis : Visual analysis is the process of using visual representations, such as charts, plots, and graphs, to explore and understand data. It is a way to quickly identify patterns, trends, and outliers in the data, which can help to gain insights and make informed decisions.
            Univariate analysis
            Bivariate analysis
            Multivariate analysis 


Univariate analysis - In simple words, univariate analysis is understanding the data with a single feature.
Bivariate analysis - To find the relation between two features we use bivariate analysis. 
Multivariate analysis - multivariate analysis is to find the relation between multiple features.

3. Splitting data into train and test : The train-test split is used to estimate the performance of machine learning algorithms that are applicable for prediction-based Algorithms/Applications. This method is a fast and easy procedure to perform such that we can compare our own machine learning model results to machine results. By default, the Test set is split into 30 % of actual data and the training set is split into 70% of the actual data.For splitting training and testing data we are using the train_test_split() function from sklearn. As parameters, we are passing x, y, test_size, random_state.

 