const express = require('express');
const router = express.Router();
const path = require('path');
const fs = require('fs');
const DB = require('./database.js');

router.get('/backup', (req, res) => {
    backupDatabase((err, result) => {
        if (err) {
            res.status(500).json({ error: 'Backup failed' });
            return;
        }
        res.json({ message: 'Backup completed successfully' });
    });
});

function backupDatabase(callback) {
    const backupFileName = 'backup.sql'; 
    const backupFilePath = path.join(__dirname, backupFileName);

    const backupStream = fs.createWriteStream(backupFilePath);

    DB.connection.query('SHOW TABLES', (err, tables) => {
        if (err) {
            console.error('Error retrieving tables:', err);
            callback(err, null);
            return;
        }

        tables.forEach(table => {
            const tableName = table['Tables_in_' + DB.connection.config.database];
            backupStream.write(`-- Table structure for ${tableName}\n`);
            backupStream.write(`SHOW CREATE TABLE ${tableName};\n\n`);
            backupStream.write(`-- Data for ${tableName}\n`);
            backupStream.write(`SELECT * FROM ${tableName};\n\n`);
        });

        backupStream.end();

        backupStream.on('finish', () => {
            console.log(`Backup completed. File saved as: ${backupFilePath}`);
            callback(null, true);
        });

        backupStream.on('error', err => {
            console.error('Error writing backup file:', err);
            callback(err, null);
        });
    });
}

module.exports = router;