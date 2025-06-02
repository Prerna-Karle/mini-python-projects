questions = [
    [
        "Who is known as the father of Artificial Intelligence?", 
        "Alan Turing", "Elon Musk", "Mark Zuckerberg", "Bill Gates", 1
    ],
    [
        "Which language is most commonly used in AI development?", 
        "Python", "Java", "C++", "Ruby", 1
    ],
    [
        "What is the full form of AI?", 
        "Automatic Intelligence", "Advanced Intelligence", "Artificial Intelligence", "Autonomous Intelligence", 3
    ],
    [
        "Which company developed the AI assistant Siri?", 
        "Google", "Apple", "Microsoft", "Amazon", 2
    ],
    [
        "Which algorithm is used in Machine Learning for making predictions?", 
        "Decision Tree", "KNN", "Both", "None", 3
    ],
    [
        "What does NLP stand for in AI?", 
        "Natural Language Processing", "Non Linear Processing", "Neural Logic Programming", "Natural Learning Program", 1
    ],
    [
        "Which AI model is popular for Image Recognition?", 
        "CNN", "RNN", "ANN", "KNN", 1
    ],
    [
        "Who founded OpenAI, the company behind ChatGPT?", 
        "Mark Zuckerberg", "Elon Musk", "Jeff Bezos", "Bill Gates", 2
    ],
    [
        "Which neural network is best suited for sequential data like time series?", 
        "CNN", "RNN", "ANN", "KNN", 2
    ],
    [
        "Which of the following is a popular reinforcement learning algorithm?", 
        "Q-Learning", "Decision Tree", "SVM", "Naive Bayes", 1
    ],
    [
        "Which AI framework is developed by Google?", 
        "TensorFlow", "PyTorch", "Keras", "Theano", 1
    ],
    [
        "What is the primary function of a ReLU activation function?", 
        "Linear Transformation", "Introduce Non-Linearity", "Normalize Data", "Classify Data", 2
    ],
    [
        "Which algorithm is commonly used in clustering problems?", 
        "K-Means", "Logistic Regression", "Decision Tree", "Random Forest", 1
    ],
    [
        "Which AI concept is used for generating images or text?", 
        "GANs", "SVM", "KNN", "CNN", 1
    ],
    [
        "What is the name of the AI model used in autonomous cars?", 
        "CNN", "RNN", "LSTM", "YOLO", 4
    ],
    [
        "Which AI model is known for outperforming humans in games like Go?", 
        "AlphaZero", "GPT-3", "Deep Blue", "Watson", 1
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
money = 0

print("Welcome to Kaun Banega Crorepati")

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]:<20} b. {question[2]:<20}")
    print(f"c. {question[3]:<20} d. {question[4]:<20}")
    reply = int(input("Enter your answer (1-4): "))

    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 16):
            money = 70000000
    else:
        print("Wrong answer!")
        break

print(f"\nYou take home Rs. {money}")
print("Thank you for playing Kaun Banega Crorepati")
