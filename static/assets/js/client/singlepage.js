$(document).ready(function () {
  const {
    host, hostname, href, origin, pathname, port, protocol, search
  } = window.location

  getNotifications()
  function fetchValue() {

    uri = origin + '/api/getmeter?id=' + document.getElementById('clientid').innerHTML
    fetch(uri)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true };
        datetimeObj = new Date(Date.parse(data.dateread))
        dateread = datetimeObj.toLocaleString('en-US', options)
        // Update the value element with the new value
        document.getElementById('currentread').innerHTML = data.currentread
        document.getElementById('total').innerHTML = data.total
        document.getElementById('dateread').innerHTML = dateread
        document.getElementById('amount').innerHTML = data.amount
      })
      .catch(error => {
        console.error('Error fetching value:', error);
      });
  }



  function getNotifications() {
    clientid = document.getElementById('clientid').innerHTML
    uri2 = origin + '/api/getnotif?id=' + clientid
    fetch(uri2)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        data =JSON.parse(data)
        html = ''
        count=0;
        data.forEach(r => {
          html += ` 
  
        <div class="item p-3">
        <div class="row gx-2 justify-content-between align-items-center">
            <div class="col-auto">
              <img class="profile-image" src="../static/assets/images/logo.png" alt="">
            </div><!--//col-->
            <div class="col"> 
              <label id="clientid" hidden>{${r.id}}</label>
              <div class="info">`


          if (r.isseen == true)   
              html+= ` <div class="desc">${r.message} </div>`
          else
              html+= ` <div class="desc"><strong>${r.message}</strong> </div>`  
              
              
          html+= ` <div class="meta">${r.period}</div>
              </div>
            </div><!--//col-->
          </div><!--//row-->
          <a class="link-mask" href= "/notifications?id=${r.id}&param=${clientid}"></a>
        </div> </div>`
          console.log(html)
          if (r.isseen == false) 
          {count ++ }
        
          
        })
          const container = document.getElementById("notif-content");   
            document.getElementById("notifcount").innerHTML = count;       
          const newElement = document.createElement("div");
          newElement.innerHTML = html;
          container.replaceChildren(newElement); 
        
      })
      .catch(error => {
            console.error('Error fetching value:', error);
          });
      ;
  }

  // Call the fetchValue function every second
  setInterval(getNotifications, 60000);
  setInterval(fetchValue, 5000);

  // Call the fetchValue function every second

});
