import unittest
import html2eml


class TestEmlToMultipart(unittest.TestCase):
    def test_eml_to_multipart(self):
        eml = html2eml.from_html("<html><body><p>Spam</p></body></html>",
                                 to=["spam@example.com", "eggs@example.com"],
                                 from_="foo@example.com",
                                 subject="Tis but a scratch",
                                 cc=["bar@example.com", "baz@example.com"],
                                 bcc=["baz@example.com", "bar@example.com"])
        multipart = html2eml.convert_eml_to_multipart(eml)
        for field in ('To', 'From', 'CC', 'BCC', 'Subject'):
            self.assertEqual(multipart[field], eml[field])
        self.assertEqual(eml.get_charset(), multipart.get_charset())
        self.assertTrue(multipart.is_multipart())
        for part in multipart.walk():
            if part.get_content_type() == 'text/html':
                self.assertEqual(eml.get_payload(decode=True), part.get_payload(decode=True))
