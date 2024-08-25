<template>
  <div>
    <el-table :data="currentPageData" style="width: 100%">
      <el-table-column prop="date" label="Date" width="180"> </el-table-column>
      <el-table-column prop="name" label="Name" width="180"> </el-table-column>
      <el-table-column prop="address" label="Address"> </el-table-column>
    </el-table>
    <!-- current-page绑定到当前页码
    page-sizes选择每页显示的数据条目
    page-size绑定数据
    layout控制分页的布局
    total控制总条数
    @size-change监听每页条数的变化
    @current-change监听当前页码的变化 
    -->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[5, 10, 20]"
      :page-size="pageSize"
      layout="total, sizes. prev, pager, next, jumper"
      :total="tableData.length"
    ></el-pagination>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        { date: "2023-01-01", name: "Tom", address: "No. 1, Xinhua Street" },
        { date: "2023-01-02", name: "Jerry", address: "No. 2, Xinhua Street" },
      ],
      currentPage: 1,
      pageSize: 5,
    };
  },
  copmuted: {
    currentPageData() {
      //计算出开始的列和结束的列
      const start = this.currentPage - 1 * this.pageSize;
      const end = start + this.pageSize;
      // 对tableData进行切片操作
      return this.tableData.slice(start, end);
    },
  },
  methods: {
    handleSizeChange(size) {
      this.pageSize = size;
    },
    handleCurrentChange(page) {
      this.currentPage = page;
    },
  },
};
</script>
