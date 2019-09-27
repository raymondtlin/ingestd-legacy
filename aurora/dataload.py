import boto3

rds_client = boto3.client('rds-data')
db = "pgprod-1"
db_cluster_arn = "arn:aws:rds:us-west-2:587405387161:cluster:pgprod-1"
db_credentials_secrets_store_arn = "arn:aws:secretsmanager:us-west-2:587405387161:secret:db/pgprod-w1FNFo"


# pgprod-1.cluster-cmham0p6srqv.us-west-2.rds.amazonaws.com

transaction = rds_client.begin_transaction(
    secretArn=db_credentials_secrets_store_arn,
    resourceArn=db_cluster_arn,
    database='pgprod-1')
    
try:
    sql=f'CREATE TABLE'
    sql_parameter_sets = []
    
    response = batch_execute_statement(sql, sql_parameter_sets, transaction['transactionId'])

except Exception:
    transaction_response = rds_client.rollback_transaction(
        secretArn=db_credentials_secrets_store_arn,
        resourceArn=db_cluster_arn,
        transactionId=transaction['transactionId']
    )
    
else:
    transaction_response = rds.client.commit_transaction(
        secretArn=db_credentials_secrets_store_arn,
        resourceArn=db_cluster_arn,
        transactionId=transaction['transactionId']
        )
    print(f'Number of records updated: {len(response["updateResults"])}')
print(f'Transaction Status: {transaction_response["transactionStatus"]}')