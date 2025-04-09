from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from my_app.models import Tag, Question

def paginate(objects_list, request, per_page=10):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page

def index(request):
    questions = Question.objects.new_questions()
    tag_names = Tag.objects.all().values_list('name', flat=True)
    
    page = paginate(questions, request, 5)
    return render(
        request,
        template_name="index.html",
        context={
            "questions": page.object_list,
            'page_obj': page,
            "tag_names": tag_names
        }
    )

def login(request):
    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="login.html",
        context={
            "tag_names": tag_names
        }
    )

def hot(request):
    hot_questions = Question.objects.hot_questions()
    page = paginate(hot_questions, request, 5)
    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="hot.html",
        context={
            "questions": page.object_list,
            "page_obj": page,
            "tag_names": tag_names
        }
    )


def not_found(request):
    return render(
        request,
        "not_found.html"
    )


def question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return not_found(request)

    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="question.html",
        context={
            'question': question,
            "tag_names": tag_names
        }
    )


def tag(request, tag_name):
    if tag_name not in TAGS:
        return not_found(request)

    tag = TAGS[tag_name]
    questions_for_tag = QUESTIONS[:tag[2]]
    tag_names = Tag.objects.all().values_list('name', flat=True)
    page = paginate(tag_names, request, 5)
    return render(
        request,
        template_name="tag.html",
        context={
            "questions": questions_for_tag,
            "page_obj": page,
            "tag": tag,
            "tag_names": tag_names,
        }
    )

def signup(request):
    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="signup.html",
        context={
            "tag_names": tag_names,
        }
    )


def ask_question(request):
    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="ask.html",
        context={
            "tag_names": tag_names
        }
    )


def settings(request):
    tag_names = Tag.objects.all().values_list('name', flat=True)
    return render(
        request,
        template_name="settings.html",
        context={
            "tag_names": tag_names
        }
    )
