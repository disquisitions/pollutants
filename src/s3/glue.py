import boto3


class Glue:

    def __init__(self):
        """
        In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
        """

        # Create a glue YAML for database, table, crawler, etc., names
        boto3.client('glue').create_crawler(
            Name='',
            Role='',
            DatabaseName='',
            Description='',
            Targets={'S3Targets': [
                {
                    'Path': ''
                },
            ]},
            TablePrefix=''
        )
