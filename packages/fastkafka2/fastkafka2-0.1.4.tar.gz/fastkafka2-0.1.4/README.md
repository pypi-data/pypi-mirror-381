# fastkafka2

Next-generation FastAPI-like DX for Kafka (version 2).

## Installation

``` bash
pip install fastkafka2
```

## Use example
### Project arch
```shell
├── api/
│   ├── kafka/
│   │   ├── handlers/
│   │   │   ├── example/
│   │   │   │   ├─ schemas.py
│   │   │   │   └─ handler.py
│   │   │   └── base_handler.py
│   │   └── lifespan.py
│
├── main.py
```

### Schemas
``` python
# api\kafka\handlers\example\schemas.py
from pydantic import BaseModel


class ExampleSchema(BaseModel):
    msg: str
```

### Handler
``` python
# api\kafka\handlers\example\handler.py
import logging

from fastkafka2 import KafkaHandler
from fastkafka2 import KafkaMessage
from fastkafka2 import KafkaProducer


handler = KafkaHandler()

kafka_producer = KafkaProducer(bootstrap_servers="127.0.0.1:9092")


@handler("example")
async def example_handler(message: KafkaMessage):
    t = int(message.headers.get("try")) + 1
    logging.info(f"Пришло: {message}")
    await kafka_producer.send_message(
        topic="example-2", data={"msg": "wddwd"}, headers={"try": f"{t}"}, key=None
    )
    logging.info(f"Отправил: {f'{t}'}")
```


### Typed validation and IDE hints
There are two ways to get strong typing and validation like in FastAPI:

1) Single-source via function annotation (recommended for IDE hints)
```python
from pydantic import BaseModel
from fastkafka2 import KafkaHandler
from fastkafka2 import KafkaMessage

class Order(BaseModel):
    id: int
    amount: float

class Hdrs(BaseModel):
    type: str
    source: str

handler = KafkaHandler(prefix="orders")

@handler("created")  # models inferred from annotation
async def on_created(msg: KafkaMessage[Order, Hdrs]):
    # msg.data and msg.headers are fully typed
    ...
```

2) Models in decorator, generic message in function (runtime validation only)
```python
@handler("created", data_model=Order, headers_model=Hdrs)
async def on_created(msg: KafkaMessage):
    # Works at runtime; for IDE hints you can optionally:
    # from typing import cast
    # msg = cast(KafkaMessage[Order, Hdrs], msg)
    ...
```

You can also split parameters:
```python
@handler("updated")
async def on_updated(data: Order, headers: Hdrs):
    ...
```

### Header filtering
Filter messages by headers before deserialization using equality or a predicate:
```python
# Equality filter
@handler("created", data_model=Order, headers_model=Hdrs, headers_filter={"type": "created"})
async def on_created(msg: KafkaMessage[Order, Hdrs]):
    ...

# Predicate filter
def high_value(h: dict[str, str]) -> bool:
    return h.get("type") == "created" and h.get("priority") == "high"

@handler("created", data_model=Order, headers_model=Hdrs, headers_filter=high_value)
async def on_high_value(msg: KafkaMessage[Order, Hdrs]):
    ...
```


### Grouping of handlers
``` python
# api\kafka\handlers\base_handler.py
from api.kafka.handlers.example.handler import handler as example_handler

from fastkafka2 import KafkaHandler

base_handler = KafkaHandler()

base_handler.include_handler(example_handler)
```


### Lifespan fastkafka app
``` python
# api/kafka/lifespan.py
import logging
from contextlib import asynccontextmanager
from fastkafka2 import KafkaApp
from api.kafka.handlers.base_handler import base_handler

from api.kafka.handlers.example.handler import kafka_producer


@asynccontextmanager
async def lifespan(app: KafkaApp):
    logging.info("Lifespan: запуск")
    try:
        await kafka_producer.start()
        yield
        logging.info("Lifespan: выполнен")
    finally:
        await kafka_producer.stop()
        logging.info("Lifespan: остановка")


app = KafkaApp(
    title="Kafka Gateway",
    description="Kafka-based microservice",
    bootstrap_servers="127.0.0.1:9092",
    lifespan=lifespan,
)

app.include_handler(base_handler)
```


### Entry point main app
``` python
# main.py
import asyncio
from logging_config import setup_logging
from api.kafka.lifespan import app

if __name__ == "__main__":
    setup_logging()
    asyncio.run(app.run())
```


