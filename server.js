const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(bodyParser.json({ limit: '10mb' })); // Support large images

// Endpoint to save the snapshot
app.post('/save-snapshot', (req, res) => {
    const { image } = req.body;
    const folderPath = path.join(__dirname, 'student_list');

    // Check if the folder exists, create it if it doesn't
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath);
    }

    // Create unique file name
    const fileName = `snapshot_${Date.now()}.png`;
    const filePath = path.join(folderPath, fileName);

    // Decode base64 image and save it to the folder
    const base64Data = image.replace(/^data:image\/png;base64,/, "");
    fs.writeFile(filePath, base64Data, 'base64', (err) => {
        if (err) {
            console.error('Error saving image:', err);
            return res.status(500).send('Failed to save image.');
        }
        console.log('Snapshot saved:', filePath);
        res.send('Image saved successfully.');
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
