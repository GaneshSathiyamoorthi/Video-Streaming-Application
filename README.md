# Video Streaming Application

Welcome to the Video Streaming Application! This application allows users to upload, view, search, and manage videos. The application is built with Django and includes REST APIs for user authentication and video management.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  
## Features

- User authentication: Sign up, log in, and log out functionalities.
- Video management: Upload, edit, and delete videos.
- Video viewing: Browse, search, and watch videos.
- RESTful API for managing users and videos.
- Frontend and backend integration with Django.

## Setup

1. **Clone the repository**:
    git clone https://github.com/GaneshSathiyamoorthi/Video-Streaming-Application
    cd video-streaming-app
 
2. **Set up a virtual environment**:
    python3.10 -m venv venv
    source venv/bin/activate

3. **Install dependencies**:
    pip install -r requirements.txt
   
4. **Migrate the database**:
    python manage.py migrate
  
5. **Create a superuser** (optional, but recommended for managing the application):
    python manage.py createsuperuser
  
6. **Run the development server**:
    python manage.py runserver
  
7. **Access the application** at `http://127.0.0.1:8000/`.

## Usage

- **User Authentication**:
    - **Sign Up**: Navigate to `/signup/` and fill out the form.
    - **Log In**: Navigate to `/login/` and fill out the form.
    - **Log Out**: Use the logout button in the navigation bar.

- **Video Management**:
    - **Upload Video**: Navigate to `/upload_video/` to upload a new video.
    - **Edit Video**: Navigate to the video list page (`/video_list/`), select a video, and click the edit button.
    - **Delete Video**: Navigate to the video list page (`/video_list/`), select a video, and click the delete button.

- **Video Viewing**:
    - **Browse Videos**: Navigate to `/video_list/` to see a list of available videos.
    - **Search Videos**: Use the search bar on the video list page to find videos by name or keyword.
    - **Watch Videos**: Click on a video in the video list to watch it.

## API Endpoints

The application includes RESTful APIs for user authentication and video management.

- **User Authentication**:
    - POST `/api/sign_up/`: Create a new user account.
    - POST `/api/log_in/`: Log in an existing user.
    - POST `/api/log_out/`: Log out the current user.

- **Video Management**:
    - GET `/api/videos/`: Retrieve a list of videos.
    - POST `/api/videos/`: Upload a new video.
    - GET `/api/videos/<id>/`: Retrieve video details.
    - PUT `/api/videos/<id>/`: Update video details.
    - DELETE `/api/videos/<id>/`: Delete a video.




 
