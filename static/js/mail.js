function submitForm(formId) {
    const form = document.getElementById(formId);
    const submitButton = form.querySelector('button[type="submit"]');
    submitButton.innerHTML = 'Submitting...';
    submitButton.disabled = true;
    if (!form) {
      console.error(`Form with ID '${formId}' not found.`);
      return; // Exit early if form not found
    }
  
    const formData = new FormData(form);
  
    fetch("/data/", {
      method: "POST",
      body:formData,
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })
    .then(response => {
      if (!response.ok) {
        return response.text().then(errorText => {  // Get error details
          throw new Error(`${errorText}`);
        });
      }
      return response.json(); // or response.text() if not JSON
    })
    .then(data => {
      console.log('Success:', data.message);
      window.alert("Thanks for your enquiry, our team will reach to you shortly")
      form.reset(); // Clear the form
      // Process successful response
    })
    .catch(error => {
      alert(error);
      console.log(error)
      // Handle error
    })
    .finally(() => {
    // Show the button and re-enable it after the request is finished
    submitButton.innerHTML = 'Start the Conversation'; // or 'block', depending on your CSS
    submitButton.disabled = false;
  });
  }
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('mail-form');
  
    if (form) {
      form.addEventListener('submit', function(event) {
        event.preventDefault();
        submitForm('mail-form');
      });
    } else {
      console.error("Form with ID  not found.");
    }
  });
  
  // HTML (same as before - make sure action and method are correct)
  /*
  <form id="myForm" action="{% url 'your_django_view_name' %}" method="POST">
    </form>
  */
  
  // Django View (same as before - remove @csrf_exempt in production!)
  /*
  @csrf_exempt  # Remove in production!
  def your_django_view_name(request):
      # ... (same Django view code)
  */