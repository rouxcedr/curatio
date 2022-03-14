from django.shortcuts import render, redirect
from .models import *
from core.models import *
from core.decorators import allowed_users
import time


# Create your views here.
@allowed_users(allowed_roles=['FORMATION'])
def training_course(request):
    try:
        if request.user.type == "OPERATOR":
            client = request.user.operatormore.client
        elif request.user.type == "CLIENT":
            client = request.user
        else:
            client = None
        client_training_course = TrainingCourse.objects.get(client=client)

    except TrainingCourse.DoesNotExist:
        client_training_course = None

    user_tracking = None
    progression = None
    next_video = None

    if client_training_course is not None:
        try:
            user_tracking = ProgressionTracking.objects.get(user=request.user)
        except ProgressionTracking.DoesNotExist:
            user_tracking = ProgressionTracking(user=request.user, test_completed=0)
            user_tracking.save()

        progression = int((user_tracking.test_completed / len(client_training_course.training_video.all())) * 100)

        try:
            next_video = client_training_course.get_next_video(request.user)
        except TrainingVideo.DoesNotExist:
            next_video = None

    context = {'user': request.user,
               "client_training_course": client_training_course,
               "next_video": next_video,
               'nbar': 'formations',
               "user_tracking": user_tracking,
               "progression": progression,
               }

    return render(request, 'formations/formations.html', context)


@allowed_users(allowed_roles=['FORMATION'])
def training_course_video_page(request, training_course_pk, training_video_pk):
    training_course = TrainingCourse.objects.get(pk=training_course_pk)
    training_video = TrainingVideo.objects.get(pk=training_video_pk)

    progression = int(( (training_video.video_order * 2 - 1) / (len(training_course.training_video.all()) * 2)) * 100)
    print(training_video.video_order)
    previous_video_quizz = None

    if training_video.video_order != 1:
        previous_video_quizz = TrainingVideo.objects.get(video_order=training_video.video_order - 1).video.video_quizz

    context = {
        "training_course": training_course,
        "previous_video_quizz": previous_video_quizz,
        "training_video": training_video,
        "progression": progression,
        'nbar': 'formations',
    }
    return render(request, 'formations/formation_template.html', context)


@allowed_users(allowed_roles=['FORMATION'])
def video_quizz_page(request, training_course_pk, video_quizz_pk):
    video_quizz = VideoQuizz.objects.get(pk=video_quizz_pk)
    video = video_quizz.video

    training_course = TrainingCourse.objects.get(pk=training_course_pk)
    training_course_video = training_course.training_video.get(pk=video.pk)

    questions = video_quizz.get_exam_questions()
    all_training_course_videos = training_course.training_video.all()

    print((len(all_training_course_videos) * 2))

    progression = int(((training_course_video.video_order * 2) / (len(all_training_course_videos) * 2)) * 100)

    previous_video = training_course_video

    next_video = None
    if training_course_video.video_order != len(all_training_course_videos):
        next_video = TrainingVideo.objects.get(video_order=training_course_video.video_order + 1)

    context = {
        "training_course": training_course,
        "questions": questions,
        "video_quizz": video_quizz,
        'nbar': 'formations',
        "previous_video": previous_video,
        "next_video": next_video,
        "progression": progression,
    }

    return render(request, 'formations/quizz_template.html', context)


@allowed_users(allowed_roles=['FORMATION'])
def finalExam(request):
    return render(request, "formations/quizz_template.html")


@allowed_users(allowed_roles=['FORMATION'])
def finish_training_course(request, training_course_pk):
    user_tracking = request.user.user_formation_tracking
    user_tracking.test_completed = TrainingCourse.objects.get(pk=training_course_pk).training_video.all().count()
    user_tracking.save()

    return redirect('training_courses')

@allowed_users(allowed_roles=['FORMATION'])
def finish_video_quizz(request, training_course_pk, training_video_pk):
    user_tracking = request.user.user_formation_tracking
    if TrainingVideo.objects.get(pk=training_video_pk).video_order - 1 > user_tracking.test_completed:
        user_tracking.test_completed = TrainingVideo.objects.get(pk=training_video_pk).video_order - 1
    user_tracking.save()

    return redirect('training_course_video_page', training_course_pk=training_course_pk, training_video_pk=training_video_pk)


@allowed_users(allowed_roles=['FORMATION'])
def practicalFormation(request):
    return render(request, template_name='formations/formation_template.html')
