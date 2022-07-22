<template>
    <div>
        <div class="name">
            {{ name }}
        </div>
        <pre class="content">
            {{ content }}
        </pre>
    </div>
</template>

<script>
export default {
    name: 'textFunc',
    props: {
        content: String,
        name: String,
    },
};
</script>

<style>
pre {
    white-space: pre-line;
}

.content {
    margin-left: 5px;
    padding-left: 5px;
    border-left: 1px solid white;
    font-size: 13px;
}
</style>
