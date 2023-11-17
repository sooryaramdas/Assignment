

<template>
  <div class="user-details">
    <h2>USER DETAILS</h2>

    <!-- Integrate SearchableTable Component -->
    <SearchableTable :users="users" @show-modal="showModal" @generate-report="generateReport" />

    <!-- User Modal -->
    <UserModal v-if="isModalVisible" :selectedUser="selectedUser" @close-modal="closeModal" />
  </div>
</template>

<script>
import axios from 'axios';
import SearchableTable from '@/components/SearchableTable.vue';
import UserModal from '@/components/UserModal.vue'; // Import UserModal component

export default {
  data() {
    return {
      users: [],
      isModalVisible: false,
      selectedUser: null,
    };
  },
  mounted() {
    // Fetch user data when the component is mounted
    this.fetchUserData();
  },
  methods: {
    fetchUserData() {
      console.log('Fetching user data...');
      axios.get('http://127.0.0.1:8000/user/api/users')
        .then(response => {
          // Assuming the response.data is an array of users
          console.log('Server response:', response.data);
          this.users = response.data;
        })
        .catch(error => {
          console.error('Error fetching user data:', error);
        });
    },
    showModal(user) {
      this.isModalVisible = true;
      this.selectedUser = user;
    },
    closeModal() {
      this.isModalVisible = false;
      this.selectedUser = null;
    },
    generateReport(user) {
      // Log a message to the console or implement actual report generation logic
      console.log('Generating report for user:', user);
    },
  },
  components: {
    SearchableTable,
    UserModal,
  },
}
</script>


<style scoped>

.user-details {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.user-info {
  margin-top: 10px;
}

.user-info p {
  margin: 5px 0;
}
</style>
