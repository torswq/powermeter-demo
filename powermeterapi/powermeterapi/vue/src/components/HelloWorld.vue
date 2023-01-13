<template>
  <div class="container">
    <div class="text-left my-2">
      <h2 class="display-4">Add new measurer</h2>
      <div class="mb-5">
        <div class="row">
          <label for="uuid4" class="form-label">UUIDv4</label>
          <div class="col-10">
            <input type="text" class="form-control" id="uuid4" v-model="this.uuid" aria-describedby="Universal Unique IDentifier Version 4">
          </div>
          <div class="col-2">
            <button type="submit" class="btn btn-primary mb-3" @click="newUUID">Generate new UUID</button>
          </div>
        </div>
        <div id="uuidhelp" class="form-text">This is a unique universal identifier</div>
      </div>
      <div class="mb-2">
        <div class="row">
          <label for="name" class="form-label">Name</label>
          <div class="col-10">
            <input type="text" class="form-control" id="name" placeholder="Customer name" v-model="this.name" aria-describedby="Measurer name">
          </div>
          <div class="col-2">
            <button type="submit" class="btn btn-primary mb-3" @click="addMeasurer">Add new measurer</button>
          </div>
          
        </div>
        <p class="lead text-muted">{{this.measurer_status}}</p>
      </div>

    </div>
    <br>
    <hr class="my-5"/>
    <br>
  </div>
  <div class="container">
    <h2 class="display-4">Add consumption</h2>
    <div class="container">
      <div class="row">
        <div class="col-sm-6">
          <select class="form-select" v-model="this.customer_uuid">
            <option selected disabled>Select an UUID</option>
            <option v-for="(measurer, index) in this.measurers" :key="'add_consumption'+measurer.uuid+'-'+index" >
              {{measurer.uuid}} - {{measurer.uuid__name}}
            </option>
          </select>
        </div>
        <div class="col-sm-3">
          <input class="form-control" type="number" v-model="this.consumption" min=0 placeholder="Add consumption in kwh">
        </div>
        <div class="col-sm-3">
          <button @click="addConsumption" class="btn btn-success">Add consumption</button>
        </div>
      </div>
      <p class="lead text-muted">{{this.consumption_status}}</p>
    </div>
    <br>
    <hr class="my-5"/>
    <br>
  </div>
  <div class="container">
    <div class="row my-2">
      <h2 class="display-4">Measurers</h2>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">UUID</th>
            <th scope="col">name</th>
            <th scope="col">Minimum consumption</th>
            <th scope="col">Average consumption</th>
            <th scope="col">Maximum consumption</th>
            <th scope="col">Total consumption</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(measurer, index) in this.measurers" :key="measurer.uuid+'-'+index" >
            <th scope="row">{{measurer.uuid}}</th>
            <td>{{measurer.uuid__name}}</td>
            <td>{{measurer.min_consumption}}</td>
            <td>{{measurer.avg_consumption}}</td>
            <td>{{measurer.max_consumption}}</td>
            <td>{{measurer.total_consumption}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { uuid } from 'vue-uuid'; 
export default {
  data() {
    return {
      name: '',
      measurer_status: '',
      consumption_status: '',
      customer_uuid: "Select an UUID",
      uuid: uuid.v4(),
      consumptions: [],
      consumption: 0.0,
      measurers: [],
    }
  },
  mounted() {
    this.getConsumptionHistory();
  },
  methods: {
    addMeasurer(){
      let params = {
        name: this.name,
        uuid: this.uuid
      }
      axios.post('http://localhost:8000/api/measurer/', params).then(
        (response) => {
          console.log(response);
          this.measurer_status = "Succesfully added measurer with id " + this.uuid
          this.uuid = ""; 
          this.name = "";
          setTimeout(()=> this.measurer_status = "", 3600)
        }
      )

    },
    addConsumption(){
      let customer_info = this.customer_uuid.split(' - ');
      let _uuid = customer_info[0];
      let _name = customer_info[1];
      let _data = {
        uuid: _uuid,
        name: _name,
        consumption: this.consumption
      }
      axios.put(
        "http://localhost:8000/api/measurer/"+_uuid+"/", _data).then(
        (response) => {
          console.log(response);
          this.consumption_status  = "Succesfully added consumption to id " + this.customer_uuid
          
          this.customer_uuid = "Select an UUID",
          this.consumption = 0.0;
          setTimeout(()=> this.consumption_status = "", 3600)
        }
      )
    },
    newUUID(){
      this.uuid = uuid.v4();
    },
    getConsumptionHistory() {
      axios.get('http://localhost:8000/api/measurerhistory/consumption_info').then((response) => {
        console.log(response.data)
        this.measurers = response.data;
      });
    },
    max_consumption() {

    },
    min_consumption() {

    },
    total_consumption() {

    },
    average_consumption() {

    },

  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
