#!/usr/bin/env python3

from aws_cdk import core

from cdk_demo.cdk_demo_stack import CdkDemoStack


app = core.App()
CdkDemoStack(
    app, "cdk-demo",
    lambda_timeout=core.Duration.seconds(15),
    env={'region': 'us-west-2'}
)

app.synth()
