function submitForm(event) {
    event.preventDefault(); // Prevent default form submission

    const form = event.target;
    const submitButton = form.querySelector('button[type="submit"]');
    
    submitButton.innerHTML = 'Submitting...';
    submitButton.disabled = true;

    const formData = new FormData(form);
    const data = {};
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }

    fetch('http://localhost:5000/submit_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
        if (result.message === 'Form submitted successfully!') {
            form.reset(); // Clear the form
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while submitting the form.');
    })
    .finally(() => {
        submitButton.innerHTML = 'Start the Conversation';
        submitButton.disabled = false;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('mail-form');

    if (form) {
        form.addEventListener('submit', submitForm);
    } else {
        console.error("Form with ID 'mail-form' not found.");
    }
});