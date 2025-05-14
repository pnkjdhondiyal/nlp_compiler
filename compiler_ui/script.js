function sendInstruction() {
  const instruction = document.getElementById('instruction').value;

  fetch('/compile', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ instruction })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById('codeOutput').innerText = data.code;
      document.getElementById('execOutput').innerText = data.output;
    })
    .catch(err => {
      console.error('Error:', err);
      alert('An error occurred');
    });
}
