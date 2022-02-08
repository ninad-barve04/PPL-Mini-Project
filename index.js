// Initialize and add the map

function initMap()
{
    // Location
    const coep = { lat : 18.5293, lng : 73.85644 };

    // Map centred at coep
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: coep,
        mapTypeId: 'satellite'
    });

    // TODO : InfoWindow data will be fetched later
    // Initial InfoWindow
    let infoWindow = new google.maps.InfoWindow(
    {
            content: "Click on any place to get local % vegetation",
            position: coep,
    });

    // Get LatLong
    infoWindow.open(map);
    // Detect mouseclick
    map.addListener("click", (mapsMouseEvent) =>
    {
    	// Close the current InfoWindow
    	infoWindow.close();
    	
    	// New InfoWindow
    	infoWindow = new google.maps.InfoWindow({
                position: mapsMouseEvent.latLng,
        });
        // New Window Content - LatLong + Zoom
        infoWindow.setContent(
            JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
            + "Zoom: " + map.getZoom()
        );
        infoWindow.open(map);
    });

    // Marker, if needed, positioned at coep
    const marker = new google.maps.Marker({
        position: coep,
        map: map,
    });
}
