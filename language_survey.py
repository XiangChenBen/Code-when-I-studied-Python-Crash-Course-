from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("You can input q to quit the question")
while True:
    response = input("Please input your response:")
    if response == "q":
        break
    else:
        my_survey.store_response(response)

print("Thank you for your response!")
my_survey.show_responses()
