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
      //makePostRequest("path that we don't have", {latitude, longitude})
      request("http://127.0.0.1:3000", {latitude, longitude})
    } else {
      alert("Not a vaild Destination");
    }
  });
  console.log(address);
}

function request(path, queryObj) {
    axios.post(path, queryObj).then(
        (response) => {
            let result = response.data;
            console.log(result);
            putthestuffonthemap(result)
        },
        (error) => {
            console.log(error);
        }
    );
}

function putthestuffonthemap(data){
  // make coords
  // var coord1 = {data.lat1, data.long1};
  // var coord1 = {data.lat2, data.long2};
  // var coord1 = {data.lat3, data.long3};

  // display geojsons
  new google.maps.Marker({
    position: coord1,
    map,
  });
  new google.maps.Marker({
    position: coord2,
    map,
  });
  new google.maps.Marker({
    position: coord3,
    map,
  });
}