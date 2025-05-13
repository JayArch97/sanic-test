gcloud builds submit --tag gcr.io/project-id/sanic-cloudrun

gcloud run deploy sanic-cloudrun \
  --image gcr.io/YOUR_PROJECT_ID/sanic-cloudrun \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
