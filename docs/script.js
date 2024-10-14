// Show iframe when loaded, hide spinner
document.getElementById("chatbotIframe").onload = function () {
    document.getElementById("spinner").style.display = "none";
    document.getElementById("chatbotIframe").style.display = "block";
};

// Toggle chatbot visibility using floating chat button
let chatVisible = false;
function toggleChat() {
    const iframe = document.getElementById("chatbotIframe");
    if (chatVisible) {
        iframe.style.display = "none";
    } else {
        iframe.style.display = "block";
    }
    chatVisible = !chatVisible;
}

// Toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}
