<template>
    <div class="container">
        <div class="host">
            <span>{{ host.name }} ({{ host.addr }})</span>
        </div>
        <boolFunc
            v-for="f in host['bool_functions']"
            :name="f"
            :status="res[host.name][f] ? 'active' : 'inactive'"
        />
        <div class="padding"></div>
        <textFunc
            v-for="f in host['text_functions']"
            :name="f"
            :content="res[host.name][f]"
        />
    </div>
</template>

<script>
import boolFunc from './boolFunc.vue';
import textFunc from './textFunc.vue';
export default {
    name: 'Host',
    props: {
        host: null,
        res: null,
    },
    components: {
        boolFunc,
        textFunc,
    },
};
</script>

<style>
.container {
    width: 30vw;
    min-height: 200px;
    height: 100%;
    -webkit-box-shadow: 5px 5px 13px 0px rgba(0, 0, 0, 0.5);
    box-shadow: 5px 5px 13px 0px rgba(0, 0, 0, 0.5);
    padding: 10px;
    margin: 5px;
    border-radius: 10px;
    background-color: rgb(85, 100, 131, 0.8);
}

.padding {
    height: 10px;
}

.host {
    font-size: larger;
}

@media (max-width: 1000px) {
    .container {
        width: 49vw;
    }
}

@media (max-width: 700px) {
    .container {
        width: 90vw;
    }
}
</style>
