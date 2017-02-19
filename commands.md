# Commands

## terminate instance:
`aws ec2 terminate-instances --instance-ids <instance id>`

## ssh:
get public_dns_name from `py aws.py show`

`ssh -i ~/.aws/patrick-x240-2.pem <public_dns_name>`

`scp -i ~/.aws/patrick-x240-2.pem initial_setup.sh ubuntu@ec2-54-196-80-181.compute-1.amazonaws.com:/home/ubuntu/ `

