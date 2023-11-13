import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_input(num1, num2):
    """
    Validate input parameters num1 and num2 for division.

    Parameters:
    - num1: Numerator
    - num2: Denominator

    Returns:
    - Tuple: (bool, str)
      - bool: True if validation passes, False otherwise
      - str: Error message if validation fails
    """
    if num1 is None or num2 is None:
        return False, "Both 'num1' and 'num2' must be provided"
    
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return False, "Both 'num1' and 'num2' must be numeric values"
    
    if num2 == 0:
        return False, "Division by zero is not allowed"
        
    return True, "Status: 200 OK"


def lambda_handler(event, context):
    try:
        # Parse the JSON from the 'body' attribute
        body = json.loads(event['body'])
        
        # Extract 'num1' and 'num2' from the body attribute
        num1 = body.get('num1')
        num2 = body.get('num2')

        # Validate input
        validation_result, validation_message = validate_input(num1, num2)
        if not validation_result:
            raise ValueError(validation_message)

        # Performing division
        result = num1 / num2

        # Log the values and result for verification
        logger.info(f"num1: {num1}, num2: {num2}, result: {result}")

        response = {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }

    except ValueError as e:
        response = {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

    except ZeroDivisionError:
        response = {
            'statusCode': 400,
            'body': json.dumps({'error': "Division by zero is not allowed"})
        }

    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }

    return response


