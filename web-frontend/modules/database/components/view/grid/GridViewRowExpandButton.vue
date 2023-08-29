<template>
  <div>
    <!-- Your other content here -->

    <button class="expand-button" @click="showModal = true">Action</button>

    <div v-if="showModal" class="modal-overlay">
      <div class="modal">
        <div class="modal-title-bar">
          <h2>Action</h2>
          <button class="modal-close-button" @click="closeModal">×</button>
        </div>
        <div class="modal-content">
          <label for="emailInput" class="modal-label"
            >Please insert your email:</label
          >
          <input
            id="emailInput"
            v-model="inputValue"
            type="email"
            class="modal-input"
            placeholder="example@example.com"
            required
            pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
          />
        </div>
        <div class="modal-footer">
          <button class="modal-button" @click="confirm">Confirm</button>
          <button class="modal-button" @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GridViewRowExpandButton',
  data() {
    return {
      showModal: false,
      inputValue: '',
    }
  },
  methods: {
    closeModal() {
      this.showModal = false
    },
    confirm() {
      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/
      if (!this.inputValue.match(emailPattern)) {
        alert('Please enter a valid email address.')
        return
      }
      const subject = 'Constructor University Bremen - Grant System'
      const title = this.$parent.row['field_' + this.$parent.fields[0].id]
      let body = 'Other Information: '
      const allKeys = Object.keys(this.$parent.row)
      allKeys.forEach((key_) => {
        if (
          key_ != 'field_' + this.$parent.fields[0].id &&
          key_.includes('field_') &&
          this.$parent.row[key_] !== null &&
          typeof this.$parent.row[key_] !== 'object'
        ) {
          body = body + '%0D%0A' + this.$parent.row[key_]
        }
      })
      body = 'Title: ' + title + '%0D%0A' + body
      const mail = this.inputValue

      window.location.href =
        'mailto:' + mail + '?subject=' + subject + '&body=' + body

      this.closeModal()
    },
  },
}
</script>

<style scoped>
/* Styles for the expand button */
.expand-button {
  background-color: #eeecec;
  color: rgb(31, 33, 184);
  border: none;
  border-radius: 20px;
  padding: 6px 12px;
  cursor: pointer;
}

.expand-button:hover {
  background-color: #a2ece0;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Adjust this value as needed */
}

.modal {
  background-color: white;
  width: 320px;
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.modal-title-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2px 12px; /* Even shorter padding */
  background-color: #f0f0f0;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.modal-title-bar h2 {
  margin: 0;
  font-size: 12px; /* Smaller font size */
}

.modal-close-button {
  border: none;
  background: none;
  cursor: pointer;
  font-size: 14px; /* Smaller font size */
  color: #777;
}

.modal-content {
  padding: 20px;
}

.modal-label {
  margin-bottom: 8px;
  font-weight: bold;
}

.modal-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
  background-color: #f0f0f0;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
}

.modal-button {
  margin-left: 5px;
  padding: 6px 12px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 2px;
  cursor: pointer;
}

.modal-button:hover {
  background-color: #0056b3;
}
</style>
