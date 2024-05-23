<template>
  <div>
    <SearchBar @search-places="searchPlaces" @move-to-current-location="moveToCurrentLocation" />
    <div id="map"></div>
    <PlaceList :places="places" @move-to-place="moveToPlace" @visit-bank="visitBank" />
  </div>
</template>

<script>
import SearchBar from './SearchBar.vue';
import PlaceList from './PlaceList.vue';
import { useFinanceStore } from '@/stores/finance';
import markerImageSrc from '/assets/marker.png'; 

export default {
  name: "KakaoMap",
  components: {
    SearchBar,
    PlaceList,
  },
  data() {
    return {
      map: null,
      places: [],
      markers: [],
      infowindow: null,
      searchTriggered: false,
    };
  },
  mounted() {
    this.loadScript();
  },
  methods: {
    loadScript() {
      if (typeof window.kakao === 'object' && typeof window.kakao.maps === 'object') {
        this.initializeMap();
      } else {
        const script = document.createElement("script");
        script.src = "//dapi.kakao.com/v2/maps/sdk.js?appkey=fb46c88703e2ee3761ca6cee1048de3c&libraries=services&autoload=false";
        script.onload = () => this.initializeMap();
        document.head.appendChild(script);
      }
    },
    initializeMap() {
      if (window.kakao && window.kakao.maps) {
        window.kakao.maps.load(() => {
          this.infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });
          this.getCurrentLocation();
        });
      } else {
        console.error("Kakao Maps API 로드 실패");
      }
    },
    getCurrentLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const locPosition = new window.kakao.maps.LatLng(lat, lon);
            this.loadMap(locPosition);
          },
          (error) => {
            const defaultPosition = new window.kakao.maps.LatLng(37.5665, 126.9780);
            this.loadMap(defaultPosition);
          }
        );
      } else {
        const defaultPosition = new window.kakao.maps.LatLng(37.5665, 126.9780);
        this.loadMap(defaultPosition);
      }
    },
    loadMap(position) {
      const container = document.getElementById("map");
      const options = {
        center: position,
        level: 3,
      };
      this.map = new window.kakao.maps.Map(container, options);

      window.kakao.maps.event.addListener(this.map, 'dragend', this.handleMapEvents);
      window.kakao.maps.event.addListener(this.map, 'zoom_changed', this.handleMapEvents);

      this.searchNearbyBanks();
    },
    handleMapEvents() {
      if (!this.searchTriggered) {
        this.searchNearbyBanks();
      }
    },
    searchNearbyBanks() {
      const center = this.map.getCenter();
      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch("은행", this.placesSearchCB, {
        location: center,
        radius: 5000,
        size: 15,
      });
    },
    searchPlaces({ province, country, bank }) {
      this.searchTriggered = true;
      let query = `${province} ${bank}`;
      if (country) {
        query = `${province} ${country} ${bank}`;
      }
      const ps = new window.kakao.maps.services.Places();
      
      // Get the location of the specific region
      this.getLocationFromAddress(province, country)
        .then(location => {
          ps.keywordSearch(query, this.placesSearchCB, {
            location: location,
            radius: 2000, // Adjust the radius as needed to narrow the search results
          });
        })
        .catch(() => {
          alert('해당 지역의 위치를 찾을 수 없습니다.');
          this.searchTriggered = false;
        });
    },
    getLocationFromAddress(province, country) {
      return new Promise((resolve, reject) => {
        const geocoder = new window.kakao.maps.services.Geocoder();
        const address = `${province} ${country}`;
        geocoder.addressSearch(address, (result, status) => {
          if (status === window.kakao.maps.services.Status.OK) {
            const location = new window.kakao.maps.LatLng(result[0].y, result[0].x);
            resolve(location);
          } else {
            reject(status);
          }
        });
      });
    },
    placesSearchCB(data, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        this.places = data;
        this.displayPlaces(data);
      } else {
        this.places = [];
        this.displayPlaces([]);
      }
      this.searchTriggered = false;
    },
    displayPlaces(places) {
      const bounds = new window.kakao.maps.LatLngBounds();
      this.removeMarker();

      for (let i = 0; i < places.length; i++) {
        const place = places[i];
        const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i, place.place_name, place.id);
        bounds.extend(placePosition);
      }

      if (places.length > 0) {
        this.map.setBounds(bounds);
      } else {
        this.map.setCenter(this.map.getCenter());
      }
    },
    addMarker(position, idx, title, placeId) {
      const imageSize = new window.kakao.maps.Size(50, 50);
      const markerImage = new window.kakao.maps.MarkerImage(markerImageSrc, imageSize);
      const marker = new window.kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      window.kakao.maps.event.addListener(marker, "mouseover", () => {
        this.infowindow.setContent(`<div style="padding:5px;font-size:12px;">${title}</div>`);
        this.infowindow.open(this.map, marker);
      });

      window.kakao.maps.event.addListener(marker, "mouseout", () => {
        this.infowindow.close();
      });

      window.kakao.maps.event.addListener(marker, "click", () => {
        const url = `https://place.map.kakao.com/${placeId}`;
        window.open(url, "_blank");
      });

      return marker;
    },
    removeMarker() {
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }
      this.markers = [];
    },
    moveToCurrentLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const locPosition = new window.kakao.maps.LatLng(lat, lon);
            this.map.setCenter(locPosition);
            this.map.setLevel(3);
            this.searchNearbyBanks();
          },
          (error) => {
            alert("현재 위치를 찾을 수 없습니다.");
          }
        );
      } else {
        alert("현재 위치를 찾을 수 없습니다.");
      }
    },
    moveToPlace(position) {
      const locPosition = new window.kakao.maps.LatLng(position.y, position.x);
      this.map.setCenter(locPosition);
    },
    visitBank(bankName) {
      const store = useFinanceStore();
      const bankUrl = store.mapSearchBankLink(bankName);
      if (bankUrl) {
        window.open(bankUrl, "_blank");
      } else {
        alert("해당 은행의 홈페이지가 없습니다.");
      }
    },
  },
};
</script>

<style scoped>
#map {
  width: 65%;
  height: 600px;
  margin: 0 auto;
  border-radius: 20px;
  border: 3px solid #00000027;
}
</style>
