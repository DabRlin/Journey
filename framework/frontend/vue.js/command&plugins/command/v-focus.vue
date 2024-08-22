<template>
  <input v-focus />
</template>

<script>
export default {
  //局部自定义指令
  directives: {
    focus: {
      //钩子函数 在绑定元素插入到DOM后立即执行
      inserted(el) {
        el.focus();
      },
    },
    demo:{
        //el是指令绑定的dom元素 用于直接操作dom
        //binding是对象包含指令绑定的各种信息
        //vnode是生成的虚拟节点 包含了标签名 子节点 数据兑现以及实际DOM引用还有上下文
        bind(el,binding,vnode){//指令第一次绑定到元素时调用 只调用一次
            //输出字符串和binding绑定的值
            console.log("bind",binding.value)
        },
        inserted(el,binding){//绑定元素插入到父节点时调用
            console.log("inserted",binding.value)
        },
        update(el,binding){//组件更新时调用//指的是组件的数据或状态更新 而不是单指指令的值
            console.log("update",bingding.value)
        },
        componentUpdated(el,binding){//组件更新完调用
            console.log("componentUpdate",binding.value)
        },
        unbind(el,bingding){//指令与元素解绑时调用
            console.log("unbind",bingding.value)
        }
    }
  },
};
</script>
