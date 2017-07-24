# python-euromsg
Python utility for sending email over euro.message (https://www.euromsg.com) service.

## Installation

```bash
$ pip install git+https://github.com/nazmizorlu/python-euromsg.git
```

## Usage

```python
>>> from euromsg import euromsg
>>> mailer = euromsg.EuromsgMailer("euromsg_user", "euromsg_password")
>>> resp = mailer.send_mail(u"From Person", "from@test.org", "reply@test.org", "To Person", "to@test.org", "Test Email Subject", """<html><head></head><body><p>Test HTML message</p></body></html>""")
>>> print(resp)  # resp is Post ID returned from euro.message
'A0CB0EB52948485690F565033C8186E1'
```
