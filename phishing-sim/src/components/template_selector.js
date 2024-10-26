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
            const template = this.selected_template.name; // Just use the name
            window.location.href = "send_email.html?template=" + encodeURIComponent(template);
        },
        go_back() {
            window.location.href = "index.html";
        }
    }
});

app.mount('#app');
