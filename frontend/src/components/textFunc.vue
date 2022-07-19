<template>
    <div>
        <div class="name">
            {{ name }}
        </div>
        <div class="res">
            {{ res }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'boolFunc',
    props: {
        res: String,
        name: String
    }
}
</script>

<style>
</style>
