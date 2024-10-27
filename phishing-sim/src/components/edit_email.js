import { gen_company_lunch, gen_saudi_prince, gen_sign_in } from './templates.js';

const app = Vue.createApp({
    data() {
        return {
            subject: "",
            quill: null,  
            initialBody: "",  
            template: ""
        };
    },
    created() {
        const urlParams = new URLSearchParams(window.location.search);
        const template = urlParams.get('template');  
        this.template = template;

        if (template === 'Company Lunch') {
            this.subject = "Company Lunch Invitation";
            this.initialBody = gen_company_lunch();  
        } else if (template === 'Saudi Prince') {
            this.subject = "Urgent Assistance Needed";
            this.initialBody = gen_saudi_prince(); 
        } else if (template === 'Google Sign in') {
            this.subject = "2-Step Verification turned on";
            this.initialBody = gen_sign_in();  
        }
    },
    mounted() {
        this.initialize_editor(this.initialBody); 
    },
    methods: {
        go_to(step) {
            if (step == 1) {
                window.location.href = 'index.html';
            } 
        },
        go_back() {
            window.location.href = 'index.html';
        },
        next() {
            // window.location.href = "enter_details.html?template=" + encodeURIComponent(this.template);
            const email_body = this.quill.root.innerHTML; 
            // console.log(email_body)
            const subject = encodeURIComponent(this.subject);
            const body = encodeURIComponent(email_body);
            
            window.location.href = `enter_details.html?template=${encodeURIComponent(this.template)}&subject=${subject}&body=${body}`;

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
            this.quill.setContents(this.quill.clipboard.convert(body)); 
        }
    }
});

app.mount('#app');
