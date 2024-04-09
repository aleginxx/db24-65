const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const router = express.Router();
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/profile', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.admin_username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
        if (err) {
            console.error('Error fetching admin data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            const { username } = req.user;

            const query = 'SELECT * FROM cook WHERE username = ?'; 
            DB.connection.query(query, [username], (err, results) => { 
                if (err) {
                    console.error('Error fetching user data:', err);
                    return res.status(500).send('Internal Server Error');
                }
                if (results.length === 0) {
                    return res.status(404).send('User not found');
                }
                const user = results[0]; 
                console.log("user");
                console.log(user);

                res.render(path.join(__dirname, '..', 'frontend', 'user'), { user });
            });
        } else {
            const admin_username = decodedToken.admin_username;

            const query = 'SELECT * FROM administrator WHERE admin_username = ?'; 
            DB.connection.query(query, [admin_username], (err, results) => { 
                if (err) {
                    console.error('Error fetching admin data:', err);
                    return res.status(500).send('Internal Server Error');
                }
                if (results.length === 0) {
                    return res.status(404).send('Admin not found');
                }
                const admin = results[0]; 

                res.render(path.join(__dirname, '..', 'frontend', 'admin'), { admin });

            });
        }
    });
});

module.exports = router;