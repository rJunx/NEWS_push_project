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

![App Structure](/app_structure.png)

* Base : Whole React App (Navbar + App)
* App : Image(title) + NewsPanel
* NewsPanel : Concludes many NewsCard such as News Lists (While user scorlling, backend send new NewsCard continously)
* NewsCard : Single News adding into NewsPanel with News image, News title, News contents, News description, News Tage and Links to News.

## Install & Init Environment
### Create React App - likes Angular cli (recommened by Facebook)
[Create React App](https://reactjs.org/blog/2016/07/22/create-apps-with-no-configuration.html)
- Deal with webpack and give a whole framework

## App

## NewsPanel

## NewsCard

## Continuous loading News (Server-Side REST API - NodeJS & Client-Side - React) 