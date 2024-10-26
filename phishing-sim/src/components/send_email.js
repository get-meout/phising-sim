import { gen_company_lunch, gen_saudi_prince, gen_sign_in } from './templates.js';

const app = Vue.createApp({
    data() {
        return {
            subject: "",
            email_link: "", // Link to be passed for each template if needed
            quill: null, // Store the Quill instance
            initialBody: "" // Store the initial body content temporarily
        };
    },
    created() {
        const urlParams = new URLSearchParams(window.location.search);
        const template = urlParams.get('template'); // Get template type from URL

        // Choose the template based on the type
        if (template === 'Company Lunch') {
            this.subject = "Company Lunch Invitation";
            this.initialBody = gen_company_lunch(this.email_link); // Set body content
        } else if (template === 'Saudi Prince') {
            this.subject = "Urgent Assistance Needed";
            this.initialBody = gen_saudi_prince(this.email_link); // Set body content
        } else if (template === 'Google Sign in') {
            this.subject = "2-Step Verification turned on";
            this.initialBody = gen_sign_in(urlParams.get('email'), this.email_link); // Set body content
        }
    },
    mounted() {
        this.initialize_editor(this.initialBody); // Initialize editor with the body after mounting
    },
    methods: {
        go_back() {
            window.location.href = 'index.html';
        },
        send_email() {
            const email_body = this.quill.root.innerHTML; // Get the HTML content from the editor

            // Here you would implement your email sending logic using `this.subject` and `email_body`
            alert(`Email sent with Subject: ${this.subject} and Body: ${email_body}`);
        },
        initialize_editor(body) {
            this.quill = new Quill('#editor', {
                theme: 'snow',
                modules: {
                    toolbar: [
                        ['bold', 'italic', 'underline'],
                        ['link', 'image'],
                        [{ list: 'ordered' }, { list: 'bullet' }],
                    ],
                },
            });
            this.quill.setContents(this.quill.clipboard.convert(body)); // Set the initial body of the email
        }
    }
});

app.mount('#app');
