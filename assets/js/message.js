const messageContainer = document.getElementById("jsMessageContainer");
const messageBtn = document.getElementById("jsMessageBtn")

function hideMessage() {
    messageContainer.classList.add('hidden');
    messageBtn.removeEventListener("click", hideMessage)
    messageBtn.addEventListener("click", showMessage)
}
function showMessage() {
    messageContainer.classList.remove('hidden');
    messageBtn.removeEventListener("click", showMessage)
    messageBtn.addEventListener("click", hideMessage)
}

function init() {
    console.log("messageBtn")
    messageBtn.addEventListener("click", showMessage)
}

if (messageContainer) {
    init()
}