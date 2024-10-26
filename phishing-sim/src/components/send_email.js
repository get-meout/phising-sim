const app = Vue.createApp({
    data() {
      return {
        template: null,
        subject: "",
        body: ""
      };
    },
    created() {
      const urlParams = new URLSearchParams(window.location.search);
      const templateData = urlParams.get('template');
  
      if (templateData) {
        this.template = JSON.parse(decodeURIComponent(templateData));
        this.subject = this.template.name;
        this.body = this.template.content;
      }
    },
    methods: {
      sendEmail() {
        // Implement the email sending function here.
        alert(`Email sent with Subject: ${this.subject} and Body: ${this.body}`);
      }
    }
  });
  
  app.mount('#app');
  