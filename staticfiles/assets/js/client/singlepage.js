$(document).ready(function () {
  const {
    host, hostname, href, origin, pathname, port, protocol, search
  } = window.location

  uri = origin + '/api/getmeter?id=' + document.getElementById('clientid').innerHTML
  function fetchValue() {
      fetch(uri)
        .then(response => response.json())
        .then(data => {
          console.log(data)
          const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true };
          dateread = data.dateread.toLocaleString('en-US', options)
          // Update the value element with the new value
          document.getElementById('currentread').innerHTML = data.currentread
          document.getElementById('total').innerHTML = data.total
          document.getElementById('dateread').innerHTML = dateread
        })
        .catch(error => {
          console.error('Error fetching value:', error);
        }); 
    }
    
    // Call the fetchValue function every second
    setInterval(fetchValue, 1000);
  });
