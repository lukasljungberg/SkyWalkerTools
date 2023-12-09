function submitForm() {
    var data = document.getElementById('input_data').value;

    // Create FormData object to send form data
    var formData = new FormData();
    formData.append('input_data', data);

    // Send the form data to the server using Fetch API
    fetch('/process_data', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Update the output div with the returned data
        var outputElement = document.getElementById('output');
        outputElement.innerText = "Server Response:\n" + data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}