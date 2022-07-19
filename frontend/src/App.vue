<script>
import boolFunc from './components/boolFunc.vue'
import textFunc from './components/textFunc.vue'
import Host from './components/Host.vue'
export default {
    data() {
        return {
            hosts: {},
            res: {}
        }
    },
    components: {
        boolFunc,
        textFunc
    },
    methods: {
        update() {
            axios
            .get('/api/hosts')
            .then((res) => {
                //console.log(res['data'])
                this.hosts = res['data'];
                for (let i = 0; i < res['data'].length; i++) {
                    let funcs_res = {};
                    for (let j = 0; j < res['data'][i]['bool_functions'].length; j++) {
                        let name = res['data'][i]['name'];
                        let addr = res['data'][i]['addr'];
                        let funcs = res['data'][i]['bool_functions'];
                        funcs_res[name] = {};
                        axios
                        .get(`/api/${addr}/${funcs[j]}`)
                        .then((res2) => {
                            funcs_res[funcs[j]] = res2['data'];
                        })
                    }
                    for (let j = 0; j < res['data'][i]['text_functions'].length; j++) {
                        let name = res['data'][i]['name'];
                        let addr = res['data'][i]['addr'];
                        let funcs = res['data'][i]['text_functions'];
                        funcs_res[name] = {};
                        axios
                        .get(`/api/${addr}/${funcs[j]}`)
                        .then((res2) => {
                            //console.log(res2['data'])
                            funcs_res[funcs[j]] = res2['data'];
                        })
                    }
                    //console.log(funcs_res);
                    this.res[res['data'][i]['name']] = funcs_res;
                }
            })
        }
    },
    mounted() {
        this.update();
        window.setInterval(() => {
            this.update();
        }, 3000);
    }
}
</script>

<template>
</template>

<style scoped>
@import "assets/base.css";
</style>
