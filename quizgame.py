from pyscript import window, document
import asyncio
mine = document.getElementById("mine")
count = 0
body = document.body
plant = document.getElementById("plants")
water_dispenser = document.querySelector(".gray-block")
async def quiz():
    await asyncio.sleep(300)
    mine.style.display("none")
    body.style.backgroundImage = "none"
    await asyncio.sleep(0.1)
    plant.style.display = "flex"
    water_dispenser.style.display = "flex"
    global count
    q_one = window.prompt("Is quartz on Mars? (True or False):")
    if q_one == "True":
        count = count + 1    
    q_two = window.prompt("Are Molecules something you can use to build? (True or False):")
    if q_two == "False":
        count = count + 1
    q_three = window.prompt("Can rockets be 100 pounds? (True or False):")
    if q_three == "False":
        count = count + 1
    q_four = window.prompt("Do other planets have Regolith that aren't Mars or the Moon? (True or False)")
    if q_four == "True":
        count = count + 1
    q_five = window.prompt("Do rockets need boosters? (True or False:")
    if q_five == "True":
        count = count + 1
    percentage = count * 20
    print ("you got " + str(percentage) + " percent [%] correct")

