internship_desire = True
while internship_desire:
    print("I need an internship")
    skills = ["Python, DeepLearning w/Pytorch, TensorFlow, Keras, Gen AI"]
    for skill in skills:
        print(f"An internship will help me enhance my {skill} abilities.")
    internship_desire = input("Have you found an internship for me? (yes/no) ").lower() != "yes"