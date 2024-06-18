$(document).ready(function () {

  $(".text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  //siri config
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.12",
    autostart: true,
  });

  //siri message animation
  $(".siri-message").textillate({
    loop: false,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });

  // mic button click event
  $("#mic-btn").click(function (e) {
    $("#Oval").attr("hidden", true);
    $("#Siri-Wave").attr("hidden", false);
    eel.allCommands();
  });

  function doc_keyUp(e) {
    // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

    if (e.key === "j" && e.metaKey) {
      eel.playAssistantSound();
      $("#Oval").attr("hidden", true);
      $("#Siri-Wave").attr("hidden", false);
      eel.allCommands()();
    }
  }

  document.addEventListener("keyup", doc_keyUp, false);

  function PlayAssistant(message) {
    if (message != "") {
      $("#Oval").attr("hidden", true);
      $("#Siri-Wave").attr("hidden", false);
      eel.allCommands(message);
      $("#chatbox").val("");
      $("#mic-btn").attr("hidden", false);
      $("#send-btn").attr("hidden", true);
    }
  }

  function ShowHideButton(message) {
    if (message.length == 0) {
      $("#mic-btn").attr("hidden", false);
      $("#send-btn").attr("hidden", true);
    } else {
      $("#mic-btn").attr("hidden", true);
      $("#send-btn").attr("hidden", false);
    }
  }

  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message);
  });

  $("#send-btn").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
      let message = $("#chatbox").val();
      PlayAssistant(message);
    }
  });
});
