const contactForm = document.getElementById('contact-form');
        const formStatus = document.getElementById('form-status');
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            formStatus.textContent = 'Transmitting...';
            const formData = new FormData(contactForm);
            
            try {
                const response = await fetch('https://formspree.io/f/mzzjrako', { // <-- REPLACE THIS
                    method: 'POST',
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                });

                if (response.ok) {
                    formStatus.textContent = 'Transmission successful. We will contact you shortly.';
                    formStatus.style.color = '#00ffff';
                    contactForm.reset();
                } else {
                    throw new Error('Network response was not ok.');
                }
            } catch (error) {
                formStatus.textContent = 'An error occurred. Please try again.';
                formStatus.style.color = '#ff4d4d';
            } finally {
                 setTimeout(() => {
                    formStatus.textContent = '';
                    formStatus.style.color = '';
                }, 5000);
            }
         });