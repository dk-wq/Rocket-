import asyncio
import random
from pyscript import document, when, window
# AI assisted Debugging
person = document.getElementById("person")
message_box = document.getElementById("game-message")
stats_box = document.getElementById("stats")
plant = document.querySelector("#plants .leaves")
water_dispenser = document.querySelector(".gray-block")
body = document.body
mine = document.getElementById("mine")

food = 10
water_level = 10
plant_health = 10
count = 0
game_over = False

message_box.innerText = (
    "You have taken off into deep space, but you have unfortunately run out of fuel for your rocket!\n"
    "It is now your job to live on the rocket and maintain it until help comes!\n\n"
    "You can dispense water at the water dispenser and water your plant to get more food!\n"
    "Click Collect Materials to fix your rocket!\n\n"
    "Be careful: your water, food, and plant health go down every 60 seconds!"
)


async def run_quiz(overlay):
    global count
    count = 0
    message_box.innerText = "IT'S TIME FOR A QUIZ!"
    # Short pause so the Game Over / Victory overlay renders before prompts appear
    await asyncio.sleep(0.3)

    q_one = window.prompt("Is quartz on Mars? (True or False):")
    if q_one and q_one.strip().capitalize() == "True":
        count += 1

    q_two = window.prompt("Are Molecules something you can use to build? (True or False):")
    if q_two and q_two.strip().capitalize() == "False":
        count += 1

    q_three = window.prompt("Can rockets be 100 pounds? (True or False):")
    if q_three and q_three.strip().capitalize() == "False":
        count += 1

    q_four = window.prompt("Do other planets have Regolith that aren't Mars or the Moon? (True or False):")
    if q_four and q_four.strip().capitalize() == "True":
        count += 1

    q_five = window.prompt("Do rockets need boosters? (True or False):")
    if q_five and q_five.strip().capitalize() == "True":
        count += 1

    percentage = count * 20
    score_text = f"You scored {percentage} percent!"
    message_box.innerText = score_text

    score_el = overlay.querySelector("#quiz-score")
    if score_el:
        score_el.innerText = score_text


def trigger_game_over(reason):
    global game_over
    if game_over:
        return
    game_over = True
    message_box.innerText = f"GAME OVER: {reason}"

    overlay = document.createElement("div")
    overlay.style.position = "fixed"
    overlay.style.top = "0"
    overlay.style.left = "0"
    overlay.style.width = "100vw"
    overlay.style.height = "100vh"
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.65)"
    overlay.style.color = "white"
    overlay.style.display = "flex"
    overlay.style.flexDirection = "column"
    overlay.style.justifyContent = "center"
    overlay.style.alignItems = "center"
    overlay.style.fontSize = "2rem"
    overlay.style.textAlign = "center"
    overlay.style.zIndex = "9999"
    overlay.innerHTML = (
        f"<div>"
        f"<h1>GAME OVER</h1>"
        f"<p>{reason}</p>"
        f"<p id='quiz-score' style='font-size:1.5rem; color:#ffd700;'></p>"
        f"<p style='font-size:1rem;'>Refresh the page to play again.</p>"
        f"</div>"
    )
    document.body.appendChild(overlay)
    asyncio.create_task(run_quiz(overlay))


def trigger_victory(reason="You fixed your rocket and survived until help arrived!"):
    global game_over
    if game_over:
        return
    game_over = True
    message_box.innerText = f"VICTORY: {reason}"

    overlay = document.createElement("div")
    overlay.style.position = "fixed"
    overlay.style.top = "0"
    overlay.style.left = "0"
    overlay.style.width = "100vw"
    overlay.style.height = "100vh"
    overlay.style.backgroundColor = "rgba(0, 80, 30, 0.75)"
    overlay.style.color = "white"
    overlay.style.display = "flex"
    overlay.style.flexDirection = "column"
    overlay.style.justifyContent = "center"
    overlay.style.alignItems = "center"
    overlay.style.fontSize = "2rem"
    overlay.style.textAlign = "center"
    overlay.style.zIndex = "9999"
    overlay.innerHTML = (
        f"<div>"
        f"<h1>VICTORY!</h1>"
        f"<p>{reason}</p>"
        f"<p id='quiz-score' style='font-size:1.5rem; color:#ffd700;'></p>"
        f"<p style='font-size:1rem;'>Refresh the page to play again.</p>"
        f"</div>"
    )
    document.body.appendChild(overlay)
    asyncio.create_task(run_quiz(overlay))


def update_stats():
    stats_box.innerText = (
        f"Food: {food} | Water: {water_level} | Plant Health: {plant_health}"
    )

    if not game_over:
        if food <= 0:
            trigger_game_over("Your food source ran out!")
        elif water_level <= 0:
            trigger_game_over("Your water source ran out!")
        else:
            if plant_health == 0:
                plant.style.backgroundColor = "#b5a788"
                message_box.innerText = "Oh no your plant died! Your plant cannot be revived..."
            elif food < 2:
                message_box.innerText = "WARNING: You are low on food! Complete more tasks!"


@when("click", "#gwater_btn")
async def getmorewater():
    if game_over:
        return
    global water_level
    mine.style.display = "none"
    body.style.backgroundImage = "none"
    await asyncio.sleep(0.1)
    plant.style.display = "flex"
    water_dispenser.style.display = "flex"
    original_pos = person.style.left
    person.style.left = "3px"
    await asyncio.sleep(0.6)
    if game_over:
        return
    getwater = window.confirm("Would you like to dispense some water?")
    if getwater:
        message_box.innerText = "Ok! Water dispensed!"
        water_level += 1
        update_stats()
    else:
        message_box.innerText = "Cancelled water refill."
    await asyncio.sleep(0.6)
    if not game_over:
        person.style.left = original_pos


@when("click", "#water-btn")
async def water_plants():
    if game_over:
        return
    mine.style.display = "none"
    global water_level, plant_health, food
    body.style.backgroundImage = "none"
    await asyncio.sleep(0.1)
    plant.style.display = "flex"
    water_dispenser.style.display = "flex"
    person.style.left = "1100px"
    await asyncio.sleep(0.6)
    if game_over:
        return
    if plant_health == 0:
        message_box.innerText = "The plant is dead and cannot be watered!"
    elif water_level > 0:
        water_level -= 1
        plant_health += 2
        food += 1
        message_box.innerText = "You watered the plants!"
    else:
        message_box.innerText = "No water left! Go to the water dispenser."
    update_stats()
    await asyncio.sleep(0.6)
    if not game_over:
        person.style.left = "500px"


async def material_reduction():
    global food, water_level, plant_health
    minutes_passed = 0
    while not game_over:
        await asyncio.sleep(60)
        if game_over:
            break
        minutes_passed += 1

        if minutes_passed == 2:
            message_box.innerText = (
                "Oh NO your food source has depleted and so "
                "has your water supply because your crew member "
                "had a huge lunch!"
            )
            food = max(0, food - 5)
            water_level = max(0, water_level - 5)
        else:
            if food > 0:
                food -= 1
            if water_level > 0:
                water_level -= 1
            if plant_health > 0:
                plant_health -= 1

        update_stats()

        if not game_over:
            if minutes_passed == 5:
                trigger_victory()


update_stats()
asyncio.create_task(material_reduction())
