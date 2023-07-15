filename = input("Enter filename: ")
with open(filename, 'r') as file:
    content = file.read()


blocks = content.split('\n\n')  # Split based on double newline
questions = []
formatted_answers = []
answers = []

#for line in blocks:
#    #line = line.strip()  # Remove leading/trailing whitespace
#    if line and line[1] == '.':
#        formatted_answers.append(line)
#    else:
#        formatted_answers[-1] += ' ' + line

#for i in range(0, len(formatted_answers), 1):
#    print(i, ": " +formatted_answers[i])

#for i in formatted_answers:
#    choices = i.split("\n")
#    for x in choices:
#        if x[1] == ".":

#for block in blocks:
#    lines = block.split('\n')
#
#    question = lines[0]  # First line is the question
#    answer_choices = lines[1:-1]  # Remaining lines are answer choices
#
#    questions.append(question)
#    answers.append(answer_choices)

# Format the output

# Print or save the formatted output
#438
#1-196
#file = open("ch2_questions.txt", 'w')



#1. Verify that questions are even and answers are odd
for i in range(0, len(blocks), 2):
    #file.write(blocks[i] + "\n\n")
    questions.append(blocks[i])
    print(i , ": " + blocks[i])

for i in range(1, len(blocks), 2):
    answers.append(blocks[i])
    print(i , ": " + blocks[i])


formattedfile = input("Enter new filename: ")
file = open(formattedfile, "w")
for i in questions:
    file.write(i + "\n\n")

for i in answers:
    file.write(i + "\n\n")


file.close()

#print(blocks[417])