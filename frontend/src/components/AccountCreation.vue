<template>
  <div class="account-creation">
    <h2>Create Account</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="userData.username" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="userData.email" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="userData.password" required>
      </div>
      <button type="submit">Create Account</button>
    </form>
    <br>
    <div v-if="formSubmitted">
        Form submitted successfully!
      </div>
  </div>
</template>



<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        email: '',
        password: ''
      },
      formSubmitted: false  // Add a boolean flag to track form submission
    };
  },
  methods: {
    submitForm() {
      // Simulate a dummy asynchronous request
      console.log('Submitting form...');

      // Simulate a delay (e.g., 2 seconds) to mimic a server response time
      const simulateRequest = new Promise((resolve, reject) => {
        setTimeout(() => {
          const randomNumber = Math.random();

          // Simulate a successful response 80% of the time
          if (randomNumber < 0.8) {
            console.log('Form submitted successfully with data:', this.userData);
            resolve('Success!'); // You can pass additional data if needed
          } else {
            // Simulate an error response 20% of the time
            console.error('Form submission failed.');
            reject('Error: Something went wrong.'); // You can pass an error message
          }
        }, 2000); // 2000 milliseconds = 2 seconds
      });

      // Handle the result of the simulated request
      simulateRequest
        .then((result) => {
          console.log(result);
          // Reset form data after successful submission if needed
          this.userData = {
            username: '',
            email: '',
            password: ''
          };
          // Set formSubmitted to true to display the success message
          this.formSubmitted = true;
        })
        .catch((error) => {
          console.error(error);
          // Handle error cases and update the UI accordingly
          // For example, display an error message to the user
        });
    }
  }
}
</script>


<style scoped>
.account-creation {
  max-width: 400px;
  margin: auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  background-color: #3498db;
  color: #fff;
  padding: 10px;
  border: none;
  cursor: pointer;
}
</style>
