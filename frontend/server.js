const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fetch = require('node-fetch'); // REQUIRED for backend forwarding
const path = require('path');

const app = express();

app.use(cors());
app.use(bodyParser.json());

// Serve the form page
app.use(express.static(path.join(__dirname, 'public')));

// API to forward form data to Flask backend
app.post('/submit', async (req, res) => {
    const data = req.body;

    try {
        const response = await fetch('http://localhost:5000/submit', { // Use localhost during local development
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        res.json(result);
    } catch (error) {
        console.error('Error reaching Flask backend:', error);
        res.status(500).json({ error: 'Could not reach backend' });
    }
});

app.listen(3000, () => {
    console.log('Frontend running at http://localhost:3000');
});
