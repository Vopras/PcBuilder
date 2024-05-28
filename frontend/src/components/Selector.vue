<template>
    <div>
      <div v-for="collection in collections" :key="collection" class="collection">
        <button @click="fetchCollectionData(collection)">{{ collection }}</button>
      </div>
      <div v-if="selectedCollectionData.length > 0">
        <h2>Data in {{ selectedCollectionName }}:</h2>
        <ul>
          <li v-for="(item, index) in selectedCollectionData" :key="index">
            {{ item }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        collections: [],
        selectedCollectionData: [],
        selectedCollectionName: ''
      }
    },
    mounted() {
      this.fetchCollections();
    },
    methods: {
      fetchCollections() {
        fetch('http://127.0.0.1:5000/collections')
          .then(response => response.json())
          .then(data => {
            this.collections = data;
          })
          .catch(error => console.error('Error:', error));
      },
      fetchCollectionData(collectionName) {
        fetch(`http://127.0.0.1:5000/collection_data/${collectionName}`)
          .then(response => response.json())
          .then(data => {
            this.selectedCollectionData = data;
            this.selectedCollectionName = collectionName;
          })
          .catch(error => console.error('Error:', error));
      }
    }
  }
  </script>
  
  <style>
  .collection button {
    margin: 1px;
  }
  </style>
  