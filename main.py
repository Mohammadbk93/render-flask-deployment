from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import smtplib

# Load environment variables from .env
load_dotenv()

# Read sensitive information from environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        age = request.form.get("age")
        message = request.form.get("message")

        # Construct email
        email_subject = "New Contact Form Submission"
        email_body = f"Name: {name}\nAge: {age}\nMessage:\n{message}"

        # Send email
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
            print(e)
            return render_template("contact.html", error=True)

    return render_template("contact.html", success=False, error=False)

if __name__ == "__main__":
    app.run(debug=True)
