<template>
  <div class="user-modal">
    <div class="modal-content">
      <h2>User Details</h2>
      <p><strong>Username:</strong> {{ selectedUser.username }}</p>
      <p><strong>Email:</strong> {{ selectedUser.email }}</p>
      <p><strong>Phone:</strong> {{ selectedUser.phone }}</p>
      <p><strong>ID:</strong> {{ selectedUser.id }}</p>
      <p><strong>Creation Date:</strong> {{ selectedUser.creation_date }}</p>
      <button @click="closeModal">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectedUser: {
      type: Object,
      required: true,
    },
  },
  methods: {
    closeModal() {
      // Emit an event to notify the parent component (UserDetails.vue) to close the modal
      this.$emit('close-modal');
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

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>