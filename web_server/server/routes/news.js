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

module.exports = router;
