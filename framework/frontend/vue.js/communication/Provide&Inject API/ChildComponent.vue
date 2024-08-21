<template>
  <div>
    {{ shareDate }}
  </div>
</template>

<script>
export default {
  //先祖组件的provide的数据
  inject: ["shareData"],//使用数组的写法将祖先组件的数据注入当前组件
};
</script>
