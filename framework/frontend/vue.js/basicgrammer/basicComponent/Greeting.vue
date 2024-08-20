<template>
    <p>Hello, {{ name }}!</p>
</template>

<script>
export default{
    //通过props接收父组件的参数
    props:["name"]
}
</script>