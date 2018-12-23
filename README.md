
- Email notification with help sendgrid.com (https://github.com/sendgrid/sendgrid-python)

* create .env
```dotenv
SENDGRID_API_KEY=
FROM_EMAIL=
SUBJECT=
```

```bash
docker-compose up -d
```
* required field 
```
email
tel
body
answer
```
* EXAMPLE
```
# HTML
<form>
<input name="email" type="email" required>
<input name="tel" type="tel" required>
<textarea name="body" rows="4"></textarea>
<input name="answer" type="textarea" required>
<button type="submit" id="submit" required>Отправить</button>
</form>
# JS
var formData = $(form).serialize();
$.getJSON('http://127.0.0.1:5441/mail?' + formData)
```
