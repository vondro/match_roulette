var playerNo = 0
var groupNo = 0
var levelNo = 0

var playerItemCounter = 1

function generatePlayerInput(form) {
    playerNo = form.playerno.value
    groupNo = form.groupno.value
    levelNo = form.levelno.value

    alert(playerNo)
    alert(groupNo)
    alert(levelNo)
}

function addFormItem(form) {
    let text = document.createElement("input")
    text.setAttribute("type", "text")
    text.setAttribute("id", "player" + playerItemCounter)

    let label = document.createElement("label")
    label.setAttribute("for", "player" + playerItemCounter)
    label.textContent = "Player " + playerItemCounter

    let br = document.createElement("br")

    form.appendChild(label)
    form.appendChild(text)
    form.appendChild(br)

    playerItemCounter++
}