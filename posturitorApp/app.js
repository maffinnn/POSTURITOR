const http = require('http');
const url = require('url');
const fs = require('fs');
const querystring = require('querystring');
const { spawn } = require('child_process');

const app = http.createServer();


fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err; 
    }       
    let ref = true;
    app.on('request', async (req, res) => {  

        const method = req.method;
        const {pathname, query} = url.parse(req.url, true);

        res.writeHeader(200, {"Content-Type": "text/html"});  
        res.write(html); 
        let post='';
        if (req.method == 'POST') {
              let body = '';
              req.on('data', function (data) {
                  body += data;
              });
              req.on('end', function () {
            //-------------parsing data from json to string-------------------------
                  post = JSON.parse(body);
                  var data = post.replace(/^data:image\/\w+;base64,/, "");
                  var buf = Buffer.from(data, 'base64');
                  ref = writeFileToSystem(buf, ref);
              });

              const python = spawn('python', ['eval.py']);
              python.stdout.on('data', function (data) {
                console.log('Pipe data from pyhton script ...');
                let dataToSend = data.toString();
                console.log(dataToSend);
                // res.write(dataToSend);
              })
          
         }
 
         res.end();  
    }).listen(8000);
    console.log("Server is listening...");
    
});

function writeFileToSystem(buf, ref){
    let path = "";
    if (ref) { path += "./images/reference.jpg"; }
    else path += "./images/posture.jpg";
     fs.writeFile(path, buf, function(err) {
         console.log("The file was saved!");
     });
     return false;
 }

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}



