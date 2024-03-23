const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const { exec } = require('child_process');
const app = express();
const http = require('http');

const router = express.Router();
router.use(bodyParser.json());

const port = 3000;

router.get('/login', (req, res) => {
    //const filePath = path.join(__dirname, '..', 'frontend', 'credentials.html');

    //exec(filePath, (error, stdout, stderr) => {
    //    if (error) {
    //        console.error(`Error executing HTML file: ${error.message}`);
    //        return res.status(500).send('Internal Server Error');
    //    }
    //    res.send(stdout);
    //});
    http.createServer(app).listen(port, () => {
        console.log(`Accessed login`);
    });

});

router.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password + '\r';

    const query = 'SELECT * FROM cook WHERE username = ? AND password = ?';
    DB.connection.query(query, [username, password], (err, results) => {
        if (err) {
            console.error('Error querying the database:', err);
            if (err.code === 'ER_DBACCESS_DENIED_ERROR' || DB.connection.config.user !== 'root' || DB.connection.config.password !== '') {
                return res.status(401).send("Not Authorized");
            } else {
                return res.status(500).send('Internal Service Error');
            }
        }

        console.log(results);

        if (results.length > 0) {
            return res.json();
            //res.redirect('/dacontest/home');
        } else {
            res.status(401).send('poutsa');
            //res.status(401).redirect('/dacontest/login');
        }
    });
});

router.get('/home', (req, res) => {
    const filePath = path.join(__dirname, '..', 'frontend', 'home.html');

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing HTML file: ${error.message}`);
            return res.status(500).send('Internal Server Error');
        }
        res.send(stdout);
    });
});


module.exports = router;