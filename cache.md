### POST Design
- [Decouple into Components](#decouple-into-components)
- [Create React App](#create-react-app)

### React Frontend UI 
- [Build up App Component with Marerialize Styling](#build-up-app-component)
- [Build up NewsPanel Component](#build-up-newspanel-component)
- [Build up NewsCard Component](#build-up-newscard-component)
- [Refactor those Components into Web Server file](#refactor-those-components-into-web-server-file)

### NodeJS Web Server 
- [Express application generator - NodeJS Server](#express-application-generator---nodejs-server)
- [Configure APP.js](#configure-appjs)
- [Server Side Routing](#server-side-routing)
- [RESTful API: Send Backend data from Server(Mock Data)](#restful-api-send-backend-data-from-server)

### Frontend and Backend Http Protocol(RESTful API)
- [NewsPanel Requests to Backend for Loading More JSON data](#newspanel-requests-to-backend-for-loading-more-json-data)
- [Access Control Allow Origin](#access-control-allow-origin)
- [Handle Scrolling](#handle-scrolling)
- [Debounce](#debounce)

###  Backend - SOA (Service Oriented Architrcture) Design
- [SOA Desgin Pattern](#soa-desgin-pattern)
- [RPC Backend Service](#rpc-backend-service)
- [JSONRPClib Libraries](#jsonrpclib-libraries)
- [Testing by Postman](#testing-by-postman)
- [NodeJS Server as a RPCclient - jayson](#nodejs-server-as-a-RPCclient---jayson)

### Backend - MongoDB connection
- [MongoDB](#mongodb)
- [Mongo Syntax](#mongo-syntax)

### CloudAMQP: Message Queue
- [CloudAMQP](#cloudamqp)
- [CloudAMQP & Pika](#cloudamqp-&-pika)
- [CloudAMQP with Python(doc)](https://www.cloudamqp.com/docs/python.html)
- [Heart Beat](#heart-beat)
- [Backend API send Request to CloudAMQPClient API for Asking News in Queue](#backend-api-send-request-to-cloudamqpclient-api-for-asking-news-in-queue)

### Pylint (Python Coding Style Check)
- [Pylint](#pylint)
- [PEP 8 - Style Guide(doc)](https://www.python.org/dev/peps/pep-0008/)

### :hammer: Refactor : Create an Operator to Receive all API Request from Backend Server
- [Refactor: Operations](#refactor-operations)
- [CloudAMQP_Client]
- [Mongodb_Client]
- [News_api_Client]
- [News_recommendation_service_Client]

### News Data Pineline 

Monitor -> Q(scrape) -> Fetcher -> Q(dedupe) 

- [Data Pineline Processing Steps](#news-pipeline)
- [News API - getNewsFromSource](#news-api)
- [News API TEST](#news-api-test)

#### News Monior

- [News Monitor w/ Redis, RabbitMQ, News API](#news-monitor)
- [Send News to Redis (hashlib)](#sent-to-redis)
- [Send to RabbitMQ](#send-to-rabbitmq)
- [Create a Took to clean the Queue](#tool-for-clean-queue)

#### News Fetcher(Scrawler)

- [Web Scrapers(has been replaced)](#web-scrapers)
- [News Fetcher](#news-fetcher)
- [Newspaper 3k replaces XPath in News Fetcher](#newspaper-3k)
- [Newspaper3k(doc)](https://github.com/codelucas/newspaper)
- [Test Monitor and Fetcher](#test-monitor-and-fetcher)

#### News Deduper

- [New Deduper - TFIDF](#news-deduper---tfidf)
- [sklearn(TfidfVectorizer)(doc)](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [TFIDF Vectorizer (>0.8)](tfidf-vectorizer---test)
- [Deduper Process](#deduper)


### Authentication
- [Authentication](#authentication)
