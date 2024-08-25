<template>
  <div>
    <el-table :data="filteredData" style="width: 100%">
      <el-table-column prop="date" label="Date" width="180" sortable>
      </el-table-column>
      <el-table-column prop="name" label="Name" width="180">
        <!-- 此处使用插槽实现筛选 筛选后调用filterTable方法将页面设置为第一页 -->
        <template slot="header" slot-scope="scope">
          <el-input
            placeholder="Filter by name"
            v-model="filters.name"
            size="mini"
            @input="filterTable"
          />
        </template>
      </el-table-column>
      <el-table-column prop="address" label="Address"> </el-table-column>
    </el-table>
  </div>
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
      filter: {
        name: "",
      },
      currentPage: 1,
      pageSize: 5,
    };
  },
  computed: {
    filterdData() {
      //先进行筛选
      let data = this.tableData;
      if (this.filters.name) {
        data = data.filter((item) => item.name.includes(this.filter.name));
      }
      //筛选后进行数据切片
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return data.slice(start, end);
    },
    methods: {
        //每次筛选页码后更新页码为1
      filterTable() {
        this.currentPage = 1;
      },
      handleSizeChange(size) {
        this.pageSize = size;
      },
      handleCurrentChange(page) {
        this.currentPage = page;
      },
    },
  },
};
</script>
