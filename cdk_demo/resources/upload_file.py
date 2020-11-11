import os
import json
import io

import boto3

BUCKET = os.environ["S3_BUCKET_NAME"]


def handler(event, context):
    session = boto3.Session()
    s3 = session.resource("s3")

    for record in event["Records"]:
        body: dict = json.loads(record["body"])
        key = body.pop("key")
        print(key, body)

        buffer = io.BytesIO()
        buffer.write(bytes(json.dumps(body)))
        buffer.seek(0)
        s3.Object(BUCKET, key).put(Body=buffer)


if __name__ == "__main__":
    test_event = {
        "key": "this/is/a/test.txt",
        "name": "michael",
        "tool": "cdk",
    }
    handler(test_event, None)
