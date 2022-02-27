let map;
let marker;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 18.5296432, lng: 73.8552409 },
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.HYBRID,
    draggableCursor: 'default'
  });
  
  marker = new google.maps.Marker({
    position: new google.maps.LatLng(18.5296432,73.8552409),
    map: map,
  });

  map.addListener('dragend', function (){

    var latlng =  map.getCenter();
    document.getElementById("dltd").innerHTML = latlng.lat();
    document.getElementById("dlng").innerHTML = latlng.lng();
    document.getElementById("zmf").innerHTML = map.getZoom();

    document.getElementById("lat").value =latlng.lat();
    document.getElementById("lng").value =latlng.lng();
    document.getElementById("zoom").value =map.getZoom();
 
    marker.setPosition(  map.getCenter());
 
  });
 
  map.addListener('zoom_changed', function(){
    document.getElementById("zmf").innerHTML = map.getZoom();
  })

}

$( document ).ready(function() {
   
  document.getElementById("dltd").innerHTML ="18.5296432";
  document.getElementById("dlng").innerHTML ="73.8552409";
  document.getElementById("zmf").innerHTML ="12";
  document.getElementById("lat").value ="18.5296432";
  document.getElementById("lng").value ="73.8552409";
  document.getElementById("zoom").value ="12";

});


function findArea()
{
   
}
 
