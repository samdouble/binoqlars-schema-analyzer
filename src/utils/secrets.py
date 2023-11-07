#import botocore 
#import botocore.session 
#from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 
#
#client = botocore.session.get_session().create_client('secretsmanager')
#cache_config = SecretCacheConfig()
#cache = SecretCache( config = cache_config, client = client)
#
#secret = cache.get_secret_string('mysecret')




import boto3
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "datajitsu_6c98210f-ff3b-4d4a-8935-698fe2ad0287"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='ca-central-1'
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Your code goes here.
    return secret
