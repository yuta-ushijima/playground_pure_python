import boto3
from botocore.exceptions import ClientError


def aws_session():
    return boto3.Session(
        region_name='ap-northeast-1',
        profile_name='jetbrains_aws_account_906875006544'
    )


def print_s3_bucket_list_names():
    try:
        session = aws_session()
        s3 = session.client('s3')
        response = s3.list_buckets()

        for bucket in response['Buckets']:
            print(bucket['Name'])
    except ClientError as e:
        # エラー情報を出力
        print("An error occurred: %s" % e)
        if 'Error' in e.response:
            print("Error code: %s" % e.response['Error'].get('Code'))
            print("Error message: %s" % e.response['Error'].get('Message'))
        else:
            print("Error: %s" % e)


if __name__ == '__main__':
    print_s3_bucket_list_names()