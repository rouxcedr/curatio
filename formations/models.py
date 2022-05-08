from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from core.models import Client, User

import random

class TrainingCourse(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='training_course')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    hours_needed = models.IntegerField()
    minutes_needed = models.IntegerField()

    def __str__(self):
        return self.name

    def get_videos(self):
        return self.training_video.order_by('video_order').all()

    def get_next_video(self, user):
        next_video_number = user.user_formation_tracking.test_completed + 1
        next_video = self.training_video.get(video_order=next_video_number)
        return next_video


class Video(models.Model):
    name = models.CharField(max_length=200)
    video_path = models.FilePathField(path="/home/grouewze/public_html/media/video_formations", recursive=True)
    # video_path = models.FilePathField(path="/home/cedric/EntreprisePR/Curatio/media/video_formations", recursive=True)

    @property
    def video_relative_path(self):
        # return self.video_path.replace("/home/cedric/EntreprisePR/Curatio", "")
        return self.video_path.replace("/home/grouewze/public_html", "")

    def get_exam(self):
        return self.video_quizz

    def __str__(self):
        return self.name


class TrainingVideo(models.Model):
    training_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, related_name='training_video')
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='trainings_courses')
    video_order = models.IntegerField()


class VideoQuizz(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_quizz')
    number_of_questions = models.IntegerField()
    good_answer_to_pass = models.IntegerField()

    def get_exam_questions(self):
        all_exam_questions = self.quizz_question.all()
        exam_questions = []
        for question in all_exam_questions:
            exam_questions.append(question.get_question_for_exam())

        random.shuffle(exam_questions)
        return exam_questions[:self.number_of_questions]

    def __str__(self):
        return self.video.name

class QuizzQuestion(models.Model):
    exam_formation = models.ForeignKey(VideoQuizz, on_delete=models.CASCADE, related_name='quizz_question')
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

    def get_question_for_exam(self):
        answers = [false_answer.answer for false_answer in self.question_possible_answer.all()]
        answers.append(self.answer)
        random.shuffle(answers)

        exam_question = {
            "q": self.question,
            "options": answers,
            "correctIndex": answers.index(self.answer),
            "points": 1,
            "correctResponse": "Bonne réponse!",
            'incorrectResponse': self.answer + ": Explication de la reponse",
        }

        return exam_question


class QuestionPossibleAnswer(models.Model):
    question = models.ForeignKey(QuizzQuestion, on_delete=models.CASCADE, related_name='question_possible_answer')
    answer = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.answer} - {self.question}"

class ProgressionTracking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_formation_tracking')
    test_completed = models.IntegerField()

    def __str__(self):
        return self.user.username

    def get_progression_percentage(self):
        try:
            if self.user.type == "OPERATOR":
                client = self.user.operatormore.client
            elif self.user.type == "CLIENT":
                client = self.user
            else:
                client = None

            client_training_course = TrainingCourse.objects.get(client=client)

        except TrainingCourse.DoesNotExist:
            client_training_course = None

        progression = int((self.test_completed / len(client_training_course.training_video.all())) * 100)
        return progression
