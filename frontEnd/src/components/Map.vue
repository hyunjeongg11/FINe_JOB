<template>
  <div>
    <SearchBar @search-places="searchPlaces" @move-to-current-location="moveToCurrentLocation" />
    <div id="map"></div>
    <PlaceList :places="places" @move-to-place="moveToPlace" />
  </div>
</template>

<script>
import SearchBar from './SearchBar.vue';
import PlaceList from './PlaceList.vue';
import { useFinanceStore } from '@/stores/finance';

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
      searchTriggered: false, // 검색 버튼 클릭 여부
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
      this.searchTriggered = true; // 검색 버튼 클릭으로 인한 검색 실행
      const query = `${province} ${country} ${bank}`;
      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch(query, this.placesSearchCB);
    },
    placesSearchCB(data, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        this.places = data;
        this.displayPlaces(data);
      } else {
        this.places = [];
        this.displayPlaces([]);
      }
      this.searchTriggered = false; // 검색 버튼 클릭 후 이벤트 처리 완료
    },
    displayPlaces(places) {
      const bounds = new window.kakao.maps.LatLngBounds();
      this.removeMarker();

      for (let i = 0; i < places.length; i++) {
        const place = places[i];
        const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i, place.place_name, place.category_name);
        bounds.extend(placePosition);
      }

      if (places.length > 0) {
        this.map.setBounds(bounds);
      } else {
        this.map.setCenter(this.map.getCenter());
      }
    },
    addMarker(position, idx, title, bankName) {
      const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new window.kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new window.kakao.maps.Size(36, 691),
        spriteOrigin: new window.kakao.maps.Point(0, idx * 46 + 10),
        offset: new window.kakao.maps.Point(13, 37),
      };
      const markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
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
        const store = useFinanceStore();
        console.log(title)
        const bankUrl = store.searchBankLink(title);
        if (bankUrl) {
          console.log('click')
          window.open(bankUrl, "_blank");
        }
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
  },
};
</script>

<style scoped>
#map {
  width: 70%;
  height: 500px;
  margin: 0 auto;
}
</style>
