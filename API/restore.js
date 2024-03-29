const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const DB = require('./database.js');

router.post('/restore', (req, res) => {
    const backupFilePath = path.join(__dirname, 'backup.sql'); 

    fs.access(backupFilePath, fs.constants.F_OK, (err) => {
        if (err) {
            console.error('Backup file not found');
            res.status(404).json({ error: 'Backup file not found' });
            return;
        }

        fs.readFile(backupFilePath, 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading backup file:', err);
                res.status(500).json({ error: 'Error reading backup file' });
                return;
            }

            DB.connection.query(data, (err, result) => {
                if (err) {
                    console.error('Error restoring database:', err);
                    res.status(500).json({ error: 'Error restoring database' });
                    return;
                }

                console.log('Database restored successfully');
                res.json({ message: 'Database restored successfully' });
            });
        });
    });
});

module.exports = router;
