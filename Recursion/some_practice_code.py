internship_desire = True
while internship_desire:
    print("I need an internship")
    skills = ["Python", "Deep Learning with Pytorch", "Tensorflow", "Transfer Learning", "Time series forecasting", "Natural Language Processing"]
    for skill in skills:
        print(f"An internship will help me improve {skill} skill immensely")
    internship_desire = input("Have you found and internship for me? (Yes/No)").lower() != "yes"