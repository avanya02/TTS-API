
function convertTextToSpeech() {
    const text = document.getElementById('text-input').value;

    if (text.trim() === '') {
        alert("Please enter some text.");
        return;
    }

    fetch('http://127.0.0.1:5000/api/text-to-speech ', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const audio = new Audio(url);
            audio.play();
        })
        .catch(error => console.error('Error:', error));
}
