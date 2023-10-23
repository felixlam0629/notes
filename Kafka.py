import time
from kafka import KafkaConsumer
import json

bootstrap_servers = ["localhost:9092"]    # Replace with actual Kafka broker addresses
topic             = "gateio_spot_tickers" # Replace with actual topic name

message_object = KafkaConsumer(
    topic,
    bootstrap_servers  = bootstrap_servers,
    auto_offset_reset  = "earliest",
    enable_auto_commit = True,
    group_id           = "my-group",
    value_deserializer = lambda m: json.loads(m.decode("utf-8"))
)

for message in message_object:
    data = message.value

    # extract the timestamp from the JSON payload
    timestamp = data["time_ms"]

    # calculate the latency
    current_time = int(round(time.time() * 1000))
    latency      = current_time - timestamp

    # print the topic, message and latency
    # print(f"Latency: {latency}ms | Topic: {message.topic} | Data: {data}")

    latest_price = data["last"]
    print(f"BTC_USDT latest spot ticker: {latest_price}")