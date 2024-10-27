from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/send_email": {"origins": "*"}})  


@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'CORS preflight'}), 200
    data = request.json
    # sender_email = data['sender_email']
    # email_password = data['email_password']
    sender_email = "baitbox001@gmail.com"
    email_password = "Tylhenatjnhvqykq"
    recipient_email = data['recipient_email']
    subject = data['subject']
    email_body = data['email_body']
    user_link = data['email_link']   

    email_body = email_body.replace("www.replaceme.com", user_link)
    email_body = email_body.replace("replaceme@gmail.com", recipient_email)
    msg = MIMEText(email_body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    print(email_body)
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, email_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return jsonify({'status': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

