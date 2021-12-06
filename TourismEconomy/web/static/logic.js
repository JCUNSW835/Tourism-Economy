// keep track of Leaflet map for use between functions
var globalMapObject;

// keep track of which map tiles have been selected
var globalCurrentTilesSelection;
var globalCurrentTiles;

// keep track of items added
var globalFeatureIDTracker = {};

// list of items to add
var itemsToAdd = [

	"Location/Singleton.geojson"
	, "Location/Shoalhaven.geojson"
	, "Location/MurrayRiver.geojson"
];

function bodyDidLoad() {
	ShowtimeHelper.setDarkModeAccordingToBrowser();
	ShowtimeHelper.initialiseSelect2();


	
	
	// OK - Ready to Initialise the map! :)

	globalMapObject = L.map('mapid').setView([-33.918, 151.23], 10);
	globalCurrentTiles.addTo(globalMapObject);

	itemsToAdd.forEach(function(item) {
		$.get(item, function(incomingGeoJSONString) {
			var incomingGeoJSON = JSON.parse(incomingGeoJSONString);
			MapHelper.processAddedUNSWFeature(incomingGeoJSON);
		});
	});


	// Example: lines

	var tripStyle = {
		"color": "red"
		,"weight": 3
		, "opacity": 0.5
		
	};

	$.get("Location/LGA2020-Visualingam-0.02.geojson", function(incomingGeoJSONString) {
		var incomingGeoJSON = JSON.parse(incomingGeoJSONString);
		MapHelper.processAddedUNSWFeature(incomingGeoJSON, tripStyle);
	});
	//Marker Icon
	var greenIcon = L.icon({
		iconUrl: 'bigcity.png',
		
	
		iconSize:     [32, 37], // size of the icon
		iconAnchor:   [16, 37], // point of the icon which will correspond to marker's location
		popupAnchor:  [-0, -30] // point from which the popup should open relative to the iconAnchor
	});
	// Example: marker
	L.marker([-33.91665415528511, 151.2257981300354],{icon:greenIcon}).addTo(globalMapObject).bindPopup('Sydney').openPopup();


	// Done!
}
