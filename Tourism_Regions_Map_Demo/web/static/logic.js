// keep track of Leaflet map for use between functions
var globalMapObject;
var globalTiles = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
});


function bodyDidLoad() {
	// OK - Ready to Initialise the map! :)

	globalMapObject = L.map('mapid').setView([-33.918, 151.23], 10);
	globalTiles.addTo(globalMapObject);
	
	$.get("postcodes-geojson/TourismRegions-Visualingam-0.02.geojson", function(incomingGeoJSON) {
		var mysubset = {
			"type": "FeatureCollection",
    		"features": []
		}
		var postcodeBoundaries = JSON.parse(incomingGeoJSON);

		postcodeBoundaries["features"].forEach(function(item, index) {
			if (
				parseInt(item["properties"]["STE_CODE21"]) == "1" // Only shows the polygons that belong to New South Wales 
				// && parseInt(item["properties"]["TR_CODE21"]) == "1R200" // North Coast NSW
				// && parseInt(item["properties"]["TR_CODE21"]) == "1R100" // Hunter
				// && parseInt(item["properties"]["TR_CODE21"]) == "1R010"  // South East
				// && parseInt(item["properties"]["TR_CODE21"]) == "1R080" // Riverina
				// && parseInt(item["properties"]["TR_CODE21"]) == "1R070" // The Murray
			) {
				mysubset.features.push(item);
			}
		});
		
		L.geoJSON(mysubset, {
			onEachFeature: function(feature, layer) {
				// https://leafletjs.com/examples/geojson/
				if (feature.properties && feature.properties["TR_CODE21"]) {
                    var preparedString = "<strong>" + feature.properties["TR_CODE21"] + "</strong>";
					layer.bindPopup(preparedString);
				}
			}
		}).addTo(globalMapObject);
	});
	var greenIcon = L.icon({
		iconUrl: 'riparianhabitat.png',
		
	
		iconSize:     [32, 37], // size of the icon
		iconAnchor:   [16, 37], // point of the icon which will correspond to marker's location
		popupAnchor:  [-3, -30] // point from which the popup should open relative to the iconAnchor
	});

	var redIcon = L.icon({
		iconUrl: 'treedown.png',
		iconSize:     [32, 37], // size of the icon
		iconAnchor:   [16, 37], // point of the icon which will correspond to marker's location
		popupAnchor:  [0, -30] // point from which the popup should open relative to the iconAnchor
	});

	 // Markers:
    // North Coast NSW
    L.marker([-28.643594390426955,153.60809326171875], {icon:greenIcon}).addTo(globalMapObject)
        .bindPopup('North Coast NSW Region: Drought = 58.20%').openPopup();
   
    // Hunter
    L.marker([-32.55954607536906,151.16775512695312], {icon:redIcon}).addTo(globalMapObject)
        .bindPopup('Hunter Region: Drought = 58.66%').openPopup();
   
    // South East
    L.marker([-34.87522849294273,150.6019592285156], {icon:redIcon}).addTo(globalMapObject)
        .bindPopup('South East Region: Drought = 63.19%').openPopup();
   
    // Riverina
    L.marker([-35.08395557927643,147.3651123046875], {icon:greenIcon}).addTo(globalMapObject)
        .bindPopup('Riverina Region: Drought = 53.31%').openPopup();
    // The Murray
    L.marker([-35.828669790550144,144.99515533447266], {icon:redIcon}).addTo(globalMapObject)
        .bindPopup('The Murray Region: Drought = 65.88%').openPopup();
    // Sydney
    L.marker([-33.84960356615536, 151.21170043945312,]).addTo(globalMapObject)
        .bindPopup('Sydney: Drought = 33.18%').openPopup();
}

