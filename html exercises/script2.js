const ageInput = document.querySelector("#age")
const message = document.querySelector("#msg")

function validateAge() {

}

function handleInput() {
    const value = ageInput.value
    if (validateAge(value)) {
        message.textContent = "Age accepted"
    } else {
        message.textContent = "Invalid Age"
    }
}

ageInput.addEventListener("input", handleInput)
