// App.js
const app = Vue.createApp({
    data() {
      return {
        templates: [
          { name: 'Google Sign in', content: 'Sign in attempt was blocked...', preview: '/src/assets/sign-in-preview.png'},
          { name: 'Saudi Prince', content: 'Hello friend, I am...', preview: '/src/assets/saudi_prince.png' },
          { name: 'Company Lunch', content: 'Company Lunch happening...', preview: '/src/assets/company_lunch.png'},
        ],
        selectedTemplate: null
      };
    },
    methods: {
      selectTemplate(index) {
        this.selectedTemplate = this.templates[index];
      },
      proceedToSend() {
        const template = JSON.stringify(this.selectedTemplate);
        window.location.href = "send_email.html?template=" + encodeURIComponent(template);
      }
    }
  });
  
  app.mount('#app');
  