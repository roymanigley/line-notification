# Line Notification

> a REST API with an endpoint to send line broadcast messages written in python

## Initial Setup

### Create a Line Channel

1. Login to the [Line Console](https://developers.line.biz/console/) and create a `provider` and a channel
2. Issue the API Key
3. Subscribe to the channel using the QR Code

## Run the application

### Initial setup

    source venv/bin/activate
    pip install -r requirements.txt

### Run the application

    export LINE_API_KEY=YOUR_API_KEY
    export API_USERNAME=admin # optional (default: admin)
    export API_PASSWORD=1234  # optional (default: 1234)
    python main.py

## Trigger a notification

    curl "http://admin:1234@localhost:8000/api/send_message?message=HelloWorld"

> with URL encoding (jq required)

    curl "http://admin:1234@localhost:8000/api/send_message?message=$(echo 'Hello World !' | jq -sRr @uri)"

## Deployment

The application can easily be deployed on [render.com](render.com), you just have to define following environment variables:
- `LINE_API_KEY=YOUR_API_KEY`
- `API_USERNAME=CHOOSE_USERNAME (default: admin)`
- `API_PASSWORD=CHOOSE_PASSWORD (default: 1234)`
- `PORT=8000`