<template>
    <button @click="handleClick">Click me</button>
</template>

<script>
export default{
    methods:{
        handleClick(){
            //emit触发自定义事件button-clicked
            this.$emit("button-clicked")
        }
    }
}
</script>