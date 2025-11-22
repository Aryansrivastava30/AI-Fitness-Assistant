1. Problem Statement
Many people struggle to choose the right diet and workout plan because they lack personalized guidance. Fitness apps often provide generic suggestions which may not suit individual body types.  
This project solves this problem by creating an AI-powered fitness assistant that generates personalized plans using user data and machine learning (KMeans clustering).

 
 2. Scope of the Project
The scope of this project includes:
- Collecting basic user data (age, weight, height, fitness goal)
- Calculating BMI and analyzing body type
- Using KMeans clustering on existing fitness dataset to categorize users
- Recommending personalized diet and workout plans based on cluster
- Displaying a fitness summary report in the terminal

Out of scope:
- Mobile app or website
- Real-time calorie tracking
- Integration with wearable devices


3. Target Users
This project is designed for:
- Beginners starting their fitness journey  
- Individuals seeking personalized fitness recommendations  
- People who want quick guidance without hiring a trainer  
- Students learning AI/ML concepts through real-world datasets  


4. High-Level Features
The project includes the following major features:

User Data Input Module
Takes user details (name, weight, height, age, goal)  
Validates inputs  
Calculates BMI  

Machine Learning Module (KMeans Clustering)
Loads CSV fitness dataset  
Clusters users based on weight, height, and age  
Predicts the cluster of the new user  

Recommendation Engine
Based on cluster + goal, generates:  
- Customized *diet plan*  
- Personalized *workout plan*  
- BMI category information  

Fitness Summary Report
Prints the final report including:  
- User details  
- BMI information  
- Assigned cluster  
- Diet plan  
- Workout plan  
