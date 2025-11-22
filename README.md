# AI-Fitness-Assistant
AI-powered fitness and diet recommendation assistant using Python and KMeans clustering.

Overview-
AI Fitness Assistant is a Python-based smart fitness guide that uses user data (weight, height, age, and goals) along with KMeans clustering to provide personalized diet and workout recommendations.
The system calculates BMI, identifies the user’s fitness category, predicts their cluster, and generates customized fitness and nutrition plans.


Features-
- BMI Calculation
- Personalized fitness category
- KMeans-based user clustering
- Goal-specific diet plans (weight loss, muscle gain, maintenance)
- Goal-specific workout plans
- Clean and simple CLI interface
- CSV-based dataset integration


Technologies Used-
- Python
- Pandas
- Scikit-learn (KMeans clustering)
- CSV Data Storage


How to Run the Project-

1. Install required libraries
pip install pandas scikit-learn

2. Run the python program

  1. User enters name, weight, height, and age  
  2. System calculates BMI and categorizes it  
  3. KMeans model assigns user to a cluster based on dataset  
  4. Diet and workout plans are shown based on fitness goal  
  5. A clean “Fitness Report” is printed  


Testing Instructions-
There are no formal tests, but you can check:
- Enter valid numbers for weight/height/age  
- Try all goals: weight_loss, muscle_gain, maintenance  
- Confirm BMI and plan output  

Screenshots-
<img width="1919" height="1017" alt="Screenshot 2025-11-23 015304" src="https://github.com/user-attachments/assets/a917e190-814b-4cf3-a2de-a1730c7a5635" />
<img width="1919" height="1022" alt="Screenshot 2025-11-23 015316" src="https://github.com/user-attachments/assets/0993a963-9b98-458a-9580-d320886a42aa" />
<img width="1919" height="1014" alt="Screenshot 2025-11-23 015420" src="https://github.com/user-attachments/assets/13c65a6d-9de0-49a5-9d1d-8902d69def10" />
<img width="1918" height="919" alt="Screenshot 2025-11-23 015434" src="https://github.com/user-attachments/assets/113669f1-825d-4e0e-a472-324f3cc7c9e6" />

Author-
Aryan Srivastava
25BAI11367
AI Fitness Assistant Project
