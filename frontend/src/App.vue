<script>
import axios from 'axios';
import boolFunc from './components/boolFunc.vue';
import textFunc from './components/textFunc.vue';
import Host from './components/Host.vue';
export default {
    data() {
        return {
            hosts: {},
            res: {},
        };
    },
    components: {
        boolFunc,
        textFunc,
    },
    methods: {
        update() {
            axios.get('/api/hosts').then((res) => {
                //console.log(res['data']);
                this.hosts = { ...res['data'] };
                for (let i = 0; i < res['data'].length; i++) {
                    let funcs_res = { ping: '123' };
                    let name = res['data'][i]['name'];
                    let addr = res['data'][i]['addr'];
                    let bool_funcs = res['data'][i]['bool_functions'];
                    let text_funcs = res['data'][i]['text_functions'];
                    this.res[name] = {};
                    for (let j = 0; j < bool_funcs.length; j++) {
                        axios
                            .get(`/api/${addr}/${bool_funcs[j]}`)
                            .then((res2) => {
                                this.res[name][bool_funcs[j]] =
                                    res2['data'].toString();
                            });
                    }
                    for (let j = 0; j < text_funcs.length; j++) {
                        axios
                            .get(`/api/${addr}/${text_funcs[j]}`)
                            .then((res2) => {
                                this.res[name][text_funcs[j]] =
                                    res2['data'].toString();
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
        }, 3000);
    },
};
</script>

<template>
    <div>{{ hosts }}</div>
    <div>{{ res }}</div>
    <div></div>
</template>

<style scoped>
@import 'assets/base.css';
</style>
