from abc import ABC
import sys    

def handler(event, context):
    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    main()
