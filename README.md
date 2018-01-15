# TOP News: Real Time News Scraping and Recommendation System

* Implemented a data pipeline which monitors, scrapes and dedupes latest news (MongoDB, Redis, RabbitMQ);
* Designed data monitors for obtaining latest news from famous websites and recommend to web server.
* Successfully fetch useful data from original news websites by building news scrapers.
* Build dedupers which filter same news by using NLP (TF-IDF) to analyze similarities of articles scraped from news websites.
* Use Tensorflow for machine learning which can shows news according to users interests.
Build a single-page web.
 
***

# Week 1 React FrontEnd Build Up

## De-Couple into Components

![App Structure](image/app_structure.png)

* Base : Whole React App (Navbar + App)
* App : Image(title) + NewsPanel
* NewsPanel : Concludes many NewsCard such as News Lists (While user scorlling, backend send new NewsCard continously)
* NewsCard : Single News adding into NewsPanel with News image, News title, News contents, News description, News Tage and Links to News.

## Install & Init Environment
### Create React App - likes Angular cli (recommened by Facebook)
[Create React App](https://reactjs.org/blog/2016/07/22/create-apps-with-no-configuration.html)
* Deal with webpack and give a whole framework

- Install CRA (Global) : Local Developing Tool
```
sudo npm install -g create-react-app
```
- Create a new React App
```
create-react-app top-news
```
- Test Connection
```
cd top-news
npm start
```

## App
- public : images
- src : Each Component has its own folder
```
App / App.js
```
### App.js
- There is only one div tag in render function
- import React , './App.css', CSS file and logo
- Use "className" instead of "class" : Since in ES6, we use class for define a App class
- 

```js
import React from 'react';
import './App.css';
import logo from './logo.png';

class App extends React.Component {
  render() {
    return(
      <div>
        <img className = 'logo' src = {logo} alt = 'logo'/>
        <div className = 'container'>
             {/* TODO */}
        </div>
      </div>
    ); 
  }
}

export default App;
```
* Why use "default App"?
* If not, while you want to import App from other file, you need to type : 
```js
import { App } from './App.js';
```
* But if you have default, you could get rid of {}

- CSS setup
```css
.App {
  text-align: center;
}

.logo {
  display: block;
  margin-left: auto;
  margin-right: auto;
  padding-top: 30px;
  width: 20%;
}
```
### Materialize CSS Design
- install in Client sie
```
npm install materialize-css --save
```
- Import 
```js
import 'materialize-css/dist/css/materialize.min.css';
```
### index.js in Client Side
- Build a index.js for starting the client side
```
touch src/index.js
```
- index.js
```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App/App';

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```


- Where is root?
* public -> index.html
```html
<div id="root"></div>
```

## NewsPanel
### Save all NewsCard and connect with BackEnd
- Create NewsPanel folder and NewsPanel.js
```
mkdir src/NewsPanel
code src/NewsPanel/NewsPanel.js
```
```js
import React from 'react';
import './NewsPanel.css';
```

- Since we Need to save the News content, we need an internal variable (need constructor)

```js
class NewsPanel extends React.Component {
  constructor() {
    super();
    this.state = { news: null };
  }
```

- state = {news: null} -> lists of JSON
- Render conditions : there is a news and then create a NewsCard or show the loading message
```js
render() {
    if (this.state.news) {
      return (
        <div>
          {this.renderNews()}
        </div>
      );
    } else {
      return (
        <div>
          Loading ...
        </div>
      );
```
- local function, renderNews() : Render out the News and dynamactiy deal with the NewCards.
* Clickable - Use A tag in HTML
* Key - in React, if you would like to use a list, need to give a 'key' since the Virtual DOM need to know which items were changed in lists and just change that item insteads of renewing all items.
* "list-group-item" needs to be put into "list-group" and show the {news_list} in list group

- Get All News from state news -> Make all news in list -> Make all news become a NewsCard -> Put NewsCards into list-group

```js
renderNews() {
    const news_list = this.state.news.map(news => {
      return (
        <a className = 'list-group-item' key = {news.digest} href = '#'>
          <NewsCard news = {news} />
        </a>  
      );
    });

    return (
      <div className = 'container-fluid'>
        <div className = "list-group">
          {news_list}
        </div>  
      </div>
    );
  }

```

- local function, loadMoreNews() : Get News from backend - init load. (Now we gave a mock data)

```js
loadMoreNews() {
  this.setState({
    news : [
      {....data
      }]
  });
}
```
- After render() was ran, it will execute componentDidMount() -> Load News in state
```js
  componentDidMount () {
    this.loadMoreNews();
  }
```

- Import NewsCard
```js
import NewsCard from '../NewsCard/NewsCard';
```
- Export NewPanel
```js
export default NewsPanel;
```
### Add NewsPanel CSS
- By default for future using
```
touch src/NewsPanel/NewsPanel.css
```

### Import NewsPanel into App.js
- App.js
```js
import NewsPanel from '../NewsPanel/NewsPanel';

<div className = 'container'>
    <NewsPanel />
</div>
```

## NewsCard - Show UI
- Create NewsCard Component Folder
```
mkdir src/NewsCard
touch src/NewsCard/NewsCard.js
src/NewsCard/NewsCard.css
```
- class NewsCard (For HTML contents)
```js
class NewsCard extends React.Component {
  render() {
    return(
  HTML....
```

### HTML Structure
* news-container
* row
* col s4 fill
* image
* col s8
* news-intro-col
* news-intro-panel
* news-description
* news-chip

- onClick -> redirectToUrl()
```js
  redirectToUrl(url, event) {
    event.preventDefault();
    window.open(url, '_blank');
  }
```
- Get the data from props.news from NewsPanel.js
```js
  <h4>
     {this.props.news.title}
  </h4>
```

- NewsCard could get the data from NewsPanel since it was passed from :
```js
  <a className = 'list-group-item' key = {news.digest} href = '#'>
    <NewsCard news = {news} />
  </a>  
```

- Dont get chips if there is no source (this.props.news.source != null &&)
```js
 {this.props.news.source != null && <div className='chip light-blue news-chip'>{this.props.news.source}</div>}
 ```

- CSS file
```css
.news-intro-col {
  display: inline-flex;
  color: black;
  height: 100%;
}

CSS....
```
## Refactor
- Create a web_server file and move top-news which was renamed "client" into it
```
mkdir web_server
mv top-news/ ./web_server/client
```
## Continuous loading News (Server-Side REST API - NodeJS & Client-Side - React) 

- Deploy to AWS, there is no different likes server and client.

- Create React App provide "Development Server" for developing, but we wont use this to serve Users

- Development: Node Server + Development Server
- Publishment: Node Server + build (built by React App)

### Express application generator - NodeJS Server
[Express Application Generator](https://expressjs.com/en/starter/generator.html)
- Install Globally
```
sudo npm install express-generator -g
```

- Create a Server in web_server
```
express server  //   Usage: express [options] [dir]
```
- Install dependencies
```
cd server
npm install
npm start
```

### Configue App.js (defualtly installed lots of requirements)

- Delete :
* bodyParser: POST Request
* cookieParser: Authentication
* logger: Login
* users: Login

- Change views engine
* Put the default folder to /client/build
```js
app.set('views', path.join(__dirname, '../client/build'));
```

- Express Static : Find the image **** Find Bug!!!!! -> missing:  '/static'
```js
app.use('/static', 
    express.static(path.join(__dirname, '../client/build/static')));
```

- Client Webpack: Build a build folder for server to use
```
npm run build
```
* static - css
* static - js

- Error Handler
```js
app.use(function(req, res, next) {
  res.status(404);
});
```

- package.json : change start
```json
  "scripts": {
    "start": "nodemon ./bin/www"
  },
```
## Server - Routes/index.js receive index.html from build

- Since init run the '/', redirect to the routes/ index.js
```
app.use('/', index);
```
- index.js : send index.html from build to server side
* Get home page!

```js
var express = require('express');
var router = express.Router();
var path = require('path';)

router.get('/', function(req, res, next) {
  res.sendFile("index.html", 
  { root: path.join(__dirname, '../../client/build')});
});

module.exports = router;

```
- bin -> www : Place for init the App.

## restAPI for sending backend data from server


### News Routes
- In routes/news.js
```
touch server/routes/news.js
```

- Give a mock data here and send as a JSON file
```js
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  news = [
    .....DATA
  ];
 res.json(news);
  ]
});

module.exports = router;
```
- In app.js require the news Route
```js
var news = require('./routes/news');
app.use('/news', news);
```

## Client Side Requests localhost:3000/news to get those JSON data(client/NewsPanel)

- NewsPanel.js -> loadMoreNews() with backEnd
* Cache: False -> if true, it might show the old news from cache
* news_url -> window.location.hostname
* 'http://' + window.location.hostname + ':3000' + '/news'
* method: GET
```js
const news_url = 'http://' + window.location.hostname + ':3000' + '/news';

const request = new Request(news_url, {method:'GET', cache:false});
```
- Fetch + .then : Http Request & Promise
* res.json -> Ansynchrons : so we need another ".then" 調用JSON
* After we got JSON, deal with the news data
* If there is no news on web, directly give the new one, but if not, "concat" to the old ones

```js
fetch(request)
    .then(res => res.json())
    .then(news => {
      this.setState({
          news: this.state.news ? this.state.news.concat(news) : news,
      });
  });
```
## Open Both Client and Server side localhost for developing!

### Access-Control-Allow-Origin
- Since we couldn't cross localhost:3000 and localhost:3001 ! Run in the different PORT.

- Temporarily access to run in different PORT
* (BUT NEED TO BE REMOVED WHEN FINAL PUBLISH)
* app.js
```js
app.all('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  next();
});
```

```
Failed to load http://localhost:3000/news: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:3001' is therefore not allowed access.
```

## Scrolling
- Keep using loadMoreNews by combining Scroll EventListener

```
-             |          |  -
document.     |          |  |
body.         |          | ScrollY
offestHeight  |          |  |
|             |__________|  _
|             |          |  -
|             |          | window.innerHeight
-             |__________|  _
```         

- window.innerHeight + scrollY >= document.body.offsetHeight - 50 means when touch the boundry of bottom -> load more News
- Couldn't use "this.loadMoreNews()" until you change handleScroll to arrow function
```js
 window.addEventListener('scroll', () => this.handleScroll);
```

- handleScroll()

```js
  handleScroll() {
    const scrollY = window.scrollY 
      || window.pageYOffset
      || document.documentElement.scrollYTop;
    if((window.innerHeight) + scrollY) >= (document.body.offsetHeight - 50);
  }

```
- DONT FORGET THE () -> THIS.HANDLESCROLL()
```js
  componentDidMount() {
    this.loadMoreNews();
    window.addEventListener('scroll', () => this.handleScroll());
  }
```
## Debounce 去抖動

[Lodash](https://lodash.com/)

- Install Lodash inclient
```
npm install lodash --save
```

- Solve the Scroll frequent problems (Scroll Events happened too much)
* Send several requests to backend too frequently
```js
import _ from 'lodash';

  componentDidMount() {
    this.loadMoreNews();
    this.loadMoreNews = _.debounce(this.loadMoreNews, 1000);
    window.addEventListener('scroll', () => this.handleScroll());
  }
```
***


# SOA (Service Oriented Architrcture)
#### All service interfaces should be designed for both internal and external users
```
Benefit:
Isolation - language / technology / tools / 
        decoupleing / independency / deployment / maintenance
Ownership - minimal gray area and gap
Scalability - easy to scale up and modify
=======
Con:
Complexity - sometimes unnecessary
Latency - network communication eats time
Test effort - all services require E2E tests
DevOp : On-call!!!
```
- Example:
* Often built as a three tier architecture:
```
   [Desktop User]
        |
 [Presentation Tier] : Client interatcion via a web browser
        | 
    [Logic Tier] : provide the appliction's 
        |          functionality via detailed processing
   |Storage Tier|: handle persisting and retrieving application data                

```
#### Unfortucately things get more complicated: Comflict!!!!!!!!!
* Ohter types of users
* Attachments
* Bulk operations
* Data pipelines
* Notifications
* Monitoring
* Testing
```
Mobile          Destop      UI
User            User       Test
            \     |       /
Chrome
Extension  -  Presentation -    Prober
                 Tier
File                          File
Upload      \      |     /   Download
                 Logic    
Notifica-   -    Tier    -  Command
tions                       Line Tool
          /       |       \
CSV             Storage        CSV    
Upload            Tier        Download
          /               \
Data                           Data
Provider                      Consumer
```

#### With SOA:
* Fort-end Service handles all external interactions
* Back-end implements one protocol to talk to front-end
* All clients see same business abstraction
* Consistent business logic enforcement
* Easy internal refactoring

![SOA Structure](image/SOA_structure.png)

***


# Week 2 Backend Service
- Servive + PRC
```

|| Client ||  || Node Server ||  || Backend Server ||  || Redis || || MongoDB ||  || ML Server ||
    |                 |                 | Check if in Redis  |            |              |
    |---------------> |                 |<------------------>|            |              |
    | fetch more news |---------------->|    (If not) get news from DB    |              |                 
    |(userID/ pageNum)| getNewsSunmmaire|<------------------------------->|              |
    |                 | sForUser        |       Get Recommended news from ML server      |
    |<----------------|(userID /pageNum)|<---------------------------------------------->|
    | Sliced News     |                 |Store combined news |            |              |                   
    |                 |<----------------|       in Redis     |            |              |
    |                 | Sliced News     |------------------->|            |              |
    |                 |                 |                    |            |              |
|| Client ||  || Node Server ||  || Backend Server ||  || Redis || || MongoDB ||  || ML Server ||

```
* Backend Server - RPC Server
* Node Server - RPC Server
* MongoDB
* CloudAMQP
* News API
* Pylint and PEP 8 

## BackEnd Server
- Copy Week 5 to Week 6
```
cp -r week5 / week6
```
- Open a file backend_server and a service.py
``` 
mkdir backend_server
touch backend_server/service.py
```
### JSONRPClib library
- Build a Client or Server to send or receive RPC Request
- Not have a good support to Python 3.5, so we need a jsonrpclib-pelix to help development
[JSONRPClib](https://github.com/joshmarshall/jsonrpclib)
[JSONRPClib-pelix](https://pypi.python.org/pypi/jsonrpclib-pelix/)

- install library
``` 
pip3 install jsonrpclib
pip3 install jsonrpclib-pelix
```
## RPC Server - Testing
* Server Host define
* Server Port define 
- (Reason why we define is that in the future if we want to change that we could only change in the first line)

* Give a function - add 
* Register host and port and your fnuctions
```py3
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

SERVER_HOST = 'localhost';
SERVER_PORT = 4040;

def add(a, b):
  print("Add is called with %d and %d " %(a, b))
  return a + b

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')

print("Starting RPC server")

RPC_SERVER.serve_forever()
```

#### Use POSTMAN to Test
- Send a REQUEST:
- jsonpc version
- id : to identify
- method : add
- params : give a & b 
```
POST Request:
{
	"jsonrpc" : "2.0",
	"id" : 1,
	"method" : "add",
	"params" : [1,2]
}

Result:
{
    "result": 3,
    "id": 1,
    "jsonrpc": "2.0"
}

Add is called with 13 and 2
127.0.0.1 - - [13/Jan/2018 14:48:25] "POST / HTTP/1.1" 200 -

```

## NodeJS Server as a Client to send Request to Backend Server
- Open a new folder in web_server/server/
```
mkdir web_server/server/rpc_client
```
- Change news.js server not to hard code the data here but get News from our backend server
```js
var express = require('express');
var router = express.Router();


/* GET News List. */
router.get('/', function(req, res, next) {
  news = backend_server.getNews();
  res.json(news);
});

module.exports = router;

```

### Make NodeJs as a client - Npm jayson
[jayson](https://www.npmjs.com/package/jayson)

- install jayson in server
```
npm install jayson --save
```

- Open a rpc_client.js with a helper method to let news.js could "getNoews()" from our backend server
```js
var jayson = require('jayson');
 
// create a client
var client = jayson.client.http({
  hostname: 'localhost',
  port: 4040
});
 
function add(a, b, callback) {
  client.request('add', [a, b], function(err, response) {
    if(err) throw err;
    console.log(response.result);
    callback(response.result);
  });
}

module.exports = {
  add : add
}
```
### Wtrite a test file
- open a rpc_client_test.js
```
touch rpc_client/rpc_client_test.js
```

- Import rpc_Client
```js
var client = require('./rpc_client');

// invoke 'add'

client.add(1, 2, function(res){
  console.assert(res == 3);
});
```
- How to test?
* Open the backend server
* Execute the rpc_client_test.js
```
node rpc_client_test.js
```


## MongoDB
- Install mongoDB (Since we need to train the data so store in the local side)
```
sudo apt-get install -y mongodb-org
```
- MongoCli
[MongoCli](https://docs.mongodb.com/getting-started/shell/client/)

- Run Mongod
```
./mongod
```
- Run Mongo shell
```
./mongo
```

### Test MongoDB (Crawling in the future)
- show DB
```
show dbs
```
- Switch DB
```
use top-news
```
- See Collections / Tables
```
show collections
show tables
```

- Query 
```
db.news.find
db.news.fundOne()
db.news.count()
```
### Export - Mongoexport
- Export db
```
./mongoexport --db top-news --collection news --out demo_news_1.json
```

### Import Data from JSON file
- Import db
```
mongoimport --db top-news --collection news --file demo_news_1.json
```

## Backend Connect to MongoDB - pymongo
[pymongo](https://api.mongodb.com/python/current/)
- Install pymongo
```
pip3 install pymongo
```

- Set up all dependencies List(likes in NPM we used package.json)

#### Requirements.txt
```txt
https://api.mongodb.com/python/current/
```
```
pip3 install -r requirements.txt
```

### Set up a MongoDB Client
- open a file utils in backend_server
```
mkdir utils
touch utils/mongodb_client.py
```
- Making a Connection with MongoClient and Getting a Database

```py3
from pymongo import MongoClient

MONGO_DB_HOST = "localhost"
MONGO_DB_PORT = 27017
DB_NAME = "test"

client = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT)

def get_db(db = DB_NAME):
  db = client[db]
  return db
```
#### MongoDB Test
- Connect to MongoClient to CURD
- Open Test File
```
touch utils/mongodb_client_test.py
```
- Set Only when user call test_basic()
-  db = client.get_db('test')!!!!! used "_"

```py
import mongodb_client as client

def test_basic():
  db = client.get_db('test')
  db.test.drop()
  assert db.test.count()  == 0

  db.test.insert({'test' : 1})
  assert db.test.count() == 1

  db.test.drop()
  assert db.test.count() == 0

  print('test_basic passed!')

if __name__ == "__main__":
  test_basic()
```

## CloudAMQP
### RabbitMQ
```
RabbitMQ is a message broker: it accepts and forwards messages. You can think about it as a post office: when you put the mail that you want posting in a post box, you can be sure that Mr. Postman will eventually deliver the mail to your recipient. In this analogy, RabbitMQ is a post box, a post office and a postman.

The major difference between RabbitMQ and the post office is that it doesn't deal with paper, instead it accepts, stores and forwards binary blobs of data ‒ messages.
```
## CloudAMQP && Pika

- AMQP URL is the address to receive and send the messages

- Pika to manupulate AMQP
[pika](https://pika.readthedocs.io/en/0.10.0/) 

[RabbitMQ Pika]

- Install Pika by adding in requirements.txt
```
pika
```
- Make a file for CloudAMQP client
```
touch backend_server/utils/cloudAMQP_client.py
```

### CloudAMQP
- String -> JSON -> Serialization
- Name of Queue based on instance thus we need to create a class
- Parameters of URL
- Set a socket timeout
- Connection by Pika(blocking Connection)
- Open a Channel for receiving message
- Declare the channel as queue name
```py
class CloudAMQPClient:
  def __init__(self, cloud_amqp_url, queue_name):
    self.cloud_amqp_url = cloud_amqp_url
    self.queue_name = queue_name
    self.params = pika.URLParameters(cloud_amqp_url)
    self.params.socket_timeout = 3
    self.connection = pika.BlockingConnection(self.params)
    self.channel = self.connection.channel()
    self.channel.queue_declare(queue = queue_name)
```
- Decode
```py
return json.loads(body.decode('utf-8'))
```
### Methods of sending and geting Message

#### SendMessage : transer body from into String
```python
def sendMessage(self, message):
  self.channel.basic_publish(exchange='',
                             routing_key = self.queue_name,
                             body = json.dumps(message))
  print("[X] Sent message to %s:%s" %(self.queue_name, message))
```

#### GetMessage: by "basic_get"
```
Get a single message from the AMQP broker. Returns a sequence with the method frame, message properties, and body.
```
```
Returns:	
a three-tuple; (None, None, None) if the queue was empty; otherwise (method, properties, body); NOTE: body may be None
```
- Geive a Delivery tag when everytime broker receive a message and return back from String to JSON
```py
  # Get a message
  def getMessage(self):
    method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
    if method_frame:
      print("[x] Received message from %s:%s" % (self.queue_name, body))
      self.channel.basic_ack(method_frame.delivery_tag)
      return json.loads(body)
    else:
      print("No message returned.")
      return None
```

#### HearBeat
- BlockingConnection.sleep is a safer way to sleep than time.sleep(). 
- This will repond to server's heartbeat.
```py
def sleep(self, seconds):
    self.connection.sleep(seconds)
```

### cloudAMQP test
- Open a test file
```
touch utils/couldAMQP_client_test.py
```

- Import CloudAMQPClient class from client, try test_basic() method with params
```py
from cloudAMQP_client import CloudAMQPClient

CloudAMQP_URL = "amqp://xggyaoov:dudqi2kLBrreuJ-tST0uhiUcD3-rWomQ@termite.rmq.cloudamqp.com/xggyaoov"
TEST_QUEUE_NAME = "test"

def test_basic():
  client = CloudAMQPClient(CloudAMQP_URL,TEST_QUEUE_NAME )

  sentMsg = {"test":"test"}
  client.sendMessage(sentMsg)

  reveivedMsg = client.getMessage()

  assert sendMsg == reveivedMsg
  print("test_basic passed!")

if __name__ == "__main__":
  test_basic()
```

## API!
- Test for get one news on service.py
- import json and package dumps to transfer from BSON to JSON
- Register server in this RPC Server
```
This module provides two helper methods dumps and loads that wrap the native json methods and provide explicit BSON conversion to and from JSON. JSONOptions provides a way to control how JSON is emitted and parsed, with the default being the legacy PyMongo format. json_util can also generate Canonical or Relaxed Extended JSON when CANONICAL_JSON_OPTIONS or RELAXED_JSON_OPTIONS is provided, respectively.
```
```py
import json
from bson.json_util import dumps

def get_one_news():
  print("get_one_news is called.")
  news = mongodb_client.get_db()['news'].find_one()
  return json.loads(dumps(news))

RPC_SERVER.register_function(get_one_news, 'get_one_news')



```
- Import 'utils' (Python file import) to import mongodb_client - use os and sys

```py
import os
import sys

# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
import mongodb_client
```

## Python - Pylint (Coding Style Check)
[PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- Install PyLint
```
pip3 install pylint
```
- Analyze Outcomes
```
C:  1, 0: Missing module docstring (missing-docstring)
E: 10, 0: Unable to import 'mongodb_client' (import-error)
C: 10, 0: Import "import mongodb_client" should be placed at the top of the module (wrong-import-position)
C: 16, 0: Invalid argument name "a" (invalid-name)
C: 16, 0: Invalid argument name "b" (invalid-name)
C: 16, 0: Missing function docstring (missing-docstring)
C: 20, 0: Missing function docstring (missing-docstring)
```
#### How to slove
* missing-docstring : Add docstring -> """XXX"""
* import-error: In our case, we need to write an exception to surpass the error
* wrong-import-position: Need to put on the top
* invalid-name : couldn't use argument named a -> num1
* bad-whitespace: 1, 2

## Refactor
- Get One New need to be put other files to let service become a simple surface just receive the API request
- open a file "operations.py"
```py
import os
import sys
import json
from bson.json_util import dumps

# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

import mongodb_client

NEWS_TABLE_NAME = "news"

def getOneNews():
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))
```
- Import operations in service.pu
```py
import operations
```

# Week 3 News Pipeline
```

```

* News API
* New Monitor(Thread) : Through News API to get the latest News URL, run every 10 sec
* Redis(Save collection News) : To solve the duplicated problems, if it has been collected, we'll ignore that News.
* RabbitMQ : Receive the accepted News URL from News Monitor and Send it to Web Scrapers
* Web Scrapers : Receive News URL and scrape the contenct(XPath) from the website
* RabbitMQ : Receive the New Contents from Web Scrapers
* NewS Deduper : Receive the scraped News from RabbitMQ and Filter the same contents News by using NLP - TLITF

## Steps
* 1. News Monitor
* 2. News Fetcher - XPath
* 3. News Deduper
* 4. News Fetcher - third party package （Replace XPtah)

## Refactor : Let Utils be used by Both Backend Server and Data pipeline
```
mkdir common
mv backend_server/utils/* common/
mv backend_server/requirements.txt ./
rmdir backend_server/utils
```
- Chagne the path from service.py and operations.py from utils to common
```py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
```

## News Monitor
[News API](https://newsapi.org/)

### Request 
```
https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=715e9632a2a94ea1a4546e3f314a76a5
```
- source :
- apiKey : 
```
status": "ok",
"totalResults": 20,
-"articles": [ ...
```

### News API
```
touch common/news_api_client.py
```
- Install requests and add in requirements.txt
```
pip3 install requests
```
- getNewsFromSource()
- private buildUrl
- DEFAULT_SOURCES / SORT_BY_TOP 
- Response is a String and we need to transfer it into a JSON and decode into utf-8
```py
import requests
from json import loads

DEFAULT_SOURCES = [CNN]
CNN = 'cnn'
SORT_BY_TOP = 'top'
NEWS_API_KEY = '715e9632a2a94ea1a4546e3f314a76a5'
NEWS_API_ENDPOINT = "https://newsapi.org/v1/"
ARTICLES_API = "article"

def _buildUrl(endPoint = NEWS_API_ENDPOINT, apiName = ARTICLES_API):
    return endPoint + apiName
 
def getNewsFromSource(sources = DEFAULT_SOURCES, sortBy = SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {'apiKey' : NEWS_API_KEY,
                   'source' : source,
                   'sourBy' : sortBy} 
        response = requests.get(_buildUrl(), params = payload)
        res_json = loads(response.content.decode('utf-8'))
```
- To see if the response is vaild
- status -> ok, source and res_json not None
- Populate news source into articles : Add Soucre into the result
```
.....'publishedAt': '2018-01-14T10:36:26Z', 'source': 'cnn'}]
```

```py
 # Extract news from response
        if (res_json is not None and
            res_json['status'] == 'ok' and
            res_json['source'] is not None):
            # populate news source in each articles.
            for news in res_json['articles']:
                news['source'] = res_json['source']
            articles.extend(res_json['articles'])

    return articles
```

### News Api test
- test_basic()
- use getNewsFromSource, makes sure the ammount of news > 0 and tries another sources
```py
import news_api_client as client

def test_basic():
    news = client.getNewsFromSource()
    print(news)
    assert len(news) > 0
    news = client.getNewsFromSource(sources=['cnn'], sortBy='top')
    assert len(news) > 0
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()
```

## News Monitor
- Connect with Redis
- Connect with RebbitMQ
- Connect with News API

### Redis
- Install Redis
```
pip3 install redis
```
- News Monitor
- number_of_news to record the number of news

- Record: title / description / text / url / author / source / publishedAt:date / urlToImage / class / digest

- What digest to be used? To see if there is a dupilcate in Redis by transfering Digest into a Hashlib which could save the space in Redis
- Others, we could use it in React Frontend
- Add back digest to News JSON
```py
"""News Monitor"""
import hashlib
import redis
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import news_api_client

NEWS_SOURCES = "cnn"

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    number_of_news = 0

    for news in news_list:
        news_diget = hashlib.md5(news['title'].encode('utf-8')).hexdigest()
```

- Connect Redis and use it to find if there is in Redis or not
```py3
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

  if redis_client.get(news_digest) is None:
      number_of_news += 1
```
- Deal with the publishAt problems. Since some news didn't get the publishAt data but we need that to sort the News. Thus, we use the datetime we got that news to represent the publishAt time
```
"publishedAt": "2018-01-14T20:17:50Z"
```
```py
   import datetime
   
    for news in news_list:
        news_diget = hashlib.md5(news['title'].encode('utf-8')).hexdigest()
        # Connect with Redis and check if it's in Redis
        if redis_client.get(news_digest) is None:
            number_of_news += 1
            # Deal with publishAt problems
            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            # Save into Redis
            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)
```

## Sned to RabbitMQ (CloudAMQP Client)
- init and import CloudAMQP Client
- Need to apply anotehr QUEUE different from TEST URL
```py

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = 
SCRAPE_NEWS_TASK_QUEUE_NAME = "top-news-scrape-news-task-queue"

SLEEP_TIME_IN_SECOND = 10
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

            # Send Tasks to cloudAMQP
            cloudAMQP_client.sendMessage(news)

    print("Fetched %d news." % number_of_news)

    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECOND)
```


### Stock in cloudAMQP Problems!(Cloudn't use the URL)
```
pika.exceptions.ProbableAuthenticationError: (403, 'ACCESS_REFUSED - Login was refused using authentication mechanism PLAIN. For details see the broker logfile.')
```

### Tool for Clearn Queue
```py
import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://cbzkwlek:4louH2OEYrE66kGmwv8RmLiOC2JZyhSi@donkey.rmq.cloudamqp.com/cbzkwlek"
SCRAPE_NEWS_TASK_QUEUE_NAME = "top-news-SCRAPE_NEWS_TASK_QUEUE"

# DEDUPE_NEWS_TASK_QUEUE_URL = #TODO: use your own config.
# DEDUPE_NEWS_TASK_QUEUE_NAME = #TODO: use your own config.

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    # clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
```

## Web Scrapers

### XPath
- XPath Helper
```py
"""//p[contains(@class, 'zn-body__paragraph')]//text() | //div[contains(@class, 'zn-body__paragraph')]//text()"""
```

### Scrapers
- Open a scrapers folder and cnn news scraper file
- Imitate the behaviors of browsers
* session & header
* Imitate a real User Agent as a Header

```py
def extract_news(news_url):
    session_requests = requests.session()
    response = session_requests.get(news_url, headers=_get_headers())
    news = {}
```

- Get the Header by looping the Mock User Agent File

```py
def _get_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
      "Connection" : "close", 
      "User-Agent" : ua
    }
    return headers
```
- Import html from lxml
- Used XPATH method by separating it into tree and news from the tree
- Join the LIST of news together to become a whole STRING
```py
from lxml import html
try:
        tree = html.fromstring(response.content)
        news = tree.xpath(GET_CNN_NEWS_XPATH)
        news = ''.join(news)
    except Exception:
        return {}

    return news

```


- Grab the Agent info form file and randomly select one of them

```py
# Load user agents
USER_AGENTS_FILE = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS = []

with open(USER_AGENTS_FILE, 'rb') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1])

random.shuffle(USER_AGENTS)
```

## Fetcher
- Take a News Url from Queue(news monitor) and use scraper to get the contents and send it into the next Queue
- While loop likes Moniter, get a message from scrape_news_queue_client and use handle message
```py
while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
```
- handleMessage()
```py
def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print('message is broken')
        return

    task = msg
    text = None
```
- Check if the source is from cnn, and extractNews by task['url'] from news scraper and Rewrite the text into task

```py
    if task['source'] == 'cnn':
        print('scraping CNN news')
        text = cnn_news_scraper.extractNews(task['url'])
    else
        print('News source [%s] is not supported. ' % task['source'])
    
    task['text'] = text
```

- Send out the task to dedupe Queue
```py
    dedupe_news_queue_client.sendMessage(task)
```
- Import os,sys and the CloudAMQP CLIENT
```py
import os
import sys


# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = 
DEDUPE_NEWS_TASK_QUEUE_NAME = "top-new-DEDUPE_NEWS_TASK_QUEUE_NAME"
SCRAPE_NEWS_TASK_QUEUE_URL = "
SCRAPE_NEWS_TASK_QUEUE_NAME = "top-news-SCRAPE_NEWS_TASK_QUEUE"

SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
```

## How to TEST
- Clear Redis
```
redis-cli flushall
```
- Queue_helper (if needed)
```
python3 queue_helper.py
```
- Get News URL From News Api (Faster)
```
python3 news_monitor.py
```
- Get News URL and Scrape on website
```
python3 news_fetcher.py
```

## DeDuper 重複數據刪除 - TFITF 
