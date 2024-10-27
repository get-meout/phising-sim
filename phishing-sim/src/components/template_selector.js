const app = Vue.createApp({
    data() {
        return {
            templates: [
                { name: 'Google Sign in', content: 'Sign in attempt was blocked...', preview: '/src/assets/sign-in-preview.png' },
                { name: 'Saudi Prince', content: 'Hello friend, I am...', preview: '/src/assets/saudi_prince.png' },
                { name: 'Company Lunch', content: 'Company Lunch happening...', preview: '/src/assets/company_lunch.png' },
            ],
            selected_template: null
        };
    },
    methods: {
        select_template(index) {
            this.selected_template = this.templates[index];
        },
        proceed_to_send() {
            if (this.selected_template) {
                const templateName = this.selected_template.name; 
                window.location.href = "edit_email.html?template=" + encodeURIComponent(templateName);
            } else {
                alert("Please select a template before proceeding.");
            }
        },
        go_back() {
            window.location.href = "index.html";
        },
        goToStep(step) {
            if (step === 1) {
                window.location.href = "index.html";
            }
        }
    }
});

app.mount('#app');
