new Vue({
  el: "#app",
  data: {
    file: null,
    campaigns: [],
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async submitFile() {
      if (!this.file) {
        alert("Please select a file.");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      try {
        const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        this.campaigns = response.data;
      } catch (error) {
        alert("Upload failed: " + error.response?.data?.error || error.message);
      }
    },
  },
});
