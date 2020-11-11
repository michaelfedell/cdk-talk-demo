import json
import pytest

from aws_cdk import core
from cdk-demo.cdk_demo_stack import CdkDemoStack


def get_template():
    app = core.App()
    CdkDemoStack(app, "cdk-demo")
    return json.dumps(app.synth().get_stack("cdk-demo").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
