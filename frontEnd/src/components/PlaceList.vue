<template>
  <div id="menu_wrap" class="container">
    <ul id="placesList" class="list-group">
      <li v-if="places.length === 0" class="list-group-item custom-list-item">
        해당 지역에는 선택한 은행이 없습니다.
      </li>
      <li
        v-else
        v-for="(place, index) in places"
        :key="index"
        class="list-group-item custom-list-item"
        @click="moveToPlace(place)"
      >
        <span class="markerbg marker_{{ index + 1 }}"></span>
        <div class="info">
          <h5>{{ place.place_name }}</h5>
          <span>{{ place.road_address_name ? place.road_address_name : place.address_name }}</span>
          <span class="tel">{{ place.phone }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PlaceList",
  props: {
    places: Array,
  },
  methods: {
    moveToPlace(place) {
      this.$emit("move-to-place", { x: place.x, y: place.y });
    }
  }
};
</script>

<style scoped>
#menu_wrap {
  position: absolute;
  top: 60%;
  right: 0;
  width: 250px;
  height: 80%;
  padding: 5px;
  background: rgba(255, 255, 255, 0.7);
  z-index: 1;
  font-size: 12px;
  border-radius: 10px;
  overflow-y: auto;
  transform: translateY(-50%);
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
