<script>
export default {
  props: {
    person_name: String,
  },
  data() {
    return {
      new_good_deed_name: '',
      new_bad_deed_name: '',
      name: this.person_name,
      good_deeds: [],
      bad_deeds: []
    }
  },
  computed: {
    category() {
      if (this.good_deeds.length >= this.bad_deeds.length) {
        return "good";
      } else {
        return "bad";
      }
    }
  },
  methods: {
    addGoodDeed() {
      if (this.new_good_deed_name === '') {
        return;
      }
      this.good_deeds.push(this.new_good_deed_name);
      this.new_good_deed_name = '';
    },
    addBadDeed() {
      if (this.new_bad_deed_name === '') {
        return;
      }
      this.bad_deeds.push(this.new_bad_deed_name);
      this.new_bad_deed_name = '';
    },
    removeGoodDeed(index) {
      this.good_deeds.splice(index, 1);
    },
    removeBadDeed(index) {
      this.bad_deeds.splice(index, 1);
    },
    modifyGoodDeed(index) {
      this.good_deeds[index] = prompt('Enter new value:', this.good_deeds[index]);
    },
    modifyBadDeed(index) {
      this.bad_deeds[index] = prompt('Enter new value:', this.bad_deeds[index]);
    },
    getJSON() {
      return {
        name: this.name,
        // Copying the arrays to avoid passing the reference
        good_deeds: [...this.good_deeds],
        bad_deeds: [...this.bad_deeds]
      }
    }
  }
}
</script>

<template>
<h1 :class="category">{{ this.name }}</h1>
<h2>Good deeds</h2>
<ol>
  <li v-for="(deed, index) in good_deeds">
    {{ deed }} <button @click="modifyGoodDeed(index)">...</button><button @click="removeGoodDeed(index)">X</button>
  </li>
  <input v-model="new_good_deed_name" type="text"/>
  <button @click="addGoodDeed">+</button>
</ol>
<h2>Bad deeds</h2>
<ol>
  <li v-for="(deed, index) in bad_deeds">
    {{ deed }} <button @click="modifyGoodDeed(index)">...</button><button @click="removeBadDeed(index)">X</button>
  </li>
  <input v-model="new_bad_deed_name" type="text"/>
  <button @click="addBadDeed">+</button>
</ol>
</template>

<style>
h1.bad {
  color: red;
}
h1.good {
  color: green;
}
</style>