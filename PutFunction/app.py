import json
import boto3

# Establish the DynamoDB resource and the table to be used
dynamodb = boto3.resource('dynamodb')
table_name = 's3-table-vv'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Specify the ID to be fetched
    ID = event.get("ID", "visitors")

    # Indicate that the item is being fetched from the database
    print(f'Retrieving item with ID {ID} from table {table_name}...')
    
    # Get the item with the specified ID
    response = table.get_item(
        Key={
            'ID': {
                "S": "visitors"
            }
        }
    )
    
    # If the item was found, update the "total_count" value
    if 'Item' in response:
        response = table.update_item(
             Key={
                'ID': {
                    "S": "visitors"
                }
            },
            UpdateExpression="set total_count = total_count + :N",
            ExpressionAttributeValues={
                ':N': 1
            }
        )
        
        # Check if the update was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f'Item updated successfully with HTTP status code {response["ResponseMetadata"]["HTTPStatusCode"]}')
        else:
            print(f'Update failed with HTTP status code: {response["ResponseMetadata"]["HTTPStatusCode"]}')
    else:
        print(f'Item with ID {ID} was not found in table {table_name}')
        
    # Return the response with CORS headers
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        }
    }
