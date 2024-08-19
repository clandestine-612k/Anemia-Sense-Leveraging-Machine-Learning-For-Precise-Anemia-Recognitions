# Anemia Sense: Leveraging Machine Learning For Precise Anemia Recognitions

 Author: Bandana Shaw\
 Date: 2024-08-02\
 Version: 1.0

Anemia is a widespread medical condition affecting millions of individuals globally, characterized by a deficiency of red blood cells or hemoglobin, leading to fatigue, weakness, and a reduced quality of life. Traditional methods for diagnosing and managing anemia often rely on standard blood tests and manual interpretation, which can be time-consuming, prone to errors, and may not provide a comprehensive understanding of the condition's underlying causes.

Problem: Despite the availability of diagnostic tools, accurately identifying the specific type and severity of anemia, predicting its progression, and determining the most effective management strategies remain challenging. This difficulty arises from the complex nature of anemia, which can be caused by various factors, including nutritional deficiencies, chronic diseases, and genetic disorders. Moreover, the variability in patient response to treatment necessitates a more personalized approach to anemia management.

Objective: Anemiasense aims to revolutionize the diagnosis and management of anemia by leveraging advanced machine learning algorithms. The goal is to develop a system that can accurately classify different types of anemia, predict disease progression, and recommend personalized treatment plans based on individual patient data. This approach promises to reduce diagnostic errors, enhance treatment effectiveness, and improve patient outcomes, ultimately addressing the significant healthcare burden posed by anemia.

Project Description:

Anemiasense leverages machine learning algorithms to provide precise recognition and management of anemia, a condition characterized by a deficiency of red blood cells or hemoglobin. Here are three general scenarios illustrating its use case:

Scenario 1: Early Detection and Diagnosis:

Anemiasense utilizes machine learning models trained on vast datasets of blood parameters and patient profiles to detect early signs of anemia. By analyzing key indicators such as hemoglobin levels, red blood cell counts, and other relevant biomarkers, the system can flag potential cases for further investigation by healthcare professionals. Early detection enables timely interventions and treatment plans, improving patient outcomes.

The Anemiasense system was completed in the following steps:

 **Data Collection & Preparation**\
Data collection is fundamental to machine learning, providing the raw material for training algorithms and making predictions. This process involves gathering relevant information from various sources such as databases, surveys, sensors, and web scraping. The quality, quantity, and diversity of collected data significantly impact the performance and accuracy of ML models.

1. Data Collection: There are many popular open sources for collecting the data. Eg: kaggle.com, UCI repository, etc. In this project, we have used .csv data. This data is downloaded from kaggle.com.

2. Reading the data : Our dataset format is in .csvc. We can read the dataset with the help of pandas. 
In pandas, we have a function called read_csv() to read the dataset. As a parameter, we give the directory of the CSV file.

3. Data Preparation : Before we can use our data to teach our machine-learning model, we need to clean it up. That means we have to deal with missing information, like when there's no data for some entries. We also have to figure out what to do with categories, like types of stages and outliers, which are really unusual data points. This activity includes the following steps. 
            Handling missing values 
            Handling imbalanced data 
            
To handle imbalanced data we have use undersampling. Undersampling addresses imbalanced data by reducing instances in overrepresented classes, achieving class balance. It mitigates model bias towards majority classes.

**Exploratory Data Analysis**\
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

**Model Building**\
Model building is the process of creating a machine learning model that can make predictions or classify data.
1. Training the model in multiple algorithms
Now our data is cleaned and it’s time to build the model. We can train our data on different algorithms. For this project, we are applying six Regression algorithms. The best model is saved based on its performance.

        1.1 Logistic Regression Model 
A variable named logistic_regression is created and train and test data are passed as the parameters. Inside the function, the Linear Regression algorithm is initialized and training data is passed to the model. fit() function. Test data is predicted with. predict() function and save d in a new variable. For evaluating the model, an accuracy score and classification report are used. 

        1.2 Random forest model
A variable named random_forest is created and train and test data are passed as the parameters. Inside the function, the RandomForestClassifier algorithm is initialized and training data is passed to the model with the .fit() function. Test data is predicted with the .predict() function and saved in a new variable. For evaluating the model, an accuracy score and classification report are used. 

        1.3 Decision Tree Model 
A function named decision_tree_model is created and train and test data are passed as the parameters. Inside the function, the Decision Classifier algorithm is initialized and training data is passed to the model the with .fit() function. Test data is predicted with the .predict() function and saved in a new variable. For even altering the model, accuracy score and classification report are used. 

        1.4 Gaussian Navies Bayes 
A variable named NB is created and train and test data are passed as the parameters. Inside the function, the Gaussian Navies Bayes algorithm is initialized and training data is passed to the model with the .fit() function. Test data is predicted with the .predict() function and saved in a new variable. For evaluating the model, an accuracy score and classification report are used. 

        1.5 Support Vector Machine Model
A function named SVC is created and train and test data are passed as the parameters. Inside the function, the Support vector machine algorithm is initialized and training data is passed to the model with the .fit() function. Test data is predicted with the .predict() function and saved in a new variable. For evaluating the model, an accuracy score and classification report are used.

        1.6 Gradient Boosting Classifier 
A function named GBC is created and train and test data are passed as the parameters. Inside the function, the Gradient Boosting algorithm is initialized and training data is passed to the model with the .fit() function. Test data is predicted with the .predict() function and saved in a new variable. For evaluating the model, an accuracy score and classification report are used. 

**Testing the model**\
Here we have tested with the Lasso model algorithm. You can test with all algorithms. With the help of the predict() function.

**Testing model with multiple evaluation metrics**\
Multiple evaluation metrics means evaluating the model's performance on a test set using different performance measures. This can provide a more comprehensive understanding of the model's strengths and weaknesses. We are using evaluation metrics for regression tasks including Accuracy scores and classification report.

Comparing the models
| Index | Model                     | Score    |   
|-------|---------------------------|----------|
| 1     | Logistic Regression       | 0.991935 |   
| 2     | Decision Tree Classifier  | 1.000000 |   
| 3     | Random Forest Classifier  | 1.000000 |   
| 4     | Gaussian Naive Bayes      | 0.979839 |   
| 5     | Support Vector Classifier | 0.939516 |   
| 6     | Gradient Boost Classifier | 1.000000 |  

We can see the accuracy of all models and based on accuracy and Test Accuracy Decision Tree, Random forest, and Gradient Boosting classifier model have highest accuracy.
 
**Saving the best model**\ 

After comparing its performance using different evaluation metrics means selecting the model with the highest performance and saving its weights and configuration. This is useful in avoiding the need to retrain the model every time it is needed and also to be able to use it in the future. Here, we have saved the **Gradient Boost Classifier model**. Later in my project I found that the model I choose was overfitting so I choose another model **Support Vector Classifier** whose accuracy score was 0.939516.

**Integrating with Web framework**\
 A web application is built that is integrated to the model we built. A UI is provided for the users where she/he has to enter the values for predictions. The enter values are given to the saved model and prediction is showcased on the UI. 

1. Building Html Pages

For this project we created two HTML files namely

        Index.html
        predict.html

and saved them in the templates folder.

2. Building python code

We created a python file named app.py and saved it in the root directory.

3. Run the web application

We run the web application using the command python app.py.

![Home Page](static/home.png?raw=true "Home Page")
![About Page](static/about.png?raw=true "About Page")
![Contacts Page](static/contacts.png?raw=true "Contacts Page")
![Prediction Page](static/prediction.png?raw=true "Prediction Page")


The link of Badges earned during this course:-
1. Inspect Rich Documents with Gemini Multimodality and Multimodal RAG Skill Badge - https://www.credly.com/badges/36eb6c27-31c1-4f75-9c0b-ae18ba37b453/public_url
2. Prompt Design in Vertex AI Skill Badge - https://www.credly.com/badges/4caddb0b-c542-4b16-b235-59a755e3a079/public_url
3. Develop GenAI Apps with Gemini and Streamlit Skill Badge - https://www.credly.com/badges/d96ebd8e-26e6-4c56-aa62-36e8eb3716a2/public_url 
