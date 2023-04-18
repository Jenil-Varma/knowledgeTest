import random

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max, Min
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Topic, Question, Quiz, Choice, QuizQuestion
from django.contrib import messages


@login_required
def index(request):
    quizzes = Quiz.objects.filter(user=request.user).order_by('-quiz_date')
    num_quizzes = quizzes.count()
    total_score = quizzes.aggregate(Sum('score'))['score__sum']
    avg_score = round(total_score / num_quizzes, 2) if num_quizzes > 0 else 0
    highest_score = quizzes.aggregate(Max('score'))['score__max']
    lowest_score = quizzes.aggregate(Min('score'))['score__min']
    return render(request, 'quiz/index.html', {
        'quizzes': quizzes,
        'num_quizzes': num_quizzes,
        'total_score': total_score,
        'avg_score': avg_score,
        'highest_score': highest_score,
        'lowest_score': lowest_score,
    })

@login_required
def select_topic(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        selected_topic_id = request.POST.get('topic_id')
        return redirect('quiz:take_quiz', topic_id=selected_topic_id)
    context = {
        'topics': topics,
    }
    return render(request, 'quiz/select-topic.html', context)


@login_required
def take_quiz(request):
    topic_id = request.GET.get('topic')
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = Question.objects.filter(topic=topic)
    if questions.count() > 5:
        random_questions = random.sample(list(questions), 5)
    else:
        random_questions = questions
    context = {
        'topic': topic,
        'questions': random_questions,
    }
    return render(request, 'quiz/take-a-quiz.html', context)


@login_required
def submit_quiz(request):
    if request.method == 'POST':
        # Get the topic from the form
        topic_id = request.POST.get('topic_id')
        topic = get_object_or_404(Topic, pk=topic_id)
        questions = []
        # Get the questions from the form
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = int(key[8:])
                questions.append(get_object_or_404(Question, pk=question_id))

        choices = []
        # Get the answers from the form and calculate the score
        score = 0
        for question in questions:
            answer_id = request.POST.get(f'answer{question.id}')  # get the selected answer id
            if answer_id is not None:
                choice = get_object_or_404(Choice, pk=answer_id) # get the answer object
                choices.append(choice)
                if choice.correct_option is True:
                    score += 1
            else:
                choices.append(None)

        # Create a Quiz object for the user
        quiz = Quiz.objects.create(user=request.user, score=score)
        quiz.save()

        # Create a list of QuizQuestion for the user
        for i in range(len(questions)):
            quiz_question = QuizQuestion.objects.create(quiz=quiz, question=questions[i], user_answer=choices[i])
            quiz_question.save()

        return redirect('quiz:quiz_result', quiz_id=quiz.id)
    else:
        return redirect('quiz:select_topic')


@login_required
def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if quiz.user.id == request.user.id:
        quiz_questions = QuizQuestion.objects.filter(quiz=quiz)
        topic_id = quiz_questions[0].question.topic.id
        topic_name = Topic.objects.get(id=topic_id)
        context = {
            'topic_name': topic_name,
            'quiz': quiz,
            'quiz_questions': quiz_questions,
        }
        return render(request, 'quiz/results.html', context)
    else:
        return redirect('/error')
