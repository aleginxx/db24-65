const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/admin/', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const admin_username = decodedToken.username;

    const query = 'SELECT * FROM administrator WHERE admin_username = ?'; 
    DB.connection.query(query, [admin_username], (err, results) => { 
        if (err) {
            console.error('Error fetching admin data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            console.log("Admin results: ", results);
            return res.status(404).send('Admin not found');
        }
        const admin = results[0]; 

        res.render(path.join(__dirname, '..', '..', 'frontend', 'admin'), { admin });

    });
});

router.get('/admin/edit', cookieJwtAuth, (req, res) => {
    const { username } = req.user;

    console.log("req.user = ", req.user);

    const query = 'SELECT * FROM administrator WHERE admin_username = ?'; 
    DB.connection.query(query, [username], (err, results) => { 
        if (err) {
            console.error('Error fetching user data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            return res.status(404).send('Admin not found');
        }
        const admin = results[0]; 
        console.log("admin");
        console.log(admin);

        res.render(path.join(__dirname, '..', '..', 'frontend', 'admin-edit'), { admin });
    });
});


router.post('/admin/edit', cookieJwtAuth, (req, res) => {
    const { username, password } = req.body;

    console.log(req.body);

    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const query_id =   `SELECT admin_id FROM administrator WHERE admin_username = ?`

    const query_username = `
        UPDATE administrator 
        SET admin_username = ?, admin_password = ?
        WHERE admin_id = ?
    `;

    DB.connection.query(query_id, [username_check], (err, results) => { 
        if (err) {
            console.error('Error fetching admin data:', err);
            return res.status(500).send('Internal Server Error');
        }
        console.log("results for admin_id: ", results);

        if (results.length === 0) {
            return res.status(404).send('Admin not found');
        }

        const id = results[0]; 
        
        DB.connection.query(query_username, [username, password, id.admin_id], (err, results) => {
            if (err) {
                console.error('Error updating admin data:', err);
                return res.status(500).send('Internal Server Error');
            }
    
            req.user.username = username;
            const token = jwt.sign(req.user, process.env.MY_SECRET);
            res.cookie('token', token, { httpOnly: true });
    
            res.redirect('/dacontest/admin/');
        });
    });
});

module.exports = router;
