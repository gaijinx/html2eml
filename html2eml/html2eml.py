import email


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
        msg[field_name] = email.header.Header(", ".join(recipients),
                                              header_name=field_name).encode()


def _prepare_header(s, charset):
    return email.header.Header(s, charset=charset).encode()
