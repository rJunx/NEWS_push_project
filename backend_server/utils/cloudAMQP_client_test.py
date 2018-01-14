from cloudAMQP_client import CloudAMQPClient

CloudAMQP_URL = "amqp://xggyaoov:dudqi2kLBrreuJ-tST0uhiUcD3-rWomQ@termite.rmq.cloudamqp.com/xggyaoov"
TEST_QUEUE_NAME = "test"

def test_basic():
  client = CloudAMQPClient(CloudAMQP_URL,TEST_QUEUE_NAME )

  sentMsg = {"test":"test"}
  client.sendMessage(sentMsg)

  reveivedMsg = client.getMessage()

  assert sentMsg == reveivedMsg
  print("test_basic passed!")

if __name__ == "__main__":
  test_basic()