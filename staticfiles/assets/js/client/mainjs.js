$(document).ready(function () {
    const {
      host, hostname, href, origin, pathname, port, protocol, search
    } = window.location
    clientid = document.getElementById('clientid').innerHTML
    uri2 = origin + '/api/getnotif?id=' + clientid
    function getNotifications() {
      fetch(uri2)
        .then(response => response.json())
        .then(data => {
          console.log(data)
          data =JSON.parse(data)
          html = ''
          data.forEach(r => {
            html += ` 
          <div class="item p-3">
          <div class="row gx-2 justify-content-between align-items-center">
              <div class="col-auto">
                <img class="profile-image" src="assets/images/profiles/adminnotif.jpg" alt="">
              </div><!--//col-->
              <div class="col"> 
                <label id="clientid" hidden>{${r.id}}</label>
                <div class="info">
                  <div class="desc">${r.message} </div>
                  <div class="meta">${r.JSONtime}</div>
                </div>
              </div><!--//col-->
            </div><!--//row-->
            <a class="link-mask" href="{% url 'notifications/${r.id}' %}"></a>
          </div>`
            console.log(html)
          })
        })
            .catch(error => {
              console.error('Error fetching value:', error);
            });
        ;
    }
  
    // Call the fetchValue function every second
    setInterval(getNotifications, 1000);
  
});
