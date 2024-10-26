from helper import generate_intro, prompt
from template_maker import template
from send_mail import send_mail

def main():
    print(generate_intro())
    # input = prompt("[1] for templates" + f"\n" + "[2] for sending emails: ")
    input = prompt("[1] for templates, [2] for sending emails: ")
    if input == '1':
        template()
    else:
        # send email
        print("send email")
        send_mail()



if __name__ == '__main__':
    while 1:
        main()
