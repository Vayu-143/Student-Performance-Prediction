import os

print("🔹 Step 1: Generating Data...")
os.system("python src/data_generator.py")

print("\n🔹 Step 2: Training Model...")
os.system("python src/train.py")

print("\n🔹 Step 3: Prediction...")
os.system("python src/predict.py")

print("\n🔹 Step 4: Visualization...")
os.system("python src/visualize.py")

print("\n✅ PROJECT COMPLETED SUCCESSFULLY!")