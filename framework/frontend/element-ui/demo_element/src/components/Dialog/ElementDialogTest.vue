<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="date" label="Date" width="180"> </el-table-column>
    <el-table-column prop="name" label="Name" width="180"> </el-table-column>
    <el-table-column prop="address" label="Address"> </el-table-column>
    <el-table-column label="Actions">
      <template slot-scope="scope">
        <!-- 使用scope返回的数据 scope允许我们访问当前行的上下文数据 -->
        <el-button size="mini" @click="handleDelete(scope.$index, scope.row)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
  </el-table>
  <!-- 对话框 dialog内容编写 -->
  <el-dialog title="Confirm Delete" :visible.sync="dialogVisible" width="30%">
    <span>Are you sure you want ti delete this item?</span>
    <!-- 此处使用具名插槽 覆盖了el-dialog中原本的内容 -->
     <!-- 使用插槽机制像子组件插入自定义内容 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="dialogVisible = false">Cancel</el-button>
      <el-button type="primary" @click="confirmDelete">Confirem</el-button>
    </span>
  </el-dialog>
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
      dialogVisible: false,
      deleteIndex: null,
    };
  },
  methods: {
    //设置要删除的列并显示对话框
    handleDelete(index, row) {
      this.deleteIndex = index;
      this.dialogVisible = true;
    },
    //确认删除
    confirmDelete() {
        //删除索引为deleteIndex的项
      this.tableData.splice(this.deleteIndex, 1);
      // 关闭对话框
      this.dialogVisible = false;
      this.$message({
        message: "Delete completed!",
        type: "success",
      });
    },
  },
};
</script>
