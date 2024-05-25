# FRONTEND

### Contents:

The FRONTEND was constructed using the [HTML](https://html.com/) and [EJS](https://ejs.co/) programming languages.

### Installation:

```bash
npm install --save body-parser
```

### Usage:
The integration of .html files in the endpoint is applied through command ```res.sendFile(filePath)``` in the [GET method](https://expressjs.com/en/guide/routing.html), while the integration of .ejs files in the frontend requires module  `body-parser`. For that purpose, the second connection between API and frontend is realized through the following command:
```bash
res.render(path.join(__dirname, '..', 'frontend', 'file_name'), { sent_data });
```
(sent_data could be omitted).

After running MySQL and Apache modules in [xampp](https://www.apachefriends.org/download.html), selecting DB `mydb` and running command ```node app.js``` through the API file in terminal, the user is now able to access the frontend through URL: ```localhost:9876/dacontest/```.