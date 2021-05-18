var express = require('express');
var app = express();

const PORT = 3000;
app.set('views','./docs');
app.use(express.static('./docs/public'));

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/docs/index.html')
})

app.get(/\/(.+)/, function (req, res) {
    res.sendFile(__dirname + '/docs/' + RegExp.$1)
})

app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    console.log(err);
});

app.listen(PORT, () => {
    console.log('Connected to port ' + PORT);
});