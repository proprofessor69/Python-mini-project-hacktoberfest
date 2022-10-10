import os
from os import environ
import telebot
import requests
import json
import csv

NUTRITIONIX_API_KEY = environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = environ.get('NUTRITIONIX_APP_ID')
HTTP_API = environ.get('http_api')


headers = {'Content-Type': 'application/json',
           'x-app-id': NUTRITIONIX_APP_ID, 'x-app-key': NUTRITIONIX_API_KEY}
user = {"first_name": None, "gender": None,
        "weight_kg": None, "height_cm": None, "birth_year": None}
bot = telebot.TeleBot(HTTP_API)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning, nutrition_csv, exercise_csv,nutrition_writer, exercise_writer
    botRunning = True
    nutrition_csv = open("nutrition.csv", "w")
    exercise_csv = open("exercise.csv", "w")
    nutrition_writer = csv.writer(nutrition_csv)
    exercise_writer = csv.writer(exercise_csv)
    nutrition_writer.writerow(["Food-Name","Quantity","Calories","Fat","Carbohydrates","Protien"])
    exercise_writer.writerow(["Exercise","Duration","Calories-Burned"]) 
    
    bot.reply_to(
        message, 'Hello! I am TeleFit. Use me to monitor your health'+'\N{grinning face with smiling eyes}'+'\nYou can use the command \"/help\" to know more about me.')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nStay Healthy'+'\N{flexed biceps}')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/nutrition Units Quantity-Type Food-Name\" command to get the nutrients of a particular food. For eg: \"/nutrition 1 piece chapati\"\n\n2.1 For using the bot to get details about an exercise you need to first set the user data using the command \"/user Name, Gender, Weight(in Kg), Height (in cm), Age\". For eg: \"/user Akshat, Male, 70, 6, 19\n\n2.2 Then you can use the command \"/execise Duration-amount Duration-unit Exercise-name\" to get data about an exercise. For eg: \"/exercise 40 minutes push-ups\"\n\n3.0. You can use the command \"/reports Report-name\" to get the reports in CSV Format. For eg: \"/reports nutrition\" to get nutrition report and \"/reports exercise\" to get exercise reports or use the command \"/reports nutrition, exercise\" to get both nutrition and exercise reports\n\n4.0. You can use the command \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['user'])
def setUser(message):
    global user
    usr_input = message.text[6:]
    usr_data = usr_input.split(", ")

    user["first_name"] = usr_data[0]
    user["birth_year"] = int(usr_data[4])
    user["height_cm"] = int(usr_data[3])
    user["weight_kg"] = int(usr_data[2])
    user["gender"] = usr_data[1]

    result = requests.put(
        "https://trackapi.nutritionix.com/v2/me/preferences", json=user)
    bot.reply_to(message, 'User set!')
    name = user["first_name"]
    gender = user["gender"]
    height = user["height_cm"]
    weight = user["weight_kg"]
    age = user["birth_year"]

    reply = f'Name: {name} \nAge : {age} \nHeight: {height} \nWeight: {weight} \nGender: {gender}'
    bot.send_message(message.chat.id, reply)


@bot.message_handler(func=lambda message: botRunning, commands=['nutrition'])
def getNutrition(message):
    bot.reply_to(message, 'Getting nutrition info...')
    q = (message.text)[11:]
    query = {
        "query": q
    }
    result = requests.post(
        "https://trackapi.nutritionix.com/v2/natural/nutrients", headers=headers, json=query)
    data = json.loads(result.text)
    name = data["foods"][0]["food_name"]
    calories = data["foods"][0]["nf_calories"]
    quantity = data["foods"][0]["serving_qty"]
    fat = data["foods"][0]["nf_total_fat"]
    carbohydrates =  data["foods"][0]["nf_total_carbohydrate"]
    protein = data["foods"][0]["nf_protein"]
    bot.send_message(message.chat.id, f"Food Name: {name}\nQuantity: {quantity} \nCalories: {calories} \nFat: {fat} \nCarbohydrates: {carbohydrates} \nProtiens: {protein}") 
    nutrition_writer.writerow([name,quantity,calories,fat,carbohydrates,protein])


@bot.message_handler(func=lambda message: botRunning, commands=['exercise'])
def getCaloriesBurn(message):
    bot.reply_to(message, 'Estimating calories burned...')
    query = (message.text)[10:]
    result = requests.post(
        "https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json={"query": query})
    data = json.loads(result.text)
    exercise_name = data["exercises"][0]["name"]
    duration = data["exercises"][0]["duration_min"]
    calories = data["exercises"][0]["nf_calories"]
    reply = f"Exercise Name : {exercise_name} \nDuration : {duration} minutes \nCalories Burned : {calories}"
    bot.send_message(message.chat.id,reply)
    exercise_writer.writerow([exercise_name,duration,calories])



@bot.message_handler(func=lambda message: botRunning, commands=['reports'])
def getCaloriesBurn(message):
    bot.reply_to(message, 'Generating report...')
    query = (message.text)[9:]
    if query == "nutrition":
        nutrition_csv.close()
        f = open("nutrition.csv","rb")
        bot.send_document(message.chat.id,f)
    elif query == "exercise":
        exercise_csv.close()
        f = open("exercise.csv","rb")
        bot.send_document(message.chat.id,f)
    else:
        bot.send_message(message.chat.id,"Please select a valid report")



@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')


bot.infinity_polling()
