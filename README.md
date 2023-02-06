# Nude-Detector

Nude-Detector is a web application that uses machine learning algorithms to detect nudity in images and videos. It is built using Flask and NudeNet, an open-source nudity detection library.

## Usage Example
To run the Flask app, follow these steps:

1. Clone the repository to your local machine
2. Navigate to the directory where the app.py file is located
3. Run the following command in the terminal:
python app.py
4. You can now access the app from your browser or a tool such as Postman. To check if a video contains nudity, make a GET request to the following URL, replacing "https://sample-videos.com/video123/3gp/144/big_buck_bunny_144p_1mb.3gp" with the URL of the video you want to check:
http://localhost:5000/check-video?url=https://sample-videos.com/video123/3gp/144/big_buck_bunny_144p_1mb.3gp
6. The response will be a JSON object with the following format:
{
"status": "success",
"is_nude": false
}

where "status" indicates whether the request was successful, and "is_nude" is a boolean value indicating whether nudity was detected in the video.

Note that the video must be publicly accessible in order for the app to download and analyze it.

## Limitations
Keep in mind that the nudity detection algorithm is not perfect, and may occasionally produce false positives or false negatives. Additionally, it is important to respect the privacy of individuals and comply with laws and regulations regarding nudity and explicit content.


