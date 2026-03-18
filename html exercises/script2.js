const ageInput = document.querySelector("#age")
const message = document.querySelector("#msg")

function validateAge(value) {
    const x = Number(value)
    if (x < 2) {
        return false
    }
    if (x > 100) {
        return false
    }
    if (Number.isNaN(x)) {
        return false
    }
    return true
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
