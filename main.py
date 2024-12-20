from dotenv import load_dotenv
from flask import Flask, render_template, request
import smtplib

load_dotenv(dotenv_path=".venv/.env")

app = Flask(__name__)

# Replace these values with your own email configuration
EMAIL_ADDRESS = "mohammadbagheri07@gmail.com"
EMAIL_PASSWORD = "zhrjbvoboyjwrrvi"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        message = request.form.get("message")

        # Construct the email message
        email_subject = "New Contact Form Submission"
        email_body = f"Name and Surname: {name}\nAge: {age}\nMessage:\n{message}"

        # Send the email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
                connection.starttls()
                connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL_ADDRESS,
                    to_addrs=EMAIL_ADDRESS,
                    msg=f"Subject:{email_subject}\n\n{email_body}"
                )
            return render_template("contact.html", success=True)
        except Exception as e:
            # If email sending fails, print the error and show error message
            print(e)
            return render_template("contact.html", error=True)

    return render_template("contact.html", success=False, error=False)

if __name__ == "__main__":
    app.run(debug=True)
