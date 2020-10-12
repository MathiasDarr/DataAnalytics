import boto3

# boto3 is the AWS SDK library for Python.
# We can use the low-level client to make API calls to DynamoDB.
client = boto3.client('dynamodb', region_name='us-west-2')

try:
    resp = client.create_table(
        TableName="TripReports",
        # Declare your Primary Key in the KeySchema argument
        KeySchema=[
            {
                "AttributeName": "Author",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Title",
                "KeyType": "RANGE"
            }
        ],
        # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                "AttributeName": "Author",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Title",
                "AttributeType": "S"
            }
        ],
        # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
        # You can control read and write capacity independently.
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)

create_trip_report_table = (""" CREATE TABLE IF NOT EXISTS trip_reports(
                            trip_id serial PRIMARY KEY ,
                            trip_name VARCHAR NOT NULL,
                            trip_report VARCHAR NOT NULL,
                            elevationGain float NOT NULL,
                            mileage INT NOT NUll,
                            trip_date DATE NOT NULL,
                            locations text[] NOT NULL);                                                    
                        """)
