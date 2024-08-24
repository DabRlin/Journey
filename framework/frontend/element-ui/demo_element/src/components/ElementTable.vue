<template>
  <el-table :data="tableData" style="width: 100%">
    <!-- prop指定列绑定的字段名 label指定这一列的表头名称 -->
    <el-table-column prop="date" label="Date" width="180"></el-table-column>
    <el-table-column prop="name" label="Name" width="180"></el-table-column>
    <el-table-column prop="address" label="Address"></el-table-column>
  </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          date: "2024-08-23",
          name: "Tom",
          address: "No. 189, Grove St, Los Angeles",
        },
        {
          date: "2024-08-22",
          name: "Jerry",
          address: "No. 189, Grove St, Los Angeles",
        },
        {
          date: "2024-08-22",
          name: "Lucy",
          address: "No. 189, Grove St, Los Angeles",
        },
      ],
    };
  },
};
</script>
