$(document).ready(function () {
    uri = 'http://127.0.0.1:8000/api/getmeter?id=' + document.getElementById('clientid').innerHTML
    function fetchValue() {
        fetch(uri)
          .then(response => response.json())
          .then(data => {
            console.log(data)
            // Update the value element with the new value
            document.getElementById('currentread').innerHTML = data.currentread
            document.getElementById('total').innerHTML = data.total
            
          })
          .catch(error => {
            console.error('Error fetching value:', error);
          });
      }
      
      // Call the fetchValue function every second
      setInterval(fetchValue, 1000);
});
