import unittest
import html2eml


class TestFromHtml(unittest.TestCase):
    params_and_headers = {'to': 'To', 'from_': 'From',
                          'cc': 'CC', 'bcc': 'BCC'}

    def test_content_type(self):
        msg = html2eml.from_html('')
        self.assertEqual(msg.get_content_type(), 'text/html')

    def test_default_charset(self):
        msg = html2eml.from_html('')
        self.assertEqual(msg.get_charset(), 'utf-8')

    def test_charset(self):
        test_charset = 'ISO-8859-1'
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
        self.assertEqual(msg['Subject'], message_subject)

    def test_subject_encoding(self):
        message_subject = 'p\xf6stal'
        msg = html2eml.from_html('', charset='ISO-8859-1',
                                 subject=message_subject)
        self.assertEqual(str(msg['Subject']), message_subject)

    def test_recipients_string(self):
        params = {
            param: '{}@test.com'.format(param)
            for param in self.params_and_headers
        }
        msg = html2eml.from_html('', **params)
        for param, header in self.params_and_headers.items():
            self.assertEqual(msg.get(header), params[param])

    def test_recipients_list(self):
        params = {
            param: [
                '{}{}@test.com'.format(param, i) for i in range(3)
            ] for param in self.params_and_headers.keys()
        }
        msg = html2eml.from_html('', **params)
        for param, header in self.params_and_headers.items():
            self.assertEqual(str(msg[header]).split('; '), params[param])


if __name__ == '__main__':
    unittest.main()
