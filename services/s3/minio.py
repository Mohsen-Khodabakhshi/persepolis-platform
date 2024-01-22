import boto3


class MinioService:
    def __init__(self, endpoint_url: str, access_key: str, secret_key: str) -> None:
        self.client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

    def put_file(self, file_path: str, bucket_name: str, object_name: str) -> None:
        self.client.upload_file(file_path, bucket_name, object_name)

    def get_file(
        self, bucket_name: str, object_name: str, local_file_path: str
    ) -> None:
        self.client.download_file(bucket_name, object_name, local_file_path)
