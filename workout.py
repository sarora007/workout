"""program to autogenerate workouts and keep track of progress"""

from random import randint
from time import sleep, strftime
import csv 

date = strftime("%B,%d,%Y")

upper_body = {
	"Chest" : ["Bench Press", "Incline Press", "Flyes", "Cable Crossovers","Bench Press", "Incline Press"],
	"Back" : ["Pull-ups", "Wide-Grip Lat Pulldown", "One-Arm Dumbell Rows", "Seated Cable Rows", "Back Extensions", "Straight-Arm Pulldowns"],
	"Shoulder" : ["Seated Dumbell Press", "Front Raises", "Lateral Raises","Reverse Flyes", "Upright Cable Rows", "Military Press"],
	"Biceps" :["Alternate Dumbell Curls", "Barbell Curls", "Preacher Curls", "Concentration Curls", "Cable Curls", "Hammer Curls"],
	"Triceps" : ["Seated Tricep press", "Skullies", "Triceps Kickbacks", "Tricep Pushdown", "Cable Extension", "Bench Dips"],
	"Abs" : ["Floor Crunches", "Oblique Floor Crunches", "Decline Crunches", "Decline Oblique", "Hanging Knee Raises", "Reverse Crunches", "Cable Crunches", "Cable Oblique Crunches"]
}
lower_body = {
	"Quadriceps" : ["Barbell Squats", "Leg Press", "Leg Extensions"],
	"Hamstrings" : ["Dumbell Lunges", "Straight-leg Deadlifts", "Lying Leg Curls"],
	"Calves" :["Seated Calf Raises", "Standing Heel Raises"],
	"Abs" : ["Floor Crunches", "Oblique Floor Crunches", "Decline Crunches", "Decline Oblique", "Hanging Knee Raises", "Reverse Crunches", "Cable Crunches", "Cable Oblique Crunches"]
}

def welcome():
	print "Welcome back!"
	print "Workout generator is opening"
	print "Today is: " + strftime("%A, %B, %d, %Y")


def start_generator():
	welcome()
	"""Checks if you completed your workout"""
	check = raw_input("Did you complete your workout today (Y/N)? ")
	if check == "Y":
		start = True 
		print "Great. Updating records."
	else:
		print "Complete your workout first. "
		start = False 
	while start:
		user_choice = raw_input("Enter U for Upper body, L for Leg Day, or V to view your workout log: ")
		user_choice = user_choice.upper()
		if user_choice == "U":
			workout_generator(upper_body)			
		elif user_choice =="L":
			workout_generator(lower_body)			
		elif user_choice == "V":
			with open('list1.csv', 'r') as csvfile:
				v = csv.reader(csvfile)
				for row in v:
					print row	
		else:
			print "Invalid choice"	

"""Generate a random upper body workout"""
def workout_generator(list_workouts):
	##generate = randint(0,len())
	i = [date]
	print "Here is your upper body workout today: "
	for area in list_workouts.values():
		generate = randint(0,len(area)-1)
		w = area[generate]
		i.append(w)
		print w
	with open('list1.csv', 'a') as csvfile:
		v = csv.writer(csvfile)
		v.writerow(i)

start_generator()

