<template>
  <!-- 使用全局注册的自定义指令 实现将元素背景色设置为随机颜色 -->
  <div v-random-bg>This div had a random background color</div>
</template>

<script>
export default {
  directives: {
    //实现局部注册自定义指令 实现将元素背景色设为随机颜色
    random_bg: {
      bind(el) {
        const randomColor =
          "#" + Math.floor(Math.random() * 16777215).toString(16);
        el.style.backgroundColor = randomColor;
      },
    },
  },
};
</script>
