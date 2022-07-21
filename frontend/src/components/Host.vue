<template>
    <div>
        <div>{{ host.name }}</div>
        <div>{{ host.addr }}</div>
        <boolFunc
            v-for="f in host['bool_functions']"
            :name="f"
            :status="res[host.name][f] ? 'active' : 'inactive'"
        />
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
