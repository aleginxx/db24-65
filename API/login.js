const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const { exec } = require('child_process');
const app = express();
const http = require('http');
const jwt = require("jsonwebtoken");

const router = express.Router();

router.get('/login', (req, res) => {
    const filePath = path.join(__dirname, '..', 'frontend', 'login.html');
    res.sendFile(filePath);
});

router.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    const capacity = req.body.capacity;

    console.log(req.body);

    if (capacity === 'user') {
        const query = 'SELECT * FROM cook WHERE username = ? AND password = ?';
        DB.connection.query(query, [username, req.body.password], (err, results) => {
            if (err) {
                console.error('Error querying the database:', err);
                if (err.code === 'ER_DBACCESS_DENIED_ERROR' || DB.connection.config.user !== 'root' || DB.connection.config.password !== '') {
                    return res.status(401).send("Not Authorized");
                } else {
                    return res.status(500).send('Internal Service Error');
                }
            }

            // console.log(results);

            if (results.length > 0) {
                const user = results[0]; 
                const payload = {
                    username: user.username
                };
                                
                const token = jwt.sign(payload, process.env.MY_SECRET, { expiresIn: "1h" });
                res.cookie("token", token);

                return res.redirect(`/dacontest/home`);
            } else {
                res.status(401).redirect('/dacontest/login');
            }
        });
    } else {
        const query = 'SELECT * FROM administrator WHERE admin_username = ? AND admin_password = ?';
        DB.connection.query(query, [req.body.username, req.body.password], (err, results) => {
            if (err) {
                console.error('Error querying the database:', err);
                if (err.code === 'ER_DBACCESS_DENIED_ERROR' || DB.connection.config.user !== 'root' || DB.connection.config.password !== '') {
                    return res.status(401).send("Not Authorized");
                } else {
                    return res.status(500).send('Internal Service Error');
                }
            }
            console.log("Admin Results: ", results);

            if (results.length > 0) {
                const admin = results[0]; 

                const payload = {
                    username: admin.admin_username
                };
                                
                const token = jwt.sign(payload, process.env.MY_SECRET, { expiresIn: "1h" });
                res.cookie("token", token);

                return res.redirect(`/dacontest/home`);
            } else {
                res.status(401).redirect('/dacontest/login');
            }
        });
    }
});

module.exports = router;