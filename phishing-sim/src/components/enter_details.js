const app = Vue.createApp({
    data() {
        return {
            template: "",
            sender_email: "",
            email_password: "",
            recipient_email: "",
            subject: "",
            email_body: "",
            template: "",
            email_link: ""
        };
    },
    created() {
        const urlParams = new URLSearchParams(window.location.search);
        this.template = urlParams.get('template');
        const subjectParam = urlParams.get('subject');
        const bodyParam = urlParams.get('body');

        console.log("Raw Body Parameter:", bodyParam); 
        try {
            this.subject = decodeURIComponent(subjectParam);
            this.email_body = bodyParam;
            // console.log(this.email_body)
        } catch (error) {
            console.error("Error decoding URL parameters:", error);
        }
    },
    methods: {
        go_to(step) {
            if (step == 1) {
                window.location.href = 'index.html';
            } else if (step == 2) {
                window.location.href = "edit_email.html?template=" + encodeURIComponent(this.template);
            }
        },
        async send() {
            try {
                const emailData = {
                    sender_email: this.sender_email,
                    email_password: this.email_password,
                    recipient_email: this.recipient_email,
                    subject: this.subject,
                    email_body: this.email_body,
                    email_link: this.email_link  
                };
                
                const response = await fetch('http://127.0.0.1:5000/send_email', {
                // const response = await fetch('/send_email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(emailData)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    // shows "Email sent successfully!"
                    alert(result.status); 
                } else {
                    alert("Error: " + result.error);
                }
            } catch (error) {
                console.error("Error sending email:", error);
                alert("Failed to send email.");
            }
        }
    }
});

app.mount('#app');
