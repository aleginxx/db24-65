const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/make-admin', (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
      if (err) {
          console.error('Error fetching admin data:', err);
          return res.status(500).send('Internal Server Error');
      }
      if (results.length === 0) {
          return res.status(404).send('You do not have permission to access this page');
      }
      else {
        const filePath = path.join(__dirname, '..', '..', 'frontend', 'make_admin.html');
        res.sendFile(filePath);
      }
    });
});

router.post('/make-admin', (req, res) => {
    const username = req.body.username; 

    const select_row = `SELECT password FROM cook WHERE username = '${username}'`;

    DB.connection.query(select_row, (err, results) => {
        if (err) {
            console.error('Error querying the database:', err);
            if (err.code === 'ER_DBACCESS_DENIED_ERROR' || DB.connection.config.user !== 'root' || DB.connection.config.password !== '') {
                return res.status(401).send("Not Authorized");
            } else {
                return res.status(500).send('Internal Service Error');
            }
        }
  
      const admin_password = results[0].password;

      const insert_query = `INSERT INTO administrator (admin_username, admin_password) VALUES (?, ?)`;
  
      DB.connection.query(insert_query, [username, admin_password], (insertError, insertResult) => {
        if (insertError) {
          res.status(500).json({ error: insertError.message });
          return;
        }
        
        return res.status(200).redirect('/dacontest/make-admin');
      }); 
   });
});
  
module.exports = router;