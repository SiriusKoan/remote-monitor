<script>
import axios from 'axios';
import Host from './components/Host.vue';
import Copyright from './components/Copyright.vue';
export default {
    data() {
        return {
            hosts: {},
            res: {},
        };
    },
    components: {
        Host,
        Copyright,
    },
    methods: {
        update() {
            axios.get('/api/hosts').then((res) => {
                //console.log(res['data']);
                this.hosts = [...res['data']];
                for (let i = 0; i < res['data'].length; i++) {
                    let name = res['data'][i]['name'];
                    let addr = res['data'][i]['addr'];
                    let bool_funcs = res['data'][i]['bool_functions'];
                    let text_funcs = res['data'][i]['text_functions'];
                    if (this.res[name] === undefined) {
                        this.res[name] = {};
                    }
                    for (let j = 0; j < bool_funcs.length; j++) {
                        axios
                            .get(`/api/${addr}/${bool_funcs[j]}`)
                            .then((res2) => {
                                this.res[name][bool_funcs[j]] = res2['data'];
                            });
                    }
                    for (let j = 0; j < text_funcs.length; j++) {
                        axios
                            .get(`/api/${addr}/${text_funcs[j]}`)
                            .then((res2) => {
                                this.res[name][text_funcs[j]] =
                                    res2['data'].trim();
                            });
                    }
                }
            });
            //console.log('hosts: ', this.hosts);
            //console.log('res: ', this.res);
        },
    },
    mounted() {
        this.update();
        window.setInterval(() => {
            this.update();
        }, 5000);
    },
};
</script>

<template>
    <h1 id="title">Monitoring</h1>
    <main>
        <Host v-for="host in hosts" v-bind="{ host, res }" />
    </main>
    <Copyright />
</template>

<style scoped>
main {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: auto auto;
    place-items: center;
    row-gap: 10px;
}

#title {
    text-align: center;
    margin: 10px;
}

@media (max-width: 1000px) {
    main {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 700px) {
    main {
        grid-template-columns: repeat(1, 1fr);
    }
}
</style>
