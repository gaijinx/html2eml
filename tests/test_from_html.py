import unittest
import email.header

import html2eml


class TestFromHtml(unittest.TestCase):
    params_and_headers = {'to': 'To', 'from_': 'From',
                          'cc': 'CC', 'bcc': 'BCC'}

    def _decode_header(self, header):
        return email.header.decode_header(header)[0]

    def test_content_type(self):
        msg = html2eml.from_html('')
        self.assertEqual(msg.get_content_type(), 'text/html')

    def test_default_charset(self):
        msg = html2eml.from_html('')
        self.assertEqual(msg.get_charset(), 'utf-8')

    def test_charset(self):
        test_charset = 'iso-8859-1'
        msg = html2eml.from_html('', charset=test_charset)
        self.assertEqual(msg.get_charset(), test_charset)

    def test_valid_html_body(self):
        some_html = '<html><body><p>Test data</p></body></html>'
        msg = html2eml.from_html(some_html)
        self.assertEqual(
            msg.get_payload(decode=True).decode('utf-8'), some_html)

    def test_subject(self):
        message_subject = 'Some optional subject'
        msg = html2eml.from_html('', subject=message_subject)
        self.assertEqual(self._decode_header(msg['Subject'])[0].decode('utf-8'), message_subject)

    def test_subject_encoding(self):
        message_subject = b'p\xf6stal'
        test_charset = 'iso-8859-1'
        msg = html2eml.from_html('', charset=test_charset,
                                 subject=message_subject)
        decoded_header = self._decode_header(msg['Subject'])
        self.assertEqual(decoded_header[0], message_subject)
        self.assertEqual(decoded_header[1], test_charset)

    def test_recipients_string(self):
        params = {
            param: '{}@test.com'.format(param)
            for param in self.params_and_headers
        }
        msg = html2eml.from_html('', **params)
        for param, header in self.params_and_headers.items():
            self.assertEqual(str(msg[header]), params[param])

    def test_recipients_list(self):
        fields_to_test = ['to', 'cc', 'bcc']
        params = {
            param: [
                '{}{}@test.com'.format(param, i) for i in range(3)
            ] for param in self.params_and_headers.keys() if param in fields_to_test
        }
        msg = html2eml.from_html('', **params)
        for header in fields_to_test:
            self.assertEqual(str(msg[header]).split(','), params[header])

    def test_header_length(self):
        fields_to_test = ['to', 'cc', 'bcc']
        params = {
            param: [
                'long_email_address{}{}@test.com'.format(param, i) for i in range(50)
            ] for param in self.params_and_headers.keys() if param in fields_to_test
        }
        msg = html2eml.from_html('', **params)
        for header in fields_to_test:
            for part in str(msg[header]).split('\n'):
                self.assertLessEqual(len(part), email.header.MAXLINELEN)


if __name__ == '__main__':
    unittest.main()
