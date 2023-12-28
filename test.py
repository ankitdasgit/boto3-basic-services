import boto3

# client = boto3.client('s3')
# client= boto3.client('ec2')
clientiam = boto3.client('iam')




############## s3 actions ##############

# response = client.create_bucket(
#     Bucket='demo-boto3-bucket-1415',
# )

# response = client.get_bucket_acl(
#     Bucket='demo-boto3-bucket-1415', 
# )
# print(response)

# s3 = boto3.client('s3')
# response= s3.upload_file('demotext.txt', 'demo-boto3-bucket-1415', 'demotext.txt')
# print(response)


############ ec2 ###############

# instances = ec2.create_instances(       
#         ImageId="ami-079db87dc4c10ac91",
#          MinCount=1,
#         MaxCount=1,
#         InstanceType="t2.micro"  
#     )

# response = client.terminate_instances(
#     InstanceIds=[
#         # 'i-010fd4f723a4eb15f',
#         # 'i-0988d99b0c23486d8',
#         'i-0763576c3dad59df9' 
#     ],
# )
# print(response)

# response = client.stop_instances(
#     InstanceIds=[
#         'i-0763576c3dad59df9',
#     ],
# )
# print(response)

# response = client.start_instances(
#     InstanceIds=[
#         'i-0763576c3dad59df9',
#     ],
# )




######## vpc/subnet ##########

# response = client.create_vpc(
#     CidrBlock='10.0.0.0/16',
# )
# print(response)


# response = client.create_subnet(
#     CidrBlock='10.0.1.0/24',
#     VpcId='vpc-a01106c2',
# )



############# IAM #############

# response = clientiam.create_user(
#     UserName='domoboto3user',
# )
# print(response)

# response = clientiam.attach_user_policy(
#     UserName='domoboto3user',
#     PolicyArn=['arn:aws:iam::aws:policy/AmazonS3FullAccess',
#                'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
#                ]
# )
# print(response)

