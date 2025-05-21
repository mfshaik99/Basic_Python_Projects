def tech_quiz():
    questions = {
        "What does CSS stand for?": "b",
        "Which programming language is known as the backbone of iOS app development?": "b",
        "What is the primary function of DNS?": "a",
        "Which of the following is NOT a NoSQL database?": "c",
        "What does API stand for?": "a"
    }

    options = {
        "What does CSS stand for?": [
            "a) Computer Style Sheets",
            "b) Cascading Style Sheets",
            "c) Creative Style System",
            "d) Colorful Style Sheets"
        ],
        "Which programming language is known as the backbone of iOS app development?": [
            "a) Java",
            "b) Swift",
            "c) Kotlin",
            "d) Python"
        ],
        "What is the primary function of DNS?": [
            "a) Translate domain names to IP addresses",
            "b) Encrypt internet traffic",
            "c) Host websites",
            "d) Manage email servers"
        ],
        "Which of the following is NOT a NoSQL database?": [
            "a) MongoDB",
            "b) Cassandra",
            "c) MySQL",
            "d) Redis"
        ],
        "What does API stand for?": [
            "a) Application Programming Interface",
            "b) Applied Programming Internet",
            "c) Advanced Programming Integration",
            "d) Automated Process Interface"
        ]
    }

    score = 0
    total = len(questions)

    print("Welcome to the Tech Quiz!\n")

    for question, correct_answer in questions.items():
        print(question)
        for option in options[question]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{correct_answer}'.\n")

    print(f"Quiz finished! Your score: {score} out of {total}")

tech_quiz()
