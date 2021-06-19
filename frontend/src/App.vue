<template>
  <div id="app">
    <el-container>
      <el-aside width="200px">
        <el-menu
            :default-active="activeMenu"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
            router>
          <!-- <el-menu
            :default-active="activeMenu"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="#304156"
            text-color="#bfcbd9"
            active-text-color="#409EFF"
            router> -->
          <el-menu-item-group>
            <template slot="title"></template>
            <el-menu-item index="/">
              <i class="el-icon-office-building"></i>
              <span slot="title">首页</span>
            </el-menu-item>
            <el-menu-item index="list">
              <i class="el-icon-pie-chart"></i>
              <span slot="title">业务统计</span>
            </el-menu-item>

            <el-menu-item index="branch">
              <i class="el-icon-school"></i>
              <span slot="title">查看支行</span>
            </el-menu-item>
            <el-menu-item index="dept">
              <i class="el-icon-suitcase-1"></i>
              <span slot="title">查看部门</span>
            </el-menu-item>
            <el-menu-item index="staff">
              <i class="el-icon-bank-card"></i>
              <span slot="title">查看员工</span>
            </el-menu-item>
            <el-menu-item index="customer">
              <i class="el-icon-s-custom"></i>
              <span slot="title">客户管理</span>
            </el-menu-item>
            <el-menu-item index="account">
              <i class="el-icon-wallet"></i>
              <span slot="title">账户管理</span>
            </el-menu-item>
            <el-menu-item index="loan">
              <i class="el-icon-coin"></i>
              <span slot="title">贷款管理</span>
            </el-menu-item>
          </el-menu-item-group>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
