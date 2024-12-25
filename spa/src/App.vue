<script>
import Person from './Person.vue';
export default {
    data() {
        return {
            new_person_name: '',
            people: [
                {name: 'Jan Paweł 2'},
                {name: 'Benedykt XVI'}
            ]
        }
    },
    components: {
        Person
    },
    methods: {
        addPerson() {
            if (this.new_person_name === '') {
                return;
            }
            this.people.push({name: this.new_person_name});
        },
        getJSON() {
            console.log(this.$refs.personRefs.map(ref => ref.getJSON()));
        }
    }
}
</script>

<template>
    <div>
        <button @click="getJSON">Get JSON</button>
        <Person v-for="person in people" :person_name="person.name" ref="personRefs"/>
        <input v-model="new_person_name" type="text"/>
    </div>
</template>