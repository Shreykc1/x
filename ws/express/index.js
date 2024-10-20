const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const app = express();
app.use(express.json());
app.use(cors());

const dataFilePath = path.join(__dirname, 'data.json');

const readData = () => {
  const data = fs.readFileSync(dataFilePath, 'utf8');
  return JSON.parse(data);
};


const writeData = (data) => {
  fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2), 'utf8');
};


app.post('/addUser', (req, res) => {
  const { name, age } = req.body;

  if (!name || !age) {
    return res.status(400).json({ error: 'Please provide id, name, and age.' });
  }


  let data = readData();
  id = data.length + 1

  if (data.length === 0) {
    data = [{ id, name, age }];
  } else {
    data.push({ id, name, age });
  }

  writeData(data);

  res.status(201).json({ message: 'User added successfully', data });
});


app.get('/', (req, res) => {
  const data = readData();
  res.status(200).json(data);
});


const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
