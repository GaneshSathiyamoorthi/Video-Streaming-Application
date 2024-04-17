from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from videoapp.models import Video
from videoapp.serializers import VideoSerializer
from videoapp.forms import VideoUploadForm  # Create a form for video upload
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'videoapp/index.html')

def video_list(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videoapp/video_list.html', context)

def video_detail(request, id):
    video = Video.objects.get(id=id)
    context = {
        'video': video
    }
    return render(request, 'videoapp/video_detail.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect the user to the home page after successful login
            return redirect('index')
        else:
            # Add an error message for invalid credentials
            return render(request, 'videoapp/login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'videoapp/login.html')

def signup_view(request):
    if request.method == 'POST':
        # Handle signup
        pass
    return render(request, 'videoapp/signup.html')

@api_view(['POST'])
def sign_up(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({'status': 'success', 'user_id': user.id})

@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not none:
        login(request, user)
        return JsonResponse({'status': 'success', 'user_id': user.id})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def log_out(request):
    logout(request)
    return JsonResponse({'status': 'success'})

@api_view(['GET', 'POST'])
def videos(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, id):
    try:
        video = Video.objects.get(id=id)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'videoapp/upload_video.html', {'form': form})

@login_required
def delete_video(request, id):
    video = Video.objects.get(id=id)
    if video.user == request.user:
        video.delete()
    return redirect('video_list')

def search_videos(request):
    query = request.GET.get('q')
    videos = Video.objects.filter(name__icontains=query)
    return render(request, 'videoapp/video_list.html', {'videos': videos})
