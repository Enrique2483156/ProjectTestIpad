const http = require('http'); // loads the http module

http.createServer((request, response)=>{

    response.writeHead(200, {
        'Content-type':'text/plain'
    });
    
    response.write('Hello, world!');

    response.end();

}).listen(1337);



