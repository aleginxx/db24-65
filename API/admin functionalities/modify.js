const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

const router = express.Router();
router.use(bodyParser.json());

const port = 3000;

router.get('/modify',(req,res)=>{
    const filePath = path.join(__dirname, '..', '..' ,'frontend', 'modify.html');
    res.sendFile(filePath);
});

router.post('/modify', (req, res) => {
    const tableName = req.body.table; // Extracting the table name from the request body
    const query = `SELECT * FROM ${tableName}`; // Constructing the SQL query
    
    // Execute the query and handle the response
    DB.connection.query(query, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).send('Error retrieving table data.');
        } else {
            // Render HTML with the table data embedded
            let htmlResult = `<html><head><title>Table Data</title></head><body><table>`;
            
            // Add table headers
            htmlResult += `<tr>`;
            for (const column in result[0]) {
                htmlResult += `<th>${column}</th>`;
            }
            htmlResult += `</tr>`;

            // Add table entries
            result.forEach(row => {
                htmlResult += `<tr>`;
                for (const column in row) {
                    htmlResult += `<td>${row[column]}</td>`;
                }
                htmlResult += `</tr>`;
            });

            htmlResult += `</table></body></html>`;
            
            res.send(htmlResult);
        }
    });
});

module.exports = router;

