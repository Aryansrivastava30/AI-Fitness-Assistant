import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("fitness_data.csv")

kmeans = KMeans(n_clusters=3, random_state=0)
df["cluster"] = kmeans.fit_predict(df[["weight", "height"]])

print("=== AI Fitness Assistant ===\n")
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))
age = int(input("Enter your age: "))
goal = input("Enter your fitness goal (weight_loss/muscle_gain/general): ")


bmi = round(weight / (height ** 2), 1)


user_cluster = kmeans.predict([[weight, height]])[0]

print("\n===== Your Fitness Report =====")
print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"Age: {age}")
print(f"Goal: {goal}")
print(f"BMI: {bmi}")
print(f"Cluster Group: {user_cluster}")

if user_cluster == 0:
    print("\n You are in Cluster 0 (Balanced fitness level).")
    print("Recommended Plan: Moderate strength + moderate cardio.")
elif user_cluster == 1:
    print("\n You are in Cluster 1 (Higher weight group).")
    print("Recommended Plan: High cardio + calorie deficit diet.")
else:
    print("\n You are in Cluster 2 (Lean build group).")
    print("Recommended Plan: Strength training + protein-rich diet.")

print("\n===== Diet Suggestion =====")
if goal == "weight_loss":
    print("• Calorie deficit diet\n• High protein\n• Low carb\n• Include salads & fruits")
elif goal == "muscle_gain":
    print("• Protein-rich diet\n• Eggs, chicken, paneer\n• Calorie surplus")
else:
    print("• Balanced meals\n• 40% carbs, 30% protein, 30% fats")

print("\n===== Workout Suggestion =====")
if goal == "weight_loss":
    print("• 30 min running\n• HIIT 4x/week\n• Core training")
elif goal == "muscle_gain":
    print("• Push Pull Legs split\n• Progressive overload\n• Heavy lifting")
else:
    print("• Mix of cardio and weights\n• Yoga & flexibility sessions")

print("\n=== End of Report ===")









