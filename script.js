 document.getElementById('submitBtn').addEventListener('click', function () {
        const text = document.getElementById('textInput').value;
        
        if (!text) {
            alert("Please enter some text.");
            return;
        }

    fetch('http://127.0.0.1:5000/api/tts', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: text }),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch audio');
    }
    return response.blob();  // Convert the response into a blob (audio file)
})
.then(blob => {
    const audioUrl = URL.createObjectURL(blob);  // Create a URL for the audio blob
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.src = audioUrl;
    audioPlayer.play();
})
.catch(error => {
    console.error('Error:', error);
})
    })
