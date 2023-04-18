document.addEventListener('DOMContentLoaded', function () {
    const textInput = document.getElementById('text-input');
    const textOutput = document.getElementById('text-output');

    textInput.addEventListener('keydown', function () {
        const text = textInput.value;
        newText = firstAndLastUp(text)
        textOutput.innerText = newText;
        textOutput.style.color = 'blue';
        textOutput.style.fontSize = '25px';
    });
});

function firstAndLastUp(text) {
    var newText = '';
    if (text[0]) {
        for (let i = 0; i < text.length; i++) {
            if (i == 0 || i == text.length - 1) {
                newText = newText + text[i].toUpperCase();
            }
            else {
                newText = newText + text[i].toLowerCase();
            }

        }

    }
    return newText.replace(/\d+/g, '');
}