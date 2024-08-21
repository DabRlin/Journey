<template>
  <div>
    <label>{{ label }}</label>
    <!-- 监听input事件向上发送一个自定义事件 event.target.value即输入框中的值 -->
    <input :value="value" @input="$emit('input', $event.target.value)" />
  </div>
</template>

<script>
export default {
  props: ["value", "label"],
};

//v-model默认绑定value和input事件，如果更改名称 需要在model中指定

// export default{
//     props:["InputValue","label"]
//     model:{
//         props:"InputValue",
//         event:"Input"
//     }
// }
</script>
