let map;

function initAutocomplete() {
        map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: 37.769138, lng: -122.449035 }, 
          disableDefaultUI: true,
          zoom: 13,
          mapTypeId: "roadmap",
        });
        // Create the search box and link it to the UI element.
        const input = document.getElementById("pac-input");
        const input2 = document.getElementById("UserInput");
        const searchBox = new google.maps.places.SearchBox(input);
      
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input2);
        // Bias the SearchBox results towards current map's viewport.
        map.addListener("bounds_changed", () => {
          searchBox.setBounds(map.getBounds());
        });
      
        let markers = [];
     
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
        searchBox.addListener("places_changed", () => {
          const places = searchBox.getPlaces();
      
          if (places.length == 0) {
            return;
          }
      
          // Clear out the old markers.
          markers.forEach((marker) => {
            marker.setMap(null);
          });
          markers = [];
      
          // For each place, get the icon, name and location.
          const bounds = new google.maps.LatLngBounds();
      
          places.forEach((place) => {
            if (!place.geometry || !place.geometry.location) {
              console.log("Returned place contains no geometry");
              return;
            }
      
            const icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25),
            };
      
            // Create a marker for each place.
            markers.push(
              new google.maps.Marker({
                map,
                icon,
                title: place.name,
                position: place.geometry.location,
              }),
            );
            if (place.geometry.viewport) {
              // Only geocodes have viewport.
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        });
}
      
window.initAutocomplete = initAutocomplete;

function sendCoordsBackend() {
  var geocoder = new google.maps.Geocoder();
  var address = document.getElementById('pac-input').value;

  geocoder.geocode({
    'address': address
  }, function(results, status) {

    if (status == google.maps.GeocoderStatus.OK) {
      var latitude = results[0].geometry.location.lat();
      var longitude = results[0].geometry.location.lng();
      console.log("lat: " + latitude);
      console.log("lng: " + longitude);
      // send lat + lng to backend
     //request("http://127.0.0.1:3000", {latitude, longitude})

    url = "http://127.0.0.1:3000/getStreetParking?lat=" + latitude + "&long=" + longitude;
    fetch(url, {
        method: 'GET',
    }).then(response => {
      // Check if the response status is OK (200 
      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the JSON response
      return response.json();
  })
  .then(data => {
      // Do something with the data
      console.log(data);
      putthestuffonthemap(data.lat1, data.long1, data.lat2, data.long2, data.lat3, data.long3)

  })
  .catch(error => {
      // Handle errors
      console.error('Error:', error);
  });

    } else {
      alert("Not a vaild Destination");
    }
  });

  console.log(address);
}

function putthestuffonthemap(lat1, long1, lat2, long2, lat3, long3){

  const contentString1 =
    '<div id="content">' +
    '<h1 id="firstHeading" class="firstHeading">1st Place Best Parking Spot</h1>' +
    "</div>";
    const contentString2 =
    '<div id="content">' +
    '<h1 id="firstHeading" class="firstHeading">2nd Place Best Parking Spot</h1>' +
    "</div>";
    const contentString3 =
    '<div id="content">' +
    '<h1 id="firstHeading" class="firstHeading">3rd Place Best Parking Spot</h1>' +
    "</div>";
  const infowindow1 = new google.maps.InfoWindow({
    content: contentString1,
  });
  const infowindow2 = new google.maps.InfoWindow({
    content: contentString2,
  });
  const infowindow3 = new google.maps.InfoWindow({
    content: contentString3,
  });
  
  // make coords
  var coord1 = { lat: parseFloat(lat1), lng: parseFloat(long1) };
  var coord2 = { lat: parseFloat(lat2), lng: parseFloat(long2) };
  var coord3 = { lat: parseFloat(lat3), lng: parseFloat(long3) };

  // display geojsons
  marker1 = new google.maps.Marker({
    position: coord1,
    map,
  });
  marker2 = new google.maps.Marker({
    position: coord2,
    map,
  });
  marker3 = new google.maps.Marker({
    position: coord3,
    map,
  });

  marker1.addListener("click", () => {
    infowindow1.open({
      anchor: marker1,
      map,
    });
  });

marker2.addListener("click", () => {
  infowindow2.open({
    anchor: marker2,
    map,
  });
});

marker3.addListener("click", () => {
  infowindow3.open({
    anchor: marker3,
    map,
  });
});
}




