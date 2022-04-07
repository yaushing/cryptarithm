console.log("IIFSC Online");

function Copytoclipboardencode() {
  var copyText = document.getElementById("copytargetencode");
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);

  var tooltip = document.getElementById("copyencodebtn");
  tooltip.innerHTML = "Copied!";
}

function outFuncencode() {
  var tooltip = document.getElementById("copyencodebtn");
  tooltip.innerHTML = "Copy to clipboard";
}
