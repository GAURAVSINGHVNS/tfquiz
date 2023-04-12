from django.shortcuts import render, HttpResponse

from tfquiz.questions import questions


def quiz(request):
    totalquestions = questions
    qno = -1
    option = -1
    n = len(totalquestions)
    showqno = ""
    result = ""
    currentquestion = "Start the Test"
    if request.GET:

        qno = int(request.GET["qno"])

        option = int(request.GET["option"])
        if qno >= 0:
            prevquestion = totalquestions[qno].get("question")
            actualanswer = totalquestions[qno].get("answer")
            print("qno", qno, "given answer", option, "question", prevquestion, "given answer", actualanswer)
            if option == actualanswer:
                result = "Correct"
            else:
                result = "Wrong"

        qno += 1

        if qno >= n:
            return HttpResponse("Test Over")
        currentquestion = totalquestions[qno].get("question")
        if qno < 0:
            showqno = ""
        else:
            showqno = str(qno + 1) + ")"

    return render(request, "quiz.html",
                  {"currentquestion": currentquestion, "qno": qno, "showqno": showqno, "result": result})

    # return HttpResponse("Home")
