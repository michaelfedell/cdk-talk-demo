import typing

from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_sqs as sqs,
    aws_iam as iam,
    aws_lambda_event_sources,
)


class CdkDemoStack(core.Stack):

    def __init__(
            self, scope: core.Construct, id: str,
            lambda_timeout: typing.Optional[core.Duration] = None,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "cdk-demo-bucket")
        uploader = lambda_.Function(
            self, "cdk-demo-function",
            code=lambda_.Code.from_asset("./cdk_demo/resources/"),
            handler="upload_file.handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout=lambda_timeout,
            role=None
        )
        bucket.grant_write(uploader)
        uploader.add_environment("S3_BUCKET_NAME", bucket.bucket_name)

        queue = sqs.Queue(self, "cdk-demo-queue")
        uploader.add_event_source(
            source=aws_lambda_event_sources.SqsEventSource(queue)
        )
