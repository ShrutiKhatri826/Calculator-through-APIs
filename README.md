# Calculator-through-APIs
This Repository contains the code for Simple Calculator built using AWS Lambda and API Gateway. The API provides four basic arithmetic operations i.e. Addition, Subtraction, Multiplication, and Division. Each operation is implemented as a separate lambda function which is invoked through its respective API through AWS API Gateway.

# Getting Started
## Clone this repository
-git clone https://github.com/your-username/repository-name.git 
-cd repository-name
## Deploy the Lambda Functions and APIs through API Gateway
AWS Lambda - https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
Amazon API Gateway - https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

PROCESS:
1. Open AWS Console -> Services -> Lambda.
2. Click on the "Create function" -> "Author from scratch."
3. In the "Function code" section, you have a few options:
      -Inline Code: You can directly paste your Lambda function code into the editor.
      -Upload a .zip file: If your Lambda function consists of multiple files, you can zip them and upload the zip file.
4. Test your function and repeat the same steps for the rest of the functions.
5. After creating all Lambda functions, you'll integrate them with AWS API Gateway.
6. You'll create separate APIs for each operation (addition, subtraction, multiplication, and division).
7. While creating APIs make sure all the logs are enabled, and the stage and the routes are properly set.
8. While enabling logs, the section "Access Logging" needs to be checked.
9. Once everything is set up, deploy your Apis in AWS API Gateway and also the lambda functions.

# Testing
Use Postman or a similar tool to test the APIs. Sample API paths:
  - Addition API: https://api-id.execute-api.region.amazonaws.com/stage/addition
  - Subtraction API: https://api-id.execute-api.region.amazonaws.com/stage/subtraction ....similarly with other operations

Make sure you replace "api-id", "region" and "stage" with actual values once you have deployed your APIs.

# Contributing
Feel free to contribute to this project. If you find any issues or have suggestions for improvement, please open an issue or create a pull request.



