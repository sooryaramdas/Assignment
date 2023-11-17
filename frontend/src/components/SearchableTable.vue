<template>
  <div>
    <!-- Search input -->
    <input v-model="searchQuery" placeholder="Search users..." />
    
    <!-- User table -->
   <table class="user-table">
      <tr>
         <th>Username</th>
         <th>Email</th>
         <th>Phone</th>
         <th>ID</th>
         <th>Creation Date</th>
      </tr>
      <tr v-for="user in filteredUsers" :key="user.id" @click="showUserModal(user)">
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.phone }}</td>
        <td>{{ user.id }}</td>
        <td>{{ user.creation_date }}</td>
      </tr>
    </table>
    
    <!-- Button to generate a report for the selected user -->
    <button v-if="selectedUser" @click="generateReport">Generate Report</button>
  </div>
</template>

<script>
export default {
  props: {
    users: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      searchQuery: '',
      selectedUser: null,
    };
  },
  computed: {
  filteredUsers() {
    const query = this.searchQuery.toLowerCase();

    const filtered = this.users.filter(user => {
      return (
        user.username.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query) ||
        user.phone.toLowerCase().includes(query) ||
        (user.id.toString().includes(query) || user.id === Number(query)) || // Updated filtering condition
        user.creation_date.toLowerCase().includes(query)
      );
    });

    return filtered;
  },
},

  methods: {
    showUserModal(user) {
      this.selectedUser = user;
      this.$emit('show-modal', user);
    },
    generateReport() {
      this.$emit('generate-report', this.selectedUser);
    },
  },
};
</script>
<style scoped>

.user-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.user-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.user-table th, .user-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.user-table th {
  background-color: #3498db;
  color: #fff;
}

.user-table tbody tr:hover {
  background-color: #f5f5f5;
  cursor: pointer;
}



.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>