"""
Python programming with AI
"""

#find the max item in [1,2,3]
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num



#find the min item in [1,2,3]
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
    
#what numpy can do?
#numpy can do matrix multiplication, linear algebra, and random number generation


#use numpy to multiply two matrices
import numpy as np
def matrix_multiply(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)
    

#use numpy to find the mean of a list of numbers
def mean(numbers):
    return sum(numbers) / len(numbers)
    

    
#use numpy to create a linear regression model
import numpy as np
def linear_regression(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    num = 0
    den = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        den += (x[i] - x_mean) ** 2
    m = num / den
    c = y_mean - m * x_mean
    return m, c
    
    

#upload an image to s3
import boto3

s3 = boto3.client('s3')
def upload_image(image_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = image_path.split('/')[-1]
    s3.upload_file(image_path, bucket_name, object_name)
    return True
    

    
#use openai to identify the sentiment of tweet data, remove the urls and special characters in the tweets 

import openai
import re

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text
    
def get_sentiment(text):
    text = clean_text(text)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Identify the sentiment of the following text: " + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
    
    

    
    
    
