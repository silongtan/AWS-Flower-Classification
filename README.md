# Flask Image Recognition with AWS S3, Lambda, Rekognition, and SageMaker

This project demonstrates how to create a Flask web application that allows users to upload images, store them in an Amazon S3 bucket, and automatically recognize the labels in the image using an AWS Lambda function and Amazon SageMaker. 

## Prerequisites

- Python 3.6 or later
- AWS account with access to S3, Lambda, and SageMaker services
- AWS CLI installed and configured with your AWS account
- A SageMaker endpoint with a pre-trained image classification model

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-repo/flask-image-recognition.git
cd flask-image-recognition
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your AWS credentials:

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, and the default region when prompted.

## Usage

1. Update the configuration settings in the `app.py` file:

- `BUCKET`: The name of the S3 bucket to store the uploaded images
- `RESULT`: The name of the S3 bucket to store the JSON files generated by the Lambda function

2. Start the Flask application:

```bash
export FLASK_APP=app.py
flask run
```

3. Open a web browser and visit `http://127.0.0.1:5000/` to access the application. Navigate to `/storage` to use the app

4. Upload an image using the provided form. The application will store the image in the S3 bucket and trigger the Lambda function.

5. The Lambda function will send the image to the ML endpoint for label prediction, and then store the prediction results as a JSON file in the `RESULT`.

6. The prediction label can be retrived in the JSON file.

## Components

- **Flask application**: A web application that provides an interface for users to upload images and displays the predicted labels.
- **Amazon S3**: Stores the uploaded images and the JSON files containing the image label predictions.
- **AWS Lambda**: Processes the image by sending it to the SageMaker endpoint for label prediction and storing the results in a JSON file.
- **Amazon SageMaker**: Hosts the pre-trained image classification model and predicts labels for the uploaded images.

## Screenshots

Interface
<img width="565" alt="app interface" src="https://user-images.githubusercontent.com/70916756/235398073-46a265cc-a8e2-4930-bf89-bf5b205b4e39.png">

Uploading Image
<img width="381" alt="upload" src="https://user-images.githubusercontent.com/70916756/235398110-2c3a2ec1-8d6c-4373-8692-0c2f386eed63.png">

Generate Result JSON
<img width="452" alt="result" src="https://user-images.githubusercontent.com/70916756/235398182-d0329d4b-0ef1-4584-8743-f960674ff108.png">

Image Bucket
<img width="1370" alt="image bucket" src="https://user-images.githubusercontent.com/70916756/235398266-916f96fb-c350-405f-b79b-75082bb56138.png">

Result Bucket
<img width="1149" alt="result bucket" src="https://user-images.githubusercontent.com/70916756/235398298-96ca6316-1b94-40fe-a63c-862e00f2ad98.png">

Result JSON
<img width="1020" alt="result json" src="https://user-images.githubusercontent.com/70916756/235398339-4fe0f32e-7461-407a-ab29-450019ca17bf.png">

Deployment
<img width="1220" alt="Screenshot 2023-05-01 at 02 58 47" src="https://user-images.githubusercontent.com/70916756/235420121-1b81ab56-095d-412b-807d-5010dd452cb4.png">

<img width="1215" alt="Screenshot 2023-05-01 at 02 59 06" src="https://user-images.githubusercontent.com/70916756/235420158-28fece03-0df3-45a6-bb1d-0469e802d163.png">

## Notes

- Make sure to properly secure your S3 buckets and restrict access to your Lambda function and SageMaker endpoint.
- For a production environment, consider using Amazon API Gateway for the Lambda function instead of invoking it directly from the Flask application.
- The provided sample code is for demonstration purposes only and should be modified and tested according to your project requirements before deploying to a production environment.
