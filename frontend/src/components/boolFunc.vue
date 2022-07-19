<template>
    <div>
        <span class="status" :class="status"></span>
        <span class="name">
            {{ name }}
        </span>
    </div>
</template>

<script>
export default {
    name: 'boolFunc',
    props: {
        status: {
            type: String,
            default: 'inactive'
        },
        name: String
    }
}
</script>

<style>
.status {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: inline-block
}

.active {
    background-color: green;
}

.inactive {
    background-color: red;
}
</style>
