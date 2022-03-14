from django.urls import path

from . import views

urlpatterns = [
    path('formations/', views.training_course, name='training_courses'),
    path('formation_video_page/<training_course_pk>/<training_video_pk>', views.training_course_video_page, name='training_course_video_page'),
    path('formation_quizz_page/<training_course_pk>/<video_quizz_pk>/', views.video_quizz_page, name='video_quizz_page'),
    path('finished_quizz/<training_course_pk>/<training_video_pk>', views.finish_video_quizz, name='finish_video_quizz'),
    path('formation_practical_page/', views.practicalFormation, name='practical_formation'),
    path('formation_finish/<training_course_pk>', views.finish_training_course, name='finish_training_course'),

    #path('upload_formations/', views.upload_formation, name='upload_formation'),
]
