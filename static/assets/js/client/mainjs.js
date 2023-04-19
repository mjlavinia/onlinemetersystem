$(document).ready(function () {
    const {
      host, hostname, href, origin, pathname, port, protocol, search
    } = window.location
    clientid = document.getElementById('clientid').innerHTML
    uri = origin + '/api/getnotif?id=' + clientid
    function getNotifications() {
        fetch(uri)
          .then(response => response.json())
          .then(data => {
            console.log(data)
        //     data.array.forEach(notif => {
        //         html += ` <div class="row gx-2 justify-content-between align-items-center">
        //     <div class="col-auto">
        //       <img class="profile-image" src="assets/images/profiles/adminnotif.jpg" alt="">
        //     </div><!--//col-->
        //       <div class="col">
        //         <label id="clientid" hidden>{${notif.id}</label>
        //       <div class="info">
        //         <div class="desc">${notif.message} </div>
        //         <div class="meta">${notif.time}</div>
        //       </div>
        //     </div><!--//col-->
        //   </div><!--//row-->
        //   <a class="link-mask" href="{% url 'notifications/${notifid}' %}"></a>`;
          
        //     })
        //   .catch(error => {
        //     console.error('Error fetching value:', error);
        //  }); 
        }
        );
  
    }
      
      // Call the fetchValue function every second
      setInterval(getNotifications, 1000);
  
});
