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
    name: 'boolFunc',
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
</style>
