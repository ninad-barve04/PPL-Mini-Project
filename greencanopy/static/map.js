let map;
let marker;

function initMap() {

  var ltd = document.getElementById("dltd").innerHTML;
  var lng = document.getElementById("dlng").innerHTML;
  var lzf = document.getElementById("zmf").innerHTML


  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: Number(ltd), lng: Number(lng) },
    zoom: Number(lzf),
    mapTypeId: google.maps.MapTypeId.HYBRID,
    draggableCursor: 'default'
  });
  
  marker = new google.maps.Marker({
    position: new google.maps.LatLng( Number(ltd),  Number(lng)),
    map: map,
  });

  
  // map.addListener('dragend', function (){

  //   var latlng =  map.getCenter();
  //   document.getElementById("dltd").innerHTML = latlng.lat();
  //   document.getElementById("dlng").innerHTML = latlng.lng();
  //   document.getElementById("zmf").innerHTML = map.getZoom();
 
  //   marker.setPosition(  map.getCenter());
 
  // });
 
  // map.addListener('zoom_changed', function(){
  //   document.getElementById("zmf").innerHTML = map.getZoom();
  // })

}

$( document ).ready(function() {
   
  console.log("doc ready");
  var ltd = document.getElementById("dltd").innerHTML;
   console.log( ltd);
  // document.getElementById("dlng").innerHTML ="73.8552409";
  // document.getElementById("zmf").innerHTML ="12";

});


function findArea()
{
   
}
 
