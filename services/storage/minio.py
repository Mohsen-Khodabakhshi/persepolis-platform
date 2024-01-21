from minio import Minio


class MinioService:
    def __init__(self, host: str, access_key: str, secret_key: str) -> None:
        self.client = Minio(endpoint=host, access_key=access_key, secret_key=secret_key)

    def create_bucket(self, bucket_name: str) -> bool:
        found = self.client.bucket_exists(bucket_name)
        if not found:
            self.client.make_bucket(bucket_name)
            return True
        return False

    def put_file(self, bucket_name: str, file_object: str, file_name: str) -> None:
        self.client.fput_object(bucket_name, file_object, file_name)

    def get_file(self, bucket_name: str, file_object: str, file_name: str) -> None:
        self.client.fget_object(bucket_name, file_object, file_name)
