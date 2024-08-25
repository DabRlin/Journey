<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="date" label="Date" width="180"> </el-table-column>
    <el-table-column prop="name" label="Name" width="180"> </el-table-column>
    <el-table-column prop="address" label="Address"> </el-table-column>
  </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        { date: "2023-01-01", name: "Tom", address: "No. 1, Xinhua Street" },
        { date: "2023-01-02", name: "Jerry", address: "No. 2, Xinhua Street" },
        // 更多数据...
      ],
    };
  },
};
</script>
