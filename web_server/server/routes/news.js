var express = require('express');
var router = express.Router();


/* GET News List. */

// "localhost:3000/news/userId/1@1.com/pageNum/2"
router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
  console.log('Fetching news...');
  user_id = req.params['userId'];
  page_num = req.params['pageNum'];

  rpc_client.getNewsSummariesForUser(user_id, page_num, function(response) {
    res.json(response);
  });
});

router.post('/userId/:userId/newsId/:newsId', function(req, res, next) {
  console.log('Logging news click...');
  user_id = req.params['userId'];
  newsId = req.params['newsId'];

  rpc_client.logNewsClickForUser(user_id, newsId);
  res.status(200);
});

module.exports = router;
