<template>
  <el-table :data="tableData" style="width: 100%">
    <!-- sortable表示可以通过点击列头进行排序 -->
    <el-table-column
      prop="date"
      label="Date"
      width="180"
      sortable
    ></el-table-column>
    <el-table-column prop="name" label="Name" witdth="180">
      <!-- 使用插槽覆盖原来table-column生成的内容 -->

      <template slot="header" slot-scope="scope">
        <el-input
          placeholder="Filter"
          v-model="filter.name"
          size="mini"
          @input="filterTable"
        ></el-input>
      </template>
      <!-- 后面可以再添加更多插槽字段等 -->
    </el-table-column>
    <el-table-column prop="address" label="Address"></el-table-column>
  </el-table>
</template>

<script>
import { filter } from "core-js/core/array";

export default {
  date() {
    return {
      tableData: [
        { date: "2023-01-01", name: "Tom", address: "No. 1, Xinhua Street" },
        { date: "2023-01-02", name: "Jerry", address: "No. 2, Xinhua Street" },
        // 更多数据...
      ],
      filter: {
        name: "",
      },
    };
  },
  methods: {
    filterTable() {
      this.tableData = this.tableData.filter((item) => {
        item.name.includes(this.filter.name);
      });
    },
  },
};
</script>
