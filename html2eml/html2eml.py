import email
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def from_html(html_text, charset='utf-8', to=None,
              from_=None, subject=None, cc=None, bcc=None):
    '''
    Creates new email.message.Message from given html_text and optional headers
    '''
    msg = email.message_from_string(html_text)
    msg.add_header('Content-Type', 'text/html')
    msg.set_charset(charset)

    _add_recipient_header(msg, to, 'To')
    _add_recipient_header(msg, from_, 'From')
    _add_recipient_header(msg, cc, 'CC')
    _add_recipient_header(msg, bcc, 'BCC')

    if subject:
        msg['Subject'] = _prepare_header(subject, charset=charset)

    return msg


def _add_recipient_header(msg, recipients, field_name):
    if recipients:
        if not isinstance(recipients, (list, tuple)):
            recipients = [recipients]
        msg[field_name] = Header(", ".join(recipients),
                                 header_name=field_name).encode()


def _prepare_header(s, charset):
    return Header(s, charset=charset).encode()


def convert_eml_to_multipart(eml_message):
    msg = MIMEMultipart()
    charset = str(eml_message.get_charset())
    msg.set_charset(charset)
    for field in ('To', 'From', 'CC', 'BCC', 'Subject'):
        if eml_message.get(field, False):
            msg[field] = eml_message[field]
    msg.attach(MIMEText(eml_message.get_payload(decode=True),
                        'html', charset))
    return msg
