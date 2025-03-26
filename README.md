Throttling-DRF-API Project
Introduction
This is a simple educational project that demonstrates how to implement Throttling in Django REST Framework (DRF). Throttling helps control the number of requests a user can make within a specific time period, preventing excessive API usage.

Features
Limits API requests for both authenticated and anonymous users.

Implements custom throttling policies for better control.

Uses Django’s built-in caching system for request tracking.

How It Works
Anonymous users have a lower request limit.

Authenticated users have a higher request limit.

When a user exceeds the allowed limit, they receive a "Too Many Requests" response.

Installation Steps
Install Django and Django REST Framework.

Create a Django project and an app.

Configure the throttling settings in settings.py.

Create API views with throttling rules.

Run the server and test the throttling limits.

Usage
After setting up the project, send multiple requests to the API endpoint to see how throttling works. The API will restrict access once the limit is reached.

Conclusion
This project provides a basic implementation of API throttling in Django REST Framework, useful for managing API usage and preventing service overload.

