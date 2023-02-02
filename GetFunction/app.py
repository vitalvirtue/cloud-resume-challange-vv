import json
import boto3

# Establish the DynamoDB resource and the table to be used
dynamodb = boto3.resource('dynamodb')
table_name = 's3-table-vv'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Specify the ID to be fetched
    ID = event.get("ID", "visitors")

    # Display a log message indicating the item ID being fetched
    print('Fetching Item with ID = {} from the DynamoDB table'.format(ID))
    
    # Attempt to retrieve the item from the table
    response = table.get_item(
        Key={
            'ID': ID
        }
    )
    
    # Check if the item was retrieved successfully
    if 'Item' in response:
        # Return a CORS-enabled response with the total count
        return {
            "statusCode": 200,
            'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*'
            },
            "body": json.dumps({"counter": response['Item'].get('total_count')}),
        }
    else:
        # If the item was not found, display an error message
        print('Item with ID = {} not found in the DynamoDB table'.format(ID))
