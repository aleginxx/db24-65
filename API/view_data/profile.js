const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/profile', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
        if (err) {
            console.error('Error fetching admin data:', err);
            return res.status(500).send('Internal Server Error');
        }

        console.log("Results: ", results);
        
        if (results.length === 0) {
            const { username } = req.user;

            const query = 'SELECT * FROM cook WHERE username = ?'; 
            DB.connection.query(query, [username], (err, results) => { 
                if (err) {
                    console.error('Error fetching user data:', err);
                    return res.status(500).send('Internal Server Error');
                }

                const user = results[0]; 
                // console.log("user");
                // console.log(user);

                res.render(path.join(__dirname, '..', '..', 'frontend', 'user'), { user });
            });
        } else {
            const admin = results[0]; 
            // console.log("admin");
            // console.log(admin);

            res.render(path.join(__dirname, '..', '..', 'frontend', 'admin'), { admin });
        }
    });
});

module.exports = router;