from django.shortcuts import render
from django.views import View
from .models import Questions, Result


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "questions/index.html")


class TestView(View):
    def get(self, request, *args, **kwargs):
        questions = Questions.objects.all()     # Get all questions
        return render(request, "questions/test.html", context={"questions": questions})

    def post(self, request, *args, **kwargs):

        ans = request.POST      # Data from forms
        correct_answers = 0     # Number of correct answers

        a = []  # Result dict

        questions = Questions.objects.all() # Get all questions
        total_questions = len(questions)    # Number of questions

        for question in questions:
            your_answer = ans.get(question.question, None)

            if your_answer:
                a.append({"question": question, "your_answer": your_answer})

                if your_answer == question.answer:
                    correct_answers += 1

        try:
            result = round(correct_answers / total_questions * 100, 2)
        except ZeroDivisionError:
            result = 0

        user = ans.get("name", "user")

        try:
            r = Result(user=user, total_questions=total_questions, correct_answers=correct_answers, result=result)
            r.save()
        except:
            print("Some error")

        return render(request, "questions/result.html", context={"answers": a,
                                                                 "total_questions": total_questions,
                                                                 "correct_answers": correct_answers,
                                                                 "result": result,
                                                                 "user": user})
