from botocore.exceptions import ClientError

from src.utils.aws_session import AwsSession


def send(recipients):
    sender = "Sender Name <no-reply@binoqlars.com>"

    # The subject line for the email.
    subject = "Amazon SES Test (SDK for Python)"

    # The email body for recipients with non-HTML email clients.
    body_text = (
        "Amazon SES Test (Python)\r\n" "This email was sent with Amazon SES using the " "AWS SDK for Python (Boto)."
    )

    # The HTML body of the email.
    body_html = """
        <html>
        <head></head>
        <body>
            <h1>Amazon SES Test (SDK for Python)</h1>
            <p>This email was sent with
                <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
                <a href='https://aws.amazon.com/sdk-for-python/'>AWS SDK for Python (Boto)</a>.
            </p>
        </body>
        </html>
    """

    # The character encoding for the email.
    charset = "UTF-8"

    # Create a new SES resource and specify a region.

    client = (
        AwsSession.instance()
        .get_session()
        .client(
            service_name="ses",
            region_name="us-east-1",
        )
    )

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                "ToAddresses": recipients,
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": charset,
                        "Data": body_html,
                    },
                    "Text": {
                        "Charset": charset,
                        "Data": body_text,
                    },
                },
                "Subject": {
                    "Charset": charset,
                    "Data": subject,
                },
            },
            Source=sender,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        return e.response["Error"]["Message"]
    else:
        return "Email sent! Message ID:" + response["MessageId"]
