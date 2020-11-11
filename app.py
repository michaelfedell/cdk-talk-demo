#!/usr/bin/env python3

from aws_cdk import core

from cdk_demo.cdk_demo_stack import CdkDemoStack


app = core.App()
CdkDemoStack(app, "cdk-demo", env={'region': 'us-west-2'})

app.synth()
