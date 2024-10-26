from helper import prompt, return_date

def template():
    email()
    # received = prompt("[1] for email templates [2] for other: ")
    # if received == '1':
    #     email()
    # elif received == '2':
    #     print("TBD")
    # else:
    #     print("Unknown command")

def email():
    template = prompt("[1] for sign in attempt, [2] for saudi prince scam, [3] for company lunch: ")
    link = prompt("Link: ")
    name = ""
    if template == 1:
        name = "generic_sign_in"
        receiver = prompt("Receiver's email (not yours): ")
        html_content = gen_v_email_template(email, link)
    elif template == 2:
        name = "saudi_prince"
        html_content = gen_saudi_prince(link)
    elif template == 3:
        name = "company_lunch"
        html_content = gen_company_lunch(link)
    else:
        print("unknow command")
        return
    create_html_file(name, html_content)
    
def gen_company_lunch(link):
    date = return_date()
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Lunch Invitation</title>
</head>
<body style="font-family: Arial, sans-serif; color: #333;">
    <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; background-color: #f9f9f9;">
        <h2 style="color: #003366; text-align: center;">Upcoming Company Lunch</h2>
        
        <p>Hello Team,</p>

        <p>We’re excited to announce an upcoming company lunch next week on {date}! It’ll be a great opportunity for everyone to relax, enjoy some delicious food, and catch up with colleagues.</p>

        <p>Please click the link below to view the menu and make your meal selection in advance:</p>

        <p style="text-align: center; margin: 20px;">
            <a href="{link}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #0066cc; text-decoration: none; border-radius: 4px;">View Menu and Select Your Meal</a>
        </p>

        <p>We look forward to seeing you all there! If you have any questions, feel free to reach out to HR.</p>

        <p>Best Regards,<br>
        <strong>Jamie Lee</strong><br>
        Office Administrator</p>
    </div>
</body>
</html>
"""

def gen_saudi_prince(link):
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Urgent Assistance Needed</title>
</head>
<body style="font-family: Arial, sans-serif; color: #333;">
    <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; background-color: #f9f9f9;">
        <h2 style="text-align: center; color: #003366;">Request for Confidential Assistance</h2>
        <p>Dear Friend,</p>

        <p>I am Prince Abdulaziz Al-Saud from the Kingdom of Saudi Arabia. I reach out to you with utmost confidence and trust, as I am in urgent need of your assistance for a matter of great importance.</p>

        <p>Due to unforeseen circumstances, I am temporarily unable to access my financial assets, amounting to USD 25,000,000. With your cooperation, I hope to transfer these funds to your account for safekeeping. You will be rewarded with a generous 20% of the total amount as a token of my gratitude.</p>

        <p><strong>To proceed, please respond with your full name, contact number, and bank details at your earliest convenience.</strong></p>

        <p>Thank you for your time and consideration. I eagerly await your positive response.</p>

        <p>Sincerely,</p>
        <p><strong>Prince Abdulaziz Al-Saud</strong><br>
        Kingdom of Saudi Arabia</p>

        <div style="text-align: center; margin-top: 20px;">
            <a href="{link}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #003366; text-decoration: none; border-radius: 4px;">
                Confirm Details
            </a>
        </div>
    </div>
</body>
</html>
    """

def gen_v_email_template(email, verification_link):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="format-detection" content="email=no"/>
        <meta name="format-detection" content="date=no"/>
        <style>
            .awl a {{ color: #FFFFFF; text-decoration: none; }} 
            .abml a {{ color: #000000; font-family: Roboto-Medium,Helvetica,Arial,sans-serif; font-weight: bold; text-decoration: none; }} 
            .adgl a {{ color: rgba(0, 0, 0, 0.87); text-decoration: none; }} 
            .afal a {{ color: #b0b0b0; text-decoration: none; }}
            @media screen and (min-width: 600px) {{
                .v2sp {{ padding: 6px 30px 0px; }} 
                .v2rsp {{ padding: 0px 10px; }}
            }}
            @media screen and (min-width: 600px) {{
                .mdv2rw {{ padding: 40px 40px; }}
            }}
        </style>
    </head>
    <body style="margin: 0; padding: 0;" bgcolor="#FFFFFF">
        <table width="100%" height="100%" style="min-width: 348px;" border="0" cellspacing="0" cellpadding="0" lang="en">
            <tr height="32" style="height: 32px;"><td></td></tr>
            <tr align="center">
                <td>
                    <table border="0" cellspacing="0" cellpadding="0" style="padding-bottom: 20px; max-width: 516px; min-width: 220px;">
                        <tr>
                            <td width="8" style="width: 8px;"></td>
                            <td>
                                <div style="border-style: solid; border-width: thin; border-color:#dadce0; border-radius: 8px; padding: 40px 20px;" align="center">
                                    <img src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png" width="74" height="24" aria-hidden="true" style="margin-bottom: 16px;" alt="Google">
                                    <div style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom: thin solid #dadce0; color: rgba(0,0,0,0.87); line-height: 32px; padding-bottom: 24px;text-align: center; word-break: break-word;">
                                        <div style="font-size: 24px;">2-Step Verification turned on</div>
                                        <table align="center" style="margin-top:8px;">
                                            <tr style="line-height: normal;">
                                                <td align="right" style="padding-right:8px;">
                                                    <img width="20" height="20" style="width: 20px; height: 20px; vertical-align: sub; border-radius: 50%;" src="https://lh3.googleusercontent.com/a/ACg8ocJJADxTQu21YeuE7NqdcM_CmSkrGG9lds6Ey80wKJgg0kVr1Q=s96-c" alt="">
                                                </td>
                                                <td>
                                                    <a style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.87); font-size: 14px; line-height: 20px;">{email}</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                    <div style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 14px; color: rgba(0,0,0,0.87); line-height: 20px;padding-top: 20px; text-align: left;">
                                        <p>Your Google Account {email} is now protected with 2-Step Verification. When you sign in on a new or untrusted device, you’ll need your second factor to verify your identity.</p>
                                        <p><b>Don't get locked out!</b><br>You can add a backup phone or get backup codes to use when you don’t have your second factor with you.</p>
                                        You can <a href="{verification_link}" style="text-decoration: none; color: #4285F4;" target="_blank">review your 2SV settings</a> to make changes.
                                    </div>
                                </div>
                            </td>
                            <td width="8" style="width: 8px;"></td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

def create_html_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"✍(◔◡◔) {filename} created ✅")