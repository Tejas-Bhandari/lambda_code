import boto3

dynamodb_client = boto3.client(
    "dynamodb",
    aws_access_key_id="AKIA6GBMCRBNFE3P4EOO",
    aws_secret_access_key="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",
)
s3_client = boto3.client(
    "s3",
    aws_access_key_id="AKIA6GBMCRBNFE3P4EOO",
    aws_secret_access_key="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",
)
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id="AKIA6GBMCRBNFE3P4EOO",
    aws_secret_access_key="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",
)

dynamodb_response = dynamodb_client.list_tables()
buckets_response = s3_client.list_buckets()
lambda_response = lambda_client.list_functions()


# print(dynamodb_response)
# print(buckets_response)
# print(lambda_response)
for i in buckets_response["Buckets"]:
    # print(i, "name of the buckets")
    print("####################################################################")
    # a = s3_client.get_bucket_acl(Bucket=i['Name'])
    # print(a, "DDDDDDDDD")
    bucket_name = i["Name"]
    try:
        try:
            # Accelerate Configuration
            accelerate_response = s3_client.get_bucket_accelerate_configuration(
                Bucket=bucket_name
            )
            bucket_accelerate_configuration = accelerate_response.get(
                "Status", "Not configured for acceleration"
            )
        except Exception as e:
            bucket_accelerate_configuration = ""
            print("Accelerate error---------------------", str(e))

        try:
            # Access Control List (ACL)
            acl_response = s3_client.get_bucket_acl(Bucket=bucket_name)
            bucket_acl = acl_response
        except Exception as e:
            print("Access Control List error------------------- ", str(e))

        # Analytics Configuration
        try:
            analytics_response = s3_client.get_bucket_analytics_configuration(
                Bucket=bucket_name
            )
            bucket_analytics_configuration = analytics_response.get(
                "AnalyticsConfiguration", "Not configured for analytics"
            )
        except Exception as e:
            bucket_analytics_configuration = ""
            print("Analytics Configuration error-------------", str(e))

        # CORS Configuration
        try:
            cors_response = s3_client.get_bucket_cors(Bucket=bucket_name)
            bucket_cors_configuration = cors_response.get(
                "CORSRules", "No CORS configuration"
            )
        except Exception as e:
            bucket_cors_configuration = ""
            print("CORS configuration error------------------->", str(e))

        # Encryption Configuration
        try:
            encryption_response = s3_client.get_bucket_encryption(Bucket=bucket_name)
            bucket_encryption_configuration = encryption_response.get(
                "ServerSideEncryptionConfiguration", "No encryption configuration"
            )
        except Exception as e:
            bucket_encryption_configuration = ""
            print("Encryption error", str(e))

        # Inventory Configuration
        try:
            inventory_response = s3_client.get_bucket_inventory_configuration(
                Bucket=bucket_name, Id="inventory-id"
            )
            bucket_inventory_configuration = inventory_response.get(
                "InventoryConfiguration", "No inventory configuration"
            )
        except Exception as e:
            bucket_inventory_configuration = ""
            print("Inventory details error-------------------->", str(e))

        # Lifecycle Configuration
        try:
            lifecycle_response = s3_client.get_bucket_lifecycle(Bucket=bucket_name)
            bucket_lifecycle_configuration = lifecycle_response.get(
                "Rules", "No lifecycle configuration"
            )
        except Exception as e:
            bucket_lifecycle_configuration = ""
            print("Lifecycle Configration error------------------------>", str(e))

        # Location
        try:
            location_response = s3_client.get_bucket_location(Bucket=bucket_name)
            bucket_location = location_response.get(
                "LocationConstraint", "us-east-1"
            )  # Default to 'us-east-1' if no location constraint
        except Exception as e:
            bucket_location = ""
            print("Location error------------------------->", str(e))

        # Logging Configuration
        try:
            logging_response = s3_client.get_bucket_logging(Bucket=bucket_name)
            bucket_logging_configuration = logging_response.get(
                "LoggingEnabled", "Not configured for logging"
            )
        except Exception as e:
            bucket_logging_configuration = ""
            print(
                "Loggin configuration error--------------------->",
                bucket_accelerate_configuration,
            )

        # Metrics Configuration
        try:
            metrics_response = s3_client.get_bucket_metrics_configuration(
                Bucket=bucket_name, Id="metrics-id"
            )
            bucket_metrics_configuration = metrics_response.get(
                "MetricsConfiguration", "No metrics configuration"
            )
        except Exception as e:
            bucket_metrics_configuration = ""
            print("Metrics error---------------->", bucket_metrics_configuration)

        # Notification Configuration
        try:
            notification_response = s3_client.get_bucket_notification(
                Bucket=bucket_name
            )
            bucket_notification_configuration = notification_response.get(
                "TopicConfiguration", "No notification configuration"
            )
        except Exception as e:
            bucket_notification_configuration = ""
            print(
                "Notification Congfiguration error------------------>",
                bucket_notification_configuration,
            )

        # Policy
        try:
            policy_response = s3_client.get_bucket_policy(Bucket=bucket_name)
            bucket_policy = policy_response.get("Policy", "No bucket policy")
        except Exception as e:
            bucket_policy = ""
            print("Policy error--------------------->", str(e))

        # Policy Status
        try:
            policy_status_response = s3_client.get_bucket_policy_status(
                Bucket=bucket_name
            )
            bucket_policy_status = policy_status_response.get(
                "PolicyStatus", "No policy status"
            )
        except Exception as e:
            bucket_policy_status = ""
            print("Policy status error------------------>", str(e))

        # Replication Configuration
        try:
            replication_response = s3_client.get_bucket_replication(Bucket=bucket_name)
            bucket_replication_configuration = replication_response.get(
                "ReplicationConfiguration", "No replication configuration"
            )
        except Exception as e:
            bucket_replication_configuration = ""
            print("Replication configuration error------------------->", str(e))

        # Request Payment Configuration
        try:
            request_payment_response = s3_client.get_bucket_request_payment(
                Bucket=bucket_name
            )
            bucket_request_payment_configuration = request_payment_response.get(
                "Payer", "Unknown"
            )
        except Exception as e:
            bucket_request_payment_configuration = ""
            print("Request Payment error------------------->", str(e))

        # Tagging
        try:
            tagging_response = s3_client.get_bucket_tagging(Bucket=bucket_name)
            bucket_tagging = tagging_response.get("TagSet", "No bucket tagging")
        except Exception as e:
            bucket_tagging = ""
            print("Taggin error-------------------->", str(e))

        # Versioning Configuration
        try:
            versioning_response = s3_client.get_bucket_versioning(Bucket=bucket_name)
            bucket_versioning_configuration = versioning_response.get(
                "Status", "Versioning not enabled"
            )
        except Exception as e:
            bucket_versioning_configuration = ""
            print("Versioning configuration error------------------->", str(e))


        # Website Configuration
        try:
            website_response = s3_client.get_bucket_website(Bucket=bucket_name)
            bucket_website_configuration = website_response.get('WebsiteConfiguration', 'No website configuration')
        except Exception as e:
            bucket_website_configuration = ''
            print("Website Configuration------------------->", str(e))

        # Construct and return details
        bucket_details = {
            "BucketName": bucket_name,
            "AccelerateConfiguration": bucket_accelerate_configuration,
            "ACL": bucket_acl,
            "AnalyticsConfiguration": bucket_analytics_configuration,
            "CORSConfiguration": bucket_cors_configuration,
            "EncryptionConfiguration": bucket_encryption_configuration,
            "InventoryConfiguration": bucket_inventory_configuration,
            "LifecycleConfiguration": bucket_lifecycle_configuration,
            "Location": bucket_location,
            "LoggingConfiguration": bucket_logging_configuration,
            "MetricsConfiguration": bucket_metrics_configuration,
            "NotificationConfiguration": bucket_notification_configuration,
            "Policy": bucket_policy,
            "PolicyStatus": bucket_policy_status,
            "ReplicationConfiguration": bucket_replication_configuration,
            "RequestPaymentConfiguration": bucket_request_payment_configuration,
            'Tagging': bucket_tagging,
            'VersioningConfiguration': bucket_versioning_configuration,
            'WebsiteConfiguration': bucket_website_configuration
        }

        print("bucket details", bucket_details)

    except Exception as e:
        print(str(e), "ERRORR")

"""
# bucket head information 
for buckets_response in buckets_response['Buckets']:
    bucket_info = s3_data.head_bucket(Bucket=buckets_response['Name'])
    print(bucket_info)
"""


"""
# tables details


"""
# for i in dynamodb_response['Tables']:
#     print(i,  "ggg")
# print(dynamodb_data.describe_table(TableName="test_dynamo"))
