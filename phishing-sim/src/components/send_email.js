 // Assuming you have templates.js in the same directory
import { gen_company_lunch, gen_saudi_prince, gen_sign_in } from './templates.js';

const initialData = {
    name: 'Wall-E',
    location: 'Earth',
    about: [
      {
        insert:
          'A robot who has developed sentience, and is the only robot of his kind shown to be still functioning on Earth.\n',
      },
    ],
  };
  
  const quill = new Quill('#editor', {
    modules: {
      toolbar: [
        ['bold', 'italic'],
        ['link', 'blockquote', 'code-block', 'image'],
        [{ list: 'ordered' }, { list: 'bullet' }],
      ],
    },
    theme: 'snow',
  });
  
  const resetForm = () => {
    document.querySelector('[name="name"]').value = initialData.name;
    document.querySelector('[name="location"]').value = initialData.location;
    quill.setContents(initialData.about);
  };
  
  resetForm();
  
  const form = document.querySelector('form');
  form.addEventListener('formdata', (event) => {
    // Append Quill content before submitting
    event.formData.append('about', JSON.stringify(quill.getContents().ops));
  });
  
  document.querySelector('#resetForm').addEventListener('click', () => {
    resetForm();
  });

const app = Vue.createApp({
    data() {
        return {
            subject: "",
            email_link: "", // Link to be passed for each template if needed
            quill: null // Store the Quill instance
        };
    },
    created() {
        const urlParams = new URLSearchParams(window.location.search);
        const template = urlParams.get('template'); // Get template type from URL
        this.email_link = urlParams.get('link'); // Get link for the email body

        // Choose the template based on the type
        if (template === 'company_lunch') {
            this.subject = "Company Lunch Invitation";
            this.initialize_editor(gen_company_lunch(this.email_link));
        } else if (template === 'saudi_prince') {
            this.subject = "Urgent Assistance Needed";
            this.initialize_editor(gen_saudi_prince(this.email_link));
        } else if (template === 'verification_email') {
            this.subject = "2-Step Verification turned on";
            this.initialize_editor(gen_sign_in(urlParams.get('email'), this.email_link));
        }
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
