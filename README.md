# html2eml
[![Build Status](https://travis-ci.com/gaijinx/html2eml.svg?branch=master)](https://travis-ci.com/gaijinx/html2eml)
[![MIT License badge](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/gaijinx/html2eml/blob/master/LICENSE)

`html2eml` is a simple package for converting HTML text to EML format (MIME RFC 822).

# Getting started

Create simple message with `to` and `from` headers
```python
>>> import html2eml

>>> msg = html2eml.from_html('<html><body><p>Hello world</p></body></html>', to='spam@example.com', from_='eggs@example.com', subject='Sausage')

>>> print(msg.as_string())
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: base64
To: spam@example.com
From: eggs@example.com
Subject: =?utf-8?q?Sausage?=

PGh0bWw+PGJvZHk+PHA+SGVsbG8gd29ybGQ8L3A+PC9ib2R5PjwvaHRtbD4=
```

`html2eml` allows changing charset of html message
```python
>>> msg = html2eml.from_html('<html><body><p>Hello world</p></body></html>', charset='ISO-8859-1', to='spam@example.com')

>>> print(msg.as_string())
MIME-Version: 1.0
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable
To: spam@example.com

<html><body><p>Hello world</p></body></html>
```

Outside of `To` and `From` fields we can also specify `CC` and `BCC`
```python
>>> msg = html2eml.from_html('<html><body><p>Hello world</p></body></html>', to='foo@example.com', from_='bar@example.com', cc='spam@example.com', bcc='eggs@example.com')

>>> print(msg.as_string())
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: base64
To: foo@example.com
From: bar@example.com
CC: spam@example.com
BCC: eggs@example.com

PGh0bWw+PGJvZHk+PHA+SGVsbG8gd29ybGQ8L3A+PC9ib2R5PjwvaHRtbD4=
```

In case of multiple recipients we can pass a list in any of those fields
```python
>>> msg = html2eml.from_html('<html><body><p>Hello world</p></body></html>', to=['foo@example.com', 'spam@example.com', 'eggs@example.com'], from_='bar@example.com')

>>> print(msg.as_string())
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: base64
To: foo@example.com,spam@example.com,eggs@example.com
From: bar@example.com

PGh0bWw+PGJvZHk+PHA+SGVsbG8gd29ybGQ8L3A+PC9ib2R5PjwvaHRtbD4
```
