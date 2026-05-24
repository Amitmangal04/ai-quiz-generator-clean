answers = {

    "What is a noun?":
    "A noun is a naming word.",

    "What is an adjective?":
    "An adjective describes a noun.",

    "Write two naming words.":
    "Boy, Girl",

    "Make a sentence using the word 'school'.":
    "I go to school every day.",

    "What is the opposite of 'happy'?":
    "Sad"

}


def create_heading(title, output_file):

    output_file.write(title + " WORKSHEET\n\n")


def process_questions(input_file, output_file):

    question_number = 1

    for line in input_file:

        text = "Q" + str(question_number) + ". " + line

        print(text)

        question = line.strip()

        if question in answers:

            print("Ans:", answers[question])

            output_file.write("Ans: " + answers[question] + "\n\n")

        output_file.write(text + "\n")

        question_number = question_number + 1


title = input("Enter Worksheet Title: ")

output_name = input("Enter Output File Name: ")


input_file = open("questions.txt", "r")

output_file = open(output_name + ".txt", "w")


create_heading(title, output_file)

process_questions(input_file, output_file)


input_file.close()

output_file.close()

print("Worksheet Saved Successfully")