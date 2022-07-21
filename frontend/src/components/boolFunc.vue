<template>
    <div class="bool-container">
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
            default: 'inactive',
        },
        name: String,
    },
};
</script>

<style>
.bool-container {
    display: flex;
}

.status {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 5px;
}

.active {
    background-color: green;
}

.inactive {
    background-color: red;
}
</style>
