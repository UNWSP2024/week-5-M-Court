#this program displays a math quiz problem

#determine numbers for problem
number1 = 100
number2 = 200

#function for adding the numbers
def add(number1, number2):
	correct_sum = number1 + number2
	return correct_sum

#call correct answer
correct_sum = add(number1, number2) 

#print problem
print(f"  {number1} \n+ {number2} \n -----")

#get user answer
user_answer = int(input("  "))

#define response
def response_to_answer(user_answer, correct_sum):
	if user_answer == correct_sum:
		print(f"Congradulations! {correct_sum} is correct!")
	if user_answer != correct_sum:
		print(f"Sorry. {user_answer} is incorrect.")

#call response
response = response_to_answer(user_answer, correct_sum)
