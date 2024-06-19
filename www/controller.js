$(document).ready(function () {
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    if (message.length >= 50) {
      message = message.slice(0, 1000) + "..."
    }
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
  }

  eel.expose(DisplayLoader);
  function DisplayLoader(value) {
    $(".siri-message").attr("hidden", !value)
    $(".loader").attr("hidden", value);
    $(".loader-message").attr("hidden", value);
  }

  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").attr("hidden", false);
    $("#Siri-Wave").attr("hidden", true);
  }

  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`;

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }

  eel.expose(receiverText);
  function receiverText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`;

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
});
