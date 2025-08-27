
const submitBtn = document.querySelector('button[type="submit"]');
const alertDiv = document.querySelector('.alert-container');

submitBtn.addEventListener('click', (event) => {
  event.preventDefault();

  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;

  fetch('/api/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username, password })
  })
  .then(response => response.json())
  .then(data => {
    if (data.status) {
      const successDiv = document.createElement('p');
      successDiv.className = 'alert alert-success';
      successDiv.textContent = data.message;
      alertDiv.innerHTML = successDiv.outerHTML
      window.setTimeout(() => {
          window.location.href = '/home';
        }, 3000);
    } else {
      const errorDiv = document.createElement('p');
      errorDiv.className = 'alert alert-danger';
      errorDiv.textContent = data.message;
      alertDiv.innerHTML = errorDiv.outerHTML;
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
