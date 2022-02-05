// Initialize and add the map

function initMap()
{
    // Location
    const coep = { lat : 18.5293, lng : 73.85644 };

    // Map centred at coep
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 5,
        center: coep,
        mapTypeId: 'satellite'
    });
    
    // Marker, if needed, positioned at coep
    const marker = new google.maps.Marker({
        position: coep,
        map: map,
    });
}
