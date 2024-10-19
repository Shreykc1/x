const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const app = express();

app.use(express.json());
app.use(cors());
// Path to the local data.json file
const dataFilePath = path.join(__dirname, 'data.json');

// Helper function to read data from data.json
const readData = () => {
  const data = fs.readFileSync(dataFilePath, 'utf8');
  return JSON.parse(data);
};

// Helper function to write data to data.json
const writeData = (data) => {
  fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2), 'utf8');
};

// POST route to insert or append data
app.post('/addUser', (req, res) => {
  const { name, age } = req.body;

  if (!name || !age) {
    return res.status(400).json({ error: 'Please provide id, name, and age.' });
  }

  // Read current data
  let data = readData();
  id = data.length + 1
  // Check if data is empty
  if (data.length === 0) {
    // Insert new array with the object if the data is empty
    data = [{ id, name, age }];
  } else {
    // Append the new object if data already exists
    data.push({ id, name, age });
  }

  // Write updated data back to the file
  writeData(data);

  res.status(201).json({ message: 'User added successfully', data });
});

// GET route to retrieve all users
app.get('/', (req, res) => {
  const data = readData();
  res.status(200).json(data);
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
