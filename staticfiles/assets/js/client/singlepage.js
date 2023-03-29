$(document).ready(function () {
    uri = 'https://oninemetermysqlproject-production.up.railway.app/api/getmeter?id=' + document.getElementById('clientid').innerHTML
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
