from cloudAMQP_client import CloudAMQPClient

CloudAMQP_URL = "amqp://mycayzfr:E4nnofIrEfvgW4oByDmkoBjvsmobCzFG@termite.rmq.cloudamqp.com/mycayzfr"
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