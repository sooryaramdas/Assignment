<template>
  <div id="app">
    <nav>
      <router-link to="/user-details">User Details</router-link> |
      <router-link to="/account-creation">Account Creation</router-link>

    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 20px;
  background-color: #3498db;
}

nav a {
  font-weight: bold;
  color: #fff;
  margin-right: 20px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.router-view {
  padding: 20px;
}
</style>