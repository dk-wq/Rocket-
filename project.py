import asyncio
from pyscript import document, when, window

msg = document.querySelector("#game-message")
body = document.querySelector("body")
plant = document.getElementById("plants")
water_dispenser = document.querySelector(".gray-block")
mine = document.getElementById("mine")
person = document.getElementById("person")


def show_text(text):
    """Helper to display messages on the webpage instead of the hidden console."""
    msg.innerText = text


@when("click", "#collect-btn")
async def collect_materials(event):
    show_text("Collecting materials...")
    mine.style.display = "flex"
    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1447433589675-4aaa569f3e05?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D')"
    body.style.backgroundSize = "cover"
    body.style.backgroundPosition = "center"
    await asyncio.sleep(0.6)
    water_dispenser.style.display = "none"
    plant.style.display = "none"
    await asyncio.sleep(0.6)
    person.style.left = "1100px"
    await asyncio.sleep(0.6)

    try:
        weight_str = window.prompt(
            "Enter rocket weight (will be multiplied by 1,000,000 pounds):"
        )
        if not weight_str:
            show_text("Ok")
            return
        rocket = int(weight_str) * 1000000

        material = window.prompt(
            "What material would you like to get first (Regolith, Titanium,"
            " Potassium, Basalt, or Helium-3):"
        )
        if not material:
            show_text("Ok")
            return

        if material.strip() in ["Regolith", "Titanium", "Potassium", "Basalt"]:
            amt_str = window.prompt(
                f"You fixed your rocket with {material.strip()}. Enter the number of"
                " pounds of that material (Don't use commas and divide rocket weight by 2.):"
            )
            if amt_str and int(amt_str) == rocket // 2:
                show_text(
                    "Your rocket is fixed! Now all you have to do is wait for help!"
                )
                return
            else:
                show_text("Wrong amount of materials! Try Again!")
        else:
            show_text("Wrong material! Try Again!")

    except ValueError:
        show_text("Please enter numbers only! Try Again!")

    finally:
        # Always resets the scene and character position when finished
        person.style.left = "48%"
        mine.style.display = "none"
        body.style.backgroundImage = "none"
        await asyncio.sleep(0.1)
        plant.style.display = "flex"
        water_dispenser.style.display = "flex"
