// Initialize and add the map
function initMap(): void {
  // The location of Uluru
  const coep = { lat: 18.5293, lng: 73.85644 };
  // The map, centered at Uluru
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      zoom: 5,
      center: coep,
    }
  );

  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: coep,
    map: map,
  });
}
