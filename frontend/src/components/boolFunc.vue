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
    align-items: center;
}

.status {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
}

.active {
    background-color: rgba(51, 252, 145, 1);
    box-shadow: 0px 0px 5px 3px rgba(37,174,92,0.65);
    -webkit-box-shadow: 0px 0px 5px 3px rgba(37,174,92,0.65);
    -moz-box-shadow: 0px 0px 5px 3px rgba(37,174,92,0.65);
}

.inactive {
    background-color: red;
    box-shadow: 0px 0px 5px 3px rgba(209,42,61,0.65);
    -webkit-box-shadow: 0px 0px 5px 3px rgba(209,42,61,0.65);
    -moz-box-shadow: 0px 0px 5px 3px rgba(209,42,61,0.65);
}
</style>
