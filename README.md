# Throttling-DRF-API Project

## Introduction
This project is a simple educational example demonstrating how to implement **Throttling** in **Django REST Framework (DRF)** to limit the number of requests allowed per user within a specific time frame.

## Features
- Limits API requests for both authenticated and anonymous users.
- Implements custom throttling policies for better control.
- Uses Django’s built-in caching system for request tracking.

## How It Works
- Anonymous users have a lower request limit.
- Authenticated users have a higher request limit.
- When a user exceeds the allowed limit, they receive a "Too Many Requests" response.

## Installation Steps
1. Install Django and Django REST Framework.
2. Create a Django project and an app.
3. Configure the throttling settings in the project settings.
4. Create API views with throttling rules.
5. Run the server and test the throttling limits.

## Usage
After setting up the project, send multiple requests to the API endpoint to see how throttling works. The API will restrict access once the limit is reached.

## Conclusion
This project provides a basic implementation of API throttling in Django REST Framework, useful for managing API usage and preventing service overload.

