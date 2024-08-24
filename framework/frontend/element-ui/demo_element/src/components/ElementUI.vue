<template>
  <!-- 布局容器 用于承载其他布局的组件 -->
  <el-container>
    <!-- 头部区域 -->
    <el-header>
      <h1>My Website</h1>
    </el-header>
    <!-- 主体区域 el-container是垂直排放的 而内部的el-container是水平排放的-->
    <el-container>
      <!-- 侧边栏区域 -->
      <el-aside width="200px">
        <!-- el-menu是element-ui的导航菜单组件 -->
        <el-menu>
          <!-- 菜单项目 -->
          <el-menu-item index="1">Home</el-menu-item>
          <el-menu-item index="2">About</el-menu-item>
          <el-menu-item index="3">Contact</el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主要内容区域 -->
      <el-main>
        <element-form></element-form>
        <element-table></element-table>
        <p>This is the main content area.</p>
      </el-main>
    </el-container>

    <el-footer>
      <p>@ 2024 My Website</p>
    </el-footer>
  </el-container>
</template>

<script>
import ElementForm from "./ElementForm.vue";
import ElementTable from "./ElementTable.vue";
export default {
  components: {
    ElementForm,
    ElementTable,
  },
  name: "App",
};
</script>

<style>
h1 {
  margin: 0;
  padding: 20px;
  text-align: center;
}
</style>
