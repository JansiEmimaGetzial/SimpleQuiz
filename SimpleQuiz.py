def new_game():
    guesses = []
    correct_guesses = 0
    question_no = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in choices[question_no-1]:
            print(i)
        guess = input("Enter Your Answer (A , B , C , D ): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_no = question_no + 1

    display_score(correct_guesses,guesses)


def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
def display_score(correct_guesses,guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")

    print("Answers :", end= " ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses :", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score= int((correct_guesses/len(questions))*100)
    print("Your Score is :" +str(score) +"%")

    if score >= 40:
        print("You passed the Quiz")
    else:
        print("You Failed the Quiz")

    


def play_again():
    response = input("Do you want to play again? (Yes / No) :")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "1.Who was the father of computer?" : "A",
    "2.Which electronics component is used in first generation computers?" : "C",
    "3.Which part of the computer is considered as Brain of the Computer?" : "B",
    "4.Joystick is ?" : "A",
    "5.What is the full form of CPU?" : "D",
    "6.What is the full form of CRT?" : "D",
    "7.Daisy Wheel term belongs to?" : "A",
    "8.Which can be the input and output devices both?" : "B",
    "9.One Nibble has?" : "B",
    "10.What does an Operating System do?" : "D",
    "11.Highest capacity of the storage are" : "B",
    "12.Which key of the keyboard is mainly used to cancel the program?" : "D",
    "13.Computer Moniter is also known as?" : "C",
    "14.Which among the following cities produces highest e-waste in India?" : "D",
    "15.Which among the following period is known as the era of second generation computer?" : "A",
    "16.If you need to cut the contents of MS Word, which command will you give?" : "A",
    "17.Who among the following has designed the JavaScript programing language?" : "C",
    "18.Magnetic disks are coated with?" : "B",
    "19.USB is a _______ storage device." : "B",
    "20.An IP address is a ______ Number." : "A",
    "21.The .com used frequently in website url can be expressed aS ____" : "C",
    "22.The term used to refer to horizontal page orientation?" : "D",
    "23.What are symbol used to identify items in a list?" : "C",
    "24.The blinking symbol on the computer screen is called the _____" : "A",
    "25.Data going into the computer is called?" : "B"


}

choices = [["A. Charles Babbage","B. Dennis Ritchie","C. Charlie Babbage","D. Ken Thompson"],
          ["A. Transistors", "B. ULSI Chips", "C. Vacuum Tubes","D. LSI Chips"],
          ["A. Random Access Memory","B. Central Processing Unit","C. Read Only Memory","D. Hard Disk"],
          ["A. An input device","B. An output device","C. An online game","D. A memory unit"],
          ["A. Central Process Unit","B. Central Progressive Unit","C. Central Programming Unit","D. Central Processing Unit"],
          ["A. Central Read Technique","B. Common Reading Technique","C. Cathode Rays Technique","D. Cathode Rays Tube"],
          ["A. Printer","B. Plotter","C. Monitor","D. Scanner"],
          ["A. Scanner","B. Touch screen monitor","C. Speaker","D. Digitizer"],
          ["A. 2 Bits","B. 4 Bits","C. 8 Bits","D. 16 Bits"],
          ["A. Memory Management","B. File Management","C. Application Management","D. All of the above"],
          ["A. Terabyte", "B. Yottabyte", "C. Zettabyte","D. Exabyte"],
          ["A. Del Key","B. Enter Key","C. Ins Key","D. Esc Key"],
          ["A. DVU","B. UVD","C. VDU","D. CCTV"],
          ["A. Delhi","B. Bengaluru","C. Chennai","D. Mumbai"],
          ["A. 1982 onwards","B. 1971 to 1980","C. 1976 to 1985","D. 1990 to 2000 "],
          ["A. Ctrl + X","B. Ctrl + C","C. Ctrl + V","D. Ctrl + Z"],
          ["A. Rasmus Lerdorf","B. Guido van Rossum","C. Brendan Eich","D. James Gosling"],
          ["A. Magnesium oxide","B. Iron oxide","C. Sulphur dioxide","D. Nitric oxide"],
          ["A. Primary","B. Secondary","C. Auxiliary","D. Additional"],
          ["A. 32-bit","B. 16-bit","C. 8-bit","D. 64-bit"],
          ["A. Corporation","B. Cooperative","C. Commercial","D. Cordial"],
          ["A. Portrait","B. Alignment","C. Table","D. Landscape"],
          ["A. Icons","B. Markers","C. Bullets","D. Graphics"],
          ["A. Cursor","B. Mouse","C. Logo","D. Hand"],
          ["A. Algorithm","B. Input","C. Output","D. Calculations"]




          ]
          
        


print("Welcome to my Simple Computer Quiz!")

play=input("Do you want to start the Quiz? (Yes/No) :")
play = play.upper()

if play == "NO":
    print("Hope to see you another time! ")
    quit()

if play == "YES":
    print("Okay lets go!")
    new_game()

while play_again():
    new_game()




print("Thanks for attending the Quiz! Byeee!")
