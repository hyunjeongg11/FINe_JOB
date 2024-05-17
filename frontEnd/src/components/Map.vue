<template>
    <div>
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
        crossorigin="anonymous"
      />
      <div class="container">
        <div class="row">
          <div class="col-md-6 offset-md-3">
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control search-input"
                v-model="keyword"
                placeholder="장소 또는 은행을 검색하세요"
                @keyup.enter="searchPlaces"
              />
              <div class="input-group-append">
                <button class="btn btn-primary search-button" type="button" @click="searchPlaces">
                  검색
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div id="map"></div>
      <div>
        <div id="menu_wrap" class="container">
          <ul id="placesList" class="list-group">
            <li
              v-for="(place, index) in places"
              :key="index"
              class="list-group-item custom-list-item"
              :class="'marker_' + (index + 1)"
            >
              <span class="markerbg"></span>
              <div class="info">
                <h5>{{ place.place_name }}</h5>
                <span>{{ place.road_address_name ? place.road_address_name : place.address_name }}</span>
                <span class="tel">{{ place.phone }}</span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <script>
  export default {
    name: "KakaoMap",
    data() {
      return {
        map: null,
        keyword: "",
        places: [],
        markers: [],
      };
    },
    created() {},
    mounted() {
      // 카카오 맵 로드 여부 확인 후 맵 초기화
      if (window.kakao && window.kakao.maps) {
        this.loadMap();
      } else {
        this.loadScript();
      }
    },
    methods: {
      // 카카오 맵 스크립트 로드
      loadScript() {
        const script = document.createElement("script");
        script.src =
          "//dapi.kakao.com/v2/maps/sdk.js?appkey=fb46c88703e2ee3761ca6cee1048de3c&libraries=services&autoload=false";
        script.onload = () => window.kakao.maps.load(() => this.loadMap());
        document.head.appendChild(script);
      },
      // 맵 초기화
      loadMap() {
        const container = document.getElementById("map");
        const options = {
          center: new window.kakao.maps.LatLng(33.450701, 126.570667),
          level: 3,
        };
        this.map = new window.kakao.maps.Map(container, options);
      },
      // 장소 검색
      searchPlaces() {
        let keyword = this.keyword.trim();
        keyword += ' 은행';
        if (!keyword) {
          alert("키워드를 입력해주세요!");
          return false;
        }
        const ps = new window.kakao.maps.services.Places();
        ps.keywordSearch(keyword, this.placesSearchCB);
      },
      // 장소 검색 콜백 함수
      placesSearchCB(data, status, pagination) {
        const menuEl = document.getElementById("menu_wrap");
        if (status === window.kakao.maps.services.Status.OK) {
          this.places = data;
          this.displayPlaces(data);
          this.displayPagination(pagination);
          menuEl.style.display = "block"; // 검색 결과가 있을 때 보이도록 설정
        } else if (status === window.kakao.maps.services.Status.ZERO_RESULT) {
          alert("검색 결과가 존재하지 않습니다.");
          this.places = [];
          menuEl.style.display = "none"; // 검색 결과가 없을 때 숨김 처리
        } else if (status === window.kakao.maps.services.Status.ERROR) {
          alert("검색 결과 중 오류가 발생했습니다.");
          this.places = [];
          menuEl.style.display = "none"; // 오류 발생 시 숨김 처리
        }
      },
      // 검색 결과 표시
      displayPlaces(places) {
        const listEl = document.getElementById("placesList");
        const menuEl = document.getElementById("menu_wrap");
        const fragment = document.createDocumentFragment();
        const bounds = new window.kakao.maps.LatLngBounds();
  
        if (listEl) {
          this.removeAllChildNods(listEl);
          this.removeMarker();
        }
  
        for (let i = 0; i < places.length; i++) {
          const place = places[i];
          const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
          const marker = this.addMarker(placePosition, i, place.place_name);
          const itemEl = this.getListItem(i, place);
          const infowindow = new window.kakao.maps.InfoWindow({
            zIndex: 1,
          });
  
          bounds.extend(placePosition);
  
          // 마커에 마우스오버 이벤트 추가
          (function (marker, title) {
            window.kakao.maps.event.addListener(marker, "mouseover", function () {
              infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
              infowindow.open(this.map, marker);
            });
  
            window.kakao.maps.event.addListener(marker, "mouseout", function () {
              infowindow.close();
            });
  
            itemEl.onmouseover = function () {
              infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
              infowindow.open(this.map, marker);
            };
  
            itemEl.onmouseout = function () {
              infowindow.close();
            };
  
            // 목록 항목 클릭 이벤트 추가
            itemEl.addEventListener("click", function () {
              this.map.setCenter(placePosition);
              this.map.setLevel(3); // 클릭 시 지도를 확대하여 표시 (레벨 3)
            }.bind(this));
          }).call(this, marker, place.place_name);
  
          fragment.appendChild(itemEl);
        }
  
        listEl.appendChild(fragment);
        menuEl.scrollTop = 0;
  
        this.map.setBounds(bounds);
      },
      // 검색 결과 항목 생성 (마커 번호 포함)
      getListItem(index, place) {
        const el = document.createElement("li");
        let itemStr =
          '<span class="markerbg marker_' +
          (index + 1) +
          '"></span>' +
          '<div class="info">' +
          "   <h5>" +
          (index + 1) + ". " +
          place.place_name +
          "</h5>";
  
        if (place.road_address_name) {
          itemStr +=
            "    <span>" +
            place.road_address_name +
            "</span>" +
            '   <span class="jibun gray">' +
            place.address_name +
            "</span>";
        } else {
          itemStr += "    <span>" + place.address_name + "</span>";
        }
  
        itemStr += '  <span class="tel">' + place.phone + "</span>" + "</div>";
  
        el.innerHTML = itemStr;
        el.className = "item";
  
        return el;
      },
      // 마커 추가
      addMarker(position, idx, title) {
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
  
        // 마커 클릭 이벤트 추가
        window.kakao.maps.event.addListener(marker, 'click', () => {
          this.map.setCenter(position);
          this.map.setLevel(3); // 클릭 시 지도를 확대하여 표시 (레벨 3)
        });
  
        return marker;
      },
      // 모든 마커 제거
      removeMarker() {
        for (let i = 0; i < this.markers.length; i++) {
          this.markers[i].setMap(null);
        }
        this.markers = [];
      },
      // 페이지네이션 표시
      displayPagination(pagination) {
        if (this.listEl && this.listEl.hasChildNodes()) {
          const paginationEl = document.getElementById("pagination");
          const fragment = document.createDocumentFragment();
  
          while (paginationEl.hasChildNodes()) {
            paginationEl.removeChild(paginationEl.lastChild);
          }
  
          for (let i = 1; i <= pagination.last; i++) {
            const el = document.createElement("a");
            el.href = "#";
            el.innerHTML = i;
  
            if (i === pagination.current) {
              el.className = "on";
            } else {
              el.onclick = (function (i) {
                return function () {
                  pagination.gotoPage(i);
                };
              })(i);
            }
  
            fragment.appendChild(el);
          }
          paginationEl.appendChild(fragment);
        }
      },
      // 인포윈도우 표시
      displayInfowindow(marker, title) {
        const content = '<div style="padding:5px;z-index:1;">' + title + "</div>";
  
        infowindow.setContent(content);
        infowindow.open(this.map, marker);
      },
      // 모든 자식 노드 제거
      removeAllChildNods(el) {
        while (el.hasChildNodes()) {
          el.removeChild(el.lastChild);
        }
      },
    },
  };
  
  </script>
  
  <style scoped>
  #map {
    width: 50%;
    height: 500px;
    margin: 0 auto; /* 가운데 정렬 */
    display: block; /* block 요소로 설정하여 margin: 0 auto가 적용되도록 함 */
    position: relative;
  }
  
  #menu_wrap {
    position: absolute;
    top: 60%; /* 수직 중앙 정렬을 위해 50% */
    right: 0; /* 지도의 오른쪽에 위치하도록 설정 */
    width: 250px;
    height: 80%; /* 화면 높이의 80%만큼 채우기 */
    padding: 5px;
    background: rgba(255, 255, 255, 0.7);
    z-index: 1;
    font-size: 12px;
    border-radius: 10px;
    display: none; /* 기본적으로 숨김 처리 */
    overflow-y: auto; /* 내용이 길면 스크롤 */
    transform: translateY(-50%); /* 수직 중앙 정렬을 위해 Y축으로 50% 이동 */
  }
  
  #menu_wrap hr {
    display: block;
    height: 1px;
    border: 0;
    border-top: 2px solid #5F5F5F;
    margin: 3px 0;
  }
  
  #menu_wrap .option {
    text-align: center;
  }
  
  #menu_wrap .option p {
    margin: 10px 0;
  }
  
  #menu_wrap .option button {
    margin-left: 5px;
  }
  
  
  
  
  </style>
  