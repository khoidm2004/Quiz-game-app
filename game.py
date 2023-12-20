from db_conn import DB_CONN

class GameLogic:
        def __init__(self) -> None:
                self.quizzes = (
        "How do you insert COMMENTS in Python code?",
        "Which one is NOT a legal variable name?",
        "What is the correct syntax to output the type of a variable or object in Python?",
        "Which collection does not allow duplicate members?",
        "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "What are 4 pillars of OOP?",
        "What does the term CSV stand for?",
        "What command is used to DELETE records in database?",
        "Which one is not a constraint in SQL?",
        "What is Tkinter in Python?"
        )
                self.choices = (
        ("A. #This is a comment ","B. //This is a comment// ","C. /This is a comment/ ","D. ?This is a comment? "),#Answer:A
        ("A. my_var","B. Myvar ","C. my-var ","D. _myvar"),#Answer:C
        ("A. print(typeof(x))","B. print(type(x))","C. print(typeOf(x))","D. print(typeOf x)"),#Answer:B
        ("A. SET","B. DICTIONARY","C. LIST","D. TUPLE"),#Answer:A
        ("A. rstrip()","B. trim()","C. len()","D. strip()"),#Answer:D
        ("A. Encapsulation, Encryption, Inheritance, Polymorphism",
         "B. Encapsulation, Abstraction, Inheritance, Polymorphism",#Answer:B
         "C. Packaging, Abstraction, Inheritance, Polymorphism",
         "D. Encapsulation, Abstraction, Concurrency, Polymorphism"
         ),
        ("A. Concatenate String Values","B. Concatenate Separated Values","C. Comma String Values","D. Comma Seperated Values"),#Answer:D
        ("A. TRUNCATE","B. REPLACE","C. DELETE","D. ALTER"),#Answer:C
        ("A. PRIMARY KEY","B. FOREIGN KEY","C. IS NULL","D. NOT NULL"),#Answer:C
        ("A. A module for creating graphical user interfaces (GUIs) in Python",#Answer:A
         "B. A package for creating machine learning models in Python",
         "C. A library for working with network sockets in Python",
         "D. A database management system in Python")
         )
                self.keys = ("A","C","B","A","D","B","D","C","C","A")
                self.guesses = []
                self.score = 0
                self.quiz_num = 0

        def leader_board(self)->None:
                print("LEADERBOARD:")
                rawData = self.get_record()
                for i in rawData:
                        print(f"Username: {i[1]} Score: {i[2]}")

        def get_record(self)-> list:
                cursor = DB_CONN.cursor()
                RECORD_STATEMENT = """SELECT * FROM leaderboard
                ORDER BY score DESC
                LIMIT 5;"""
                cursor.execute(RECORD_STATEMENT)
                records = cursor.fetchall()
                DB_CONN.commit()
                cursor.close()
                return records

        def game_play(self)->None:
                while self.quiz_num < len(self.quizzes):
                        print(self.quizzes[self.quiz_num])
                        for choice in self.choices[self.quiz_num]:
                                print(choice)
                        try:
                                guess = input("Enter your answer (A,B,C,D): ").upper()
                                if guess not in ['A','B','C','D']:
                                        raise ValueError("Unknown option.")
                                self.guesses.append(guess)
                                if guess == self.keys[self.quiz_num]:
                                        self.score+=1
                                        print("CORRECT!")
                                        print()
                                else:
                                        print("INCORRECT!")
                                        print(f"{self.keys[self.quiz_num]} is the correct annswer")
                                        print()
                                self.quiz_num += 1
                        except ValueError:
                                print("Unknow option. Try again!")
                                print()

        def get_result(self)->None:
                if self.score < 6:
                        print(f"Your result is {self.score}/{len(self.quizzes)}")
                        print("You need to practice more")
                elif 6 <= self.score <=8:
                        print(f"Your result is {self.score}/{len(self.quizzes)}")
                        print("You got Python's basic knowledge")
                elif self.score == 9:
                        print(f"Your result is {self.score}/{len(self.quizzes)}")
                        print("Good job")
                elif self.score == 10:
                        print(f"Your result is {self.score}/{len(self.quizzes)}")
                        print("Excellent")

        def insert_keyboard(self)->tuple:
                user_name = input("Enter your name or nickname: ")
                score = self.score
                obj1 = (user_name,score)
                return obj1
        
        def insert_data(self)->None:
                cursor = DB_CONN.cursor()
                INSERT_STATEMENT = ("INSERT INTO leaderboard (user_name,score) VALUES(?,?)")
                obj = self.insert_keyboard()
                cursor.execute(INSERT_STATEMENT,obj)
                DB_CONN.commit()
                cursor.close()
                








