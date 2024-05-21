const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

const router = express.Router();
router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'delete.html');

router.get('/delete', (req, res) => {
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
        res.sendFile(filePath);
      }
    });
});

router.post('/delete', (req, res) => {
    const tableName = req.body.tableName;
    const columnName = req.body.columnName;
    const columnValue = req.body.columnValue;

    const deleteQuery = `DELETE FROM ${tableName} WHERE ${columnName} = ?`;

    DB.connection.query(deleteQuery, [columnValue], (err, result) => {
        if (err) {
            console.error('Error executing search query:', err);
            return res.status(500).send('Error retrieving table data.');
        } else {
            res.status(200).send('Entry deleted successfully.');
        }
    });
});

module.exports = router;
