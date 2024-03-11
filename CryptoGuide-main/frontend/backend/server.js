const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');  

require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const uri = "mongodb+srv://whitewater:4LWpNZFBrYV8iyF0@cluster0.onfbu8r.mongodb.net/Cryptodata?retryWrites=true&w=majority&appName=Cluster0"
mongoose.connect(uri, {useNewUrlParser: true});
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
})

const cryptoRouter = require('./routes/crypto');
const summaryRouter = require('./routes/summary');

app.use('/cryptos', cryptoRouter); 
app.use('/summaries', summaryRouter)

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
})
